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

## 2026-07-28 Google Ads 账户整改（账户 407-451-4233，经 NotFair MCP 执行）

诊断基准（近 30 天）：花费 ¥10,936、真实购买 7 笔、购买总值 ¥6,804、真实 ROAS ≈ 0.62。
报表显示 51 个"转化"，实际只有 7 笔购买——根源是转化目标污染（见下）。

| # | 改动 | change ID |
|---|------|-----------|
| 1 | 转化目标去污染：加购(37次/30天)、发起结账(5次)从主要转化降为仅观察，Purchase 成为唯一竞价目标。此改动同时修复了转化价值虚高（¥50,791 中约 ¥44,000 是加购/结账携带的整单价值，单笔购买记录值本身正常） | 530764-65 |
| 2 | 购物系列 Sales-Shopping-1：出价从"尽量点击(无上限，实际CPC ¥16.3)"改为"尽量点击 + ¥4 CPC 上限"；关闭搜索合作伙伴网络 | 530766-67 |
| 3 | Charleston 从购物系列排除（产品图仍是莫奈占位图，图不符+零转化；正式素材上线后恢复投放） | 530770 |
| 4 | 新建否定词列表 "Junk & Irrelevant"（12 词，PHRASE）挂到两个系列：costco / travel / christmas / pickleball / tips / strategy guide / rules / how to play / solitaire / free mahjong / mahjong online / cheap | 530771-86 |
| 5 | 搜索系列 RSA 落地页曾改为集合页，后按店主决定**改回单品页** /products/monets-garden（Charleston 未正式上线前，集合页呈现不完整） | 530768→530844 |

### 运营备忘

- **竞品词未否定**（sweet jojo / oh my mahjong / the mahjong line / lucky bam / wildwonder）：有转化迹象但数据薄，每周观察后再定
- **christmas 否定词 Q4 前必须移除**（圣诞礼品季是目标流量）
- **Charleston 正式图上线后**：恢复购物系列投放（移除排除项）+ 考虑把泛词落地页换回集合页
- 智能出价 1–2 周学习期内不动预算/出价；每周跑一次搜索词三步清洗（垃圾→否定、转化词→加词、漂移→收紧）
- 升级路径：真实购买稳定 15+/月 → 购物系列升"尽量转化"；30+/月 → 搜索系列上 tCPA、拆广告组（品牌/American/泛词三组）
- 7 月 8–18 日曾出现投放骤停（日均 ¥500+ → ¥5-160），骤停骤启会重置学习期，预算调整按 ±20% 步进
- 账户币种 CNY、时区 Asia/Shanghai，投放目标美国（geo 2840）；所有金额换算按此口径

## 2026-07-29 搜索词第一轮清洗（改动后 2 天复查）

按"垃圾→否定、赢家→加词、漂移→收紧"三步执行，change ID 530904–530922：

- **撤回否定 `costco`**：按转化动作拆分后发现 `costco mahjong` 是全账户 CAC 最好的搜索词（<¥100 花费 → 1 购买 + 2 加购 + 2 结账）。教训：零售商词也能截流转化，否定前必须看"按动作拆分"的数据，不能只看聚合转化列
- **竞品词收网**（观察期结束，30 天 0 购买、只有加购）：否定 oh my mahjong / sweet jojo / mahjong line / lucky bam / wildwonder / ahmahj / haute mahjong / aerin mahjong + 捡漏词 discount code / warehouse sale
- **新漏网垃圾**：否定 rummikub / table / affordable / cards 2026（NMJL 年卡意图）
- **赢家加词**：averill mahjong [完全]（品牌词此前靠泛词词组匹配进来，CPC 高达 ¥13.5）、mahjong tiles [词组]（花费第一 + 1 购买 5 加购）、monet garden mahjong tiles [完全]、monet mahjong tiles [完全]（近零成本出购买）
- 观察名单（未动）：macys / target / near me / mahjong card（单数）/ 小竞品一次性词——下轮清洗再定

## 2026-07-31 改动后首次数据复盘（7/28–7/31）

- **事故与修复**：搜索系列在竞价目标收紧（仅购买）后发生出价塌陷——智能出价失去 85% 学习信号，预估转化率趋零，展示从日均 1,100 次崩至 1–4 次（7/30 日花费 ¥6.4、7/31 ¥2.5）。审核/预算均正常（独立预算已排查，非共享预算问题）。修复：出价改为尽量点击 + ¥8 CPC 上限（change 546020）。**教训：收紧竞价目标时，若该系列月转化量低于智能出价学习门槛（约 30），必须同步降级出价方式，两件事要当作一个改动做**
- **购物系列验证通过**：¥4 CPC 上限生效，CPC ¥9.46 → ¥2.5，日点击 74 → 258（3.4×），7/29 出 1 单。日花费 ¥700 = 预算 2 倍超投（Google 正常行为，月上限 30.4×¥350 兜底）
- **转化口径修复验证通过**：报表"转化"现在 = 真实购买（7/28、7/29 各 1 单，单值 ¥1,082 ≈ 订单额）
- 观察名单新增（购物系列搜索词）：hobby lobby / chinese mahjong set / bakelite / mahjong game / alice in wonderland——下轮清洗定夺

## 2026-08-03 预算再平衡 + 第二轮搜索词清洗（change 571685-96）

依据云端日报（框架 v1.1 首刊）的建议复核后执行：

- **购物系列预算 ¥350 → ¥280**（-20%）：零单判定阈值触发（7/30 起累计 1022 点击 0 购买）。实为封顶——花费已自然回落至 ¥280
- **搜索系列预算 ¥150 → ¥180**（+20%）：近 7 天 ROAS 1.66、预算利用率 98%、因预算丢失 17% 展示份额，账户唯一值得加钱处。加钱前已查搜索词，CTR 摊薄主因是 mahjong tiles 词组放量，质量可接受
- **否定词 +10**（共享列表，两系列生效）：mahjong game / chinese / bakelite / alice in wonderland / hobby lobby / sam's club / mahjong cards / clearance / wholesale / riichi。判定依据均含转化动作拆分（10 词合计 50+ 点击、0 购买 0 加购）
- 保留观察：costco 家族（已证实出单）、near me（曾有加购）、anthropologie（人群契合）、virora / brouk and co（后者有加购）等一次性竞品词
- 云端日报框架升至 v1.2：新增日期口径规则（标题日期 = 运行日北京日期、"昨日" = 前一完整自然日、进行中数据不计入累计）

## 2026-08-05 渠道洞察：社媒群组是当前隐形的最优渠道

- 8/4-8/5 新订单经 Shopify 转化详情核实为 direct 单（1 次会话、无 gclid/UTM），店主确认实际来源为**社媒群组分享**——群组链接普遍丢失来源信息，全部被记为 direct
- 对比：同期购物广告一周约 ¥2,400 花费零单。社媒群组零成本出单，是目前 ROI 最高渠道
- **执行规范（立即生效）**：所有群组分享链接必须带 UTM，如 `?utm_source=community&utm_medium=social&utm_campaign=<群标识>`，让群组渠道从 direct 中显形，为未来渠道预算分配积累一手数据
- 建议（待办）：Shopify 加装免费 post-purchase survey 应用（"你从哪里知道我们的？"），小单量阶段逐单归因

## 2026-08-05 Semrush 竞争情报 + 第三轮词库扩充（change 582402-46）

情报来源：Semrush 美国库（Keyword Magic + Advertising Research，经店主授权的会话查询）

**市场基准**：`american mahjong set` 月搜 14,800 / CPC $0.47；品类 CPC 普遍 $0.3-0.9 → 我们搜索系列 ¥4.58（$0.64）处于中位，¥8 上限充足。`mahjong tiles` 月搜 49,500——现有词组词的天花板远未触及，预算是唯一瓶颈。

**竞品解剖（ohmymahjong.com，135 词 / 月广告费 $4.7K）**：55% 预算防守自家品牌词（未来 averill 长大后的前车之鉴，品牌完全匹配词永久保留）；大量收割竞品词；连 $0.09 的教育词都买（月预算 3 万美元的玩法，现阶段不跟）。

**执行**：
- 关键词 +5：luxury american mahjong set [词组]、american mahjong set for beginners [完全]、american mahjong starter set [完全]、american mahjong game set [词组]、american mahjong tile sets [词组]
- 否定词 +14：used / vintage / antique（二手古董，月量 650+）、amazon / ebay（渠道导航）、rack / racks / pusher / pushers / mat（配件套装需求，我们不含，月量 600+）、jongyance / yellow mountain / linda li / winning solutions（竞品牌）

**产品路线图信号（Semrush 需求验证）**：travel 系约 1,000/月、带 racks+mat 的配件套装约 600/月，是需求量最大的两个未覆盖品类——出新品时优先评估。

## 2026-08-05 付费竞争版图全景（Semrush Advertising Research）

**梯队**（美国库，月广告费）：
1. ohmymahjong.com — $4.7K/135词：品牌防守55% + 泛词 + 全面收割竞品
2. myfairmahjong.com — $1.1K/61词：**教育流量套利**——51% 付费流量来自 `how to play mahjong`（月搜33,100，CPC 仅 $0.06）落到博客新手指南；竞品词流量导向 /collections/clearance（用清仓价接竞品比价客）
3. themahjongline.com — $1K/55词：**邻近游戏套利**——`hand and foot card game`、`rummikub rules`（各月搜12,100，CPC $0.01-0.41）落到"怎么玩"页面交叉转化；34.6% 预算收割 OMM 品牌词
4. 小玩家：bambirdboutique / birdandbamboo / ymimports / peacelovemahjong / mahjonggmaven 等（<$500/月）

**对 Averill 的战略含义**：
- 我们月预算约 $2K，实为品类第二梯队体量——不是玩不起，是要选对打法
- **品类共识玩法 = 教育内容 + 付费分发**（$0.01-0.19 的 CPC 是全品类最便宜的获客）。前置条件：先有 how to play American mahjong 的教学页 → 内容计划中该文章的优先级从"SEO 长线"提升为"广告基建"
- 竞品互相收割是常态；我们的品牌词防线（averill mahjong 完全匹配）要永久保持
- luxury/premium 定位词无人竞争——我们新加的 luxury 词是空白地带
- 三家都有配件/旅行品类矩阵——再次验证产品路线图信号
- 风险监控：myfairmahjong 的收割名单未来可能加上 averill，定期搜自己品牌看 SERP

## 2026-08-05 新手教学文章（广告基建）草稿完成

- 《How to Play American Mahjong: A Beginner's Guide》已按店主提供的 2026 官方规则卡撰写（约 1,500 词），以**草稿**创建于 News 博客（Article 618452582697），待店主审核发布
- 内容基于规则卡逐条核实：152 张标准配置（8花+8百搭）、白板作 0、Charleston 流程（右-对-左强制 / 左-对-右可选 / 盲传 / 礼貌传）、百搭七条精简为五条、X/C 露牌门清、无百搭翻倍等；**未复制牌型表**（卡片有版权声明，仅按九大类概述并引导用户看实体卡）
- 160 vs 152 张的疑问在 FAQ 中明确解释（标准 152 + 备用白牌）
- 内链：Monet 产品页 ×2、cozy night 文章、party 文章；SEO title/description 已设（global metafields）
- **发布后的下一步**：① GSC 请求收录；② 开教育词广告组（how to play mahjong 系，市场 CPC $0.06-0.19，MFM 已验证的品类最便宜获客通道）

## 2026-08-05 教学文章发布 + 教育词系列上线（change 584832-57）

- 文章《How to Play American Mahjong: A Beginner's Guide》已发布：/blogs/news/how-to-play-american-mahjong-beginners-guide（待店主 GSC 请求收录）
- 新系列 **Education-HowToPlay-US**（id 24111419407）：¥40/天，尽量点击 + ¥1.5 CPC 上限，美国 PRESENCE 定向，关闭搜索伙伴与展示网络
- 关键词 8 个（how to play mahjong 家族，词组为主 + charleston 完全匹配）；专属否定列表 "Education Negatives"（online/free/solitaire/app/download/chinese/riichi/video）——**独立于电商否定列表**（那边把 how to play/rules 设为否定，两系列各司其职，经典的"同词异用"案例）
- RSA：10 标题（首位固定 "How to Play American Mahjong"）+ 4 描述，落地页为教学文章
- 日报框架升至 v1.4：教育系列纳入监控，评估口径为低价流量（CPC/点击量）而非 ROAS

## 2026-08-06 购物系列优化策略执行（change 593570 + Shopify）

- **预算第二阶段降档提前执行**：¥280 → ¥225（店主指示；依据 7/30 起 1,261 点击 0 购买、实际日花费已滑至 ¥183）。购物系列定位明确为"存在感渠道"：日均 7-11K 展示的低价品牌曝光
- **Feed 品类字段补齐**：两个产品的 productType 由空设为 "American Mahjong Set"（进入 MC feed 的 product_type 属性，改善购物匹配；不影响店面显示）
- **广告价格事故闭环**：同事已将 RSA 价格声明改回与店铺一致（Was $189.99, Now $159.99 / Save $30），过程记录：8/5 曾出现广告 $127.99 vs 页面 $159.99 的错价并跑了约一天——教训：**文案改动上线前必须先核对落地页实价**
- **发现**：Charleston 商品状态已被改为 UNLISTED（同事操作，配合占位图下架，合理）
- 待店主执行：Google & YouTube 应用里把 feed 标题改为 "American Mahjong Set 160 Engraved Tiles — Monet's Garden | Averill"（只影响购物 feed，不动网站 SEO）
- 日报框架升至 v1.5：购物进入第三阶段判定（8/17 暂停评估），预算基线更新

## 2026-08-06 受众体系启动（change 593745-59）

**画像验证**（30 天账户数据 vs 店主情报"东南部中年女性"）：
- 性别：女性占点击 87%、转化 83% ✅
- 年龄：比"中年"更年长——55-64 与 65+ 贡献了 23 个已知年龄转化中的 18 个，**65+ 转化率最高** ✅（修正：核心买家是 55-75 岁女性）
- 地理：转化集中在 TX(5)/AL(3)/CA(3)/FL(1)/VA(1)，流量前十里东南部占七席（TX/FL/GA/NC/SC/TN/VA）✅（CA 是唯一的非南部例外）
- 佐证：搜索词中出现 lsu / ole miss / alabama / southern living 等南方大学与生活方式牌面需求

**执行**：Google & YouTube 应用自动创建的零售再营销列表已在蓄水（全站访客搜索列表约 540 人、商品浏览者 200、弃购者 8、已购 8）。以观察模式挂载：搜索系列（访客+商品浏览+弃购）、购物系列（访客+弃购）、教育系列（访客）。不影响任何投放，只开始按人群拆分报表。

**解锁路线**：① 访客列表 ≥1,000 → RLSA（对回访者搜索加价）；② 月底用纯购买口径复核分州数据 → 东南部 +10-15% 出价系数；③ 弃购列表 ≥100 → 弃购再营销专项。**创意侧应用**（受众知识优先进创意的原则）：未来 RSA 变体可测试南方社交场景文案；55+ 群体注意落地页字号与可读性。

## 2026-08-06 购物系列出价策略试验启动（change 593838）

- 背景：Google 销售（yichengzeng@google.com）建议购物系列改"尽可能提高转化价值"。我方评估为数据上不成立（单SKU无价值差异、1,400点击0购买无学习信号、丢失¥4 CPC上限），店主决定用受控试验裁决
- 官方实验功能不支持购物系列（仅 SEARCH 类型），采用**时间盒对照**：8/7-8/20 整系列切换，与 7/30-8/6 基线对比（CPC ¥1.7-2.5 / 日点击 110-180 / 购买 0）
- 风险边界：日预算 ¥225 不变；预注册回滚规则（CPC 三日均值>¥8 提前回滚；到期购买≤0且CPC更高回滚、购买≥2转正）；回滚命令一步（尽量点击+¥4上限）
- 日报框架 v1.7：试验期每日强制报告试验进度，第三阶段零单判定冻结至试验结束

## 2026-08-06 跨平台战略定稿 + Meta 渠道验证

**财务框架（店主提供 COGS $75 后首次建立）**：净客单 $132 / 毛利率约 43%（保守口径）→ **保本 ROAS 2.2x、目标 3.5x、CAC 上限 ≈$57**。直面结论：当前 Google 全线在保本线以下（搜索 1.66），维持不加码，增量给新渠道验证。

**$3,000/月预算分配**：Google 搜索 26% / 购物 31%（试验后调整）/ 教育 6% / **Meta 新开 30%（$900：Advantage+ 静态图 prospecting $22/天 + Pixel 再营销 $8/天）** / 机动 7%。TikTok 明确不做（55-75 女性人群错位）。

**Meta 渠道质疑与验证**（店主发现广告库搜 mahjong 全是游戏 App，质疑实体套装无人投放）：按**广告主**而非关键词复查 Meta 广告库——
- Oh My Mahjong：4 月起持续在投（儿童套装/分系列牌面/配件视频，多版本测试）
- The Mahjong Line：**2025 年 12 月起连投 8 个月**（新色系上市、Big Card 免费送促销、防水演示视频）
- 生态发现：南方精品店（K. McCarthy Nashville / Pink Pineapple / Peters Billiards）自费投广告卖 OMM 的货——**批发/寄售渠道存在**，未来铺货线索
- 结论：初始质疑是关键词搜索被游戏广告淹没的假象；两大头部 8 个月连续投放 = Meta 付费在品类内被验证。竞品创意规律：产品优先、上新驱动、8-14 秒短视频、免费赠品钩子

**前置待办（店主）**：Shopify 安装 Facebook & Instagram 官方应用（Pixel + CAPI + 目录同步），装好后由 Claude 搭建两系列并接入日报监控。

## 2026-08-06 竞品 Meta 投放落地链接实录（广告库跳转链解码）

**OMM（14 条）**：/collections/mahjong-tile-sets、/products/birdie-mahjong-tiles、/products/nantucket-tiles、/collections/racks-pushers、/collections/card-folios、**/pages/become_a_teacher（招募麻将老师！社区基建型广告）**；生态经销商自投：kmccarthynashville、thepinkpineapple850（含联名 bundle）、belleandblush；网红 IG 号广告：giftedhh、coastal_mahjong

**TML（11 条）**：/products/the-big-card-2026、新色系发售页 ×4（petal-pink/lilac/americana-blue）、/collections/aquamahj（泳池麻将）、IG 主页涨粉广告 ×2、**luma.com 活动页 + 达拉斯 Stoneleigh 酒店活动页（线下活动广告！）**

**品类 Meta 打法结论**：两家都在为"非直接卖货"目标花钱——OMM 建教师网络、TML 办线下活动+涨粉。麻将品类的 Meta 终局是社区基建，产品广告只是入口。对 Averill：现阶段先跑产品广告，但社媒群组渠道的进化路线已被两家验证（群组 → 教师/活动 → 城市社群页）。

## 2026-08-06 竞价洞察实录（店主从后台导出，Google 官方数据）

**电商搜索场**：Amazon IS 40%/OMM 32%/Etsy 23%/芝加哥论坛报 17%/MFM 12%；我们 14%（绝对顶部仅 4.4%）。OMM 与我们 44% 同场、90% 排上方——竞品 Google 投放强度获官方数据盖章。TML 不在电商场（其搜索预算集中于教育/邻近游戏，与 Semrush 互证）。
**教育场**：MFM IS 41.6%、79% 同场率（教育赛道霸主）；chatgpt.com 也在买 how-to 词（<10%）。我们 11%。
**判定**：低价存在者定位被验证（别人抢顶部、我们捡量），保本 ROAS 达成前不抢排名。
**新待办**：① chicagotribune（报纸游戏板块）出现在电商场 → 下轮清洗重点查 play/game 变体漏网词；② 品牌词拆独立系列的时点从"月购买30+"提前至"15+"（获得纯净的品牌蹭量监控）。

## 2026-08-07 信任层修复启动（战略转向：流量采购 → 转化与留存）

店主诊断（数据佐证成立）：CPC 正常、加购率 5.5% 正常，但加购→付款断裂——根因是信任层缺失（无评价、无真人IP、无邮件熟化、社群无人运营），四个问题一个病根。30 天修复排序：
1. **邮件熟化（本周，已交付）**：全套文案见 docs/email-flows.md——4 封熟化序列（欢迎/教学/UGC征集/首单激励）+ 28 老客评价邀请单发。待店主确认 A4 优惠方案后排期
2. **评价体系（第1-2周）**：Judge.me 安装（店主）→ 28 老客补邀 → 产品页星级。加购断裂的直接手术
3. **真人 IP（第2-4周）**：先轻量版（Story页真人化 + 社群UGC转发），出镜人选待定；内容日历与口播脚本随后交付
4. **社群运营（持续）**：需指定 owner；SOP + 群专属优惠码方案随后交付
广告降级为最小健康仓位（搜索+教育 ¥220/天），信任层修复前不加码；购物试验 8/10 裁决后释放预算转投寄测/PR。

## 2026-08-08 试验监控 + 教育系列上限修复（change 614700）

- **购物出价试验第 1 完整日（8/7）确认塌陷**：42 次展示 = 基线 0.6%，"尽可能提高转化价值"零信号弃赛（与 7/30 搜索塌陷同病理）。按预注册规则 8/9 复查，仍 <10% 基线即裁决回滚（尽量点击 + ¥4 上限）
- **教育系列 8/7 零投放**：非暂停非拒登——¥1.5 CPC 上限被拍卖价顶穿（8/6 均价 ¥1.47 已贴顶；教育场 MFM 42% IS 压价）。修复：上限 ¥1.5 → ¥2.0（仍处套利价位）。框架 v1.9 更新告警阈值
- 8 月截至 8/7 纯购买仅 1 单（8/1）；8/4 的 2 个发起结账未完成——信任层诊断再获数据支撑
- 运维备忘：NotFair 共享 API 配额有限（quota_error=2，20 分钟窗口），人工查询降频，常规监控交给每日日报

## 2026-08-09 订单归因直连 + 日报升级 v2.0

- SEO-fixes 应用新增 read_orders/read_customers 权限，实现订单归因 API 直查（customerJourneySummary）
- **首次渠道台账（近 6 单）**：自然搜索 3 单（7/31、8/2、8/8——SEO 整改后 4 天即开始出单）、direct 2 单（群组）、Instagram 1 单；**全部 6 单的访问路径无广告点击参数**。Google Ads 认领的 8/1 购买与 Shopify 归因存在多触点分歧——广告真实增量待月底复审
- 日报框架 v2.0：新增订单渠道台账（每日新订单逐单归类 + 本月渠道累计），Shopify 凭据仅存于云端任务配置（不入仓库）

## 2026-08-09 GSC 打通：SEO 流量数据并入日报（框架 v2.1）

- 店主创建 GCP 服务账号 gsc-reader@mahjong-seo.iam.gserviceaccount.com 并授权 GSC 只读；属性格式为 `sc-domain:averillmahjong.com`（URL 前缀格式无权限）；密钥仅存云端任务配置
- 首拉基线（8/1-8/7）：日均自然点击 4-7、展示 40-70。品牌词 averill mahjong 排名 1.0；monet garden mahjong tiles 3.5、monet mahjong tiles 3.4（长尾已上首页）；american mahjong set 家族 32-37 位（第 4 页，下一里程碑=进前 20）。页面侧：首页 22 点击最多，集合页展示最多（184）但 CTR 低，教学博客 40 展示 0 点击（标题/摘要可优化候选）
- 日报新增 SEO 速览行（每日）+ Top 词深度段（每周一）；GSC 数据延迟约 2 天，日报按最近可用日报告

## 2026-08-09 CTR 双优化：SEO 元信息改写 + 搜索广告附加图片（change 625029-32）

**SEO 元信息改写**（Admin API，动 SEO 字段不动正文；依据：GSC 首拉发现两页"有展示没点击"）：
- 教学博客 how-to-play-american-mahjong-beginners-guide（7 天 40 展示 0 点击）：标题改 `How to Play American Mahjong — Easy Beginner's Guide | Averill`；描述改 one evening / step by step / no jargon 钩子（旧值：`How to Play American Mahjong: Beginner's Guide (2026 Rules)` + step-by-step 描述）
- 集合页 american-mahjong-sets（184 展示 4 点击，CTR 2.2%）：标题改 `American Mahjong Sets — 160 Engraved Tiles, Gift-Ready | Averill`；描述加 free shipping / 30-day returns（与 SERP 商家标注呼应）（旧值：`American Mahjong Sets — Engraved 160-Tile Sets | Averill`）
- 效果观察：2-3 周后看 GSC 这两页的 CTR 变化（基线 0% / 2.2%）
- 教训修正：此前疑似"集合页标题乱码"为本地控制台 GBK 显示问题，API 存储值一直正常（用 ensure_ascii 转义读回验证）

**搜索系列附加图片**（响应 Google Ads 后台 +2.7% 建议，选择手动上传而非动态抓取以控制素材）：
- 4 张 AD_IMAGE 资产挂到搜索系列 23889289563：蜂鸟特写 1:1、全套牌面 1:1、牌架 1.91:1、序数牌阵 1.91:1
- 事后发现：该系列此前已有 10 张图片资产（5/26 产品摄影批次，同事上传），现共 14 张（上限 20）。Google 后台"+2.7%"建议实际指的是"动态附加图片"（落地页自动抓图），因素材不可控维持不启用；两周后按各图展示数据汰换
- 素材来源：产品页 CDN 原图 + Shopify CDN 裁切参数（&width=&height=&crop=center）现场生成合规尺寸，无需本地图片处理
- 待观察：图片资产需过审（1-2 个工作日）；上线后看展示率与 CTR

## 2026-08-09 日报 v2.2：账户改动审计并入

- 每日日报新增"账户改动（近24h）"栏：查 change_event，列出周期内全部 Google Ads 账户改动（操作者/时间/内容），非团队改动（Google 销售、自动应用建议）单独点名，未记录改动触发告警
- 动机：历史上两次"暗改"教训——云端 cron 被 UI 时区显示陷阱重置、Google 销售建议的出价改动缺乏留痕；改动透明化后，多人协作（店主/同事/AI/Google）的账户有了每日对账机制

## 2026-08-09 图片资产盘点：14 张审 5 删（change 625111）

逐张核了 30 天数据 + 图面质量，搜索系列 AD_IMAGE 从 14 张精简到 9 张：

**保留**：0556_1:1（6514 展示/CTR 3.2%，头号功臣）、5260511_1:1（CTR 3.9%）、0515_1:1（CTR 3.9%）、0549_1:1（2.6%）、5260511_1.91:1，加当日新传 4 张
**移除**（仅解挂载，资产留库可回挂）：
- 0556_1.91:1：整张虚焦（横裁把清晰前景裁掉了）
- 0549_1.91:1：横裁只剩牌背墙，无信息量
- 0515_1.91:1：1413 展示 CTR 0.5%（同行 1/6），数据判死
- stilllife 两张（兔子野餐场景，1:1+1.91:1）：白色花纹牌与落地页莫奈珊瑚色不符（疑似查尔斯顿/概念素材），图文不符
**经验**：① 横版裁切必须逐张人工过目，自动裁切易产生虚焦/无主体废片；② 图片素材与落地页产品必须同款；③ 两周后按各图展示数据再汰换一轮

## 2026-08-10 购物试验回滚（change 629505）+ 教育系列诊断

- **购物系列出价回滚**：按预注册规则执行（8/7-8/9 展示 42/51/104 = 基线 1-2%，触发"复查仍 <10% 基线即回滚"条件），"尽可能提高转化价值"→ 尽量点击 + ¥4 CPC 上限。试验结论（供回复 Google 销售）：月购买 <15 的账户上，价值出价没有学习信号，切换后智能出价直接饿死——与 7/30 搜索系列同病理，账户第二次验证
- **教育系列零投放诊断**：排除资格/审核问题（8 关键词 QS 6-10 全合格、广告过审、系列 SERVING/LEARNING），根因 = ¥2.0 上限仍被拍卖顶穿（lost_rank 恒 90%+）。8/5-8/6 的 ¥1.47 低价窗口已被教育词场的大预算竞对关闭。待店主决策：A 提价到 ¥2.5-3.0 / B 暂停并把 ¥40 转给搜索（搜索 lost_budget 已达 33.9%）
- 当日新订单 #1046（$159.99）：又一单自然搜索直落产品页——本月 SEO 3 单 vs 广告归因 0 单

## 2026-08-10 教育系列暂停，预算转投搜索（change 629522-23）

店主拍板选项 B：暂停 Education-HowToPlay-US（¥2.0 上限被教育词场拍卖持续顶穿，lost_rank 90%+，提价则"低价教育流量"逻辑失效）；¥40/天 转给搜索系列（¥180 → ¥220，总预算盘子不变，不违反"信任层修复前不加码"）。搜索系列 lost_budget 33.9% 是账户当前唯一被预算掐量的地方。教育获客改由 SEO 承接（教学词已开始自然收录，博客元信息 8/9 已优化）。

## 2026-08-10 折扣码归因上线（日报 v2.3）：码即渠道签名

- 读取订单 discountCodes 后渠道真相修正：#1042/#1047 访问路径显示"Google SEO"，但分别带 LADIESTHATMAHJ、AVERILLMAH 码——社群种草在先，搜索只是回购路径。本月修正后：纯 SEO 全价单 2（#1045/#1046，$159.99×2，零折扣纯增量）、社群相关 4（含借道搜索）
- 已发现的码：BlackGirlsMahjongToo（75折，FB 群专属）、LADIESTHATMAHJ（8折，群专属）、AVERILLMAH（通用，力度从 85折 调至 8折——单笔折扣 $32 ≈ 毛利 38%，幅度变化需留意）
- 日报 v2.3：订单台账加折扣码列，群组专属码优先于访问路径定渠道；新码名自动报告

## 2026-08-10 归因地理裁决上线：8/9 广告认领转化翻案为真实助攻

- 方法：Ads 认领购买但 Shopify 路径无广告触点时，用 user_location_view 拆转化点击所在州 vs 订单收货州
- 实证：8/9 认领的两笔转化点击州 NC/VA，与 #1045（NC Carolina Beach）、#1046（VA Portsmouth）收货州双双吻合（当日全美仅 39 点击）——买家确实点过广告，最后经 SEO 会话下单，属跨设备/跨会话助攻，非归因抢功
- 修正：撤回"广告 0 单"的严判；月底广告增量复审按"辅助触点"口径计。日报 v2.3 分歧处理升级为三档：广告直接单（gclid）/ 跨设备助攻（地理吻合）/ 归因存疑（地理不符）
- 渠道认知现状：社群种草（折扣码为证）+ 广告助攻（地理为证）+ SEO 收口（referrer 为证）三层漏斗，各层证据链齐了

## 2026-08-10 关键词级归因钉死：两笔广告助攻精确到城市

- click_view（点击级：关键词+城市+设备）与订单收货地对照：
  - "mahjong sets for sale" 手机点击来自 Carolina Beach, NC = #1045 收货地（城市级精确命中，该镇当日全美唯一点击）
  - "mahjong tiles set" 桌面点击来自 Chesapeake, VA ≈ #1046 收货地 Portsmouth（接壤邻市，IP 定位正常漂移）
- 路径还原：两位买家均为「点广告 → 未当场买 → 转自然搜索回访 → 全价下单」。此前"#1045/#1046 是 SEO 纯增量"的说法作废——本月两张全价单均为广告首触、SEO 收口
- 渠道角色定型：广告=首次触达器（本次助攻成本 ¥54/¥19 每次点击），SEO=收口层，社群=独立种草源（折扣码单）。月底广告评估需按此口径
- 方法沉淀：click_view 城市级核查是归因分歧的终极裁决手段（州级吻合之上再上一层），日报遇分歧时州级裁决已够用，城市级留作人工深查

## 2026-08-10 日报 v2.4：广告助攻单的渠道列写完整旅程

店主反馈：#1045/#1046 渠道列只写"自然搜索+助攻符号"埋没了广告首触的事实。规则修正：地理裁决判定助攻成立的订单，渠道列必须写完整旅程「广告首触(关键词) → 自然搜索收口（跨设备·地理吻合）」，广告出现在开头——与"多次访问报首触"同一原则。

## 2026-08-11 否定词冲突修复：mahjong game 词组降级为完全匹配（change 630954/630968）

- Google 建议"移除冲突否定词"（+2.6%）诊断正确但处方错误：一键 Apply 会整个删掉 "mahjong game" 否定，游戏类垃圾流量回灌
- 实际执行（外科版）：`"mahjong game"` 词组 → `[mahjong game]` 完全匹配。只拦裸查询（纯游戏意图），放行被误伤的自有关键词 "american mahjong game set"（8/5 Semrush 扩词）
- 冲突根因：8/3 加否定在先、8/5 扩词在后，扩词时未对照否定词表。**流程修正：以后每次加词前先跑一遍与共享否定列表的冲突检查**
- 兜底不变：solitaire / free mahjong / mahjong online 等否定词继续拦截其他游戏意图；每周搜索词清洗盯 "mahjong game app/download" 类是否漏进来

## 2026-08-11 Google 建议四连审 + 附加链接升级（change 630991-631004）

对后台四条推荐的裁决（延续"建议逐条审、不点 Apply all"原则）：

| 建议 | 裁决 | 理由 |
|---|---|---|
| 附加链接加描述（+0.1%） | ✅ 已做 | 6 条附加链接（Shop Now/FAQ/About/Shipping/Refund/Home）全部换为带双行描述的新资产（旧链接解挂），文案主打 160 tiles / free shipping / 30-day returns 信任要素，广告占屏面积变大 |
| Import Customer Match（+2.3%） | ⏸ 暂缓 | 现有客户数据约 240 人（28 买家+210 订阅），低于 Search 服务门槛 1,000；且上传客户 PII 需店主明确同意。与 RLSA 解锁点合并等待列表长大 |
| 加词 "game of mahjong"（+0.2%） | ❌ 不采纳 | 游戏意图词，与 8/11 刚修的 [mahjong game] 否定策略一致 |
| Google tag gateway | ⏸ 暂缓 | 转化标签由 Shopify Google 渠道托管，动它风险>收益；当前归因链路已验证畅通（gclid 认领可与订单对上） |

**附带排查**：建议卡片预览里出现 /mahjong/preorder 老落地页和 "early bird pricing" 文案，核查在跑 RSA（811029307407）确认干净（落地 /products/monets-garden、无 preorder 字样、价格 $159.99 正确）——预览是 Google 渲染的历史缓存，无风险。

## 2026-08-11 SEO 专报上线：独立日报+周报（新云端任务）

- 新增独立云端任务：每天 10:06（北京）发【Averill SEO 日报】短报（最新日指标、词层异动、里程碑进度条、元信息改写追踪）；每周一升级为【SEO 周报】全景（Top10 词表、新收录清单、四词群趋势、页面表现、SEO 订单周记、内容建议）
- 分析框架：.claude/skills/seo-report/SKILL.md v1.0；主广告日报升 v2.5，SEO 深度段移交专报、只留一行速览
- 专报数据源仅 GSC + Shopify（不占 NotFair 广告 API 配额），与主日报错峰 1 小时

## 2026-08-10 SEO 周报建议落地：规则速查页 + 尺寸词捡漏（内容层）

按 SEO 周报两条建议执行（依据：教学词 5 词收录但全在 56-70 位且承接页 0 点击；尺寸词 3 词首次收录即 7-10 位）：

1. **新建规则速查页** `/blogs/news/american-mahjong-rules`（Article 618480894249）：清单式规则参考（牌构成表、发牌数字、Charleston 顺序、叫牌规则、Joker 六条、明暗手、胡牌验证、计分惯例、死手判罚、荒庄、规则 FAQ×5），与教程型 beginner's guide 形成"教程+速查"分工；SEO 标题瞄准 rules 词族；未复制 NMJL 牌型卡内容（版权）；互链教程/尺寸文/产品页
2. **尺寸文升级**（mahjong-tile-size-readability）：SEO 标题改 `Standard Mahjong Tile Sizes: Chart & What Reads Best | Averill`（呼应 standard size 词族），正文顶部插入四档尺寸对照表（travel/标准/Averill 0.87×1.25/超大 + 牌架兼容列，数据全部取自文内既有事实）
3. **教程文互链**：首段增加指向规则速查页的入口

观察：教学词族排名（周报每周跟踪）；尺寸词 CTR。新页收录可在 GSC 手动"请求编入索引"加速（店主侧 2 分钟，可选）

## 2026-08-10 SEO 专报 v1.1：操作台账入报

SEO 专报新增"操作台账"栏（对标广告日报的账户改动审计）：每期列出进行中的 SEO 操作及其观察状态，跟踪到出结论结案。首批登记 5 项（8/9 两页元信息改写、8/10 规则页/尺寸文/互链）。

## 2026-08-11 Klaviyo EDM 体系盘点：基建已成，差临门三脚

经 API 审计（key 已由店主提供）：
- **已 live**：Shopify 集成（订单/加购/结账事件流入）、欢迎序列 4 封（AV Welcome，Claire 人设文案）、弃购挽回 3 封（AV Abandon，第三封引导回信 Claire）
- **评价体系定案：Klaviyo Reviews（不装 Judge.me）**——产品页组件已嵌（源码 4 处标记）、评价请求流已建（2 封：What did you think / Thoughts on，订单事件触发，draft）、现无真实评价（仅 1 条被拒的内部测试）
- **三个缺口**：① campaign 发送记录为零——210 订阅者+28 老客是流上线前的存量，永远不会被欢迎流触达，需一次性激活 campaign；② 评价请求流 draft 未开；③ 流内链接 UTM 规范未核（邮件渠道在订单台账显形的前提）
- 待店主批准的动作：评价请求流转 live；给存量发激活/评价邀请 campaign（文案先过目）
- docs/email-flows.md 已加状态注记（载体 Shopify Email → Klaviyo；Judge.me → Klaviyo Reviews），保留作文案底稿

## 2026-08-11 EDM 到达率病根已修，进入验证期

- 旧欢迎流打开率 6-11%（行业基准 40-60%）的两个病根均已修复：① DKIM/SPF 域名验证（约 8/7-8/8 完成）；② 垃圾感文案（"Your welcome code is here"），8/10 换新 AV 序列（Claire 人设文案）并将旧流转 draft
- **验证期（至约 8/18）**：新 AV 欢迎序列在干净环境下积累数据（转盘订阅约 3 人/天进入），第 1 封打开率回到 40%+ = 到达率修复确认
- 行动排序：评价请求流转 live（待店主确认）→ 新流打开率验证通过 → 再执行存量激活 campaign（210 订阅+28 老客）。在验证通过前不做任何群发

## 2026-08-11 EDM 专报上线：第三份定时报告（日报+周报）

- 新增云端任务：每天 11:04（北京）发【Averill EDM 日报】（各流效果/列表增长/到达率验证期跟踪/评价进度/操作台账）；周一升级周报（分流分邮件表格、归因收入占比、列表健康、BFCM 季节段）
- 框架 .claude/skills/edm-report/SKILL.md v1.0，判分基准引自 ecommerce-email-marketing-builder（欢迎流打开 40-60%、弃购人均 $5.81、退订 <0.5%、举报 <0.1%）
- 三报格局定型：09:06 广告 → 10:04 SEO → 11:04 EDM，同群错峰；Klaviyo key 仅存云端任务配置

## 2026-08-11 Instagram API 接入（无 FB 主页方案）

- 接入方式：Instagram API with Instagram Login（IG 独立授权，不绑 Facebook 主页——规避店主担心的封号连带；开发者应用死亡最坏后果=数据断流，IG 账号本身无恙）
- 首拉基线：@averillmahjong，Business 号，77 粉丝、5 帖；**6/25 后停更**，近 30 天触达 59。对照：本月 #1041（Instagram 引荐）、#1048（Facebook 引荐）2 单——社媒是已验证出单渠道但内容断供，恢复发帖优先级应提高
- 数据并入：SEO 专报升 v1.2，周一周报加社媒段（粉丝/触达/新帖表现+停更告警）；token 60 天效期，10 月初续期（专报会自动提醒）
- TikTok 暂不接入（官方 API 需应用审核、投入产出不划算），周度手动看板即可

## 2026-08-11 社媒专报独立（第四报）

- 店主定调：社媒不并入 SEO 专报，独立成报。新增云端任务：每天 12:06（北京）【Averill 社媒日报】（触达/粉丝/新帖/停更计数），周一升级周报（周环比、帖子表、订单联动、内容建议、TikTok 手动占位段）
- 框架 .claude/skills/social-report/SKILL.md v1.0；SEO 专报升 v1.3（摘除社媒段，回归纯 SEO）
- 四报格局（8/11 定稿，应店主要求集中在 9-10 点）：09:06 广告 → 09:18 SEO → 09:30 EDM → 09:42 社媒，12 分钟错峰；graph.instagram.com 已加云端白名单

## 2026-08-11 店铺经营专报上线（第五报，每日首发）

- 新增云端任务：每天 ~08:54（北京，四份流量报之前）发【Averill 经营日报】——昨日成交/履约账龄/库存水位/站点巡检；周一升级【经营周报】含单位经济核算（收入−COGS $75−广告费−手续费=贡献毛利）、渠道毛利拆分、库存周转、运营卫生
- 权限验证：现有 scopes 已够（displayFulfillmentStatus/totalRefundedSet/inventoryQuantity 均可读），无需重装授权
- 框架 .claude/skills/biz-report/SKILL.md v1.0；五报格局：08:54 经营 → 09:06 广告 → 09:18 SEO → 09:30 EDM → 09:42 社媒
- 待办：站点巡检需云端白名单放行 www.averillmahjong.com；TEST/副本变体清理提醒已内置周报

## 2026-08-11 竞品全量基线报告 + 评价流上线

- **评价请求流转 live**（店主拍板）：新买家发货后自动收评价邀请（Klaviyo Reviews），产品页星级供给线打通
- **竞品报告**：接入公司内部竞品监控系统（16 站 266 SKU 全量），产出 docs/competitor-landscape-2026-08.md。核心发现：**Averill $159.99 为全市场最低价**（全尺寸正装地板价 virora $189，行业锚点 $350）；高端缺货潮（TML 可购率 47%、两家超高端全线无货）；预售为行业标准玩法。头号建议：提价评估（方案 A 莫奈 →$189.99 / 方案 B 查尔斯顿 $189.99 上市对照），待店主与张勇决策
- 竞品周度监控暂以浏览器会话人工读数，待内部系统提供 API token 后并入经营周报自动化

## 2026-08-11 飞书企业应用机器人上线（文件与卡片通道）

- 店主创建企业自建应用「Averill 数据机器人」（权限：send_as_bot / im:resource / im:chat:readonly / im:message），已入两群（美式麻将外贸、美式麻将C端日报）
- 通道验证：tenant_access_token 换取 ✓ → 竞品报告 PDF 上传 ✓ → 文件消息发入日报群 ✓（chat_id oc_f92e446e402e2b73b3968e15e3c377c9）
- 能力解锁:发文件本体（PDF 报告直达群）、富文本卡片消息（五报排版升级候选）；webhook 通道保留作降级
- App Secret 仅存云端任务配置与本地会话，不入仓库

## 2026-08-11 竞品专报上线（第六报）：内部监控系统只读 feed 接入

- 开发同事交付只读 feed API（/api/feed/competitors/*，Bearer key 鉴权，无需登录会话）——解决了此前 Supabase 会话令牌无法用于无人值守任务的问题
- 新增云端任务：每天 ~09:54 发【Averill 竞品日报】（变化驱动：新品/调价/下架/价格地板监察，平稳则一行）；周一竞品周报全景（价格带对比基线、促销榜、可购率变迁、抓取健康）
- 框架 .claude/skills/competitor-report/SKILL.md v1.0；基线参照 docs/competitor-landscape-2026-08.md
- 六报格局：08:54 经营 → 09:06 广告 → 09:18 SEO → 09:30 EDM → 09:42 社媒 → 09:54 竞品
- 待办：云端白名单需放行 kol-1-outlook-2-3-usps.vercel.app

## 2026-08-11 GSC 结构化数据修复：Offer 补 3 字段（Merchant listings 警告清除）

- GSC 邮件报 5 个 non-critical 字段缺失，分两类处置：
  - **已修（3 个，theme/snippets/schema.liquid，两个 Offer 分支均补）**：validFrom（产品发布日）、shippingDetails（免运费 + 配送 US）、hasMerchantReturnPolicy（30 天退货窗口 + ReturnByMail）。线上已验证：JSON-LD 解析正常、新字段渲染正确
  - **待评价数据（2 个）**：review / aggregateRating——根因是尚无真实评价，评价请求流 8/11 已 live，首批评价进来后验证 Klaviyo Reviews 组件是否自带 schema，不带则从 metafields 补
- 注意：本次修改在主题副本工作流风险清单内（README 顶部），若换发主题需重放此文件（本仓库有前后版本可 diff）
- GSC 预计 1-2 周内重新抓取后消警；不用手动请求验证

## 2026-08-12 IG 应用被 Meta 风控封禁 → 换新应用恢复

- 首个开发者应用（1608169120892550）创建约 24h 后被 Meta 事后风控封禁 API 访问（"API access blocked"，新应用+新账号+非美 IP 的标准命中画像）。**IG 账号本身无恙**——无 FB 主页绑定方案的风险隔离生效，损失仅为数据断流一天
- 已换新应用重新授权，新 token 8/12 签发（约 60 天效期至 10 中旬），社媒专报云端配置已更新；insights 调用改为动态取账号 id（再换应用无需改配置）
- 顺带：粉丝 77 → 85（+8）
- 经验：Meta 开发者应用尽量用账龄老的 FB 账号创建；新应用 48h 内是风控高危期

## 2026-08-12 社媒日报接入 IG 私信监测（v1.1）

- 每日检查 IG 收件箱待回复会话（最后一条来自对方=待回复），有才报（发送人/首句摘要/等待时长），意向信号（价格/发货/礼包装询问）标 💰 置顶；待回复超 24h 黄牌
- 用途边界经店主确认：仅客服响应与意向线索识别；私信摘要只出现在飞书日报，不入仓库
- 已知盲区：陌生人"消息请求"文件夹 API 不可见，周报每周提醒人工查看

## 2026-08-16 战略转向：Google 纯防守 + Meta 试验开启（change 699174-699192）

店主拍板，数据背书（8/1-16 关键词账本）：
- **暂停购物系列**：8/13 恢复判定失败+零单钟双触发（7/30 起 0 购买烧 ¥2,400+），提前一天执行
- **搜索瘦身 20 词 → 5 词**：留 averill mahjong（品牌防守）、monet 双词（产品词）、mahjong sets for sale + mahjong tiles set（唯二城市级验证出单参与，助攻 $43/单<毛利）；停泛词三巨头（¥1,020/认领单>毛利纯亏）及杂词 15 个
- **预算 ¥445 → ¥80/天**，释放 ~$50/天 试 Meta：Phase A = IG Boost（App 内手动，$10-15/天，55+女性/美国，UTM 必带 utm_source=instagram&utm_medium=paid）；约 9/6 裁决：台账 ≥1 单或 ≥5 加购 → Phase B 建正式 Meta 投放体系；否则止损
- 日报框架 v2.6：防守模式口径（基线重置、升级梯子冻结、Meta 试验每日跟踪）

## 2026-08-16 集合页失位修复：反挤占手术（三件套）

- **病理确认（GSC 词×页交叉）**：品类词展示的承接页从集合页（上周 76 次）完全转移到博客（本周集合页 0 次，how-to-play 23 + 规则页 15）——新信息页把商业页挤出了品类 SERP，SEO 专报告警属实
- **手术①集合页补正文**：原 80 词描述扩至约 350 词选购指南（NMJL 全配置清单、尺寸可读性、新手引导、送礼要点），内链尺寸文/规则页/教程
- **手术②博客回链**：规则页与教程页尾部加品类锚文本 CTA（"American mahjong sets"→集合页），向 Google 声明品类主页归属
- **手术③尺寸文抢精选摘要**：SEO 标题前置具体数字（0.87 × 1.25 in），正文追加 FAQPage 结构化数据（3 问答，script 标签确认存活）
- 观察：SEO 专报操作台账跟踪，预期 1-2 周品类词展示回流集合页；若 8/30 仍未回流，下一步考虑博客页加"主话题指向"（文首导语链接）

## 2026-08-16 补记：销量爆发定性与运营口径更正

- 8/14 起的销量爆发（单日峰值 7 单，IG 引荐+linktr.ee 为主）为**有机社群爆发**，与 IG Boost 无关（Phase A 尚未启动，试验计时改为从首笔 paid 流量起算）；PINKMAHJ 为新社群码，台账按码归群组
- 履约口径：海外仓自动关联发货+人工审核，8/14-16 的 11 单积压属审核队列节奏；48h 红线暂维持，若与仓库正常时效冲突再调
- Charleston 素材拍摄修图中；提价方案 A/B 搁置（清仓期 $128 价与提价冲突，店主定夺"再说"）

## 2026-08-17 Amazon 渠道并入经营日报（SP-API 直连）

- 店主提供 SP-API LWA 凭据，连通验证：北美联合账户全 FBA，近 30 天 35 单（zovadros 莫奈 ~$145 + 垫 ~$32）
- 重大情报入档：**双品牌结构**（Amazon 白牌 zovadros + Averill）；**Charleston 已在 Amazon 建 listing 并压货 576 套**（可售 288+在途 288），首发主战场为 Amazon；zovadros 莫奈主 SKU 存量 58 件（约 6-8 周销速）
- 经营日报 v1.1：新增 Amazon 段（日订单/FBA 库存水位/到仓进度/断货告警），周一单位经济加 Amazon 渠道毛利（佣金 15%+FBA 费粗估）
- 双价风控：同货 Amazon $145 vs 独立站 $159.99，周报每期提示素材差异化
- 凭据仅存云端任务配置；白名单需加 api.amazon.com 与 sellingpartnerapi-na.amazon.com

## 2026-08-24 Amazon 专报上线（第七报）

- 新增云端任务：每天 08:42（北京，七报之首）发【Averill Amazon 日报】——分 SKU 订单/FBA 库存水位与可售周数/Charleston 到仓与首发监测；周一周报含 SKU 环比表、补货倒计时、双渠道收入比
- 分工：经营日报 Amazon 段=速览+红线；Amazon 专报=全部细节。框架 .claude/skills/amazon-report/SKILL.md v1.0
- 七报格局：08:42 Amazon → 08:54 经营 → 09:06 广告 → 09:18 SEO → 09:30 EDM → 09:42 社媒 → 09:54 竞品

## 2026-08-24 Amazon 真实单位经济打通（Finances API）

- 已结算订单可逐单拿真实账本（佣金/FBA费/税分列）。样本（7/22 单）：$149.99+运费$2.99−FBA$8.23=**到手$144.75**，−COGS$75=**毛利~$70/单**
- **⚠ 佣金监察启动**：当前 Commission=$0（疑似新卖家限时减免，正常品类费率 15%≈$22.5/单）——周报每期盯，减免结束即红色告警并重算补货/定价模型。待张勇确认减免政策与到期日
- Amazon 周报 v1.1：单位经济改用 Finances API 真实口径；广告费待确认是否投 Amazon PPC（需另接 Ads API）；头程成本待店主提供

## 2026-08-24 Amazon 口径重大修正 + 专报 v1.2（交易流水视角）

- **修正**：前一节"佣金$0、到手$144.75"漏读了 PromotionList——每单实有 **-$22.50 促销返点**（15% 促销成本）。真实到手 $119.26/单，毛利 ≈$44（COGS $75，头程/广告未计）。教训入档：Finances 解析必须读满 ItemChargeList+PromotionList+ItemFeeList 三个列表
- 流水中另见：退款（8/21 -$127.49）、清算回款（数笔 $8-12，有库存走清算通道，待确认哪批货）、月服务费 $39.99
- 专报 v1.2：日报改交易流水视角（对齐 Seller Central 交易一览：类型/促销返点/费用/到手逐列）；只报 US 市场；新增退款/清算告警；扣费结构监察（佣金$0 与 15% 返点双盯）
- 待张勇确认：15% 促销返点是什么促销、能否关；清算回款对应哪批库存

## 2026-08-24 渠道分工更正

- **独立站（Shopify）负责人：张勇；Amazon 负责人：许世然**（此前误认为张勇兼管 Amazon）
- 前文所有 Amazon 相关"待张勇确认"事项（15% 促销返点是什么促销/能否关、清算回款对应哪批库存、佣金 $0 减免政策与到期日、头程成本、是否投 Amazon PPC）→ **改为待许世然确认**

## 2026-08-24 Amazon 退货率分析（FBA 退货报告 60 天全量）

- 60 天退货 59 套（莫奈）+5 垫，粗算退货率 ~50% 量级（分母待许世然核）；51/64 退回可再售，损失主为双向物流
- 三大主因（买家留言聚类）：①**主图色差**——listing 呈橙色/文案写 orange，实物珊瑚/蜜桃色，≥15 条留言点名，占退货 1/3；②内容物与质感预期落差（误以为含牌架、雕刻深度、尺寸偏小、"not worth the price"）；③比价型买家（Prime day 找到更低价 ×4、转买其他套装 ×5，15% 促销引流的低承诺客）
- 修复清单已出（主图校色+措辞改 Coral/What's Included 图卡/尺寸五点/大促期停 15% 券），待许世然执行
- Amazon 周报 v1.3 新增退货监测段：周退货率/原因 Top3/色差类计数/修复效果跟踪

## 2026-08-24 Amazon 周报增设评价监测（v1.4）

- 可行性已验证：产品页可抓（本地实测 4.5 星/33 评分，评论标题可解析）；每周一抓取入报，含差评专列与退货主因对照、星级告警线 4.3；反爬降级策略内置（被拦即跳过，连续 2 周改人工）
- 待办：云端白名单加 www.amazon.com
