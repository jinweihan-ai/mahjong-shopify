---
name: edm-report
description: Averill EDM（Klaviyo）专报的分析方法论与输出规范（云端日报/周报任务专用，v1.0）
---

# Averill EDM 专报框架 v1.0

云端 EDM 专报任务的分析大脑。与广告日报/SEO 专报并列的第三份报告，覆盖 Klaviyo 邮件营销全链路。基准参考 ecommerce-email-marketing-builder 方法论。

## 日期口径

- Klaviyo 数据近实时；"昨日" = 北京时间前一自然日；周一发周报（上周 vs 再上周），其他天发日报
- 用 Bash date 确认北京时间与星期

## 背景与基线（随进展更新本节）

- **到达率验证期（至约 8/18）**：旧欢迎流曾因域名未验证+垃圾感文案打开率仅 6-11%（历史病历，不入基线）。8/7-8 完成 DKIM/SPF、8/10 上线新 AV 序列。验证判据：新欢迎流第 1 封累计打开率 ≥40%（样本 ≥20 再判）
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

## 日报内容（非周一，短报 8-12 行）

1. 昨日/近7天速览：各 live 流 收件/打开率/点击率/归因订单与收入
2. 列表增长：昨日新订阅 N（近 7 天日均对比）
3. 验证期跟踪（8/18 前每天必报）：新欢迎流第 1 封累计样本数与打开率 → 距 40% 门槛
4. 评价进度：累计 approved 数（产品页星级的燃料）
5. 操作台账：从 README 提取 EDM 相关在途操作，跟踪到结案（同 SEO 专报机制）
6. 无异动明说"平稳"

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
纯文本单条飞书消息，末尾水印"📚 EDM框架 v1.0"（与本文件标题版本一致，不可省略）
