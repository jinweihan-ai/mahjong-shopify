# Google Ads 配置的数据结构剖析

**内部培训材料 · 进阶篇（与《Google Ads 账户诊断与整改实操》配套）**

实操篇讲"怎么修"，本篇讲"为什么长这样"。所有例子来自同一个真实账户（Averill Mahjong，407-451-4233）：实操篇里踩过的每一个坑，都能映射到 Google Ads 数据模型里的一个具体结构。理解了结构，下次排查就不用背案例——先问"这个设置挂在哪个对象上、被谁引用"，十有八九就定位了。

---

## 一、主干：一棵四层的归属树

```
Customer (4074514233)            币种 CNY、时区、自动标记 —— 账户级属性，定了几乎不可改
└── Campaign (23889289563 "monets-US-144$")     投放渠道类型、状态
    └── AdGroup (202159253732 "广告组 1")
        ├── AdGroupAd (811029307407)             ← 广告
        └── AdGroupCriterion (…)                 ← 关键词等条件
```

每个对象有全局唯一 ID，API 里写作资源名 `customers/407.../campaigns/238...`。

**关键认知：树只负责"归属"，不负责"配置"。** 真正有意思的是配置挂在哪一层，以及哪些东西根本不在树上。

---

## 二、引用型对象：树外的共享实体（最容易踩坑的一类）

这些对象独立存在，campaign 只是"指向"它们。**凡是引用型对象，都可能被多个 campaign 共享，也就都有"牵一发动全身"的风险。**

| 对象 | 案例账户实例 | 结构要点 |
|---|---|---|
| **CampaignBudget** | ¥150 / ¥350 两个独立预算 | 预算不是 campaign 的属性，是被引用的独立实体，带 `explicitly_shared` 标志。排查投放停摆时第一个要查它：若多系列共享一个预算池，最便宜的系列会饿死其它系列。它还自带超投语义：单日最高花 2 倍日预算，月度以 30.4 倍日预算兜底 |
| **SharedSet（否定词共享列表）** | `12172690837 "Junk & Irrelevant"` | 词存在列表实体里，列表通过 CampaignSharedSet 链接对象挂到各 campaign。改列表一行，所有挂载的系列同时生效（实操篇"撤回 costco"只改了一行的原因） |
| **BiddingStrategy** | 案例账户为内嵌式 | 两种形态：内嵌在 campaign 里（只影响自己），或独立的"组合出价策略"被多 campaign 引用（改一处影响一片）。诊断时先分清是哪种 |
| **ConversionAction** | 8 个（Shopify Google 渠道应用创建） | 账户级实体，定义"什么事件算转化"：计数方式（ONE/MANY_PER_CLICK）、默认价值、归因窗口 |
| **CustomerConversionGoal** | `ADD_TO_CART × WEBSITE → biddable: false` | **与 ConversionAction 是两套东西。** Goal 是按"类别 × 来源"组成的矩阵，控制该类事件"是否参与竞价"。实操篇的转化目标去污染，改的是这个矩阵，不是转化动作本身——在 ConversionAction 列表里翻半天找不到开关，就是因为这个分层 |

---

## 三、Criterion：一个多态的"万能条件"类型

Google Ads 把所有"定向/限制条件"抽象成 Criterion 一种类型，靠 `type` 字段区分（KEYWORD / LOCATION / DEVICE / AD_SCHEDULE / LISTING_GROUP / …），且**同一类型可出现在两层，语义不同**：

```
Campaign 层 (campaign_criterion)：
├── LOCATION: geoTargetConstants/2840（美国）      ← 地理定向
├── KEYWORD + negative: true                       ← 系列级否定词
├── DEVICE: bid_modifier                           ← 设备出价系数（-100% 即排除）
└── LISTING_GROUP: 商品分组树                       ← 购物系列专属（见下）

AdGroup 层 (ad_group_criterion)：
├── KEYWORD: "averill mahjong" EXACT + 质量得分 + 出价   ← 正向关键词
└── LISTING_GROUP: 细分节点
```

两个实战映射：

- **质量得分（QS）是 keyword-criterion 层的属性**，不是 campaign 的。诊断 QS 必须下钻到词级；"账户 QS"这种说法在数据模型里不存在
- **购物系列的商品控制是一棵"剖分树"（product partition tree）**：根节点"所有商品"，可按 item_id / 品牌 / 商品类型 / 自定义标签逐层剖分，每个叶子要么有出价、要么被排除。实操篇"排除 Charleston"的真实操作：在树上剖出 `item_id = shopify_zz_10133...` 的叶子并标记 excluded。**不存在"暂停某个商品"的操作，只有树结构变换**——这也是为什么购物系列没有"商品级暂停按钮"

---

## 四、广告：三明治结构

```
AdGroupAd（包装层）              ← 投放状态、审核结果 (policy_summary) 挂这层
└── Ad (811029307407)           ← 广告本体：final_urls（落地页）挂这层
    └── RSA 素材：headlines[≤15] + descriptions[≤4]   ← 数组，可 pin 固定位置
```

- 排查"广告怎么不投了"看**包装层**的 approval_status（出价塌陷排查时查的就是它）
- 改落地页改的是 **Ad 层**的 `final_urls`
- RSA 的本质是"给 Google 自由组合的素材数组"，"广告效力"评的是数组的多样性与覆盖度，不是某一条文案的好坏

---

## 五、报表层：一切皆视图（View）

GAQL 查的不是表，是**预定义视图 + 段（segments）爆破**：

- `campaign` / `keyword_view` / `search_term_view` / `shopping_performance_view`——**FROM 决定行的粒度，没有 JOIN**。想跨粒度分析只能查多次自己拼
- **segments 是行爆破器**：加 `segments.date` 一行变 N 行；加 `segments.conversion_action_name` 再爆一次。实操篇破解"转化价值 ¥50,791 之谜"用的正是这一招——聚合数字骗人，按段爆开就对账了
- 三个度量衡约定，读错必误判：
  1. 金额全是 **micros**（除以 10⁶ 才是元）
  2. 枚举是**整数**（如出价策略 `9` = TARGET_SPEND、`10` = MAXIMIZE_CONVERSIONS）
  3. **转化记在点击发生日**，不是转化发生日——这就是"转化回填"现象的由来：历史日期的购买数会随时间上涨，日报必须回看历史行而不是只看昨天

---

## 六、修改层：全量审计的 mutate 流水

所有写操作都是 mutate operation，写入后进入 `change_event` 流水（实操篇每笔改动的 change ID 530764、546020… 即来自此层）。

**含义：账户没有"悄悄改了"这回事。** 谁在哪天砍了预算、建了测试系列、改了出价，change_event 都能翻出来——接手陌生账户时，先拉 30 天变更流水，比听任何人口头交接都可靠。

---

## 七、实战坑位 → 数据结构对照表

| 实操篇踩的坑 | 数据结构层面的原因 |
|---|---|
| 48 个"转化"只有 6 笔购买 | ConversionAction（定义事件）与 CustomerConversionGoal（竞价矩阵）分层，三类事件都在矩阵里开了 biddable |
| 转化价值虚高 7 倍 | conversions_value = 所有 biddable 动作的价值之和；不用 segments 爆破就看不见构成 |
| 智能出价塌陷（展示掉到 1 次/天） | 内嵌 BiddingStrategy 依赖 Goal 矩阵产出的信号量——数据模型里是两个独立对象，业务上却强耦合，改一个不改另一个就出事 |
| 否定词一次生效两个系列 | SharedSet 引用结构 + CampaignSharedSet 链接 |
| "排除" Charleston 商品 | listing group 剖分树的叶子节点操作 |
| 预算 ¥350 花出 ¥700 | CampaignBudget 独立实体自带超投语义（日 2×、月 30.4× 兜底） |
| 品牌词 CPC ¥13.5 | 品牌查询靠泛词 phrase-criterion 匹配进来，QS 挂在词级——没有专属 criterion 就没有专属的质量积累 |

---

## 总结

**Google Ads = 一棵浅的归属树 + 一堆可共享的引用实体 + 一个多态 Criterion 系统 + 只读的视图报表层 + 全审计的修改流水。**

排查任何配置问题的通用三问：

1. 这个设置挂在**哪个对象**上？（树上哪层 / 还是树外的引用实体？）
2. 这个对象**被谁引用**？（改它会波及哪些 campaign？）
3. 我看到的数字是**哪个视图、什么粒度、爆了哪些段**？（聚合数字先拆分再下结论）
