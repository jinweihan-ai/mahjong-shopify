# 选题台账

**每产出一篇必须更新本文件。** 这是防止关键词蚕食和重复选题的唯一记录。
写文章前先读这里，再跑 `audit_blog.py --cannibalize`。

最后更新：2026-08-26

## 已占用的主关键词

| 主关键词 | 月搜索量 | 文章 | 发布日 |
| --- | --- | --- | --- |
| how to host a mahjong night | 0（长尾） | how-to-host-a-cozy-mahjong-night-at-home | 2026-05-26 |
| mahjong gifts | 1,200 | mahjong-gifts-game-night-hosts | 2026-07-13 |
| mahjong party ideas | 200 | mahjong-party-ideas-welcoming-game-night | 2026-07-17 |
| how to play american mahjong | — | how-to-play-american-mahjong-beginners-guide | 2026-08-05 |
| mahjong tile size | 880 | mahjong-tile-size-readability | 2026-08-07 |
| mahjong accessories | 3,600 | mahjong-accessories-guide | 2026-08-07 |
| how to teach mahjong | 260（竞争 MEDIUM / index 62） | how-to-teach-mahjong-to-beginners | 2026-08-08（已由用户发布） |
| why are mahjong sets so expensive | 260（竞争 HIGH / index 100） | why-are-mahjong-sets-so-expensive | 草稿 2026-08-10，待用户配图发布 |
| mahjong for seniors | **2,900（竞争 LOW / index 30）** | mahjong-for-seniors | 草稿 2026-08-12，待用户配图发布 |
| mahjong group | 390（竞争 LOW / index 5） | how-to-start-a-mahjong-group | 2026-08-14（已由用户发布） |
| 3 player mahjong | **1,600（竞争 LOW / index 13）** | 3-player-mahjong | 草稿 2026-08-17，待用户配图发布 |
| mahjong tournament | **720（竞争 LOW / index 1）** | your-first-mahjong-tournament | 草稿 2026-08-20，待用户配图发布 |
| how to clean mahjong tiles | 110（竞争 LOW / index 9） | how-to-clean-mahjong-tiles | 草稿 2026-08-24，待用户配图发布 |
| 2 player mahjong | **2,900（竞争 LOW / index 29）** | 2-player-mahjong | 草稿 2026-08-25，待用户配图发布 |
| mahjong lessons | **3,600（竞争 LOW / index 7）** | mahjong-lessons | 草稿 2026-08-26，待用户配图发布 |

**2026-08-17 实查修正**：`mahjong-for-seniors` 与 `how-to-start-a-mahjong-group` 已由用户发布（`--inventory` 实查 10 篇已发布 + 1 篇草稿）。台账原记录的「草稿待发布」已过期。仍为草稿的只有 `why-are-mahjong-sets-so-expensive`（2026-08-10 建）。

## 方向覆盖度

| 方向 | MJTI 帖数 | 已发布篇数 | 状态 |
| --- | --- | --- | --- |
| Hosting | — | 2 | **饱和**，不要再加 |
| Gifting | — | 1 | **饱和**（重复的那篇已删） |
| 规则 / 新手 | — | 1 | 够用（学玩家视角） |
| 教学 / 社群带新 | — | 1 | 新开方向，教学者视角，与「规则/新手」意图不同 |
| 设计与可读性 | 952 | 1 | 可再加 1 篇（牌背/牌侧角度） |
| 配件与收纳 | 929 | 1 | 可再加 1 篇（收纳专题） |
| 选购与搭配 buying_matching | 595 | 0 | **空白**，但 2026-08-10 实测主要入口词全部蚕食（见否决表） |
| 图案与主题 tile_theme_pattern | 532 | 0 | **整簇否决**，见否决表 2026-08-10 条目 |
| 牌垫与桌面 mat_table_surface | 464 | 0 | 空白，但已否决（与配件篇重叠） |
| 品质与风险 quality_risk | 170 | 1（草稿） | 2026-08-10 用价格/成本角度切入，方向已开 |
| 年长玩家 / 可及性 accessibility | 131 条匹配帖（跨话题） | 1（草稿） | **2026-08-12 新开方向**。不在原 MJTI 六大话题分类里，是横切主题，所以此前一直没被发现。仍有空间 |
| 组局 / 找局 community_group | 96 条匹配帖（跨话题，两次检索去重后） | 1（已发布） | **2026-08-14 新开方向**。同样是横切主题。词簇竞争度全表最低（index 2–7），且站上完全没有 group / club / meetup 语料，天然免蚕食。仍有空间（「主持人轮值」可再拆，但「两桌怎么排」已被 2026-08-17 的三人局篇部分吸收） |
| 锦标赛 / 竞技场合 tournament_competitive | 35 条匹配帖（跨话题，tournament / tourney 检索） | 1（草稿） | **2026-08-20 新开方向**。第四次验证「按人群与处境找词」。判别词 `tournament` 站上零实质语料，蚕食天然干净。整簇竞争指数 0–6，与组局簇并列为台账见过最低。**社群证据强度是历次最高的一次**：头部帖 2,351 互动 / 484 评论，且是直接证据（有人在问锦标赛怎么回事）而非邻近证据。仍有空间：gentle / beginner tournament 专题、锦标赛计分与判罚细则（但有事实过期风险） |
| 保养 / 售后 maintenance_care | 97 条匹配帖（跨话题，clean / wash / yellowed / acetone 等检索），精确检索 10 条 | 1（草稿） | **2026-08-24 新开方向**。第五次验证「按人群与处境找词」，这次的处境是「手里已经有一副牌，且它脏了 / 旧了 / 是继承来的」。判别词 clean/wash 在站上虽有语料但**全是假朋友**（见变更记录）。簇容量小（约 170/月），但产品机制连接是全台账最硬的一次。仍有空间：牌垫/牌桌清洁（16 互动那条问新垫子塑料味）、racks 五金氧化 |
| 找课 / 上课 lessons_classes | 103 条匹配帖（跨话题，lesson / class / teacher / instructor / 社区中心 / 图书馆 等检索） | 1（草稿） | **2026-08-26 新开方向**。第六次验证「按人群与处境找词」，这次的处境是「我想找个人教我，但不知道去哪找、也不知道自己在报什么」。判别词 `lessons` 站上零命中、`classes` 仅 1 处从句。**这是台账开始以来「量级 × 低竞争 × 证据强度」综合最好的一次**（3,600 / index 7，且社群证据 103 条为历次最多）。仍有空间：**「怎么读牌型卡」是这一簇里最痛但最难写的一层**（事实过期风险，见否决表 `how to read mahjong card`）；另有「上完课之后怎么维持」可与组局篇合并深挖 |
| 人数不是四 / 出勤适配 table_count | 18 条匹配帖（跨话题，rotate / sits out / bettor / uneven 检索）+ 83 条（two-player / 教配偶 检索） | 2（均草稿） | **2026-08-17 新开方向**，2026-08-25 加第二篇（两人局）。判别词 `player(s)` 在站上是泛词，但「三人怎么打」「两人怎么打」站上零覆盖。五人局 / bettor 已关闭。**两桌轮换排班仍空白**。⚠️ 本方向现有两篇草稿意图相邻，见 08-25 变更记录的自蚕食管理 |

## 已否决的关键词（不要重复提案）

| 关键词 | 月量 | 竞争 | 否决原因 |
| --- | --- | --- | --- |
| how many tiles in american mahjong | 1,300 | index 25（低） | 新手指南 FAQ 已答「How many tiles does American mahjong use?」。**改为在该篇加 FAQ 条目**，不新写文章 |
| how many flowers in american mahjong | 1,000 | index 5（极低） | 同上，新手指南已覆盖 8 Flowers |
| acrylic mahjong tiles | 1,900 | HIGH | 交易型意图，应由产品页承接，文章里只作次关键词 |
| mahjong set / mahjong tiles | 37,000 / 34,000 | KD 64 / 47 | 大词，新站单篇文章拿不到，作内链锚文本 |
| linda li mah jongg set | 1,300 | HIGH | 竞品品牌词，不做 |
| mahjong gifts for women | 200 | — | 标题含被禁短语 `for women`；且 gifting 方向已饱和 |
| mahjong tile back designs | 无数据（UNSPECIFIED） | — | Keyword Planner 无量级数据，簇内 `mahjong tile designs` 仅 170 且 index 99；牌背角度只够做现有设计篇的补充段落，不单独成篇 |
| best mahjong mat / mahjong table cover | 590 / 1,000 | HIGH index 100 | `--cannibalize` 报 MED，与 `mahjong-accessories-guide` 的「A mat or table cover」小节重叠 100% 判别词。要做只能在配件篇内扩写，不新开页 |
| vintage / antique mahjong set 簇 | 1,900 / 1,300 | HIGH index 100 | 全簇竞争 index 100，且为二手收藏与估值意图，与 Averill 新品无转化关系，判定不划算 |
| american mahjong set for beginners | 210 | MEDIUM index 61 | 2026-08-10 蚕食 **HIGH**（vs `how-to-teach-mahjong-to-beginners`，判别词 body 命中 100%，已有小节 “Choose a set beginners can read”）。要做只能在教学篇内扩写 |
| flowers in mahjong | 320 | LOW index 12 | 2026-08-10 蚕食 **HIGH**（vs 新手指南的 “8 Flowers, and 8 Jokers” 小节，heading 命中 100%） |
| mahjong symbols meaning / tile symbols / what do mahjong tiles mean / mahjong flower tiles 簇 | 260 / 480 / 70 / 320 | MED–HIGH | 2026-08-10 全簇蚕食 MED。根因：站上已有 4 篇 tile 密集文章，任何含 `tile(s)` 或 `flower(s)` 的判别词都会命中。**「图案与主题」方向整簇关闭**，除非先合并现有文章 |
| mahjong set price / mahjong set cost | 260 / 260 | HIGH index 100 | 2026-08-10 蚕食 MED（4 篇命中）。同义的 `why are mahjong sets so expensive` 与 `how much does a mahjong set cost` 检查 clean，已改走后者 |
| difference between chinese and american mahjong | 880 | LOW index 22 | 2026-08-12 蚕食 **HIGH**（vs 新手指南）。**真重叠不是判别力衰减**：新手指南里有一条 FAQ 标题就叫 “What's the difference between American and Chinese mahjong?”，heading 命中 100%。量级和竞争度都很好，**建议改为扩写新手指南那条 FAQ**，不新开页 |
| mahjong table size / mahjong table dimension | 720 / 720 | HIGH index 100 | 2026-08-12 蚕食 **HIGH**（vs `mahjong-tile-size-readability`，title/meta 命中 100%）。另有 4 篇 MED。牌垫桌面方向再次确认关闭 |
| mahjong scoring / mahjong points | 1,000 | LOW index 13 | 2026-08-12 否决。量与竞争度都好，但意图主要是中式/日式计分，美式计分在 NMJL 牌型卡上逐年变，写死有事实风险；且 points/betting 措辞贴近赌博红线 |
| travel mahjong set | 8,100 | HIGH index 100 | 2026-08-12 否决。交易型意图，且 Averill 没有旅行款产品，写了无法承接 |
| free mahjong for seniors / mahjong solitaire for seniors | 1,300 / 320 | LOW index 29 / 19 | 2026-08-12 否决。免费在线消消乐意图，与实体牌无关。**但它们的存在说明 `mahjong for seniors` 2,900 的量里混有一部分在线游戏意图，见变更记录的量级折扣说明** |
| mahjong room ideas | 260 | **HIGH index 100** | 2026-08-14 否决。台账里原写「待拉」，实测竞争度满格，量只有 260，且意图是家装改造（Pinterest 主场），Averill 不卖家具，转化承接不了。MJTI 那两条高互动改造帖（4,201 / 2,377）是社群内的分享冲动，不等于 Google 上有对应的可承接搜索 |
| mahjong club | 4,400 | LOW index 7 | 2026-08-14 **不作主关键词**。量看着最好，但同簇的 `mahjong club app` 480 / `mahjong club online` 720 / `gamovation mahjong club` 140 / `mahjong club solitaire` 说明 4,400 里主体是一款叫 Mahjong Club 的手机消消乐 App。已作次关键词用在 `how-to-start-a-mahjong-group` 里 |
| where to buy mahjong games | 590 | HIGH index 100 | 2026-08-14 否决。交易型意图，应由产品页/集合页承接，不写文章 |
| joker 簇：`how many jokers in mahjong` / `can you use a joker in a pair for mahjong` / `mahjong joker rules` / `mah jongg joker rules` / `joker rules in mahjong` | 880 / 480 / 260 / 260 / 110 | **全簇 LOW index 1–7** | 2026-08-17 否决，**整簇关闭**。这是台账开始以来量级 × 低竞争最诱人的一簇（约 2,000/月，竞争指数全部个位数），但**是真重叠不是判别力衰减**：`american-mahjong-rules` 里已有 H2 `Joker Rules` 和 FAQ `Can a joker be used in a pair?`，heading 命中 100%；新手指南另有 `Jokers, Tamed in Five Rules` 整节五条规则。要吃这簇只能扩写 `american-mahjong-rules` 的 Joker Rules 一节 + 加 FAQ 条目，**不能新开页** |
| learn american mahjong online | 90 | LOW index 24 | 2026-08-17 蚕食 **HIGH**（vs `how-to-teach-mahjong-to-beginners` 的 "How long does it take to learn American mahjong?" 与 `mahjong-for-seniors` 的 "Is American mahjong hard to learn later in life?"，heading 均 67%）。量本来就小，从候选池移除 |
| mahjong terms | 720 | LOW index 15 | 2026-08-20 **从候选池移除，改为扩写旧文**。脚本连续三次报 clean（08-12 / 08-14 / 08-20），但正文实证发现新手指南有一节 H2 `The Words You'll Hear at the Table`，内含 Pung / Kong / Quint / Sextet / Pair / Run / 1-2-3 colors / Exposure / NEWS 共 9 条术语，**直接回答该词的搜索意图**。脚本判 clean 的原因是站上从不使用 `terms` 这个词本身，用的是同义表达。**这是「脚本报 clean 但实为真重叠」的首例**，与 3-player 那次（脚本报 HIGH 实为伪报）方向相反，见变更记录的方法论条目。建议扩写该节并加一条 FAQ |
| american mahjong practice / american mah jongg practice | 1,000（同一个量桶） | LOW index 13 | 2026-08-20 否决。同簇 `american mahjong practice app` 590 / index 1、`free american mahjong practice` 20、以及一批 `practice 2019/2020/2021/2022` 年份变体，说明主体是在找练习 App 与在线对局。Averill 无对应产品，与 travel 簇同理 |
| mahjong bettor / mah jongg bettor | 90（同一个量桶） | **HIGH index 67** | 2026-08-20 否决。量小、竞争高，且 bettor 措辞贴近赌博红线，与 `mahjong scoring` 被否同源。三人局篇 FAQ 已答五人局 |
| 5 player mahjong | 20 | LOW index 11 | 2026-08-20 否决，量太小，三人局篇 FAQ 已覆盖。**至此 2026-08-17 候选池里「五人局 / bettor 角色」这一条正式关闭** |
| how to store mahjong tiles | 20 | HIGH index 100 | 2026-08-20 否决。量小且竞争满格，配件篇已有逐字同名 FAQ「What is the best way to store mahjong tiles?」 |
| mahjong tournament near me / mah jongg tournaments near me | 480 / 70 | LOW index 3 / 4 | 2026-08-20 **不作主关键词**，按「near me 本地意图」规则处理，已作 FAQ 一条写进锦标赛篇并导向组局篇 |
| destination mah jongg tournaments | 260 | LOW index 0 | 2026-08-20 不单独立项。已在锦标赛篇 FAQ 里作次关键词提到，单独成篇会自己蚕食 |
| how to set up mahjong / how to set up a mahjong game / how to set up mahjong game | 720（**同一个量桶**） | LOW index 16 | 2026-08-25 否决，**真重叠不是判别力衰减**。脚本报 10 篇全 HIGH，判别词退化到只剩 `set` 一个泛词，看着像伪报，**但正文实证确认是真重叠**：`american-mahjong-rules` 的 TOC 里有一节 H2 逐字叫 **`Setup`**（内容：洗牌、各人砌墙、East 掷骰定断口、四张一取三轮、East 多取两张 = 14/13），新手指南另有一节 **`Setting Up`** 写同一件事。这就是该词的搜索意图本身。要吃只能扩写这两篇 + 加 FAQ，不能新开页。**这是「单判别词报 HIGH 但确为真重叠」的首例**，与 08-17 的 `3 player mahjong` 伪报方向相反 |
| how to set up american mahjong / how to set up mahjong tiles | 90 / 170 | LOW index 32 / 33 | 2026-08-25 同上，整簇随主词关闭 |
| national mah jongg league card / mah jongg league cards | 14,800（同一个量桶） | LOW index 31 | 2026-08-25 否决。08-12 台账标注「量极大，值得单独评估」，**本次正式评估并否决**。兄弟词 `www nationalmahjonggleague org order online` 1,900 / index 100、`nationalmahjonggleague org cards` 1,000 / index 100、`nationalmahjonggleague org store` 90 说明这是**导航型意图**，用户要去 NMJL 官网买当年的牌型卡。Averill 截不住，且是他人组织名，另有牌型卡逐年更新的事实过期风险。**「值得单独评估」这条待办至此关闭** |
| how to read mahjong card | 320 | LOW index 33 | 2026-08-25 否决。蚕食报 7 篇 MED，且核心事实（牌型卡内容）逐年更新，与 `mahjong scoring` 被否同源。信息型意图不错，但要写只能写成「怎么读一张不特定的卡」，价值有限 |
| mahjong hands / all mahjong winning hands | 1,900 / 110 | HIGH index 88 / 91 | 2026-08-25 否决。竞争高，且牌型逐年变，事实过期风险最高的一类 |
| mahjong wall / mahjong wall setup / mahjong dealing | 480 / 210 / 260 | MED index 46 / 46 / 30 | 2026-08-25 否决，随 `how to set up mahjong` 整簇关闭（rules 篇 `Setup` 一节已覆盖砌墙与发牌） |
| mahjong classes for beginners | 260 | LOW index 4 | 2026-08-26 否决为主词。蚕食 **MED**（vs `how-to-teach-mahjong-to-beginners`，title/meta 与 heading 均 50%，已有小节 “Choose a set beginners can read”）。**「for beginners」这个轴在本站已被教学篇占住**，找课方向必须避开它。已作次关键词写进 `mahjong-lessons` |
| mahjong lessons near me / mahjong class near me / mah jong classes near me / mahjong teachers near me | 4,400 / 4,400（同桶）/ 480 | **全簇 LOW index 4–6** | 2026-08-26 **不作主关键词**，按「near me 本地意图」规则处理（与 08-20 的 `mahjong tournament near me` 同源）。量看着极大（约 8,800），但 Google 上半屏是地图包与 Meetup，全国性品牌博客拿不到那一层。已在 `mahjong-lessons` 的「Where to look for a class」一节把这批意图接成方法论（parks & rec 目录 / 图书馆日历 / 去 open play 现场问） |
| learn to play mahjong / learn to play mah jongg / learn to play mahjong game | 2,400（**同一个量桶**） | MEDIUM index 44 | 2026-08-26 不作主词。量好但竞争是找课簇里最高的一档，且同簇 `learn mahjong online` 880 / `learn how to play mahjong online` 480 / `learn to play mahjong online free` 110 说明相当比例是在线玩法意图。已作次关键词。**本站要吃「学」这一层，入口是新手指南不是新页** |
| american mahjong strategy | 210 | LOW index 24 | 2026-08-17 暂缓。`mahjong strategy` 1,300 单独查 **clean**，但加了 `american` 后 4 篇 MED（`american` 在站上是泛词）。真正的问题是**事实风险**：美式策略高度依赖当年 NMJL 牌型卡，写死会过期，与 `mahjong scoring` 被否的理由同源。要做必须写成「不依赖具体牌型的判断原则」，是下次的备选而非首选 |

## 候选池（下次优先，均已过蚕食检查）

| 候选主关键词 | 月量 | 竞争指数 | 方向 | 蚕食检查 | 备注 |
| --- | --- | --- | --- | --- | --- |
| mahjong etiquette | 110 | **LOW index 9** | 社交/待客 | **clean（2026-08-25 脚本 + 正文双重实证）** | 本次复核通过但未采用，因为 `2 player mahjong` 量级高 26 倍。**实证结论已升级为可直接采信**：14 篇正文搜 10 个礼仪同义词只有 7 处命中，其中 `courtesy pass` ×4 是 Charleston 的**规则机制不是礼仪**（新增假朋友），`etiquette` ×1 只是新手指南里的一个从句，`table rules` ×2 在组局篇讲的是新群定规矩不是牌桌举止。**`manners` / `polite` / `rude` / `unwritten` / `good guest` 全部零命中。** 下次可直接用，不必再实证 |
| ~~where to learn mahjong near me~~ | 390 | LOW index 4 | 组局/新手 | — | **2026-08-26 已被 `mahjong-lessons` 吸收，从候选池移除。** 本次实拉发现同方向有量级大 9 倍的非本地头词 `mahjong lessons` 3,600 / index 7，直接改用它作主词，该条已作次关键词覆盖，再开新页就是自己蚕食自己 |
| gentle / beginner tournament 专题 | 未拉 | 未拉 | 锦标赛 | 待查 | 2026-08-20 锦标赛篇里只用一小节 + FAQ 一条带过。社群里「标准赛 vs gentle 赛」的分歧反复出现（130 互动那条明说「不是社交下午茶」），可能撑得起单独一篇，但要先确认有没有对应搜索量，很可能没有 |

**2026-08-14 已被本轮吸收、不要再单独立项的词**：`mah jongg groups near me` 1,300 / index 7、`mahjong club near me` 1,000 / index 4、`where to play mahjong near me` 480 / index 6、`mahjong meetup` 210 / index 2、`how to start a mahjong group` 50 / index 4。这些已作次关键词写进 `how-to-start-a-mahjong-group`，再开新页就是自己蚕食自己。

**2026-08-12 更新：候选池不再见底。** 上次的「见底」结论下得太早，原因是选题一直在 MJTI 的六个话题分类内部找，而那六类都是围绕**器物**（牌、配件、垫子）划分的。这次换成按**玩家处境**找词（年龄、视力、找局、社交场合），立刻拿到 `mahjong for seniors` 2,900/LOW 和另外三个 clean 的低竞争词。

**方法论结论：当「按品类找词」枯竭时，改「按人群与处境找词」。** 前者受制于站上已有语料的名词重叠，后者的判别词（seniors / etiquette / group）站上完全没有，天然避开蚕食。

**结构性结论（2026-08-10 提出，仍然成立但需修正）：站上 tile 密集文章多，任何含 `tile`/`tiles`/`flower` 的新关键词几乎必然报 MED。但这只限制「器物类」选题，不限制「人群/处境类」选题。**优化现有文章仍然该做**（尤其把 `difference between chinese and american mahjong` 880/LOW 折进新手指南那条已存在的 FAQ），但新增文章还没到天花板。

**用前必须做**：① 拉 `getKeywordIdeas` 确认量级与竞争度 ② 跑 `--cannibalize` 复核（博客内容在变，历史结论会失效）。

## 变更记录

- 2026-08-26：新增草稿 `mahjong-lessons`（gid://shopify/Article/618611835177，未发布，待用户配图）。主关键词 `mahjong lessons` **3,600/月，竞争 LOW index 7**。
  - **这是台账开始以来「单词量级 × 低竞争」组合最好的一次**（3,600 配 index 7；对照：`2 player mahjong` 2,900/index 29、`mahjong for seniors` 2,900/index 30、`mahjong club` 4,400 但被同名手游买断）。**且它不在候选池里** —— 候选池那条是 `where to learn mahjong near me` 390/index 4，本次按方向去实拉才发现同一处境下有量级大 9 倍的非本地头词。**教训：候选池记的是「上次拉到的词」，不是「这个方向的最优词」，用之前必须重拉一次整簇。**
  - **簇容量（已按 08-17 同桶规则去重）约 6,200/月的非本地部分**：3,600（`mahjong lessons` / `mah jongg lessons` 同桶，四项指标逐位相同）+ 1,900（`mahjong classes` / `mah jongg class` 同桶，index 3）+ 320（`mahjong lessons online`）+ 260（`mahjong classes for beginners`）+ 210（`mahjong lessons for beginners`）+ 90 + 70 + 50 + 50。**另有本地层约 8,800**（`mahjong lessons near me` 4,400 + `mahjong class near me` / `mah jong classes near me` 4,400 同桶 + `mahjong teachers near me` 480 + `mah jongg lessons near me` 320），**已按 near me 规则整体排除**。
  - **量级要打折，且这次折扣要打得比上次重。** 与 08-25 那次不同：`2 player mahjong` 的消消乐污染检查是历次最干净的，本次不是。裸词 `mahjong lessons` 3,600 里，**相当比例的人其实想要的是「我家附近的课」**，只是没打 near me，Google 也会给他们地图结果。这一层博客接不住。另有 `learn mahjong online` 880 / `mahjong lessons online` 320 / `mahjong lessons on youtube` 50 说明还有一部分在线课意图。**保守估计可承接 800–1,500/月，这是判断不是测量，比 08-25 那次的折扣重得多。**
  - **蚕食：脚本对主词报 clean，并按 08-20 升级后的规则做了正文实证，确认是真 clean。** 实证做法：15 篇正文（含 5 篇草稿，不只 atom feed 的 10 篇）落盘，正则搜 20 个找课意图同义词（lesson/lessons/class/classes/teacher/instructor/tutor/tutorial/course/workshop/seminar/enroll/sign up for/community center/rec center/senior center/library/YouTube/video）。**总命中仅 15 处，其中 14 处是假朋友或无关**：`golf course` 是比喻、`senior center` ×4 全是「活动中心放假导致牌局取消」的排期句、`lesson` 在教学篇里指的是教学方式之争（教师视角）、`teachers` 在两人局篇指「大多数有经验的老师会怎么开第一课」。**唯一的实质命中只有一处**：组局篇 `Where new groups actually play` 一节里有一个从句「the parks and recreation catalog, which often lists mahjong classes that turn into groups」。**一个从句不构成覆盖**，且那篇的搜索意图是「怎么开一个局」不是「怎么找一个课」。可以写。
  - **⚠️ 与 `how-to-teach-mahjong-to-beginners` 的自蚕食风险已刻意管理。** 两篇都关于「教与学」，但**读者身份相反**：教学篇的读者是**要教别人的人**，本篇的读者是**要被教的人**。管理做法：① 九个 H2 与教学篇零重复；② **刻意避开 `for beginners` 这个轴**（`mahjong classes for beginners` 260 实测蚕食 MED，已写进否决表），标题/meta/slug 全部以 `mahjong lessons` 为轴；③ 本篇末尾主动把「如果你变成那个讲解的人」导流给教学篇，用内链把两篇的分工写明。
  - **社群证据（MJTI 3,642 帖，lesson/class/teacher/instructor 等检索 103 条，取高互动）。是直接证据不是邻近证据，且 103 条是历次检索命中最多的一次**：
    - **1,108 互动 / 135 评论**「我叫 Anne，八月上了第一堂美式麻将课……**一开始完全是懵的，什么都不懂**，但我一直练，也不怕问」——**全文第三节整节由此而来，也是开篇场景的原型**。她还提到自己在孤独症谱系上，成文里**刻意没有写这一点**（会把一篇找课指南变成励志故事，且是他人身份信息），只留下「第一堂课懵是常态」这个可复用的结论。
    - **1,629 互动 / 820 评论**「我今天拒绝了一group女士的教学邀约……**看着越来越多『两小时端着酒杯就学会』的速成课**，有些还是几个月前才学会的人在教」——本篇「怎么分辨认真的老师和赶场的老师」一节的来源。**注意：这条帖 `how-to-teach-mahjong-to-beginners` 已用过**，但那篇是从**教师视角**问「你会不会也拒绝」，本篇是从**学生视角**问「你怎么知道自己报的课靠不靠谱」。同一条证据两种用法，不是重复。
    - **353 互动 / 153 评论**「我妹妹跟一个小班和老师学了一阵，打起来很挫败……**我和表姐都觉得她的老师没资格教**」——成文「伤害是后来才显现的」那段，也是「问老师会不会区分规则和桌规」这条建议的来源。**这条是本篇独有的，之前没用过。**
    - **1,172 互动 / 171 评论**「对麻将热潮里的过度商业化感到震惊……**我们组 45 个人，每次都在本地图书馆免费打**」——费用一节的来源，也是「价格不是质量信号」这个结论的依据。
    - 167 互动 / 33 评论「**我不收学费**，这样学生起步成本就低」——免费老师真实存在。
    - 666 互动 / 173 评论「我已经在线上打过、**看了大约 48 小时的视频**……还是报了课」——第一节「视频给不了什么」的来源。
    - 454 互动 / 58 评论「同事发了张她在课上的照片，我一下子就懂了……现在周一是『Mahjongg Mondays』」+ 223 互动 / 14 评论（Vero Beach 教了十五年的老师，学生自己攒出了社群）——结尾「最后一课之后」一节的两条来源。
  - **事实红线处理**：**没有写任何具体价格**（地区差异极大，写死会过期，与 `mahjong scoring` 被否同源），只写「价格不是质量信号」和「先查 parks & rec 和图书馆」这两条可核查的判断。课程时长写成「多数四到六节」并标明因人而异。**没有对孤独症/学习障碍作任何宣称**。老年中心那条写成「很多镇上对六十五岁以下开放，去问不要假设」，是可核查的建议不是断言。
  - **产品连接刻意收窄，并写了两条对自己不利的话**：产品放在「课与课之间在家练」这个真实场景，落点仍是**四张快速参考卡**（练习桌上一人一张，不用传一张卡），但**主动写明盒里没有 racks / pushers / mat**，并**紧接着写「没有任何一副牌能解决牌型卡，而牌型卡才是真正难的部分。牌好读只能缩短摸牌的迟疑，缩短不了牌型卡」**。另外「What to bring」一节**直接劝读者第一天不要买牌**，等上过两三节再说 —— 这是本站第一次在正文里明确劝延后购买。产品事实全部按线上产品页 2026-08-26 实查：160 张（154 在玩 + 6 张空白备用）、carved acrylic、0.87W × 1.25H × 0.6D、珊瑚橙纯色牌背、拉链袋 + 说明手册 + 4 张快速参考卡、180 天保修。用 `carved`（产品页仍是 `engraved` 与 `printed with precision` 自相矛盾，按 spec 统一）。**未提 NMJL 牌型卡**（Set Includes 里没有）。
  - **竞品红线**：证据里出现的品牌与个人（OMM、South Jersey Mahjong、NMJL、Hobby Lobby、具体教师姓名与地名 Vero Beach）**全部抽象成「一位群友」「一位教了十五年的老师」，无一指名**。Anne 的名字与身份信息未写入正文。质量抱怨抽象成「怎么分辨认真的老师」这一判断标准。
  - 内链：`american-mahjong-rules`、`mahjong-tile-size-readability`、`how-to-start-a-mahjong-group`、`how-to-teach-mahjong-to-beginners`、`how-to-play-american-mahjong-beginners-guide`，共 5 篇 + 1 产品页。**五篇全部实查 `PUB=True`**（五篇草稿一条没链）。
  - **字数**：纯正文 1,501 词，卡在 spec 上限 1 词。初稿 1,710 超标 14%，逐段压缩 209 词，**五个内链、全部社群证据、全部产品事实、两条不利限制一条未减**，只砍掉了 223 互动那条证据的细节（晚宴那一句）。create 脚本口径 1,646。
  - 本轮否决：`mahjong classes for beginners` 260（蚕食 MED）、near me 整簇约 8,800（本地意图）、`learn to play mahjong` 2,400（MED index 44 + 在线玩法意图）。候选池移除 `where to learn mahjong near me`（被本篇吸收）。
  - **⚠️ 站点问题：`--full` 本轮报 2 条 HIGH，比前五轮多了一条新的。**
    - 旧的那条（连续第六次）：`american-mahjong-rules`（已发布）缺封面图，Article 结构化数据缺 `image`。
    - **新增**：`american-mahjong-rules` 锚点 `cheat-sheet` **指向不存在的 id**（TOC 16 条 vs 12 个 id，是全站唯一 TOC 数大于 id 数的一篇）。这是已发布文章上的坏锚点，读者点了不会跳。**按硬规则只报告未擅自修复**，需用户确认后再动。
    - 另有 5 条缺图 MED 全部是待发布草稿（属正常）、1 条 thin-content MED（`how-to-host-a-cozy-mahjong-night-at-home` 604 词 vs 中位数 1,496）、1 条 LOW 作者名不一致（`Averill` / `The Averill Team` / `Averill Mahjong` 三种并存）、3 篇无 tags、2 篇 meta title 超 60 字符、1 篇 meta desc 166 字符、1 篇封面图缺 alt。
  - **方法论新发现：候选池会「过期低估」，不只是「过期失效」。** 此前记录的失效模式都是「上次 clean 这次蚕食了」。本次是反向的：候选池那条 390/index 4 本身没错，但它只是上次按 `where to learn` 这个措辞拉词的产物，**同一个读者处境换成 `lessons` / `classes` 措辞去拉，头词量级大 9 倍**。**规则：从候选池取词时，先把该词的读者处境翻译成 2 到 3 种别的措辞各拉一次，再决定用哪个当主词。**
  - **新增假朋友（追加到 08-20 / 08-24 / 08-25 那三份）**：`golf course` 里的 `course` 不是课程（两人局篇的比喻）；`senior center` 在本站四处全部是**排期句**（活动中心放假导致牌局取消），不是「老年中心开课」；教学篇里的 `lesson` 是教师视角的教学方式之争，不是「上课」；`class` / `classes` 在牌面可读性篇里出自 `size class` 与 `size classes`，指的是**牌的尺寸档位**不是班级（这是 `mahjong classes` 脚本报 LOW 的唯一来源）。
- 2026-08-25：新增草稿 `2-player-mahjong`（gid://shopify/Article/618568188201，未发布，待用户配图）。主关键词 `2 player mahjong` **2,900/月，竞争 LOW index 29**。
  - **这是台账开始以来「单词量级 × 意图纯净度」最好的一次，且意图污染检查是历次最干净的。** 按 08-12 定下的检测方法（主词加 free / online / solitaire / app / download 再拉一次）实测：`free 2 player mahjong`、`2 player mahjong solitaire`、`2 player mahjong download` **全部 UNSPECIFIED 无数据**，`2 player mahjong app` 仅 30 / index 9，`2 player mahjong online` 仅 140 / index 3。**对照组**：`mahjong for seniors` 2,900 的同簇 `free mahjong for seniors` 有 1,300（重度污染），`mahjong club` 4,400 被同名手游买断。本次几乎没有消消乐/App 污染，**折扣可以打得比历次都轻**。
  - **簇容量（已按 08-17 规则去重）约 5,110/月**，是台账见过最大的一簇：2,900（`2 player mahjong` / `2 person mahjong` / `2 player mahjong game` / `2 player mahjong games` 四写法**同一个量桶**，四项指标逐位相同）+ 1,000（`2 person mahjong rules` / `2 player mahjong rules` 同桶，index 16）+ 880（`mahjong for two players`，MED index 39，独立桶）+ 70 + 50 + 40 + 40 + 30 + 30 + 20×3 + 10。**已剔除** `2 player mahjong online` 140、`2 player riichi mahjong` 30（日式）、`2 player mahjong app` 30。仍应打折：`mahjong` 一词在美国大众语境里常指消消乐，头部泛词一定混杂，**保守估计可承接 2,000–3,000/月，这是判断不是测量**。
  - **蚕食：脚本报 2 篇 HIGH，其中 `3-player-mahjong` 是 title/meta 100%。这是本次最需要判断的一点。** 判别词退化到只剩 `player`（站上泛词），按 08-17 规则必须回正文实证。实证做法：14 篇正文（含 4 篇草稿）落盘，正则搜 9 个两人局变体（two-player / 2-player / two-handed / 2-handed / two people / two of you / two players / just two / only two）。**12 处命中全部是假朋友**：rules 篇与新手指南的 "if two players call the same tile"「两家同时叫牌」是**出牌规则**；"the other two players pay face value" 是**付牌句**；3-player 篇的 "the other two players take one" 是**发牌句**、"the only two people at the table are your right and your left" 说的是**三人局里的两个邻家**。**真正的「两个人怎么打」零覆盖。**
  - **⚠️ 自蚕食是本次唯一的实质风险，已刻意管理，但用户需知情。** 与 `3-player-mahjong` 草稿同属「人数不是四」方向，Google 有可能判为近似意图。管理做法：① **读者处境刻意分开** —— 三人篇是「今晚第四个人临时来不了」的**突发事件**（开头就是五点钟那条短信），两人篇是「我们家就两个人想常打 / 我在教我先生」的**长期习惯**；② **八个 H2 与三人篇零重复**，且两人篇不使用「人数不是四」这个框架词；③ 标题、meta、slug 均以 `2 player` 为轴，不出现 `fewer than four` 之类的共用表述。**遗留问题：两篇无法互链**，因为 `3-player-mahjong` 仍是草稿（链过去 404，违反 08-24 定的内链规则）。**用户发布这两篇后应补一组互链**，这是本次唯一未闭环的动作。
  - **社群证据（MJTI 3,642 帖，两人局 / 教配偶 / 一对一学 检索 83 条，取高互动）。是直接证据不是邻近证据**：
    - **619 互动 / 272 评论**「我在教我先生打美式麻将。花色和牌都认得了，也懂各种组合和目标。**但一看到 NMJL 牌型卡就完全懵掉、很挫败**，说那些括号看不懂……希望他能加入我们的局」——**全文最关键的一条，也是本篇整个立意的来源**。它说明两人局的真实痛点不是规则，是**牌型卡**。成文里「牌型卡才是那堵墙，不是牌」整节由此而来。
    - **235 互动 / 48 评论**「在博洛尼亚到罗马的火车上打麻将！牌墙放在袋子里，弃牌丢进塑料盒，亮牌摆在后排朝向对家。**就我们两个人，所以不做传牌。**」——**逐字给出了本篇最核心的机制结论**（Charleston 在两人局失效），而且是玩家自己实践出来的，不是我推的。成文直接引用了这句五个词的原话。
    - 192 互动 / 130 评论「和我先生用新的大牌型卡打，碰到一个我发现自己也答不上来的问题」——两人在家常打是真实存在的常态。
    - 208 互动 / 46 评论「作为一个打麻将的男性……**我太太和我都很喜欢这副牌**」——夫妻搭档。
    - 319 互动 / 36 评论「女儿放假从大学回来刚学会，我们在 LAX 转机时间打了一会」+ 327 互动 / 25 评论「外孙一见面就问『外婆你带麻将了吗』」——**成文结尾三个场景全部来自这两条与上面那条**，不是编的。
  - **事实红线处理**：全文开篇第三段即明写**美式麻将没有官方两人玩法**，NMJL 牌型卡是按四座写的，后面所有方案一律称 house adaptation。**牌数与牌墙的数字是可核查的推导**：在玩 154 张，四人发 53、三人发 40、两人发 27，故约 127 张留在墙里。**没有写任何具体分值**，避开 `mahjong scoring` 的事实过期风险。未提 NMJL 牌型卡是否随盒附送（产品页 Set Includes 里没有）。
  - **产品连接刻意收窄，并主动写了两条对自己不利的话**：雕刻牌面的好处只主张「牌面好读」，并**紧接着明写「雕刻对牌型卡一点帮助都没有，而牌型卡才是新搭档真正的障碍」**；另主动写明**racks / pushers / 牌垫不在盒里**。产品事实全部按线上产品页 2026-08-25 实查：160 张（154 在玩 + 6 张空白备用）、carved acrylic、0.87W × 1.25H × 0.6D、珊瑚橙牌背、拉链袋 + 说明手册 + 4 张快速参考卡、180 天保修。**四张快速参考卡是本次产品连接的落点**，因为它正好对上 619/272 那条帖的痛点（学的人可以自己拿着参考，不用每半分钟去借牌型卡）。用 `carved`（产品页 engraved 与 printed 措辞仍自相矛盾，按 spec 统一）。
  - **竞品红线**：证据里出现的品牌（The Mahjong Line、My Fair Mahjong、All That Mahj、OMM、Where The Wind Blows、Hobby Lobby）**全部抽象成「一位群友」「一对搭档」，无一指名**。
  - 内链：`american-mahjong-rules`、`how-to-teach-mahjong-to-beginners`、`how-to-play-american-mahjong-beginners-guide`、`mahjong-tile-size-readability`、`how-to-start-a-mahjong-group`，共 5 篇 + 1 产品页。**五篇全部实查 `PUB=True`**（按 08-24 定的规则，四篇草稿一条没链）。
  - **字数**：纯正文 1,499 词，卡在 spec 1,100–1,500 上限内 1 词。初稿 1,592 超标，逐段压缩 93 词，**五个内链、全部社群证据、全部产品事实、两条不利限制一条未减**。inventory 脚本口径 1,626。
  - 本轮否决：`how to set up mahjong` 720（**真重叠，见否决表，是本次方法论收获**）、`national mah jongg league card` 14,800（导航型意图，08-12 遗留待办至此关闭）、`how to read mahjong card` 320、`mahjong hands` 1,900、`mahjong wall` 簇。
  - **方法论新发现：单判别词报 HIGH，两种结论都出现过了，判定只能靠正文实证。** 08-17 的 `3 player mahjong`（判别词只剩 `player`）实证下去是**伪报**，可以写；本次的 `how to set up mahjong`（判别词只剩 `set`）实证下去是**真重叠**，不能写。**两次脚本输出形态几乎一样（10 篇全 HIGH、判别词 1 个泛词、title/meta 0%），结论却相反。** 结论：**判别词退化时脚本输出不含任何信息量，必须 100% 依赖正文实证，不要再试图从分数形态上找规律。**
  - **新增假朋友（追加到 08-20 / 08-24 那两份）**：`courtesy pass` 是 Charleston 的传牌机制**不是礼仪**（查 etiquette 类候选词时必踩）；`two players` 在 rules 篇与新手指南里指的是「两家同时叫牌」和「另外两家付牌」，**不是两人局**；`the other two players take one` 是三人局的发牌句。
  - **站点问题（连续第五次报告，未擅自改动）**：`--full` 仍报 1 条 HIGH，`american-mahjong-rules`（已发布）缺封面图，导致 Article 结构化数据缺 `image`。**这是用户侧动作，已连续五轮未处理。** 另有 4 条缺图 MED 全部是待发布草稿（属正常）、1 条 thin-content MED（`how-to-host-a-cozy-mahjong-night-at-home` 604 词 vs 中位数 1,496）、1 条 LOW **作者名不一致**（站上同时存在 `Averill` / `The Averill Team` / `Averill Mahjong` 三种，会写进 Article.author.name），另有 3 篇无 tags、1 篇 meta title 62 字符超长、1 篇封面图缺 alt。
- 2026-08-24：新增草稿 `how-to-clean-mahjong-tiles`（gid://shopify/Article/618560487721，未发布，待用户配图）。主关键词 `how to clean mahjong tiles` **110/月，竞争 LOW index 9**。
  - **量级是台账里最小的一次，必须说清楚为什么还值得做。** 整簇去重后约 170/月：主词 110、`how to clean mah jongg tiles` 110（**与主词同桶，不重复计**）、`how to wash mahjong tiles` 30、`how do you clean` 10、`how to clean ivory` 10、`how to clean yellow` 10。这个量单看不值得写一篇。做它的三个理由：① 竞争指数 9，新站有机会真的排上去，而不是排第 4 页；② 搜索者**已经持有一副牌**，转化偏弱，但正好落在「旧牌该修还是该换」这个决策点上，是本站少见的能自然导向购买的售后场景；③ **产品机制连接是全台账最硬的一次**（见下）。**预期不要按流量规划，按「补齐售后语料 + 拿一个能排上的词」规划。**
  - **蚕食：脚本报 8 篇 MED，实证推翻，判定为判别力衰减。** 判别词只有 `clean` + `tiles`，而 `tiles` 满站命中，`mahjong` 被判泛词。**本次按 08-20 升级后的判定规则做了意图实证**：把 13 篇正文（含 3 篇草稿，不只是 atom feed 的 10 篇已发布）落盘，正则搜 20 个保养意图同义词（clean/wash/wipe/scrub/soap/detergent/alcohol/sanitiz/disinfect/yellowed/discolor/grime/sticky/residue/dishwasher/maintenance/care for/polish/restore/stain）。**17 处命中全部是假朋友**，且 scrub / detergent / alcohol / sanitize / yellowed / grime / residue / dishwasher / maintenance / restore **零命中**。真正的清洁保养内容零覆盖，可以写。
  - **假朋友清单（追加到 08-20 那份，下次直接用）**：`clean block` / `clean line` / `clean edges` / `cleanly` 是「视觉干净」的形容词不是清洁；`wipe clean` 与 `easier to wipe` 出现在牌垫和 racks 段落不是牌；`washing the tiles` 是洗牌；`wash out` 是灯光把牌面冲淡；`Soap` 是白板绰号；`polished` 说的是待客氛围。**结论：这个站的 `clean` 一词几乎从不表示「清洁」。**
  - **社群证据（MJTI 3,642 帖。宽检索 97 条，精确检索 10 条，取高互动）。是直接证据不是邻近证据**：
    - **89 互动 / 36 评论**「我用**丙酮把原来的颜色整个剥掉了**，然后用丙烯马克笔重画」——**全文最关键的一条**。社群自己已经把实验做完了：丙酮确实能把牌面整个抹掉。这不是我推测的机制，是有人做成功了。
    - **263 互动 / 179 评论**「一张白板端上有变色，我们用**洗甲水**想把那块墨去掉，没用……有没有办法遮一下」——同一种溶剂，一次抹掉整副，一次救不回一张。成文里把这两条并排放，机制就自己说清楚了。
    - **64 互动 / 28 评论**「朋友送了我一副 bakelite 老牌……**任何关于怎么清洁这些牌的信息我都感激**」——**逐字就是本篇标题的搜索意图**，直接证据。
    - 129 互动 / 67 评论「奶奶那副 26 张花牌的老牌，**在我开始清理之前**再拍几张」——继承牌场景。
    - 56 互动 / 47 评论「车库拍卖淘的老牌，很多牌**磨到没法打了**，racks 的金属件锈得清不掉」——成文「有些牌是救不回来的」一节，也是「修还是换」决策点的来源。
    - 559 互动 / 64 评论 一位七十多岁先生捐出母亲的牌，「盒子磨损很重……**现在都清干净了**，下周我们就用这副牌打，纪念 J.Lehman」——成文里「清理能清的，然后用它打一局」这个结局的来源。
    - 46 互动 / 16 评论「几张牌上有变色，这算 delamination 吗」——分层/氧化是真实困扰。
    - 16 互动 / 16 评论「新牌垫塑料味很重，怎么清洗」——**未采用**，留作下次牌垫保养选题。
  - **产品连接是可验证的机制，不是营销话术**：印刷/涂层牌面是**表面层**，敌人正好是溶剂和摩擦，而这两样就是清洁本身；雕刻牌面是**切进牌体的几何形状**，颜色沉在凹槽里，布擦过只碰到高点，**形状擦不掉**。成文同时写了三条对自己不利的限制：雕刻牌照样会刮花、材料本身泛黄雕刻也挡不住、凹槽边缘几十年洗牌后照样会磨。**主张被刻意收窄成「雕刻的几何结构扛得住清洁，印刷不一定」**，而不是「雕刻牌更耐用」。
  - **事实红线处理**：没有给任何具体化学品配比。泛黄那一节**直说清洁没用**（是材料整体氧化不是表面污垢），并**明确劝阻**社群里流传的过氧化氢+日晒漂白法（来自复古电脑翻新，结果不稳定）。产品事实全部按线上产品页实查：160 张（154 在玩、6 张空白备用）、0.87W × 1.25H × 0.6D、珊瑚橙纯色牌背、拉链袋 + 4 张快速参考卡 + 说明手册、180 天保修，并**主动写明盒里没有 racks / pushers / mat**。用 `carved`。**未提 NMJL 牌型卡**（产品页 Set Includes 里没有，但集合页文案里有，是矛盾源，按 spec 不采信集合页）。
  - **竞品红线**：证据里出现的品牌（Hobby Lobby、The Mahjong Line、My Fair Mahjong、Amazon 卖家）**全部抽象成「一位群友」**，无一指名。质量抱怨抽象成「印刷面 vs 雕刻面的失效方式不同」这一购买判断标准。
  - 内链：`mahjong-tile-size-readability`、`how-to-start-a-mahjong-group`、`mahjong-for-seniors`、`mahjong-accessories-guide`，共 4 篇 + 1 产品页。**刻意补了 `--full` 报出的唯一一条内链 MED**：`mahjong-for-seniors` 入站链接 1 → 2（达标）。**三篇未发布草稿一条都没链**（会 404），这是本次专门检查的一项。
  - **字数**：纯正文 1,472 词（不含标题与锚点导航），在 spec 的 1,100–1,500 区间内；含标题 1,551；inventory 脚本口径 1,610。初稿 1,906 词，砍掉 355 词，做法是逐段压缩，**四个内链、全部社群证据、全部产品事实一条未减**。**三种口径差异要记住：脚本口径 = 纯正文 + 标题 79 词 + 锚点导航约 59 词。**
  - 本轮否决：无新增否决词（本次直接用了候选池里已实证的那一条）。
  - **站点问题（连续第四次报告，未擅自改动）**：`--full` 仍报 1 条 HIGH，`american-mahjong-rules`（已发布）缺封面图，导致 Article 结构化数据缺 `image`。**这是用户侧动作，已连续四轮未处理。** 另有 3 条缺图 MED 全部是待发布草稿，属正常。新增 1 条 MED：`how-to-host-a-cozy-mahjong-night-at-home` 仅 604 词 vs 中位数 1,496，属早期文章，建议扩写而非新增。
- 2026-08-20：新增草稿 `your-first-mahjong-tournament`（gid://shopify/Article/618539745577，未发布，待用户配图）。主关键词 `mahjong tournament` **720/月，竞争 LOW index 1**，蚕食 clean 且已正文实证。
  - **方法论新发现（重要，与 08-17 那条互补）：`--cannibalize` 报 clean 也可能是假的。** 本轮候选 `mahjong terms` 720 / index 15 连续三次报 clean，但把 atom feed 十篇正文落盘后按标题结构检查，发现新手指南有一节 H2 叫 `The Words You'll Hear at the Table`，里面是一张 9 条术语表（Pung / Kong / Quint / Sextet / Pair / Run / colors / Exposure / NEWS）。**那一节就是「mahjong terms」这个查询要的东西**。脚本判 clean 的机制很简单：站上从来不写 `terms` 这个词，用的是 `Words`，而脚本比的是词不是意图。
    - **两个方向的误判现在都有实例了**：08-17 的 `3 player mahjong` 是**脚本报 HIGH、实为伪报**（判别词退化到只剩一个泛词）；本次的 `mahjong terms` 是**脚本报 clean、实为真重叠**（站上用同义词写了同一件事）。
    - **判定规则升级**：`--cannibalize` 的两种结论都只是线索。**动手写之前，必须把候选词的搜索意图翻译成 2 到 3 个同义表达，再回正文与 H2 标题里搜一遍。**只搜关键词本身会漏掉同义覆盖。本次生效的具体做法：把 atom feed 拆成十个 txt，对「意图」而不是「词」做正则（清洁类搜 clean/wash/wipe/yellow，术语类搜 glossary/terminology/vocabulary/term，锦标赛类搜 tournament/competitive/tourney）。
  - **假朋友清单（这个站特有，下次直接用）**：`washing the tiles` 是洗牌不是清洁；`wipe clean` 出现在牌垫段落；`wash out` 说的是反光把牌面冲淡；`Soap` 是白板的绰号；`Declaring Mah Jongg` 里的 `mah`/`jongg` 会让任何含 `mah jongg` 的候选词报 HIGH。本轮 `mah jongg tournament` 报 HIGH 就是最后这一条造成的，实为伪报。
  - **社群证据（MJTI 3,642 帖，tournament / tourney 检索 35 条，取高互动）。这次是直接证据不是邻近证据**：
    - **2,351 互动 / 484 评论**「I Played My First Mahjong Tournament. The Tiles Won. A Survivor's Field Report. **Nobody warned me.**」——全数据集里互动最高的帖子之一，且主题与本篇逐字对应。成文开头那三段的来源。
    - 853 互动 / 220 评论「大家是真的分不清锦标赛和平时打有什么区别。1. 要交报名费……」——明确指出「认知差」这件事本身就是需求。
    - 616 互动 / 123 评论「『聪明到会打麻将，难道不该适应任何牌面？』——能适应不是问题所在。问题是竞技场合该不该让人把注意力花在解码牌面上」——成文「你会打到没见过的牌」一节，也是产品连接的来源。
    - 395 互动 / 99 评论 一位一年办四场的联合主席自述赛制：33 桌、三轮、每轮四局——成文赛制描述的唯一具体数字来源，且文中明写「下一家会不一样」。
    - 223 互动 / 172 评论 有人报「bird bam」被要求说全「one bam」，拒绝后全桌尴尬——成文「报牌要报全」一节。
    - 130 互动 / 45 评论「锦标赛就是竞技环境，不是友谊赛。除非是 gentle 场，不熟 NMJL 规则、打不完一局就别来」——成文「你该不该去」一节，也是不劝进的依据。
  - **事实红线处理**：赛制**因主办方而异**，全文开篇即说「没有全国统一模板」，所有具体数字都归给某一位主办方，并把「报名页与规则单是权威」重复了三次。**没有写任何具体分值**，只说分值来自当年 NMJL 牌型卡，避开了 `mahjong scoring` 被否的事实过期风险。
  - **赌博红线处理**：`entry fee` 与 `prizes` 各出现一次，且都写成活动运营成本（场地、工作人员、午餐、奖品），不写金额、不写现金、不出现 betting / wager / stakes / payout。`bettor` 一词全文未用。
  - **产品连接刻意不过度**：Averill 是花卉主题牌，而社群正在吵主题牌该不该进赛场。**文中没有声称 Averill 是「tournament legal」**，反而主动写了一条对自己不利的提醒：「带自己的牌时，主题牌要多想一层，这是主办方的问题，不是厂家能替你回答的。」产品放在「赛前在家练」这个真实场景上，讲的是雕刻牌面为什么好读（有边缘有阴影，不是平面涂层），并明写不含 racks / pushers / mat / 牌型卡。
  - **量级要打折**：锦标赛簇去重后约 2,030/月（720 + 480 + 260 + 170 + 170 + 110 + 70 + 30 + 20，`mahjong fever tournaments` 140 是主办方品牌名已剔除）。但其中 `near me` 两条 550 与 `destination` 260 属本地/找活动意图，全国性博客接不住；`online` 20 无关。**可承接的信息型部分保守估计 400–700/月，这是判断不是测量。**
  - 内链：`mahjong-tile-size-readability`、`american-mahjong-rules`、`how-to-start-a-mahjong-group`、`mahjong-for-seniors`、`mahjong-party-ideas-welcoming-game-night`，共 5 篇 + 1 产品页。**刻意覆盖了 `--full` 报出的两条 MED**：`mahjong-for-seniors` 入站链接 0 → +1，`how-to-start-a-mahjong-group` 入站 1 → +2（达标）。
  - **字数守回规范**：正文 1,500 词（不含脚本自动生成的锚点导航），inventory 脚本口径 1,558。上一篇 1,714 超标 14% 是有意识偏离，本篇改回区间内，做法是逐段压缩而不是删小节，五个内链与全部社群证据一条未减。**两种口径差 58 词就是 TOC 导航，比较字数时要统一口径。**
  - 本轮否决：`mahjong terms`（脚本 clean 但真重叠，改扩写旧文）、`american mahjong practice` 1,000（App 意图）、`mahjong bettor`（赌博措辞 + 竞争高）、`5 player mahjong` 20（量太小，08-17 候选池该条关闭）、`how to store mahjong tiles`（配件篇已有同名 FAQ）。详见否决表。
  - **站点问题（连续第三次报告，未擅自改动）**：`--full` 仍报 1 条 HIGH，`american-mahjong-rules`（已发布）缺封面图，导致 Article 结构化数据缺 `image`。这是用户侧动作。另有 2 条缺图 MED 是两篇待发布草稿，属正常。
- 2026-08-17：新增草稿 `3-player-mahjong`（gid://shopify/Article/618520445225，未发布，待用户配图）。主关键词 `3 player mahjong` **1,600/月，竞争 LOW index 13**。
  - **蚕食检查报 HIGH，但判定为判别力衰减伪报，已实证推翻**。脚本对 `3 player mahjong` 只剩一个判别词 `player`（`3` 被剥掉、`mahjong` 被判泛词），于是任何含 "player" 的文章都得 100%，命中 `how-to-start-a-mahjong-group` 的 `Plan for the fifth player`。**实证方法**：把 atom feed 的 10 篇正文落盘，正则搜 `three[- ]player|3[- ]player|missing fourth|short a player` 等 12 个变体，全站只有 3 处命中，且全部无关——rules 篇是「all three players pay double」的付款句，group 篇是「a session with three players who chat」的出勤句，新手指南是一句**明确推掉本主题**的话："three-player table variants exist, but learn the four-player game first"。零实质覆盖，可以写。
  - **方法论沉淀（重要）**：单判别词关键词的 `--cannibalize` 结果不可直接采信。判别词只剩 1 个时，分母为 1，命中率非 0 即 100，噪音极大。**判定规则：判别词 ≤1 个且该词在本站属于泛用词（player / set / game / card）时，必须回到正文实证，不能只看脚本。** 反例对照：2026-08-12 的 `difference between chinese and american mahjong` 同样报 HIGH，但那次实证下去发现新手指南有一条 FAQ 标题逐字相同，是真重叠。两次的区别不在分数，在有没有回正文查。
  - **量级要打折**：1,600 这个数 Keyword Planner 对 `3 player mahjong` / `3 people mahjong` / `3 person mahjong` 报的是同一个值，**是同一个量桶的三种写法，不能相加成 4,800**。同簇另有 `3 player mahjong rules` 390 / index 12、`3 player mahjong set up` 50 / index 20、`american mahjong rules for 3 players` 20 / index 11。另外 1,600 里混有日式三人麻将（sanma）和在线三人局意图，簇内可见 `3 player riichi mahjong` 30、`3 player mahjong online` 10，占比不大但头部泛词一定更杂。保守估计能承接的美式实体牌意图在半数上下，是判断不是测量。
  - **社群证据（MJTI 3,642 帖，rotate / sits out / bettor / uneven / short a player 等检索共 18 条，去重取高互动）**：
    - 366 互动 / 189 评论「至少两桌时玩家怎么轮换？来的人在 4、5、6（**那次我们就打了两桌三人**）到 12 之间浮动」——直接证明真实群组会打三人局，是本篇最硬的一条。
    - 729 互动 / 156 评论「麻将过夜局来了五个人，与其有人坐冷板凳，我把两副牌合起来加了 38 张让五个人一起打」——全站检索里互动最高的一条，证明玩家会主动发明适配方案。
    - 227 互动 / 47 评论「我八岁那年因为我妈的局缺人，被按在桌上叫我『就摸就打』」——最常见的解法其实是塞一个人进去。
    - 98 互动 / 60 评论「五个人打、第五人当 bettor，被押的那家诈胡了该怎么算」——bettor 规则至今没有共识，60 条评论还在吵。成文中「写下你们桌的规矩」这条建议的来源。
    - 97 互动 / 24 评论「13 个人三桌，我们轮流把 East 换下来」——轮换排班的具体做法。
  - **证据强度要说清楚**：MJTI 这个 CSV 是**设计与配件话题筛过的子集**，不是全量群帖。直接搜「三人怎么打」只有 10 条命中且多数无关（"only three colors" 之类的误命中），换成搜出勤/轮换/人数才拿到上面 5 条。所以本篇的证据是**邻近证据**（人数不是四的困境）而非**直接证据**（有人在问三人局规则）。这个方向的需求主要由 Keyword Planner 的 1,600 支撑，社群证据是佐证。
  - **事实红线处理**：美式麻将**没有官方三人玩法**，NMJL 牌型卡是按四座写的。全文把所有方案明写为 house adaptation 而非规则，Charleston 的处理给了两种做法并说「都不是官方的，开局前定好」。另主动写了一条**反向建议**：不要发一副 13 张的 dummy hand，因为那 13 张牌整局退出流通，可能让牌型卡上的某些牌型变得不可能完成而没人知道原因。可推导、可核查，不是编的。
  - **产品事实按线上产品页实查**（不凭记忆）：160 张牌 = 108 + 16 + 12 + 8 flowers + **10 jokers** + 6 blanks，在玩 154。0.87W × 1.25H × 0.6D。拉链袋 + 4 张快速参考卡 + 说明手册。**产品页 Set Includes 里没有 NMJL 牌型卡**，文中未提。用 `carved`（产品页 engraved 与 printed 措辞自相矛盾，按 article-spec 统一）。文中主动写明「盒里没有 racks、dice、mat」。
  - 内链：`how-to-teach-mahjong-to-beginners`、`mahjong-accessories-guide`、`how-to-start-a-mahjong-group`、`how-to-play-american-mahjong-beginners-guide`，共 4 篇 + 1 产品页。
  - 本轮否决：joker 整簇（约 2,000/月、index 1–7，但真重叠，见否决表）、`learn american mahjong online`（HIGH）、`american mahjong strategy`（事实过期风险）。
  - **字数 1,714，超出 article-spec 的 1,100–1,500 上限约 14%**。取舍：可压的只剩机制解释或社群证据，两者都是本篇相对竞品的差异点，判断是不压。站上最长的 `mahjong-tile-size-readability` 是 1,692，量级相当。**这是有意识的偏离，不是失控。**
- 2026-08-14：新增草稿 `how-to-start-a-mahjong-group`（gid://shopify/Article/618511860009，未发布，待用户配图）。主关键词 `mahjong group` 390/月，**竞争 LOW index 5**，蚕食仅 2 篇 LOW（脚本判 safe）。
  - **真正的价值不在主词，在整簇**：`mah jongg groups near me` 1,300 / index 7、`mahjong club near me` 1,000 / index 4、`where to play mahjong near me` 480 / index 6、`where to learn mahjong near me` 390 / index 4、`mahjong meetup` 210 / index 2。整簇约 3,500/月，竞争指数**全部低于 10**，是台账开始以来竞争最低的一簇。
  - **量级要打两道折，不要按 3,500 规划预期**：① 「near me」是本地意图，Google 上半屏给地图包和 Meetup/Facebook，全国性品牌博客拿不到那一层；② 这些词里有相当比例的人最后去了 Meetup 或本地 Facebook 群，根本不点内容页。本文能承接的是「查了一圈没有本地局，那我自己开一个」这一小段人群，以及信息型的「怎么开、怎么维持」。保守估计可承接三成以下，这是判断不是测量。作为对照：整簇竞争指数低到个位数，本身就说明广告主认为这批词商业价值低。
  - **方法论第二次验证**：2026-08-12 得出的「按品类找词枯竭时改按人群与处境找词」这次再次生效。判别词 group / club / meetup / near me 在站上 10 篇文章里完全没有语料，所以蚕食检查天然干净，不需要绕。
  - **社群证据（MJTI 3,642 帖，两次正则检索共 96 条匹配，去重后取高互动）**：
    - 366 互动 / 189 评论「至少两桌时玩家怎么轮换？我们每周固定局，来的人在 4 到 12 之间浮动」——组局最核心的运营问题是出勤不稳定，直接成文中「Plan for the fifth player」一节。
    - 374 互动 / 241 评论「一群 60+ 女士的每周局，因为不摇骰子破墙起了争执」+ 245 互动 / 108 评论「新组的局里争 joker 要不要被夹在中间」——桌规争议才是散伙原因，成文中「Settle the table rules in the first month」一节。
    - 209 互动 / 163 评论「有没有比折叠牌桌更结实的桌子？我想在家里主持我们的局」+ 87 互动 / 72 评论「对折式牌桌几个月就坏了」——场地一节的具体建议来源。
    - 94 互动 / 52 评论「我在带朋友入门，想把我们镇上的局做大，有没有现成的入门小抄」——「What keeps a group meeting after month three」一节。
    - 56 互动 / 28 评论「我想在镇上开个麻将俱乐部，我是不是牌买太多了」+ 138 互动 / 45 评论「去图书馆公开局要带便宜的那副，好的那副留家里」——「How many sets a new group needs」一节。
    - 243 互动 / 37 评论「老年活动中心放假，我周一的局没了」——借场地要提前定后备主持人这条建议的来源。
  - **产品连接是结构性的不是硬凑**：开局的人几乎必然是买牌的人（56 互动那条帖直接说了）。文中把产品放在「一副还是两副」这个真实决策点上，并**主动写明不含 racks / pushers / mat**，避免用户到货后落差。
  - 内链：`mahjong-tile-size-readability`、`mahjong-gifts-game-night-hosts`（`--full` 显示入站链接只有 1，本次补 1）、`american-mahjong-rules`、`how-to-teach-mahjong-to-beginners`，共 4 篇 + 1 产品页。
  - 本轮否决：`mahjong room ideas`（HIGH index 100，且家装意图）、`mahjong club` 4,400（量被同名手游污染，只作次关键词）、`where to buy mahjong games`（交易型）。详见否决表。
  - **站点问题**：`--full` 报出 1 条 HIGH，`american-mahjong-rules`（已发布）没有封面图，导致 Article 结构化数据缺 `image`。这是用户侧动作，本次未改动任何已发布文章。
- 2026-08-12：新增草稿 `mahjong-for-seniors`（gid://shopify/Article/618497081641，未发布，待用户配图）。主关键词 `mahjong for seniors` **2,900/月，竞争 LOW index 30，蚕食 clean**，是本台账开始以来「量级 × 低竞争 × clean」组合最好的一次。
  - **量级要打折看，不要按 2,900 规划预期**：同簇的 `free mahjong for seniors` 1,300 和 `mahjong solitaire for seniors` 320 说明「老年人 + 麻将」的搜索里有相当一部分是在找**免费在线消消乐**，跟实体牌无关。Keyword Planner 不拆意图，所以 2,900 里有多少是买牌意图无法从数据直接读出。保守估计可承接的部分在三到五成，这是判断不是测量。应对办法是标题写成 “Setting Up a Table”，明确指向实体牌桌，让消消乐意图的人不点进来（点进来也会立刻跳出，反而伤指标）。
  - **新方向来源**：MJTI 数据集里按 senior/elderly/eyesight/grandma 等词跨话题检索，命中 131 帖。证据帖：81 岁母亲改造麻将房（2,377 互动 / 395 评论）、社群自发编写的「无障碍牌面设计最佳实践」清单（452 互动 / 169 评论）、「大牌好读，我们都是老花眼」（251 互动 / 99 评论）、老年活动中心放假导致周一局取消（243 互动）。
  - **产品连接是真实的不是硬凑**：Averill 是雕刻而非印刷牌面 + 单色纯背，正好命中社群那份无障碍清单里的两条。但**文章刻意没有把 0.87 × 1.25 in 说成「超大牌」**，只说处于常见区间偏大端，并明确请读者拿数字去比而不要信形容词。这是可核查的说法，不是营销话术。
  - 无医疗宣称。没有写麻将防痴呆或有认知益处，只写可观察的社交事实。
  - 内链指向 `mahjong-tile-size-readability`、`how-to-teach-mahjong-to-beginners`、`american-mahjong-rules`。后两篇在 `--full` 审计里入站内链只有 1，这次各补 1。
  - 本轮否决：`difference between chinese and american mahjong`（HIGH，真重叠）、`mahjong table size`（HIGH）、`mahjong scoring`（事实与赌博措辞风险）、`travel mahjong set`（无对应产品）。详见否决表。
- 2026-08-10：新增草稿 `why-are-mahjong-sets-so-expensive`（gid://shopify/Article/618475520297，未发布，待用户配图）。主关键词 `why are mahjong sets so expensive` 260/月，竞争 HIGH index 100，但蚕食检查 clean，次关键词 `how much does a mahjong set cost` 110/月同样 clean。**接受高 competitionIndex 的理由**：index 反映广告主出价竞争（零售商在抢），不等于自然排名难度；这是问句式信息意图，自然结果里排的是内容页；而所有低竞争候选本轮全部蚕食。新开「品质与风险 quality_risk」方向，用成本结构角度切入，把社群里的质量抱怨抽象成购买判断标准，未点名任何竞品。本轮否决 `american mahjong set for beginners`、`flowers in mahjong`（均 HIGH）以及整个 tile symbols/theme 簇（全 MED，见否决表）。文章内链刻意指向 `mahjong-gifts-game-night-hosts` 与 `how-to-teach-mahjong-to-beginners`，这两篇在 `--full` 审计里入站内链为 0。
- 2026-08-08：新增草稿 `how-to-teach-mahjong-to-beginners`（gid://shopify/Article/618471293225，未发布，待用户配图）。主关键词 `how to teach mahjong` 260/月 MEDIUM index 62，是本次拉词中唯一「有量 + 竞争不满格 + 蚕食 clean」的组合。新开「教学 / 社群带新」方向：与已有新手指南的意图分离（学 vs 教）。同时否决牌背、vintage、mat 三簇（见否决表）。候选池接近见底，下次需用户决策扩展方向：① 是否进入非麻将品类/新产品线主题 ② 是否给 Apify 充值恢复社群抓取以获取新证据 ③ 是否转为优化现有 6 篇（补 FAQ、内链、结构化数据）而非新增。
- 2026-08-07：新增 `mahjong-tile-size-readability`、`mahjong-accessories-guide`（均由用户人工配图后发布）。否决低竞争的 tiles/flowers 计数簇，改走新手指南 FAQ 路线。删除重复的 `mahjong-gifts` 草稿。全部已发布文章补齐锚点导航。修复新手指南 82 个乱码字符。
