---
name: edm-report
description: Averill EDM（Klaviyo）专报的分析方法论与输出规范（云端日报/周报任务专用，v1.1）
---

# Averill EDM 专报框架 v1.1

云端 EDM 专报任务的分析大脑。与广告日报/SEO 专报并列的第三份报告，覆盖 Klaviyo 邮件营销全链路。基准参考 ecommerce-email-marketing-builder 方法论。

## 日期口径

- Klaviyo 数据近实时；"昨日" = 北京时间前一自然日；周一发周报（上周 vs 再上周），其他天发日报
- 用 Bash date 确认北京时间与星期

## 背景与基线（随进展更新本节）

- **到达率验证：✅ 已通过**（8/16 实测新欢迎流打开率 56-63%、弃购流 67-100%，远超 40% 门槛；旧流 6-11% 为历史病历不入基线）。**存量激活 campaign（210 订阅+28 老客）已解锁**，待店主审批文案后发送——发送前每周提醒一次该解锁项，不再每日跟踪
- **行业基准（判分标准）**：欢迎流打开率 40-60%；弃购流人均收入基准 $5.81（Klaviyo 2026）；退订 <0.5%/封；垃圾举报 <0.1%
- **现役资产**：AV 欢迎序列 4 封（live，8/10 起）；AV 弃购 3 封（live）；评价请求 2 封（draft，待店主开闸）；Klaviyo Reviews 已嵌产品页（0 真实评价起步）
- **列表底数**：约 210 订阅 + 28 老客（8/11 时点）；转盘新增约 3 人/天
- **待办里程碑**：① 评价请求流转 live；② 验证期过后存量激活 campaign（210+28，文案需店主过目）；③ 流内链接 UTM 核查（utm_source=klaviyo）
- **季节节点预警**（提前 3 周提醒）：Labor Day 9/1；BFCM 预热 11 月初、主战 11/27-11/30——10 月中旬起周报须含 BFCM 邮件计划段

## 数据拉取（Klaviyo API，Header: Authorization: Klaviyo-API-Key <key>, revision: 2024-10-15）

1. 流清单与状态：GET /api/flows/
2. 流效果：POST /api/flow-values-reports/（timeframe last_7_days；周报加 last_30_days；conversion_metric_id=XzHWzs 即 Placed Order；statistics: recipients, delivered, open_rate, click_rate, conversions, conversion_value, unsubscribes, bounced, spam_complaints）
3. 列表增长：POST /api/metric-aggregates/（metric_id=UAetYY "Subscribed to Email Marketing"，measurements ["count"]，interval day，近 7 天，timezone Asia/Shanghai）
4. 评价：GET /api/reviews/（按 status 计数：approved/pending/rejected）
5. campaign（如有）：GET /api/campaigns/?filter=equals(messages.channel,'email')

## 同构原则

日报=变化驱动快讯（异动与待办才出现），周一=全景。

## 日报内容（非周一，短报；全无异动时"EDM 平稳"一行+评价数）

1. 流指标：仅当任一 live 流昨日指标对 7 日均值异动 ±20%（或出现退订/举报）才展开该流一行；平稳不逐流罗列
2. 列表增长：仅当昨日新订阅为 0（连 3 天触发🟡）或单日 ≥10（异常放量）才报
3. 评价进度：approved 数有新增才报（"评价 +N → 累计 X"）
4. 操作台账：仅列状态有变化或到结论窗口的项
5. 归因收入：昨日有邮件归因订单才报（这是最该被看见的信号）

## 周报内容（周一，全景）

1. 周环比总览：总发送/打开/点击/归因收入/退订
2. 分流分邮件表格：每封 收件/打开/点击/转化
3. 邮件归因收入 vs 店铺总收入占比（成熟 DTC 基准 20-30%，起步期不设指标只报趋势）
4. 列表健康：净增长、退订率、跳出率、垃圾举报
5. 待办里程碑进度（评价流/存量激活/UTM）
6. 建议 ≤2 条带置信度；BFCM 窗口期（10 月中起）附计划段

## 告警（触发才写）

- 🔴 任一流打开率 <20%（样本 ≥20）——到达率问题复发
- 🔴 垃圾举报率 >0.1% 或 单日退订 >5
- 🟡 弃购流连续 3 天 0 触发（Shopify 集成断线嫌疑）
- 🟡 列表连续 3 天零新增（转盘/表单故障嫌疑）

## 输出格式

标题：【Averill EDM 日报 YYYY-MM-DD】或【Averill EDM 周报 YYYY-MM-DD（第N周）】
纯文本单条飞书消息，末尾水印"📚 EDM框架 v1.1"（与本文件标题版本一致，不可省略）
