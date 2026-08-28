# Article Spec

## 语气

Averill Journal 风格：冷静、克制、设计主导的编辑体，不是通用 SEO 内容。

- 具体视觉语言胜过泛泛的奢侈词
- 柔和生活场景：牌局之夜、家庭牌桌、女主人时刻、送礼仪式、南方社交温度
- 商业上有用但不硬推
- 把 Monet's Garden 当作一件有桌面存在感的设计物，不是一个 SKU

**用**：table、gathering、game night、ritual、gift-ready、readable、carved acrylic artwork、floral、garden-inspired、American mahjong set。以及具体细节：可读性、牌面、牌背/牌侧、配件、摆桌、收纳、待客体验。

**不用**：
- AI 腔：`elevate your experience`、`perfect for every occasion`、`ultimate guide`、`delve into`、`it's important to note`、`a testament to`、`when it comes to`、`in today's fast-paced`
- 没有细节支撑的空形容词：`beautiful`、`elegant`、`premium`
- 标题里的生硬关键词，尤其 `for women`
- 正文里的直接折扣话术（除非明确是促销文）
- 关键词密集堆砌
- **em dash 滥用**。这是最强的 AI 信号之一。需要停顿时优先用句号、冒号或逗号重写。已发布文章里有 em dash 是历史遗留，不是要模仿的范式。

## 结构

1. 用一个人的场景或决策瞬间开场（不要用定义或"随着……"）
2. 点出那个有用的购买/送礼/待客问题
3. 给出可操作的判断标准
4. 通过设计与桌面使用契合度自然引入 Monet's Garden
5. FAQ，仅当确实回答真实读者问题时
6. 柔和收尾，不要响亮的销售 CTA

字数：1,100–1,500 词（对齐站上表现最好的几篇）。

## 必备 SEO 字段

| 字段 | 要求 |
| --- | --- |
| H1 / title | 自然，主关键词靠前，无被禁短语 |
| meta title | ≤60 字符，**必须以 ` \| Averill` 结尾**（站内统一，否则 Shopify 会补一个不一致的 ndash） |
| meta description | 120–160 字符，含主关键词 |
| slug | 小写连字符，含主关键词，不含年份 |
| 主关键词 | 1 篇 1 个，出现在 H1、前 100 词、meta title、meta desc、slug |
| 次关键词 | 3–5 个，自然分布在 H2 与正文 |
| 内链 | ≥1 个产品页 + ≥1 个站内文章。**只能链已发布文章** |
| FAQ | 3 条，真实问题（为将来的 FAQPage 结构化数据铺路） |

## 锚点导航（站内统一写法，必须有）

正文第 2–3 段之后、第一个 H2 之前插入。每个 h2 **和** h3 都要有 id，但 **只有 h2 进 TOC**。FAQ 的 h2 文字统一用 `FAQ`，id 用 `faq`。

```html
<nav id="article-toc" aria-label="On this page">
<strong>On this page</strong>
<ul>
<li><a href="#slug">标题文字</a></li>
</ul>
</nav>

<h2 id="slug">标题文字</h2>
```

slug 规则：去标签 → 去撇号 → 非字母数字转空格 → 空格转连字符 → 小写。

**不要手写**，用 `scripts/shopify_article.py` 的 `create`（自动加）或 `toc` 子命令，它会校验每条锚点都能解析。

## 内链只能指向已发布文章（2026-08-24 加）

站上长期同时存在若干**未发布草稿**（等用户配图）。草稿的 URL 返回 404，链过去就是给新文章塞死链。

**写前必做**：`audit_blog.py --inventory`，只从 `PUB=True` 的 handle 里选内链目标。2026-08-24 那次可选的 10 篇里有 3 篇是草稿，占比不低，凭印象选必踩。

**顺带**：优先链 `--full` 报 `internal-links` MED（入站 <2）的那几篇，一次动作同时满足内链要求和修站点问题。

## 字数三种口径（2026-08-24 加，比较前先统一）

| 口径 | 含什么 | 对应 spec |
| --- | --- | --- |
| 纯正文 | 只有段落文字 | **就是本文的 1,100–1,500** |
| 含标题 | + 全部 h2/h3 文字（约 60–80 词） | 无 |
| inventory 脚本 | + 标题 + 锚点导航（再约 60 词） | `--inventory` 的 WORDS 列 |

脚本口径大约比纯正文高 130–140 词。**看到 WORDS 1,610 不等于超标**，减掉两层才是 1,472。历史记录里的「1,714 超标」「1,558 达标」都是脚本口径，比较时要换算。

## 产品事实（写之前核对线上产品页，不要凭记忆）

160 张牌、雕刻亚克力（`carved`，不是 `hand-carved`，不是印刷）、0.87"W × 1.25"H × 0.6"D、拉链收纳袋（不是 carrying bag）、说明手册、4 张快速参考卡、适合送礼包装、180 天保修、预计 4–9 个工作日送达。

**牌数拆解（2026-08-10 按线上产品页核实，此前 skill 与品牌记忆里的「152 在玩」是错的）**：
Dots/Bams/Craks 1-9 各 4 张 = 108，四风各 4 张 = 16，三元牌各 4 张 = 12，Flowers = 8，**Jokers = 10**，Blank spares = 6，合计 160。**在玩的是 154，不是 152。**（152 对应 8 jokers 的常见配置，Averill 是 10 jokers。）已发布的 `mahjong-tile-size-readability` 里写着 152，是待修正的事实错误。

产品页「Set Includes」里**没有**单列 Official Standard Hands and Rules 卡，只有说明手册 + 4 张快速参考卡。写文章时不要凭旧记忆加上那张卡。产品页同时出现 `engraved` 和 `printed with precision` 两种互相矛盾的措辞，文章统一用 `carved`。

Monet's Garden 外观：白色牌身、多彩花卉与角色图案、**珊瑚橙色牌背**。

## 事实性表述的红线

- 美式麻将牌**没有官方标准尺寸**。NMJL 发布牌型卡，不发布牌的尺寸。谈行业尺寸只能给区间并明确说明无官方标准，不能收紧成单一"标准尺寸"断言。
- NMJL 牌型卡每年重发，不要写死年份以外的规则细节。
- 不指名贬低竞品。社群里的质量抱怨要抽象成购买判断标准。
- 不用赌博/博彩措辞。
- Monet 作品属公共领域可作灵感，但不得暗示与美术馆/遗产管理方/官方授权有关。

## 交付格式

按项目 CLAUDE.md 约定：英文正文之后必须附**完整中文对照翻译**（逐句，不是摘要），用户需要先看懂再决定是否发布。审阅包写成文件交付，聊天里只给要点。
