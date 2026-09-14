# 数据 API 文档(镜像库 · PostgREST)

更新:2026-09-14。长期维护:表结构、口径或同步策略一变就改这里。配套:[data-lineage.md](data-lineage.md)。

## 0. 一句话

应用**只读镜像库,永不直连 Amazon/Shopify/云仓**。读永远不阻塞;数据是不是新的看 `meta.freshness`;觉得旧了就调 `rpc/request_sync` 排队一次同步,然后继续用手里的数据,稍后再读。**「查不到就同步」不做**:空结果常常是正确答案(那天就是没订单),按空触发会把 API 配额打爆、把请求挂住几分钟。

## 1. 接入

| 项 | 值 |
|---|---|
| 库 | Postgres 15(supabase/postgres 镜像),首尔服务器,库名 `mirror` |
| REST | PostgREST v12,`http://127.0.0.1:3000`(**只绑本机**;外部应用先走 SSH 隧道,上完整 Supabase 后走 Kong+JWT) |
| 直连 | `PG_DSN`(首尔 env),Python 用 `mirror.py` |
| schema | `raw` 原始镜像 · `derived` 派生(预留)· `meta` 同步状态与请求 |
| 选 schema | 读:请求头 `Accept-Profile: raw`;写/RPC:`Content-Profile: meta` |
| 角色 | `web_anon`:raw/derived/meta 只读 + 允许调 `meta.request_sync` |

PostgREST 语法速查:`?select=a,b&col=eq.x&col2=gte.2026-09-01&order=col.desc&limit=100`;嵌入 JSON 列用 `payload->>'key'`;分页 `Range: 0-99`。

```bash
curl -H 'Accept-Profile: raw' 'http://127.0.0.1:3000/wms_orders?select=order_code,platform,date_shipping&platform=eq.TIKTOK&order=date_shipping.desc&limit=50'
curl -H 'Accept-Profile: meta' 'http://127.0.0.1:3000/freshness'
curl -X POST -H 'Content-Type: application/json' -H 'Content-Profile: meta' -d '{"p_source":"wms","p_by":"daily-report"}' http://127.0.0.1:3000/rpc/request_sync
```

Python:
```python
import mirror
mirror.ensure(['wms'])                     # 超过 6h 未同步就先同步(阻塞);wait=False 则后台同步、先用旧数据
rows = mirror.q('select * from raw.wms_orders where date_shipping >= %s', ('2026-09-01',))
mirror.status()                            # = meta.sync_state
```

## 2. 新鲜度与同步(应用该怎么用)

- **定时**:`mirror_sync.py` 每天 06:30、18:30 全部来源增量;周日 22:00 拉 Amazon 台账/退货报告(慢,单独)。
- **看新鲜度**:`meta.freshness`(视图):`source, last_ok, age_minutes, stale(>6h), rows_last, note`。应用把 `age_minutes` 显示在页面上,而不是猜。
- **要求同步**:`meta.request_sync(p_source, p_by)`(RPC)。来源可填组名 `amazon / shopify / wms / mercury` 或细项 `amazon_orders / amazon_finance / amazon_fba / amazon_reports`。返回 `{ok, queued, request_id, age_minutes}`;同一来源已在排队或运行时 `queued=false`,不会重复起。
- **谁去跑**:`sync_worker.py` 每分钟一次,整机单飞(文件锁),按请求顺序执行 `mirror_sync.py <source>`,结果写回 `meta.sync_requests(status: queued/running/done/failed, note)`。应用可以轮询 `sync_requests?id=eq.N` 或直接看 `freshness` 的 `last_ok` 变了没有。
- **耗时预期**:shopify / wms / mercury 各 5–15 秒;amazon_orders 增量 1–3 分钟(订单行限流 0.5 rps),全量 30 分钟以上;amazon_finance 1–5 分钟;报告类只走周日。
- **建议阈值**:日报、看板用 6h;做月结、对账用 24h 内即可;需要「此刻」的场景(库存断货判断)先读旧值展示,再 `request_sync('wms')`,下一次刷新自然变新。

## 3. 表目录(raw)

约定:每张表都有 `payload jsonb`(原始对象,字段以平台为准)和 `synced_at`;抽出来的列只为了索引和常用查询。主键=平台唯一键。**只 upsert 不删**;快照类表按 `snap_date` 追加。

### Amazon(SP-API,美国站)
| 表 | 主键 | 关键列 | 口径/备注 |
|---|---|---|---|
| amazon_orders | order_id | purchase_date, last_update, status, order_total, currency, items_shipped | 增量按 LastUpdatedAfter 回看 3 天;零元订单=达人 100% 折扣码寄样 |
| amazon_order_items | order_item_id | order_id, seller_sku, asin, qty, item_price | 只对更新过的订单重拉 |
| amazon_finance_groups | group_id | start_at, end_at, status(Open/Closed), original_total | Open 组每次重拉 |
| amazon_finance_events | event_id(组 id+内容哈希) | group_id, event_type(ShipmentEventList/RefundEventList/ProductAdsPaymentEventList/ServiceFeeEventList/AdjustmentEventList…), posted_at, order_id, seller_sku, qty | 结算口径;单品账只从这里取平台费/退款,销量与收入以 amazon_orders/order_items 的下单日为准 |
| amazon_fba_inventory_daily | (snap_date, seller_sku) | fulfillable, reserved, inbound, unsellable | 每天一行 |
| amazon_ledger_events | row_hash(行+出现序号) | event_date, msku, event_type(Receipts/Shipments/CustomerReturns/Adjustments/VendorReturns/WhseTransfers), qty, disposition, fc | 来自 GET_LEDGER_DETAIL_VIEW_DATA;**同内容重复行是真实事件**,不能去重 |
| amazon_returns | row_hash | return_date, order_id, sku, qty, disposition(SELLABLE/CUSTOMER_DAMAGED/…), status, reason | 来自退货报告 |

### Shopify(独立站)
| 表 | 主键 | 关键列 | 口径/备注 |
|---|---|---|---|
| shopify_orders | id(gid) | name, created_at, updated_at, test, cancelled_at, financial_status, total, subtotal, shipping, tax, discounts, refunded | payload 含 lineItems / refunds / transactions(fees=支付手续费);updated_at 回看 3 天 |
| shopify_order_lines | line_id | order_id, sku, title, qty, original_total, discounted_total | discounted_total 已含订单级折扣分摊 |
| shopify_inventory_daily | (snap_date, variant_id) | sku, inventory_quantity | 前台可售数,不分仓 |

### YunWMS(海外仓,SOAP)
| 表 | 主键 | 关键列 | 口径/备注 |
|---|---|---|---|
| wms_orders | order_code | reference_no(平台单号), platform(SHOPIFY/TIKTOK/OTHER=寄样), status(D 已发/W 待发/X 取消), date_shipping, total_fee, fee_currency | payload.items 行项目;payload.fee_details 每单运费/操作费 |
| wms_order_items | (order_code, product_sku) | qty | product_sku:1=莫奈,2=查尔斯顿 |
| wms_inventory_daily | (snap_date, product_sku, warehouse_code) | sellable, reserved, onway, pending, unsellable, shipped | 每天一行 |
| wms_cost_water | cbl_id | order_code, ft_code, ft_name, kind(扣款/入款/退款), amount, currency, add_time | **费用只取 kind=扣款**;入款是给账户充值(工行付远邦的钱) |
| wms_storage_costs | wis_id | is_date, amount, currency, volume, qty | 按日仓租 |
| wms_asn | receiving_code | status(E 已收/Z 在途…), date_create, date_received | 入库单 |
| wms_asn_items | (receiving_code, product_sku) | qty_expected, qty_received | 分仓的依据 |

### Mercury(美元账户)
| 表 | 主键 | 关键列 | 备注 |
|---|---|---|---|
| mercury_transactions | id | posted_at, amount, counterparty, description, kind, status | 目前只有 Shopify 打款进账 |

### meta
| 对象 | 说明 |
|---|---|
| sync_state | 每来源:last_ok, last_try, watermark, rows_last, note |
| freshness(视图) | 加 age_minutes、stale(>6h) |
| sync_requests | 请求队列:source, requested_by, status, started_at, finished_at, note |
| request_sync(text, text) | RPC,见第 2 节 |

## 4. 常用查询(可直接抄)

```sql
-- 独立站每日按 SKU 出库(以海外仓发货为准)
select date_shipping::date d, i.product_sku, sum(i.qty) units
from raw.wms_orders o join raw.wms_order_items i using(order_code)
where o.platform='SHOPIFY' and o.status='D' group by 1,2 order by 1;

-- 海外仓每月尾程费用按 SKU 分摊
select to_char(c.add_time,'YYYY-MM') m, i.product_sku, round(sum(c.amount*i.qty::numeric/t.total_qty),2) usd
from raw.wms_cost_water c join raw.wms_order_items i using(order_code)
join (select order_code, sum(qty) total_qty from raw.wms_order_items group by 1) t using(order_code)
where c.kind='扣款' group by 1,2 order by 1,2;

-- Amazon 按下单日的 SKU 销量与商品收入(不等结算)
select o.purchase_date::date d, i.seller_sku, sum(i.qty) units, sum(i.item_price) gross
from raw.amazon_orders o join raw.amazon_order_items i using(order_id)
where o.status not in ('Canceled','Pending') group by 1,2 order by 1;

-- FBA 数量平衡
select msku, event_type, disposition, sum(qty) from raw.amazon_ledger_events group by 1,2,3 order by 1,2,3;
```

## 5. 变更规则

- 加表/加列:改 `mirror_sync.py` 的 DDL(`create table if not exists` / `alter table add column if not exists`),部署即生效;同时改本文第 3 节。
- 改口径(比如某列含义变了):不覆盖旧列,加新列;派生表跟着改,血缘文档同步。
- 凭据:只在首尔 env(`PG_DSN`、`YUNWMS_*`、`AMZ_*`、`SHOPIFY_*`、`MERCURY_API_TOKEN`),不进仓库、不进文档。
- 对外暴露:上完整 Supabase 之前,不把 3000/5432 端口开到公网;应用与库同机或走 SSH 隧道。

## 6. 已知限制

- Amazon 单品口径=**下单日**:销量/收入来自订单行(下单当天可见),平台费结算到了用实付、没到按该 SKU 近 60 天每件均费预估并记在「预估平台费USD」「未结算套数」两列;结算到齐后自动替换成实数。退款按退款日。
- 镜像起始:Amazon 2026-01-01,Shopify 2025-10-01(实际 2026-07 开卖),YunWMS 2026-01-01,Mercury 2025-10-01。更早的没有。
- 台账/退货报告靠周日定时,平时是上周的;需要更新走 `request_sync('amazon_reports')` 只重装本地 JSON,不重拉报告。
- 内存 1.9G:不要在库里跑大 join 的实时看板,派生结果落 `derived` 或飞书表。
