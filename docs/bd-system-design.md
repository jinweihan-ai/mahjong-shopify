# 达人 BD 人机协作系统设计 v1.0（2026-08-26 店主已拍板:架构C / 寻源a / 新建BD群 / Bot名 BD Copilot）

一句话:人少不搞矩阵——一个飞书群、一个 BD Bot、一张主表(张勇 API),AI 干重复活,人做判断。

## 0. 三条不可违背的原则(店主定)

1. **单一事实来源**:达人状态只存在主表(张勇系统);群是沟通界面,表是数据库。禁止信息只活在私聊/群消息里。
2. **对外必审**:AI 生成的一切对外文案必须经人确认后才可发送。
3. **认领制**:表有"负责人"字段;催办只 @ 负责人,不 @ 全群。
4. 效率约束:人每天操作 ≤30 分钟——投票/审核/拍板之外全部交给机器人;能用指令的不强迫开系统(手动改始终是兜底)。

## 1. 架构(三案待选)

- **A. 首尔机自托管 Coze Studio**:❌ 当前 2C/1.9GB 跑不动(官方最低 4GB);需升配+另配模型 key
- **B. coze.cn 云版**:零运维可视化,数据过第三方,模型火山系
- **C. 复用 fire-routine 链路(推荐)**:飞书事件 → 首尔 dispatcher(指令解析路由) → fire 云端 BD routine(参数=指令+内容) → Claude 会话按 BD-SKILL 执行(调张勇 API/IG API/生成内容) → 回群。提示词=repo 内 SKILL/配置文件,git 版本控制,/prompt 指令可改。零新组件、零新计费、已全链路验证。

## 2. 达人状态机(单一 status 字段,API 侧校验迁移合法性)

| 状态 | 说明 | 进入方式 | SLA/自动化 |
|---|---|---|---|
| lead 线索池 | scout 或人工录入,未触达 | /scout 入库 | 3 天无人认领→晨报提示 |
| rejected 已淘汰 | 人终筛淘汰(终态) | /drop | 记原因 |
| contacted 已触达 | 首次 DM/邮件已发(经人审) | draft→[发送]确认 | 7 天无回复→自动转 ghosted |
| replied 已回复 | 对方有响应 | 人 /log 或 DM 检测 | 48h 未跟进→催办@负责人 |
| negotiating 洽谈中 | 谈条件/报价 | /log | 5 天停滞→催办 |
| to_ship 待寄样 | 谈成待地址/发货 | /log | 3 天未发→催办 |
| shipping 寄样中 | 已发货 | /log(记单号) | 10 天未签收→催查物流 |
| delivered 已签收 | 样品到手,创作期 | /log 或物流检测 | 10 天无内容→温和催稿(经人审) |
| pending_post 待发布 | 承诺发布待上线 | /log | 7 天未发→催办 |
| published 已发布 | 内容上线 | **自动**(feed latest_published_at)或 /log | 自动核对折扣码/链接,闭环收入 |
| partner 长期合作 | 二次+合作 | /log | 每月主动维护提醒 |
| ghosted 失联 | 超时无响应(可唤醒) | 自动 | 30 天后建议二次唤醒或转 rejected |
| unfit 不合适 | 任意阶段人工终止(终态) | /drop | 记原因(调性/报价/风险) |

主表字段需求:handle/平台/主页链接/粉丝数快照/互动率/评分/来源关键词/status/负责人/下次跟进日/最近动作时间/报价+币种/样品SKU+物流单号/折扣码/内容链接[]/淘汰原因/审计(操作者=AI|人名)。进展日志独立表(append-only)。

## 3. 指令集

| 指令 | 触发 | 作用 |
|---|---|---|
| /scout 关键词 [数量] | 手动 | 拉线索+打分排序推卡;人点"入库"才写表 |
| /analyze @handle | 手动 | 尽调卡:受众画像/近期内容/互动质量/合作痕迹/风险点 |
| /draft @handle 合作类型 | 手动 | 邀约 DM+邮件双版;卡片带[发送]确认,仅负责人可点(对外必审) |
| /log @handle 描述 | 手动 | 一句话进展→结构化写日志;AI 附状态迁移建议,人一键确认 |
| /status [负责人\|状态] | 手动 | 漏斗快照 |
| /card @handle | 手动 | 单人完整档案+历史动作 |
| /assign @handle 人名 | 手动 | 认领/转负责人 |
| /remind @handle 日期 备注 | 手动 | 设跟进提醒 |
| /drop @handle 原因 | 手动 | 淘汰(终态) |
| /prompt list \| show 指令 \| set 指令 <内容> | 手动 | 查看/修改各指令提示词(存 repo 配置,set=commit,即时生效有版本史) |
| /help | 手动 | 群规则+指令清单 |
| BD 晨报 | 每日 09:30 | 今日待办/超时催办(@负责人)/漏斗 delta;无事一行 |
| BD 周报 | 周一 | 漏斗全景/转化率/成本/收入闭环(码→订单) |

## 4. 数据层:给张勇的 API 需求(现 feed 只读,需新增)

1. `POST /api/feed/creators` 创建线索(handle+platform 去重,返回 id)
2. `PATCH /api/feed/creators/{id}`:status(服务端按状态机校验迁移)/owner/next_follow_up/price/currency/sample_tracking/score/content_links/reject_reason
3. `POST /api/feed/creators/{id}/activities`:{ts, actor, type, text} append-only 进展日志
4. `GET /api/feed/creators?status=&owner=&follow_up_before=` 过滤;`GET /creators/{id}` 详情含 activities
5. 字段新增:source_keyword/score/audit(actor 区分 AI|人)/reject_reason
6. 状态枚举采用本文档第 2 节定义;非法迁移返回 4xx

## 5. IG 寻源约束(诚实版)

现 IG token 为"无 FB Page 绑定"模式(封号风险隔离,当初刻意选择)——**不支持 hashtag search / business_discovery**,纯 API 拉陌生达人不可行。两案:
- (a) 绑 FB Page 换完整 Graph API:解锁 hashtag 搜索(30标签/7天限额),但与隔离决策冲突,封号连带风险回来
- (b) **推荐起步**:寻源半自动——人贴候选名单/从竞品报&社群提及收集,AI 负责打分排序+尽调全自动;/scout 输入从"关键词"变"名单"
待店主拍板。

## 6. 群公告草稿(置顶用)

> 【本群工作方式】达人 BD 人机协作群。
> ① 所有达人状态以主表为准,群里聊完必须 /log 落表;
> ② AI 生成的对外文案必须负责人点[发送]确认后才发出;
> ③ 催办只 @ 负责人;谁发起谁负责,认领用 /assign;
> ④ 常用指令:/scout 找人 /analyze 尽调 /draft 写邀约 /log 记进展 /status 看漏斗 /help 全部指令;
> ⑤ 改 AI 的提示词:/prompt show <指令> 查看,/prompt set <指令> 修改;
> ⑥ 每早 09:30 机器人发 BD 晨报,周一发周报。

## 7. 落地顺序(拍板后)

1. 张勇 API 需求发出(第 4 节)+ 状态机对齐
2. BD-SKILL 全套提示词入 repo(.claude/skills/bd-copilot/)
3. 云端 BD routine 创建 + fire 凭据
4. 首尔 dispatcher 扩展:斜杠指令解析→路由(与重跑指令并存)
5. 新建 BD Bot(飞书),事件订阅指到首尔机(路径 /bd)
6. 群公告置顶,试运行一周,晨报周报开闸

## 8. 已拍板(2026-08-26)

1. 架构 **C**(fire-routine 链路);2. IG 寻源 **(a)** 绑 FB Page 解锁 hashtag 搜索——**用独立新 FB 应用**,不动现有社媒日报的无绑定 token,风险单元隔离;3. **新建 BD 专用群**,Bot 名 **BD Copilot**
4. 提示词管理:默认提示词在 .claude/skills/bd-copilot/SKILL.md;/prompt set 的覆盖存 BD 配置表(bitable),执行时覆盖优先——群内可改,repo 有底

## 9. 人机协作协议(2026-08-27 定稿,系统宪法层)

**发起权不对称**:人→AI 发起的是命令(必须执行);AI→人 发起的只能是提醒与请求,无人响应的默认行为=什么都不做,**沉默即否决**。

AI 主动发起的全部事件与人的接法:

| AI 发起 | 触发 | 人的接法(封闭动词集) | 不接的后果 |
|---|---|---|---|
| 晨报 | 每日 09:30 | 做了→/log;推迟→/remind;放弃→/drop | 未处理项次日继续出现 |
| SLA 催办 | 状态停留超时(@负责人) | 同上三选一 | 重复提醒,永不升级为代做 |
| 审稿请求 | /draft 之后 | 自发后回「已发 @x」;不满→/prompt set 再出 | 稿子作废,零副作用 |
| 状态确认 | /log 识别出可补事实 | 回「确认」 | 不写,原文仍落日志 |
| 入库确认 | /scout 打分后 | 回「入库 @a @b」 | 不入库,候选作废 |
| 贺报 | published 检测 | 无需接 | — |
| 故障自报 | token/API/权限故障 | 转店主 | 指令不可用直至修复 |

三条设计规则:①接口动词封闭(人接 AI 只用 确认/已发/入库/log/remind/drop 几个动词,保住 30 分钟/天预算;人对 AI 说什么都行,结构化是 AI 的活);②提醒的升级维度是频率与显眼度,永远不是权限——催办永不变代做;③每个 AI 发起必有唯一收件人,无负责人事项只进晨报待认领区,禁止 @全群。

一句话:人是决策者和对外的手;AI 是记录员、分析师和闹钟——闹钟可以一直响,但永远不能替你起床。
