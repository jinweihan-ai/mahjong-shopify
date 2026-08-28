# Shopify API Playbook（Averill）

底层脚本：`.claude/skills/seo-article/scripts/shopify_admin.py`（已随本 skill 一起进仓库，凭据从环境变量读）
认证：Dev Dashboard client credentials，配置在该 skill 的 `config\thecrystaldreams.json`（文件名历史遗留，内容是 Averill）。token 每次现换，长期有效。

**日常操作一律用本 skill 的 `scripts/shopify_article.py`**，它把下面所有坑都封装了。只有需要主题/产品操作时才直接用 `shopify_admin.py`。

---

## 坑 1：GBK 控制台静默损坏正文（严重，会造成永久数据损坏）

**现象**
文章正文里出现 `��`，em dash 变成两个替换字符。2026-08-07 实际损坏了 `how-to-play-american-mahjong-beginners-guide` 的 82 个字符。

**根因**
`shopify_admin.py` 用 `print(json.dumps(...))` 输出到 stdout。Windows 控制台默认 GBK/cp936。重定向到文件时，em dash（U+2014）被写成 GBK 字节 `A1 AA`。之后用 `decode('utf-8','replace')` 读回，`A1` 和 `AA` 都不是合法 UTF-8 起始字节，各变成一个 U+FFFD。把这个字符串再写回 Shopify，损坏就固化了。

字符映射表（实测确认）：

| 原字符 | cp936 字节 | utf-8/replace 读回 |
| --- | --- | --- |
| em dash `—` U+2014 | `a1 aa` | `��`（2 个 U+FFFD） |
| en dash `–` U+2013 | `a8 43` | `�C`（1 个 U+FFFD + 字面 `C`，如 `1–9` → `1?C9`） |
| curly apos `’` U+2019 | `a1 af` | `��`（2 个） |
| left dquote `“` U+201C | `a1 b0` | `��`（2 个） |
| hyphen `‐` U+2010 | `a9 5c` | `�\`（1 个 + 反斜杠） |

**关键**：2 个 U+FFFD 可能是 em dash、也可能是弯引号或弯撇号，**必须按上下文消歧，不能一律替换成 em dash**。判据：前后都是空格 → dash；紧贴单词 → 引号/撇号。

**检测**
```bash
python scripts/shopify_article.py scan-mojibake        # 扫全部文章
```
或对任意正文字符串 `body.count('\ufffd')`。

**防护（三层，都要做）**
1. 调用 `shopify_admin.py` 前 `export PYTHONIOENCODING=utf-8`
2. 正文写入走 `--variables-file`（UTF-8 文件），绝不走命令行参数或 stdout
3. `shopify_article.py` 在**写入前**强制自检，发现 U+FFFD 直接拒绝写入

**修复流程**
1. 用干净路径读回损坏正文
2. 逐个 U+FFFD run 消歧（看前后字符）
3. 替换
4. **做反向替换校验**：把替换后的字符再换回 U+FFFD 序列，结果必须与损坏原文逐字节相同。这证明只改了目标字符，正文其余部分未被动过。这一步不能省。
5. 写回时显式带发布状态与原 `publishDate`

---

## 坑 2：`articleUpdate` 只传 body 会把文章变成已发布

**现象**
更新草稿正文后，草稿变成 `isPublished: true`，公开可访问。

**根因**
`ArticleUpdateInput.isPublished` 默认 `true`。不传 = 传 true。

**防护**
- 改草稿：必须显式 `isPublished: false`
- 改已发布文章：必须显式 `isPublished: true` **且带 `publishDate` 原值**，否则发布日期被重置为当前时间，会污染 `Article` 结构化数据的 `datePublished`
- 字段名不对称：写入用 `publishDate`，读取用 `publishedAt`
- `shopify_article.py` 的 `update` 子命令强制要求 `--published` 或 `--draft` 二选一，不给默认值

**误发布后的止损核查**（2026-08-07 实际执行过）
```bash
# 1. 立刻改回 isPublished:false
# 2. 确认没有公开暴露：
curl -sS "https://www.averillmahjong.com/sitemap_blogs_1.xml" | grep -c '<loc>'   # 条数应未变
curl -sS -o /dev/null -w "%{http_code}\n" "https://www.averillmahjong.com/blogs/news/<handle>"  # 应为 404
```

---

## 坑 3：curl 验证不出线上改动（全页缓存）

**现象**
Admin API 读回是新内容，但 curl 抓线上页面还是旧的，十几分钟不变；加 `?cb=`、`?v=随机数`、`Cache-Control: no-cache`、`Pragma: no-cache` 全部无效；多次抓取字节数完全相同。

**根因**
Shopify 全页缓存。缓存键不受未知 query 参数影响。不同 URL 的缓存新鲜度还不一致——同一批写入的两篇文章，一篇立刻生效、另一篇十几分钟不生效。

**检测/验证顺序**
1. **Admin API 读回** — 真源
2. **`/blogs/news.atom`** — 独立表面，不走页面缓存，**含完整正文**。2026-08-07 就是靠它证明修复已生效（feed 显示 0 个 U+FFFD、38 个 em dash，而 HTML 页面仍显示 82 个 U+FFFD）
3. **渲染浏览器** — 也可能吃到缓存，但比 curl 可靠
4. **curl** — 最不可信

**区分「存储损坏」和「传输编码问题」**
不要用 `errors='replace'` 读线上 HTML 后就下结论——那会把原始字节也显示成 U+FFFD。要看原始字节：

| 原始字节 | 含义 |
| --- | --- |
| `e2 80 94` | 正常的 UTF-8 em dash |
| `ef bf bd` | 真正的 U+FFFD（存储侧已损坏） |
| `a1 aa` | 裸 GBK 字节（传输/编码问题） |

---

## 坑 4：轮询脚本把 curl 失败当成成功

**现象**
轮询「线上是否已修复」的脚本报告已修复，实际没有。

**根因**
curl 遇到 SSL 握手失败（本机偶发 `schannel: failed to receive handshake`）返回空输出，`count('\ufffd')` 得 0，被判成干净。

**防护**
轮询必须同时校验：curl 退出码 + 响应体大小下限（Averill 文章页约 318KB，阈值取 50KB）。

---

## 坑 5：GraphQL schema 细节

| 问题 | 结论 |
| --- | --- |
| `Article.seo` | **不存在**。SEO 标题/描述走 metafields `global.title_tag` / `global.description_tag`，类型 `single_line_text_field` |
| 批量取多篇 body | query cost 高且正文大，容易触发控制台编码崩溃。用 `PYTHONIOENCODING=utf-8` + 输出到文件 |
| `articlesCount` | 是对象，要写 `articlesCount { count }` |
| API 版本 | 默认 `2026-01` |
| 主题 range 字段 | 值必须精确落在 schema 的 step 上，否则 422（`overlay_opacity` 40/45 可以、42/46 报错；`title_size_mobile` min16/max32/step2 时 23 报错） |

---

## 坑 6：品牌记忆会过期

`brand-memory.md` 的 SEO 段落写「博客只有 1 篇可见文章」，实查是 4 篇已发布 + 1 篇未发布草稿（2026-08-07）。**博客现状一律实查 Shopify API，不要引用记忆里的篇数。**

---

## 可用命令速查

```bash
# 一切操作前
export PYTHONIOENCODING=utf-8

# 文章清单 + 审计
python scripts/audit_blog.py --inventory
python scripts/audit_blog.py --full
python scripts/audit_blog.py --cannibalize "mahjong tile size"

# 读正文到文件（不经 stdout）
python scripts/shopify_article.py get --id gid://shopify/Article/xxx --out body.html

# 建草稿（默认不发布，自动加锚点导航，自动 mojibake 自检）
python scripts/shopify_article.py create \
  --title "..." --handle "..." --body-file body.html \
  --meta-title "..." --meta-desc "..." --summary "..." --tags "a,b,c"

# 改正文（必须显式指定发布状态）
python scripts/shopify_article.py update --id gid://... --body-file body.html --draft
python scripts/shopify_article.py update --id gid://... --body-file body.html --published --publish-date 2026-08-05T09:37:50Z

# 验证
python scripts/shopify_article.py verify --id gid://...
python scripts/shopify_article.py scan-mojibake
```


## 坑：`audit_blog.py` 偶发 SSL/代理异常，退出码仍然是 0

**现象**（2026-08-14）：连续跑多个 `--cannibalize` 时，其中一次没有输出蚕食报告，而是抛了一串 `urllib3` 的 `_prepare_proxy` / `ssl_wrap_socket` 堆栈。

**根因**：本机走代理访问 Shopify Admin API，偶发 TLS 握手失败。这是环境层的瞬时故障，不是脚本 bug，也不是数据问题。

**检测方法**：真正的坑在于——**这种失败下 shell 里读到的退出码仍然可能是 0**（在 `for` 循环里 `$?` 取的是管道最后一个命令 `tail` 的状态）。所以不能靠退出码判断，必须确认标准输出里出现了 `Cannibalisation check for '<词>'` 这一行以及结论行。没有结论行 = 这次检查没做，不是「检查通过」。

**修复/防护**：
1. 原样重跑一次，通常立刻成功。
2. 循环跑多个词时不要用 `cmd | tail` 后读 `$?`，逐个跑或者显式检查输出内容。
3. **绝不要把「没看到报错」当成「检查通过」。** 蚕食检查是硬闸门，漏跑一次的代价是一篇会自我蚕食的文章上线。

## Bash 工具处理不了 CJK 路径（2026-08-26 新增）

> **仅限本地 Windows 环境。云端 Linux 沙箱不存在这个坑**——云端产出目录写在仓库内的 `blog-seo-<date>/`，用 Bash 正常读写即可。

**现象**：在 Bash 工具里对 `C:\Users\DEV\Desktop\麻将资产文件\...` 做 `mkdir -p` + heredoc 写文件，整条命令以 ``unexpected EOF while looking for matching `'`` 失败，**文件根本没被创建**，而报错信息指向 heredoc 的行号，看起来像引号写错，极易误判。随后 `ls` 该目录报 `No such file or directory`，路径里的中文被显示成 `$'\351\272\273...'` 八进制转义。

**根因**：这台机器上的 Bash 工具是 Git Bash，与 Windows 之间的路径编码转换对非 ASCII 目录名不可靠。**与 GBK 那个坑不是同一件事**：GBK 坑是 stdout 损坏正文内容，这个坑是**路径本身进不去 shell**，命令整条不执行。

**检测方法**：命令失败且报错行号落在 heredoc 里、或 `ls` 把中文路径显示成八进制转义，就是这个坑。**注意它会静默吃掉同一条命令里前面的 `mkdir`**，所以不要以为「至少目录建好了」。

**修复/防护**：
- **凡是落在 `C:\Users\DEV\Desktop\麻将资产文件\` 下的文件读写，一律用 Write / Edit / Read 工具，不要用 Bash。** 本项目的产出目录 `blog-seo-<date>\` 和台账 `seo-state\topic-ledger.md` 全部在这个路径下。
- 确实需要在 Python 里访问该路径时，**用转义码拼而不是直接写中文**：`"C:/Users/DEV/Desktop/" + "\u9ebb\u5c06\u8d44\u4ea7\u6587\u4ef6" + "/..."`，并且**不要放进 `python -c` 的行内字符串**（`\U` 会被当成 unicode 转义报 `SyntaxError`）。写成 `.py` 文件放到 scratchpad 再执行。
- `shopify_article.py --body-file` **可以**接 CJK 路径（它是 Python 参数不经过 shell 路径解析），本轮 create 就是这么跑通的。所以只有 shell 内建命令受影响。
