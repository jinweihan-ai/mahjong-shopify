# 数据 API 文档(镜像库 · PostgREST)

更新:2026-09-14。长期维护:表结构、口径或同步策略一变就改这里。配套:[data-lineage.md](data-lineage.md)。

## 0. 一句话

应用**只读镜像库,永不直连 Amazon/Shopify/云仓**。读永远不阻塞;数据是不是新的看 `meta.freshness`;觉得旧了就调 `rpc/request_sync` 排队一次同步,然后继续用手里的数据,稍后再读。**「查不到就同步」不做**:空结果常常是正确答案(那天就是没订单),按空触发会把 API 配额打爆、把请求挂住几分钟。

## 1. 接入

| 项 | 值 |
|---|---|
| 库 | Postgres 15(supabase/postgres 镜像),首尔服务器,库名 **`postgres`**(2026-09-14 从 `mirror` 迁入;旧库暂留作备份) |
| REST | Supabase 网关(Kong)`https://data.szzn-company.online/rest/v1/`(DNS 解析并签证书后可用);本机 `http://127.0.0.1:8000/rest/v1/`。**每个请求带 `apikey: <ANON_KEY>`**(匿名只读);写/RPC 用登录后的 JWT 或 SERVICE_KEY。key 在首尔 env `SB_ANON_KEY` / `SB_SERVICE_KEY` |
| 直连 | `PG_DSN`(首尔 env),Python 用 `mirror.py` |
| schema | `raw` 原始镜像 · `derived` 派生(预留)· `meta` 同步状态与请求 |
| 选 schema | 读:请求头 `Accept-Profile: raw`;写/RPC:`Content-Profile: meta` |
| 角色 | `anon`(匿名):raw/derived/meta 只读;`authenticated`/`service_role`:另可调 `meta.request_sync`。Studio 在 `https://data.szzn-company.online/`(HTTP Basic,账号密码在首尔 env `SB_DASHBOARD_*`);Auth 在 `/auth/v1/`(已关自助注册,用户由 Studio 或 service key 创建) |

PostgREST 语法速查:`?select=a,b&col=eq.x&col2=gte.2026-09-01&order=col.desc&limit=100`;嵌入 JSON 列用 `payload->>'key'`;分页 `Range: 0-99`。

```bash
A="apikey: $(grep ^SB_ANON_KEY= /opt/feishu-rerun/env | cut -d= -f2)"
curl -H "$A" -H 'Accept-Profile: raw' 'http://127.0.0.1:8000/rest/v1/wms_orders?select=order_code,platform,date_shipping&platform=eq.TIKTOK&order=date_shipping.desc&limit=50'
curl -H "$A" -H 'Accept-Profile: meta' 'http://127.0.0.1:8000/rest/v1/freshness'
# RPC 要登录身份:apikey 用 SERVICE_KEY(服务端)或用户 JWT(前端)
S="$(grep ^SB_SERVICE_KEY= /opt/feishu-rerun/env | cut -d= -f2)"
curl -X POST -H "apikey: $S" -H "Authorization: Bearer $S" -H 'Content-Type: application/json' -H 'Content-Profile: meta' -d '{"p_source":"wms","p_by":"daily-report"}' http://127.0.0.1:8000/rest/v1/rpc/request_sync
```

Python:
```python
import mirror
mirror.ensure(['wms'])                     # 超过 3h 未同步就先同步(阻塞);wait=False 则后台同步、先用旧数据
rows = mirror.q('select * from raw.wms_orders where date_shipping >= %s', ('2026-09-01',))
mirror.status()                            # = meta.sync_state
```

## 2. 新鲜度与同步(应用该怎么用)

- **定时**:`mirror_sync.py` **每 2 小时**(整点,0/2/4…22 点)全部来源增量,和请求队列共用一把锁(`/tmp/sync_worker.lock`)不会并跑;周日 22:00 拉 Amazon 台账/退货报告(慢,单独)。
- **看新鲜度**:`meta.freshness`(视图):`source, last_ok, age_minutes, stale(>3h), rows_last, note`。应用把 `age_minutes` 显示在页面上,而不是猜。
- **要求同步**:`meta.request_sync(p_source, p_by)`(RPC)。来源可填组名 `amazon / shopify / wms / mercury / uppromote` 或细项 `amazon_orders / amazon_finance / amazon_fba / amazon_reports`。返回 `{ok, queued, request_id, age_minutes}`;同一来源已在排队或运行时 `queued=false`,不会重复起。
- **谁去跑**:`sync_worker.py` 每分钟一次,整机单飞(文件锁),按请求顺序执行 `mirror_sync.py <source>`,结果写回 `meta.sync_requests(status: queued/running/done/failed, note)`。应用可以轮询 `sync_requests?id=eq.N` 或直接看 `freshness` 的 `last_ok` 变了没有。
- **耗时预期**:shopify / wms / mercury 各 5–15 秒;amazon_orders 增量 1–3 分钟(订单行限流 0.5 rps),全量 30 分钟以上;amazon_finance 1–5 分钟;报告类只走周日。
- **建议阈值**:日报、看板用 3h(定时是 2h 一次,超过 3h 说明定时挂了);做月结、对账用 24h 内即可;需要「此刻」的场景(库存断货判断)先读旧值展示,再 `request_sync('wms')`,下一次刷新自然变新。

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
| shopify_finance_daily | snap_date | payments_balance_usd(Shopify Payments 待打款), unfulfilled_paid_usd / unfulfilled_paid_orders(已付未发=预收) | 每天一行 |

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
| mercury_accounts_daily | (snap_date, account_id) | name, status, available_balance, current_balance | 每天一行 |

### UpPromote(达人佣金)
| 表 | 主键 | 关键列 | 备注 |
|---|---|---|---|
| uppromote_unpaid_daily | (snap_date, row_no) | affiliate, total_commission | 未付佣金快照,每天一行一笔 |

### meta
| 对象 | 说明 |
|---|---|
| sync_state | 每来源:last_ok, last_try, watermark, rows_last, note |
| freshness(视图) | 加 age_minutes、stale(>3h) |
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
- 对外暴露:只经 nginx(80/443)→ Kong(127.0.0.1:8000);5432 只绑本机。Studio 有 Basic Auth,REST 必须带 apikey;前端应用用 `@supabase/supabase-js` 直接连 `https://data.szzn-company.online` + ANON_KEY。

## 6. 已知限制

- Amazon 单品口径=**下单日**:销量/收入来自订单行(下单当天可见),平台费结算到了用实付、没到按该 SKU 近 60 天每件均费预估并记在「预估平台费USD」「未结算套数」两列;结算到齐后自动替换成实数。退款按退款日。
- 镜像起始:Amazon 2026-01-01,Shopify 2025-10-01(实际 2026-07 开卖),YunWMS 2026-01-01,Mercury 2025-10-01。更早的没有。
- 台账/退货报告靠周日定时,平时是上周的;需要更新走 `request_sync('amazon_reports')` 只重装本地 JSON,不重拉报告。
- 内存 1.9G:不要在库里跑大 join 的实时看板,派生结果落 `derived` 或飞书表。

### raw.uppromote_referrals(2026-09-14 新增)

UpPromote 每单佣金。列:id(主键)/order_id(Shopify 订单数字 id)/order_number/created_at/affiliate_id/affiliate/status(approved|pending|denied)/quantity/total_sales/commission/coupon/tracking_type/refund_id/payload。与 `raw.shopify_order_lines` 用 `split_part(order_id,'/',5) = referrals.order_id` 关联,把佣金按订单行金额摊到 SKU。来源 `uppromote`,每 2 小时全量翻页(接口固定每页 10 条)。

### raw.amazon_mcf_orders / raw.amazon_mcf_items(2026-09-14 新增)

Amazon 多渠道配送(MCF,FBA 替独立站等非 Amazon 单发货)。orders:id(卖家侧单号,如 Shopify #1100 …)/displayable_id/received_at/status(Complete|Cancelled|Planning|Processing|…)/action/ship_state/ship_country/shipments/payload(已去掉收件人姓名与地址);items:id/order_id/seller_sku/qty/qty_shipped/qty_cancelled。来源 `amazon_mcf`(amazon 组),列表 queryStartDate = 水位 −30 天,逐单取明细。用途:独立站订单去向、跨渠道调货件数、MCF 配送费归独立站。

## derived 库(派生结果,带版本与 as-of 日期;2026-09-15 起)

与 raw 同一个 Supabase 库,schema `derived`,由首尔 `derived.py` 维护(凭据只在首尔 env)。凡是核心口径算出来、写进飞书 🤖 表的行,同时落这里;飞书表是给人看和人填的入口,derived 是给 GUI 和重放用的。

- `derived.rows(table_name, as_of, key, payload jsonb, core_version, script, run_id, computed_at)`,主键 (表名, as_of, 键):**同一天重跑覆盖当天,不同天各自保留**,所以任一天的派生结果都能原样重放:`select payload from derived.rows where table_name='批次账🤖' and as_of='2026-09-15'`
- `derived.latest` 视图:每张表每个键最新一份(GUI 读这个);`derived.tables` 视图:每张表有几天、最新一天几行、最近一次计算时间
- `derived.runs(run_id, script, as_of, core_version, started_at, finished_at, status, tables)`:每次脚本运行一条,tables 记本次各表写了几行
- 接法:脚本开头 `import derived; derived.hook(kc, '<script>')`,之后所有 `kc.upsert` 写飞书的同时写 derived(表名按 table_id 反查);不经 kc.upsert 的写法(batch_update、自有 http)显式 `derived.write(表名, rows, key=…, script=…)`。dry 模式不写飞书也就不写 derived;落库失败只打印不影响飞书
- 已接:batch_ledger(批次账🤖/批次月度🤖/寄样🤖/期间费用月度🤖)、batch_master(批次主数据🤖 派生列)、rev_sku(单品日销🤖/单品月度🤖/平台费用月度🤖)、sku_report(SKU档案🤖;另落三张只进 derived 不进飞书的结构化表:`SKU算账·基础🤖` 表 1 十行、`SKU算账🤖` 表 2/3/4 渠道账逐行、`SKU档案摘要🤖` 29 个 KPI,键 `SKU|批次`,2026-09-16 起)、fin_daily(Mercury流水/头寸日更🤖)、payouts_ledger(回款🤖,只有新追加的行)、stock_balance(批次数量平衡🤖/批次表·剩余实物🤖)、inv_snapshot(库存快照🤖/库存现状🤖)、biz_daily(经营日销🤖/经营快照🤖/经营周报🤖)、cash_model(现金推演🤖/现金月度🤖/补货窗口🤖/提成推演🤖/现金跑道摘要🤖/推演输入🤖,2026-09-16 起;店主私有,含提成与固定支出合计)、viz_extract(复盘·周cohort🤖/月cohort🤖/退货原因🤖/买家原话🤖/日销🤖/转化窗🤖/流量日🤖/Google周🤖/干预时间线🤖/封店损失🤖/拉取记录🤖,2026-09-16 起;干预时间线按键累积)
- 不落:工资表/工资月度🤖/社保公积金(店主:工资只进私有 base)
- 查看:`python3 derived.py` 打印各表天数与最近运行
- 只读 GUI 权限(2026-09-16 起):nginx basic auth 用户名经 `X-Remote-User` 传给 fin_gui,角色在首尔 `/opt/feishu-rerun/fin_roles.json`(owner / finance / team,表白名单 + 视图 + 口径过滤,服务端强制);账号用 `/opt/feishu-rerun/fin_user.sh add|passwd|del|list`,密码只进 htpasswd。`/fin/api/me` 返回当前账号、角色、可看视图。 飞书登录(2026-09-16 起,与 basic auth 并存,nginx `satisfy any` + `auth_request`):`/fin/auth/login` 跳飞书授权 → `/fin/auth/callback` 换 token、取 open_id、按 fin_roles.json `feishu` 段定角色(owners → owner;财务群成员 → finance;同租户 → team)、发 7 天签名 cookie;`/fin/auth/logout`。2026-09-16 起已配好、可用范围已放宽;根地址未登录自动 302 到登录,`/fin/api/*` 未登录回 401 JSON;`/fin/api/me` 另带 `name`/`avatar`/`feishu`。
- 只读 GUI(首尔 `fin_gui.py`,nginx `/fin/` basic auth):`/fin/api/tables`、`/fin/api/table?name=&as_of=`、`/fin/api/history?name=&key=&column=`、`/fin/api/explain?name=&column=`(列级来源,核心 `provenance.COLS`)、`/fin/api/explain_label?label=&channel=`(渠道表行级来源,核心 `provenance.LABEL_RULES`)、`/fin/api/sku[?key=SKU|批次]`(SKU 档案页数据)、`/fin/api/runway[?as_of=]`(头寸与跑道页数据)、`/fin/api/review[?as_of=]`(复盘页数据)、`/fin/api/runs`、`/fin/api/rules`;页面 https://fin.szzn-company.online/ (`?v=table&t=<表>` / `?v=sku&k=<SKU|批次>` / `?v=runway&d=<推演日>` / `?v=review&d=<复盘日>`)
