# Averill Mahjong SEO 修改记录

店铺：averillmahjong.com（Shopify，原始域名 `1129i1-nf.myshopify.com`）
日期：2026-07-26
背景：SEO 审计后落地整改。审计核心结论：新站尚未被 Google 收录；首页 title/描述/H1 缺失；无品类集合页；产品 SEO 字段为空；博客缺 Article 结构化数据。

## 如何看代码改动

```bash
git log --oneline          # 两个提交：改动前基线 → SEO 修复
git diff 666b0ea 53ece53   # 查看全部改动 diff
git diff 666b0ea 53ece53 -- theme/sections/av-mod1.liquid   # 单看某个文件
```

`theme/sections/` 是线上主题（"260720-2 的副本 的副本"，id 183190880553）被修改的 3 个文件的前后版本；`store/` 是通过 Admin API 修改的店铺配置快照。

## 改动清单（Claude 通过 Admin API 执行）

| # | 改动 | 位置 | 说明 |
|---|------|------|------|
| 1 | 产品 SEO 标题+描述 | 2 个正式产品 | 原先全空，Google 只能回退抓产品描述前 320 字符（超长截断）。新标题含核心词 "American Mahjong Set"，描述约 155 字符 |
| 2 | 新建集合页 | `/collections/american-mahjong-sets` | 含品类介绍文案 + SEO 字段，收入 2 个产品。用于竞争 "american mahjong set" 品类词 |
| 3 | 导航 Shop 改指集合页 | Main menu | 原先直接指向单品 `/products/monets-garden` |
| 4 | 修复首页双 H1 | `theme/sections/header-*.liquid`（共 14 个 header 布局变体） | header 在首页把 logo 图包在 `<h1>` 里（产生空文本 H1），改为恒用 `<div>`。主题（Ella 6.7.6）有 16 个 header 布局变体，实际用哪个由 `header_layout` 设置决定，故全部修复 |
| 5 | Hero 标题参数化 | `theme/sections/av-mod1.liquid` | 原先 `<h1>A softer spring.</h1>` 硬编码；改为主题编辑器可编辑的 setting（默认值不变，显示无变化） |
| 6 | 博客 Article 结构化数据 | `theme/sections/codex-article-page.liquid` | 新增 JSON-LD：headline、发布/更新时间、作者、配图、canonical |
| 7 | 集合页侧栏模板残留清理 | `theme/templates/collection.json` | 移除 8 个 Ella 演示 blocks（演示商品、Custom Block、空 Categories、Color/Size 筛选等），保留库存/价格筛选 |
| 8 | 移除 Recently Viewed 区块 | `theme/templates/collection.json`、两个在用产品模板 | 该区块对新访客/无痕模式显示 "Example product title" 占位卡（JS 无浏览记录可替换）；2 个 SKU 的店该轮播无价值，整体移除 |

**运维备忘**：该店页面缓存不随 section/template 文件修改自动失效（可滞留 1 小时+）。强制全站刷新：给 `layout/theme.liquid` 追加/删除一个换行再保存。绕过缓存看最新渲染：URL 加 `?preview_theme_id=183190880553`。

## 店主手动完成的改动

- 集合页发布到 Online Store 渠道（API 权限不含 publications）
- 首页 title：`Averill Mahjong | Luxury American Mahjong Sets & Gifts`
- 首页 meta description：`Beautifully crafted American mahjong sets with 160 engraved tiles, gift-ready packaging, and everything you need to gather and play.`（后台 → 在线商店 → 偏好设置）

## 重要注意事项

- **主题副本工作流的风险**：店铺在用"复制主题再发布"的方式迭代。若之后发布了其他主题副本，上表 4/5/6 三处主题修改会丢失，需要在新主题上重放（本仓库有完整前后版本，照 diff 重做即可）。
- **API 凭据**：使用 Dev Dashboard 应用 `SEO-fixes` 的 client credentials 换取的 24 小时临时 token，已过期失效。Client Secret 曾在聊天中传输，建议在 Dev Dashboard 里轮换。
- **还原方法**：主题文件还原 = 把本仓库基线版本（`git show 666b0ea:theme/sections/<文件>`）通过 themeFilesUpsert 写回；产品/集合/导航还原参考 `store/` 目录基线快照。

## 尚未完成（下一步优先级）

1. ~~Google Search Console + Bing Webmaster 注册、提交 sitemap~~ ✅ 已完成（2026-07-27）；记得对首页、2 个产品页、集合页、3 篇博客逐个"请求编入索引"
2. **Charleston Garden No. 8 正式素材**：当前产品图是 Monet's Garden 的占位图，正式照片拍好后需替换图片并同步更新 alt 文本（现在的 alt 带 "Monet's Garden" 字样，与产品不符）
3. 清理 2 个 DRAFT 测试产品（`TEST-...` 和 `...（副本）`）
3. Hero 文案可考虑改含 "American Mahjong" 的表述（现已可在主题编辑器直接改）
4. 上评价应用（Judge.me / Loox），积累评价后产品 schema 自动带星级
5. 博客每月 2–4 篇（选题方向见审计报告：教学类 / 选购对比类 / 礼品场景类）
6. 外链起步：Pinterest、礼品清单媒体、麻将社群、微型 KOL 寄测
7. 收录一个月后回看 GSC 数据做第二轮关键词优化

## 2026-07-27 第二轮：模板扫雷 + 产品文案（后续）

- **搜索页清理**（templates/search.json）：移除侧栏 Lorem Ipsum "Custom Block"、空 "Recent Post" 图片块、"Categories" 块
- **集合页**：补移 Recently Viewed 区块（先前已从两个产品模板移除）
- ~~产品描述加深~~ **已回滚**：主题在购买区渲染描述字段时会拍平 HTML 标签，约 220 词的结构化内容显示成一整坨文字，视觉效果差。经验：该主题下产品页的长内容应放在模板 section（DESCRIPTION / DESIGN & CRAFT 手风琴等）里维护，描述字段保持单段简洁
- **全模板扫描结论**：首页、产品页、博客、文章、关于、联系、FAQ、404、购物车、集合列表页均无演示残留；关于页/产品页的图片块为正牌品牌素材
- **待决定（需店主确认）**：`/pages/avada-faqs`（FAQ 应用自建页，在 sitemap 里，疑似与 /pages/faqs 重复 → 建议在应用里关掉或隐藏该页）；`/pages/collab` 若暂未启用合作计划可暂时隐藏
