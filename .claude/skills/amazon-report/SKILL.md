---
name: amazon-report
description: Averill Amazon 专报的分析方法论与输出规范（云端日报/周报任务专用，v1.5）
---

# Averill Amazon 专报框架 v1.5

第七份定时报告，只讲 Amazon。与经营日报的分工：经营日报的 Amazon 段是"速览+红线"，本报承载全部细节与渠道运营判断。

## 日期口径

- "昨日" = 北京时间前一自然日（Amazon 订单 PurchaseDate 为 UTC，换算归日）
- 周一发周报（上周 vs 再上周），其他天发日报

## 账户基线（2026-08，随进展更新）

- **只报 US 市场（ATVPDKIKX0DER）**，CA/MX/BR 一律不拉不报（店主定）；全 FBA
- **双品牌**：zovadros（白牌）= 莫奈套装 B0GCHWVXK9（~$145）+ 麻将垫 B0G14B92XR 等（~$32）；**Averill** = Charleston B0HDCQR7LD（可售 288 + 在途 288，尚未开售/首发主战场）
- 基线销速：约 35 单/月（8 月中）；莫奈主 SKU（TB-MDGB-2KGR）可售 58 件
- 双价风控背景：zovadros 莫奈 $145 vs 独立站 Averill $159.99

## 日报内容（非周一）——交易流水视角（对齐 Seller Central 交易一览）

1. **昨日交易流水表**（Finances API listFinancialEvents，PostedDate 昨日）：
   `日期 | 类型 | 订单尾号 | 商品价 | 促销返点 | 亚马逊费用 | 到手`
   类型映射：Shipment=订单付款；Refund=退款；ServiceFee=服务费；Adjustment/其他=清算等（照实翻译）。**逐项必读 ItemChargeList + PromotionList + ItemFeeList 三个列表**（教训：漏 PromotionList 会虚高 $22.5/单）；Tax/ShippingTax 代收代缴剔除
2. 昨日合计：到手 $X（订单付款 X 笔 − 退款 X 笔 − 费用）
3. FBA 库存水位表：各在售 SKU 可售/在途；按近 7 天销速估算可售周数
4. **Charleston 到仓监测**：在途 288 的落仓进度，可售数变化当天必报
5. 平稳就短，不硬凑

## 周报内容（周一，全景）

1. 周环比：订单/收入/AOV，分 SKU 表
2. 库存周转与补货倒计时：各 SKU 触线预估日期
3. 渠道对比一句话：Amazon vs 独立站本周收入比
4. MX/CA/BR 扫一眼（有单才展开）
5. 双价风控提示（每期固定一句）
6. 建议 ≤2 条带置信度

## 真实单位经济（v1.5，仅周一，数据源 Finances API）

对上周已结算订单逐单拉 GET /finances/v0/orders/<AmazonOrderId>/financialEvents（逐单 sleep 1 秒防限速）：
- 单均真实到手 = Principal + ShippingCharge − 促销返点（PromotionList）+ 各项费用（ItemFeeList 负值直接加）；Tax 代收代缴剔除。**基线（2026-08）：套装单均到手 ≈ $119.26**（$149.99 − 促销返点 $22.50 − FBA $8.23），毛利 ≈ $44/单（COGS $75，头程未计）
- 周合计另列：退款笔数与金额、清算回款、月服务费 $39.99（出现当期计入）
- **扣费结构监察（每周必报）**：① Commission 当前 $0（疑似新卖家减免）——转非零即 🔴"佣金开始收取，毛利再 −$22 量级"；② 促销返点当前恒定 -$22.50/单（15% 促销）——**待张勇说明这是什么促销、能否关**；返点率变化 ±3pt 即报
- 广告费：账户如投 Amazon PPC 需另接 Ads API（未接入前注明"广告费未计"）

## 退货监测（v1.5，仅周一，数据源 Reports API）

每周拉 FBA 退货报告（POST /reports/2021-06-30/reports，reportType=GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA，近 30 天窗口，轮询 DONE 后下载解析 TSV）：
- 报：周退货件数、粗算退货率（÷ 同期订单数）、原因 Top3、**色差类留言计数**（关键词 color/orange/peach/coral/bright）
- 背景基线（2026-08-24 全量分析）：60 天退 59 套，三大主因=①主图色差（橙 vs 珊瑚，~1/3）②内容物/质感预期落差（牌架/雕刻深度/尺寸）③比价型买家（Prime 促销期集中）。修复清单已交许世然（主图校色/What's Included 图卡/尺寸五点/促销重审）
- **修复效果跟踪**：listing 修复上线后，色差类退货周计数应趋势性下降；连续 2 周不降 → 提示修复未生效
- 🟡 周退货率 >15% 或色差类留言周增 ≥3 条

## 评价监测（v1.5，仅周一，数据源：产品页抓取）

每周一抓 zovadros 莫奈产品页（https://www.amazon.com/dp/B0GCHWVXK9，带完整浏览器 UA + Accept-Language: en-US；Charleston B0HDCQR7LD 开售后加入）：
- 解析：星级（`([\d.]+) out of 5 stars` 首个）、总评分数（`([\d,]+) global ratings`）、页内评论标题与各自星级（review-title 与 a-icon-alt 标记）
- 报：当前星级 | 总评分数及周增 | 本周新见评论标题；**≤3 星差评专列**并提炼主题词（色差/质量/尺寸/缺件），与退货三大主因对照——退货修复生效的话差评主题也应同步收敛
- 基线（2026-08-24）：4.5 星 / 33 评分；页内高频词"Beautiful tiles"
- **反爬降级**：被 robot check 拦截则写"⚠ 评价抓取被拦，本周跳过"（一次尝试不重试）；连续 2 周被拦 → 提示改人工通道（许世然后台导出）
- 🟡 星级跌破 4.3 或单周新增 ≥2 条 ≤3 星差评

## 告警（触发才写）

- 🔴 莫奈主 SKU 可售 <30 / 🟡 <45
- 🟡 任一在售 SKU 断货超 3 天
- 🟡 昨日 0 单且近 7 天日均 ≥1
- 🟡 出现退款（单笔即报：订单号+金额）
- 🟡 出现清算（Liquidation）回款——说明有库存进入清算通道，列明细并提示人工确认是哪批货
- 🔴 Charleston 可售数开始下降但从未报告过开售（说明悄悄开卖了，需要人工确认定价与 listing 状态）
- 🔴 API 拉取连续 2 天失败（refresh token 或权限问题）

## 输出格式

标题：【Averill Amazon 日报 YYYY-MM-DD】或【Averill Amazon 周报 YYYY-MM-DD（第N周）】
纯文本单条飞书消息，末尾水印"📚 Amazon框架 v1.5"（与本文件标题版本一致，不可省略）
