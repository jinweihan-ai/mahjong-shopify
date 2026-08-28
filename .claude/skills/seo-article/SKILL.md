---
name: seo-article
description: "Averill Mahjong 的统一 SEO 工作台：博客选题与撰写、Shopify 草稿创建、博客与站点 SEO 审计、关键词数据获取、蚕食检测、锚点导航与结构化数据修复。当用户要求写 SEO 文章 / 发博客 / 做 SEO 审计 / 查关键词 / 检查内链或锚点 / 分析排名与索引问题，或提到 averillmahjong.com 的 blog、Journal、News 博客时使用。也用于每日定时 SEO 产出任务。Supersedes averill-blog-seo-operator for blog + audit work."
---

# Averill SEO Operator（云端版）

运行环境是 Anthropic 云沙箱（Linux, UTF-8），工作目录是 checkout 好的 `mahjong-shopify` 仓库根目录。
所有路径都相对仓库根。Shopify 凭据从环境变量读（`SHOPIFY_SHOP` / `SHOPIFY_CLIENT_ID` / `SHOPIFY_CLIENT_SECRET`），由 routine 提示词导出。

Averill Mahjong（`www.averillmahjong.com`）SEO 工作的唯一入口。取代 `averill-blog-seo-operator` 处理博客与审计工作。

## 硬规则（违反会造成真实损失，不要绕过）

1. **不自动发布。** Shopify 文章一律 `isPublished=false` 创建，由用户人工审核后手动发布。只有用户在**当次会话中明确说要发布**才发布。
2. **正文字符串绝不经过 stdout。** 这条在云端 Linux 上不再有 GBK 损坏风险，但保留：脚本的文件流转和 U+FFFD 自检同时也是防止半截正文被截断的护栏。一律用 `scripts/shopify_article.py`，它内建防护。详见 `references/shopify-api-playbook.md`。
3. **改文章必须显式传发布状态。** `articleUpdate` 的 `isPublished` 默认 true，只传 body 会把草稿变成已发布。
4. **不用 curl 验证线上改动。** 有全页缓存，`?cb=` 和 `no-cache` 都无效。验证顺序见下方「验证顺序」。
5. **写文章前必须查选题台账**（`seo-state/topic-ledger.md`，仓库内），防止关键词蚕食和重复选题。
6. **不点名贬低竞品。** 社群里的质量抱怨可以抽象成「购买判断标准」，不能指向具体品牌。
7. **不用赌博/博彩措辞**，会危及 Google Ads 账户和 GMC 审核。
8. **Monet 相关**：作品属公共领域可作设计灵感，但不得暗示与美术馆/遗产管理方/官方授权有关，`Claude Monet` 不得作品牌名使用。

## 必读上下文

- 仓库 `README.md` 末尾最近 2-3 个日期节 — 品牌与渠道近况。（本地的 `american-mahjong-brand-memory` 技能不在云端仓库里，产品事实以下方常量表和线上产品页为准。）
- `references/article-spec.md` — 文章结构、语气、锚点导航写法、质量闸门
- `references/shopify-api-playbook.md` — 所有 Shopify API 坑与可用命令
- `references/seo-audit-checklist.md` — 审计方法与已知发现
- `references/keyword-research.md` — 关键词数据获取路径与降级方案
- `seo-state/topic-ledger.md` — 已覆盖方向、已用关键词、已否决关键词（每次产出后必须更新，并 commit + push 回仓库，否则下次运行看不到）
- `seo-state/fb-discussions.csv` — MJTI Facebook 群组 3,642 条讨论，社群需求证据来源

## 关键常量

| 项 | 值 |
| --- | --- |
| 店铺 | `1129i1-nf.myshopify.com` / `www.averillmahjong.com`（canonical 用 www） |
| Blog GID | `gid://shopify/Blog/117575811369`（handle `news`） |
| 产品页 | `https://www.averillmahjong.com/products/monets-garden` |
| 凭据 | 环境变量 `SHOPIFY_SHOP` / `SHOPIFY_CLIENT_ID` / `SHOPIFY_CLIENT_SECRET`（routine 提示词导出） |
| 作者名 | `Averill Mahjong`（统一，勿用 `Averill`） |

产品事实（每次写文章前核对线上产品页 `https://www.averillmahjong.com/products/monets-garden`，**不要凭记忆**，品牌记忆里曾有 166 张牌 / carrying bag 等错误值）：160 张牌（对局 152 + 备用空白）、雕刻亚克力（用 `carved`，不用 `hand-carved`）、0.87"W × 1.25"H × 0.6"D、拉链收纳袋、说明手册、4 张快速参考卡、官方标准牌型与规则卡、适合送礼包装、180 天保修。

## 日常工作流（单篇产出）

```
1. 实查博客现状      python scripts/audit_blog.py --inventory
2. 读选题台账        seo-state/topic-ledger.md
3. 选题 + 拿关键词    references/keyword-research.md（Google Ads MCP getKeywordIdeas 为首选）
4. 蚕食检查          python scripts/audit_blog.py --cannibalize "<候选主关键词>"
5. 写正文            references/article-spec.md
6. 建草稿            python scripts/shopify_article.py create --body-file X.html ... （默认不发布）
7. 验证              python scripts/shopify_article.py verify --id <gid>
8. 更新台账          改 seo-state/topic-ledger.md，然后 git commit + push
9. 交付审阅包        写进 blog-seo-<日期>/review_package.md 并 commit；同时把要点+完整中文对照翻译直接写在本次运行的最终回复里
```

## 选题规则

**先看台账已覆盖什么，再选没覆盖的方向。** 已验证的方向池（按 MJTI 3,642 帖数据集的话题规模排序）：

| 方向 | MJTI 帖数 | 状态 |
| --- | --- | --- |
| 设计与可读性（tile_design_readability） | 952 | 已覆盖 1 篇 |
| 配件与收纳（accessory_storage） | 929 | 已覆盖 1 篇 |
| 选购与搭配（buying_matching） | 595 | 未覆盖 |
| 图案与主题（tile_theme_pattern） | 532 | 未覆盖 |
| 牌垫与桌面（mat_table_surface） | 464 | 未覆盖 |
| 品质与风险（quality_risk） | 170 | 未覆盖 |
| Hosting | — | 已覆盖 2 篇（饱和） |
| Gifting | — | 已覆盖 2 篇（饱和，且有重复页问题） |
| 规则/新手 | — | 已覆盖 1 篇 |

选题必须同时满足：搜索意图明确、适合新站能排上（优先 competitionIndex 低的）、有社群需求证据、能自然连到产品页、能用 Averill 语气写而不别扭。

**降权**：大词单独做首篇；规则争议/谜题/群务帖；标题里塞 `for women`、`ultimate guide`、`best ever`、`what to know before you choose`。

## 验证顺序（真源优先，不可颠倒）

1. **Admin API 读回** — 唯一真源
2. **`/blogs/news.atom`** — 独立表面，不走页面缓存，含正文，适合验证正文改动是否生效
3. **渲染浏览器** — 验证可见性、计算样式、锚点能否跳转、结构化数据
4. **curl** — 最不可信，全页缓存可能滞后十几分钟

轮询线上页面时**必须同时校验响应体大小**：curl 失败返回空响应，`count()` 会得 0，会被误判成「已修复」。

## 质量闸门（任一不过就不建草稿）

- 标题自然，无被禁短语
- Averill 语气，无 AI 痕迹（无 em dash 滥用、无 "elevate your experience" / "perfect for every occasion"）
- 源帖证据与选题角度匹配
- 主关键词出现在 H1、前 100 词、meta title、meta description、slug
- 至少 1 个自然产品链接 + 1 个站内文章链接
- 锚点导航齐全且每条都能解析（`shopify_article.py` 会自动校验）
- 正文不含 SEO 批注或大纲占位符
- 产品事实与线上产品页一致
- 无竞品指名、无赌博措辞
- **U+FFFD 自检为 0**

## 如何把新经验沉淀进本 skill

这是本 skill 的硬性维护要求。每次做完 SEO 工作，按下面归位：

| 新经验类型 | 写到哪 |
| --- | --- |
| API/工具踩坑及解法 | `references/shopify-api-playbook.md` 的「坑」表 |
| 新的审计发现类型 | `references/seo-audit-checklist.md` 的检查项 |
| 语气/结构/写法约定 | `references/article-spec.md` |
| 关键词数据源变化、降级方案 | `references/keyword-research.md` |
| 本次用掉/否决的关键词与方向 | 共享台账（**每篇必更**） |
| 影响全站的品牌事实 | 写进 `american-mahjong-brand-memory`，**但需用户明确要求** |

写入格式要求：坑必须带**现象 → 根因 → 检测方法 → 修复/防护**四段，不能只写结论。审计发现必须带**证据获取方式**，否则下次无法复现。
