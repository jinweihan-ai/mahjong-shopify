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
