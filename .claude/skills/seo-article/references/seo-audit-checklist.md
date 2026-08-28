# SEO Audit Checklist（Averill 博客）

大部分检查已自动化：`python scripts/audit_blog.py --full`。本文件说明每项**证据怎么取**，以及只能人工做的部分。

## 自动化检查（audit_blog.py --full）

| 检查 | 判据 | 严重度 |
| --- | --- | --- |
| 关键词蚕食 | 两篇标题的加权词重叠 ≥60% | HIGH |
| ~~FAQ 内容存在但缺 FAQPage 结构化数据~~ | **2026-08-10 已从脚本移除，不要再加回来**，理由见下方「FAQPage 已作废」 | 已作废 |
| 缺封面图 | `image.url` 为空 → `Article` schema 缺 `image`，丧失富摘要资格 | HIGH（已发布）/ MED（草稿） |
| 缺产品链接 | 正文无 `/products/monets-garden` | HIGH |
| 锚点指向不存在的 id | TOC href 无对应 h2/h3 id | HIGH |
| 正文乱码 | U+FFFD 计数 > 0 | HIGH |
| 链接指向未发布草稿 | 内链目标是 draft handle（会 404） | MED |
| 内链入链不足 | 已发布文章入链 < 2 | MED |
| 薄内容 | 字数 < 已发布文章中位数的 60% | MED |
| 缺锚点导航 | H2 ≥4 但 TOC 为 0 | MED |
| 缺 meta 字段 | 无 `title_tag` / `description_tag` metafield | MED |
| meta 长度/后缀 | title >60 字符或缺 ` \| Averill`；desc 不在 120–160 | LOW |
| 无标签 / 作者名不一致 | tags 为空；author 出现多个值 | LOW |

**加权蚕食检测**：`mahjong` 出现在每个标题里，不加权会导致所有候选词都误报。脚本会自动忽略出现在 >60% 标题中的词。同时检测 h2/h3/`<strong>` 级别的重叠——真正的蚕食风险常在现有文章的 FAQ 里而不在标题里（`how many tiles in american mahjong` 就是这样被抓出来的）。

### 坑：判别词被剔光会让蚕食检查静默失效

**现象**：`--cannibalize "mahjong set"` 这类候选词，两个词一个是 generic（`mahjong`）、一个太泛（`set`），剔除后判别词几乎为空，脚本会报 `no meaningful overlap - safe to target`，看起来是干净的。

**根因**：脚本剔除 >60% 标题中出现的词是为了防误报，但候选词本身若几乎全由 generic 词构成，剩下的判别词不足以形成有意义的比对，「无重叠」是样本不足的结论，不是安全结论。

**检测方法**：看输出里 `discriminating terms:` 那一行。若列表为空或只剩 1 个极泛的词（`set`、`game`、`play`），结论不可信。正常情况应有 1 个以上具体词（例：`how to teach mahjong` → `['teach']`，有效；`best mahjong mat` → `['best','mat']`，有效并正确报出 MED）。

**修复/防护**：候选主关键词必须至少含一个非 `mahjong` 的具体名词或动词。若判别词为空，改为人工比对现有 6 篇的 H2 与 FAQ 标题，不要采信 exit code 0。

### 坑：只剩 1 个泛判别词会让蚕食检查误报 HIGH（上一条的镜像，2026-08-17 发现）

**现象**：`--cannibalize "3 player mahjong"` 报 `[HIGH] how-to-start-a-mahjong-group`，heading/FAQ 命中 100%，看起来是硬重叠不能写。实际全站对「三人怎么打」零覆盖，是误报。

**根因**：上一条讲的是判别词被剔光导致**假阴性**（该报不报），这条是它的镜像——**假阳性**。`3` 被非字母数字规则剥掉、`mahjong` 被判 generic，判别词只剩 `['player']`，分母为 1。分母为 1 时命中率只能是 0% 或 100%，没有中间值，于是任何正文里出现过 "player" 的文章都会顶格得分。命中的 `Plan for the fifth player` 讲的是「人多了怎么办」，和「人少了怎么办」正好相反。

**检测方法**：看 `discriminating terms:` 的**个数**，不只看内容。若只有 1 个，且该词在本站属于高频泛用词（`player` / `set` / `game` / `card` / `rules` / `american`），分数不可信，必须回正文实证。实证做法（不消耗 API 额度）：

```bash
python -c "import urllib.request;d=urllib.request.urlopen(urllib.request.Request('https://www.averillmahjong.com/blogs/news.atom',headers={'User-Agent':'Mozilla/5.0'})).read().decode('utf-8');open('news.atom','w',encoding='utf-8').write(d)"
# 再按 <entry> 切分、html.unescape 出 <content>，对每篇正文跑主题的 10+ 个同义变体正则
```

对本例跑 `three[- ]player|3[- ]player|three players|missing fourth|short a player|three-handed|play with three` 等 12 个变体，全站仅 3 处命中且全部无关（付款句「all three players pay double」、出勤句「a session with three players who chat」、以及新手指南里一句**明确推掉本主题**的话）。判定可写。

**修复/防护**：**判别词 ≤1 个且是泛用词时，脚本结论（无论 HIGH 还是 safe）都只作提示，一律回正文实证再决定。** 判别词 ≥2 个时脚本可信。

**反例对照（防止把这条用成万能免死金牌）**：2026-08-12 的 `difference between chinese and american mahjong` 同样报 HIGH，实证下去发现新手指南有一条 FAQ 标题逐字相同，是**真重叠**，正确结论是折进那条 FAQ 而不是新开页。2026-08-17 的 joker 簇（约 2,000/月、竞争 index 1–7，极诱人）同样实证为真重叠：`american-mahjong-rules` 有 H2 `Joker Rules` 和 FAQ `Can a joker be used in a pair?`。**两次的区别不在分数高低，在有没有回正文查。分数永远不是结论，正文才是。**

### 坑：脚本报 clean 也可能是假阴性，因为站上用同义词写过同一件事（2026-08-20 发现）

**现象**：`--cannibalize "mahjong terms"` 连续三次（08-12 / 08-14 / 08-20）报 `no meaningful overlap - safe to target`，判别词 `['terms']` 是个具体名词、不是泛词，按上面两条坑的规则属于「可信」区间。实际上新手指南里有一节 H2 叫 `The Words You'll Hear at the Table`，内容是一张 9 条术语表（Pung / Kong / Quint / Sextet / Pair / Run / 1-2-3 colors / Exposure / NEWS），**正是这个查询要的东西**。若照 clean 结论新开一页，就是自己蚕食自己。

**根因**：脚本比的是**词**，不是**意图**。站上从头到尾没用过 `terms` 这个词，用的是 `Words`。同义覆盖对字面匹配完全不可见。这跟前两条坑不是一回事：前两条的失效原因是判别词的**数量**出了问题（被剔光、或只剩一个泛词），这一条的判别词数量和质量都正常，失效原因是**语言本身有同义词**。所以「判别词 ≥2 个时脚本可信」这句话要收窄成「判别词 ≥2 个时，脚本的 HIGH/MED 可信；它的 clean 仍然不可信」。

**检测方法**：不要搜候选关键词本身，要搜**它的搜索意图的 2 到 3 个同义表达**，并且**必须包含 H2/H3 标题**，因为覆盖同一意图的旧内容往往就是一整节。落盘实证脚本同上一条（atom feed 拆十篇），再按意图跑正则，例如：

| 候选词 | 只搜它本身（会漏） | 应该搜的同义集合 |
| --- | --- | --- |
| mahjong terms | `term` | `glossar\|terminolog\|vocabular\|\bterm\b\|lingo\|jargon\|what .{0,20} mean` **以及扫一遍全部 H2 标题** |
| how to clean mahjong tiles | `clean` | `clean\|wash\|wipe\|scrub\|grime\|sticky\|yellow\|discolo\|sanitiz` |
| mahjong tournament | `tournament` | `tournament\|tourney\|competiti\|bracket\|prize` |

**本站已知的假朋友（命中了但其实无关，直接抄用）**：

- `washing the tiles` = 洗牌，不是清洁。两篇规则/新手文里都有。
- `wipe clean` 出现在配件篇的**牌垫**段落。
- `wash out` 说的是**反光把牌面冲淡**，出现在可读性与老年篇。
- `Soap` 是**白板的绰号**，不是肥皂。
- `Declaring Mah Jongg` 里的 `mah` / `jongg` 会让任何写成 `mah jongg X` 的候选词报 HIGH（2026-08-20 的 `mah jongg tournament` 即因此误报）。
- 派对篇有 `Use Small Prizes Without Making the Night Competitive`，会命中 `prize` / `competitive`，但立场与锦标赛正好相反。

**修复/防护**：**动手写之前，把候选词的意图翻译成 2–3 个同义表达，回正文和 H2 标题里各搜一遍。** 三种结论都要落到同一个判断上：

| 脚本结论 | 正文实证结果 | 正确动作 |
| --- | --- | --- |
| HIGH / MED | 命中的 heading 与意图无关 | 伪报，可以写（例：3 player mahjong、how to clean mahjong tiles） |
| HIGH / MED | 有 heading 直接回答该词 | 真重叠，扩写旧文（例：joker 簇、difference between chinese and american） |
| clean | 同义搜索也搜不到 | 可以写（例：mahjong tournament） |
| **clean** | **有同义 heading 直接回答该词** | **真重叠，扩写旧文（例：mahjong terms）** |

### 坑：正文实证只落盘 atom feed，会漏掉未发布草稿（2026-08-24 发现）

**现象**：前几轮做蚕食正文实证时，落盘用的是 `/blogs/news.atom`。2026-08-24 实查时站上有 13 篇文章，其中 **3 篇是未发布草稿**，atom feed 里一篇都没有。也就是说按老办法做实证，实际只覆盖了 10/13 的语料，漏检率 23%。草稿一旦被用户配图发布就是真实竞争页面，漏掉它们会让「clean」结论在几天后自动失效。

**根因**：atom feed 是**公开表面**，按设计只输出已发布内容。它的优点（不走页面缓存、含完整正文）掩盖了这个覆盖缺口。

**检测方法**：先跑 `audit_blog.py --inventory` 看 `PUB` 列有几个 `False`，再拿这个数跟 atom feed 的 `<entry>` 数对比。两者不相等就说明 atom 覆盖不全。

**修复/防护**：改用 Admin API 落盘，它同时返回草稿。`audit_blog.load()` 已经在做这件事，直接复用即可（`_text` 已是去标签正文，`_h2` 是标题列表）：

```python
import sys; sys.path.insert(0, ".claude/skills/seo-article/scripts")
import audit_blog as A
for n in A.load():                      # 13 篇，含草稿
    open(out/(n["handle"]+".txt"), "w", encoding="utf-8").write(
        "H2S: " + " | ".join(n["_h2"]) + "\n\n" + n["_text"])
```

把 H2 列表写进文件头，同义词正则一次就能同时扫正文和标题，不用扫两遍。

**2026-08-24 追加的假朋友（`clean` 专项，本站几乎从不用这个词表示「清洁」）**：`clean block` / `clean line` / `clean edges` / `cleanly` / `clean look` 全是「视觉干净」的形容词；`easier to wipe` 说的是 racks；`polished` 说的是待客氛围不是抛光。反向确认同样重要：`scrub` / `detergent` / `alcohol` / `sanitiz` / `disinfect` / `yellowed` / `grime` / `residue` / `dishwasher` / `maintenance` / `restore` 在 13 篇里**零命中**，这才是判定「保养方向零覆盖」的真正依据。**只看命中容易被假朋友骗，要同时看哪些词一次都没出现。**

## 2026-08-08 复查

`--inventory` 实查：6 篇已发布、0 草稿（本次新增前）；全部 U+FFFD=0、全部有 TOC、全部有产品链接、全部有图。A1/A4/A13 保持已解决状态，无新的 HIGH 级损坏。A3（FAQPage + BreadcrumbList）仍未处理，仍是最高优先级，且随本次新增第 7 篇 FAQ 内容而进一步扩大未领取的富摘要面。

## 2026-08-10 复查

`--inventory` 实查：7 篇已发布、0 草稿（本次新增前）。全部 U+FFFD=0、全部有 TOC、全部有产品链接、全部有图。**A3 已在渲染浏览器复验，仍未修复**（见下方结构化数据小节的 2026-08-10 实测）。`--full` 的 8 条发现里唯一 HIGH 就是 A3，无乱码、无坏锚点、无缺产品链接，因此本次继续新增文章是安全的。

新出现的 MED：`mahjong-gifts-game-night-hosts` 与 `how-to-teach-mahjong-to-beginners` 入站内链均为 0。本次新文章已刻意内链到这两篇，下次 `--full` 应看到该项消失。

### 新检查项：已发布文章的产品事实漂移

**发现**：`mahjong-tile-size-readability` 正文写「160 tiles, which covers the 152 in play plus spare blanks」，与线上产品页不符。产品页的 Tile Breakdown 实为 108 + 16 winds + 12 dragons + 8 flowers + **10 jokers** = **154 在玩** + 6 blank spares = 160。skill 与品牌记忆里的「152」也是错的（152 对应 8 jokers 的配置，Averill 用 10 jokers）。

**证据获取方式**：抓 `https://www.averillmahjong.com/products/monets-garden`，剥标签后搜 `Tile Breakdown`，逐项相加核对总数。不要引用 skill 或品牌记忆里的数字。

**为什么值得单列**：这类错误 `--full` 检不出（不是乱码、不是坏链），只有人工比对产品页才会发现，而它直接影响买家对「盒子里到底有什么」的判断。**每次写文章核对产品页时，顺手核对已发布文章里引用的同一批数字。**

**处理**：属于事实错误而非损坏，按 skill 硬规则先报告、不擅自改。已列入待办。

## 必须人工做的检查

### 结构化数据（不能只看静态 HTML）

`curl` 和 `WebFetch` 看不到 JS 注入的 JSON-LD，**只凭静态 HTML 报「无 schema」是错误结论**。必须在渲染浏览器里跑：

```js
[...document.querySelectorAll('script[type="application/ld+json"]')]
  .map(x => JSON.parse(x.textContent)['@type'])
```

2026-08-07 实测结果：只有 `Organization` + `Article`，**无 `FAQPage`、无 `BreadcrumbList`**。
2026-08-10 在 `mahjong-tile-size-readability` 页面复验，结果不变：仍只有 `["Organization","Article"]`。

**只需要关心 `BreadcrumbList`。`FAQPage` 不用查了，见下节。**

## FAQPage 已作废（2026-08-10 查证，Google 官方文档为准）

**结论：给 Averill 加 FAQPage 标注，在谷歌搜索里的收益是零。这条不再是审计发现，已从 `audit_blog.py` 删除，不要因为「站上有 FAQ 却没有 FAQPage」而重新加回来。**

时间线（Google Search Central 官方文档 + changelog）：

| 日期 | 事件 |
| --- | --- |
| 2023-08 | FAQ 富摘要收窄，只对「知名、权威的政府与医疗网站」展示。原因是滥用：大量站点为了占更多搜索结果版面而硬塞 FAQ |
| **2026-05-07** | **FAQ 富摘要在谷歌搜索中全面停止展示**，包括 2023 年后仍保留资格的政府/医疗站 |
| 2026-06-15 | Google 直接删掉了 FAQPage 的整个文档页 |
| 2026-06 | Search Console 富媒体报告与 Rich Results Test 移除 FAQ 支持 |
| 2026-08 | Search Console API 移除 FAQ 支持 |

**为什么之前把它标成 HIGH 是错的**：2026-08-07 和 08-08 两次审计把它列为最高优先级，依据是「已有多篇文章写好问答，是未领取的富摘要位」。这个判据在 2023 年 8 月就已经对商业站点失效，2026 年 5 月对所有站点失效。**审计发现如果依赖某个平台功能，必须记下判据来源和查证日期，否则会像这次一样连续三轮复读一个已经不存在的机会。**

**还剩什么**：`FAQPage` 仍是合法的 schema.org 类型，Google 表示仍会解析它来理解页面。但「会被解析」和「会带来可见收益」是两回事，后者没有可验证的数据。**正文里继续写 FAQ 小节是对的**（真实读者会读，也帮助机器理解内容），只是不要为了标注去改模板。

**仍然值得做的是 `BreadcrumbList`**：这是另一个功能，目前仍在生效，作用是把搜索结果里那行 URL 换成「首页 › News › 文章标题」的层级路径。收益比 FAQ 富摘要小得多，属于顺手可做、不必优先。
新手指南的 `Article` schema 缺 `image`（因为当时没有封面图），其余字段齐全。

也可用 Google Rich Results Test：`https://search.google.com/test/rich-results`

### 锚点是否真能跳转

```js
[...document.querySelectorAll('#article-toc a')].map(a => ({h: a.hash, ok: !!document.querySelector(a.hash)}))
```

### 可见性（元素存在 ≠ 可见）

检查 `getComputedStyle` 的 display/visibility/opacity 和 `getBoundingClientRect().height`，避免主题 CSS 把元素藏了却误判为正常。

### 搜索意图匹配

自动化无法判断文章是否真的满足搜索意图。人工核对：标题承诺 = 正文交付？读者拿到答案了吗？

## 技术基础（已验证通过，2026-08-07）

- `averillmahjong.com` → `www.averillmahjong.com` 单跳 301 ✓
- canonical 主机名与 GMC 决策一致（用 www）✓
- 每篇恰好一个 H1 ✓
- canonical 自指正确 ✓
- `robots.txt` 允许抓取并声明 sitemap ✓
- `sitemap_blogs_1.xml` 只含已发布文章，正确排除草稿 ✓
- 文内图片 alt 齐全 ✓

## 2026-08-07 审计发现的处理状态

| 编号 | 发现 | 状态 |
| --- | --- | --- |
| A1 | 两篇礼品文章重复（`mahjong-gifts` 草稿 vs 已发布版） | **已解决** — 用户删除了重复草稿 |
| A2 | 两篇 hosting 文章意图重叠 | 未处理 |
| A3 | 全站缺 FAQPage + BreadcrumbList 结构化数据 | **FAQPage 部分作废**（2026-08-10 查证，Google 已于 2026-05-07 全面停用 FAQ 富摘要）。剩余的 BreadcrumbList 降为 LOW，顺手可做 |
| A4 | 新手指南缺封面图 | **已解决** — 用户已补图 |
| A5 | 新手指南 title_tag 缺 `\| Averill` 后缀 | 未处理 |
| A6 | 3 篇无标签 | 部分（新文章已带标签） |
| A7 | 作者名 `Averill` vs `Averill Mahjong` 不一致 | 未处理 |
| A8 | 最早那篇 604 词偏薄 | 未处理 |
| A9 | 内链横向深度不足 | 部分改善 |
| A10 | 绝对/相对链接混用 | 未处理（仅美观） |
| A11 | schema description 被截断 | 部分（新文章有显式 summary） |
| A12 | 技术基础干净 | 无需处理 |
| A13 | 一半已发布文章缺锚点导航 | **已解决** — 全部补齐 |

## 下一步优先级（2026-08-10 重排）

FAQPage 从榜首移除后，剩下的都是内容侧的活，这也和「新增文章已触顶、该转向优化现有文章」的判断一致（见 `keyword-research.md`）。

1. **修 `mahjong-tile-size-readability` 的产品事实错误**：152 → 154 在玩（见上方「产品事实漂移」）。一行字，但它是错的事实，优先级最高。
2. **把已否决的低竞争词以 FAQ 条目形式并进现有文章**，不要新写：`how many tiles in american mahjong` 1,300/月 index 25、`how many flowers` 1,000/月 index 5 → 新手指南；`learn american mahjong online` 90/月 index 24 → 教学篇；`mahjong flower tiles meaning` 90/月 index 4 → 新手指南。这是目前投入产出比最高的动作。
3. A8 + A2：把 604 词那篇扩写或与另一篇 hosting 文章合并 + 301。
4. A5 / A7 / A6：meta 后缀、作者名、标签统一（机械活，可批量脚本化）。
5. BreadcrumbList（LOW，顺手可做）。

## 坑：判别词退化成 1 个泛词时，脚本输出不含任何信息量（2026-08-25 定案）

**现象**：`--cannibalize` 剔除 generic 词后只剩 1 个判别词，且该词是本站泛用词（`set` / `player` / `game` / `card`）时，几乎必然对全部文章报 HIGH，形态高度一致：10 篇全 HIGH、`title/meta 0%`、`exact phrase x0`、`discriminating terms in body 100%`。

**根因**：分母为 1，命中率非 0 即 100。这一点 2026-08-17 已记过。**本次新增的是关键一步：这种形态下，HIGH 既可能是伪报，也可能是真重叠，无法从分数区分。**

两个实例，脚本输出形态几乎相同，结论相反：

| 候选词 | 退化后的判别词 | 脚本 | 正文实证 | 结论 |
| --- | --- | --- | --- | --- |
| `3 player mahjong`（08-17） | `player` | 10 篇全 HIGH | 12 变体全站仅 3 处命中，且新手指南明确把该主题推掉 | **伪报，可以写** |
| `how to set up mahjong`（08-25） | `set` | 10 篇全 HIGH | `american-mahjong-rules` 有一节 H2 逐字叫 `Setup`，新手指南有 `Setting Up`，内容都是洗牌/砌墙/掷骰/发牌 | **真重叠，不能写** |
| `2 player mahjong`（08-25） | `player` | 2 篇 HIGH，其一 title/meta 100% | 9 变体 12 处命中全是假朋友（叫牌/付牌/发牌句） | **伪报，可以写** |

**检测方法**：把候选词的**搜索意图**翻译成 2–3 个同义表达，回正文与 h2/h3 标题里正则搜一遍。看的是**有没有一节内容在回答这个查询**，不是看某个词出现了几次。

**修复/防护**：判别词 ≤1 且为泛词时，**脚本结论直接丢弃，100% 依赖正文实证**。不要再试图从 title/meta 百分比或命中篇数上找规律，上表已证明规律不存在。

**证据获取方式（可复现）**：
```bash
# 已发布 10 篇走 atom（不受页面缓存影响），草稿走 Admin API
python - <<'PY'
import urllib.request,re,html,os
raw=urllib.request.urlopen(urllib.request.Request(
  "https://www.averillmahjong.com/blogs/news.atom",
  headers={"User-Agent":"Mozilla/5.0"}),timeout=60).read().decode("utf-8")
os.makedirs("corpus",exist_ok=True)
for e in re.findall(r"<entry>(.*?)</entry>",raw,re.S):
    slug=re.search(r'<link[^>]*href="([^"]+)"',e).group(1).rstrip("/").split("/")[-1]
    body=html.unescape(re.search(r"<content[^>]*>(.*?)</content>",e,re.S).group(1))
    open(f"corpus/{slug}.txt","w",encoding="utf-8").write(body)
PY
# 草稿必须补进来，否则会漏（08-25 那次 4 篇草稿占 14 篇的 29%）
python scripts/shopify_article.py get --id gid://shopify/Article/<id> --out corpus/<slug>.txt
```
然后对**意图同义词**做正则，命中处打印前后 110 字符人工判读。

## 本站假朋友清单（累积，查蚕食时直接用）

命中这些词**不代表**站上覆盖了对应主题。每次实证发现的新条目都要追加。

| 词 | 在本站的真实含义 | 会误伤哪类候选词 |
| --- | --- | --- |
| `clean block` / `clean line` / `clean edges` / `cleanly` | 视觉干净的形容词 | 清洁保养类 |
| `wipe clean` / `easier to wipe` | 出现在牌垫和 racks 段落，不是牌 | 清洁保养类 |
| `washing the tiles` | **洗牌**，不是清洗 | 清洁保养类 |
| `wash out` | 灯光把牌面冲淡 | 清洁保养类 |
| `Soap` | 白板的绰号 | 清洁保养类 |
| `polished` | 待客氛围 | 清洁保养类 |
| `Declaring Mah Jongg` 里的 `mah` / `jongg` | 任何含 `mah jongg` 的候选词都会报 HIGH | 全部 `mah jongg` 写法 |
| `courtesy pass`（×4，2026-08-25 新增） | **Charleston 的传牌机制，不是礼仪** | `mahjong etiquette` 及礼仪簇 |
| `two players`（2026-08-25 新增） | 「两家同时叫牌」「另外两家付牌」的**出牌规则句** | 两人局簇 |
| `the other two players take one`（2026-08-25 新增） | 三人局的**发牌句** | 两人局簇 |
| `terms` 的同义覆盖（08-20） | 站上从不写 `terms`，写的是 `The Words You'll Hear at the Table` | 术语簇（脚本会报假 clean） |

**这个站的 `clean` 一词几乎从不表示「清洁」**，`player` / `set` 则是纯泛词。

## 自蚕食：同方向第二篇的管理办法（2026-08-25 新增）

**现象**：`2-player-mahjong` 与 `3-player-mahjong` 同属「人数不是四」方向，脚本报 title/meta 100%。

**根因**：不是判别词问题，是**两篇文章的读者处境真的相邻**。这类风险脚本测不出来，只能靠选题时的框架设计。

**检测方法**：新文章与同方向旧文的 **H2 列表**并排看。若出现 2 条以上语义等价的 H2，或两篇的开场处境是同一个，就是真自蚕食。

**修复/防护**（08-25 实际用的四条）：
1. **读者处境分开**：三人篇 = 突发（今晚第四人来不了），两人篇 = 长期（家里就两个人 / 在教配偶）。
2. **H2 零重复**，且第二篇不复用第一篇的框架词（本次两人篇不出现 `the number is not four`）。
3. 标题 / meta / slug 全部以各自的数字词为轴。
4. **两篇互链**——但**只能在都已发布后补**。草稿链过去是 404（见 article-spec 的内链规则）。**本次这一步未闭环，已写进审阅包的用户待办。**

## 已发布文章上新出现的坏锚点（2026-08-26 新增发现）

**现象**：`--full` 本轮首次报出第二条 HIGH：`american-mahjong-rules`（**已发布**）的 TOC 里 `#cheat-sheet` 指向一个不存在的 id，读者点了不跳转。此前五轮审计（08-10 起）都只报「缺封面图」一条 HIGH，明确写过「无坏锚点」。

**根因**：这一篇的 TOC 是 **16 条 href vs 12 个 h2/h3 id**，是全站唯一 TOC 数大于 id 数的文章。多出来的 href 没有对应标题，说明**曾经有过一个叫 Cheat Sheet 的小节，后来标题被改掉或删掉，而 TOC 没跟着改**。`shopify_article.py` 的 `create` / `toc` 会自动重建并校验锚点，所以这类残留只可能来自**绕过脚本的手工编辑**。

**检测方法**：`--inventory` 的 `TOC` 与 `IDS` 两列直接对比即可，**不需要跑 `--full`**。
- `TOC > IDS` → 有 href 找不到落点，**必然有坏锚点**（本例 16 vs 12）
- `TOC < IDS` → 正常（h3 有 id 但按规范不进 TOC）
- 全站其余 14 篇都是 `TOC ≤ IDS`

**修复/防护**：
- 修复只需对该文跑 `shopify_article.py toc`（会重建 TOC 并校验），**但它属于已发布文章，按 skill 硬规则 3 必须显式传发布状态，且需用户确认后再动**。本轮只报告未修复。
- 防护：**每轮审计把 `--inventory` 的 TOC/IDS 两列扫一眼**，这是零成本的早期信号，比等 `--full` 报 HIGH 更早。

## 假朋友追加（2026-08-26，找课/上课簇）

| 词 | 在本站的真实含义 | 会误伤哪类候选词 |
| --- | --- | --- |
| `course`（两人局篇） | `driving range / golf course` 的**比喻**，不是课程 | 找课簇 |
| `senior center`（4 处，跨 2 篇） | 全部是**排期句**（活动中心放假导致牌局取消），不是「老年中心开课」 | 找课簇、组局簇 |
| `lesson`（教学篇 ×3） | **教师视角**的教学方式之争（两小时速成课算不算课），不是「上课」 | 找课簇 |
| `class` / `classes`（牌面可读性篇） | 出自 `size class` / `size classes`，指**牌的尺寸档位** | `mahjong classes`（脚本报 LOW 的唯一来源） |

**本轮实证规模**：15 篇正文（含 5 篇草稿）× 20 个找课意图同义词，总命中 15 处，**14 处是假朋友**。唯一实质命中是组局篇的一个从句（parks and recreation 目录里常有麻将课），**一个从句不构成覆盖**。
