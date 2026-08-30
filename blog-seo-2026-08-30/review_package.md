# 审阅包 · 2026-08-30

## 一句话结论

草稿已建成、未发布：主题是「规则都会了却总赢不了」的打法判断篇，主关键词 `how to win at mahjong`（1,600/月，竞争 LOW index 13）。你下一步：配封面图 → 审阅正文 → 手动发布。

---

## 1. Shopify 草稿

| 项 | 值 |
| --- | --- |
| 文章 GID | `gid://shopify/Article/618631233833` |
| handle | `how-to-win-at-mahjong` |
| 标题 | How to Win at Mahjong: Habits That Outlast Any Year's Card |
| **isPublished** | **False**（Admin API 实查确认；线上 URL 返回 404，符合预期） |
| meta title | `How to Win at Mahjong: Habits That Last | Averill`（49 字符） |
| meta desc | 138 字符，含主关键词 |
| tags | american mahjong, mahjong strategy, gameplay, game night |
| 字数 | 纯正文 1,495 词（spec 区间 1,100–1,500）；脚本口径 1,646 |
| 锚点 | 9 links / 12 ids，校验通过 |
| 乱码自检 | U+FFFD = 0 |
| em dash | 0 |
| 本地文件 | `blog-seo-2026-08-30/how-to-win-at-mahjong.html` |

## 2. 关键词（Google Ads Keyword Planner 实时数据，未降级）

**主关键词**：`how to win at mahjong` — **1,600/月，竞争 LOW，competitionIndex 13**

同桶写法（四项指标逐位相同，不可相加）：`how do you win mahjong` / `how to win at mah jongg` / `how to win mahjong game`。

**次关键词**：`american mahjong strategy` 210 / index 24、`mahjong tips for beginners` 170 / MED 61、`mahjong how to win` 140 / index 5、`how to get better at mahjong` 140 / MED 37、`mahjong strategy for beginners` 90 / MED 41。

**簇容量约 2,710/月**（已去重）。**但要打折**：裸词里混有中式打法与在线玩家意图，这一层博客接不住。**保守估计可承接 700–1,200/月，这是判断不是测量。**

**意图污染检查（按台账 08-12 的方法）结果偏干净**：`how to win mahjong solitaire` 仅 70、`how to win mahjong soul` 仅 10、`free mahjong win` 无数据。对照组 `mahjong for seniors` 的同簇免费消消乐词有 1,300。

**本轮否决**（已写进台账否决表）：
- `mahjong charleston` 簇（720 / 1,300 / 320）→ **整簇关闭**，站上五篇各写了 Charleston 的一面，heading 命中 100%
- `how long does a game of mahjong take` 320 / index 3 → 新手指南有逐字同名 FAQ，改为扩写那条
- `mahjong house rules` 210 / index 20 → vs `mahjong-etiquette` 蚕食 HIGH
- `mahjong for kids` / `teaching kids mahjong` / `mahjong for families` / `mahjong with grandchildren` → **四个措辞全部无搜索量数据**
- `mahjong cruise` 390 / `mahjong retreat` 140 / `mahjong fundraiser` 90 → 竞争极低但踩事实过期与他人组织名两条红线，保留观察

## 3. 蚕食检查

`audit_blog.py --cannibalize "how to win at mahjong"` → **no meaningful overlap, safe to target**（唯一判别词 `win`）。

按台账 08-20 升级后的规则做了**正文实证**（脚本两种结论都不可直接采信）：17 篇正文（含 4 篇草稿）+ 全部 h2/h3 落盘，正则搜打法判断类同义词。

| 词 | 全站命中 | 判定 |
| --- | --- | --- |
| `strateg` | 3 | 全部假朋友：两处是同一句推迟句，一处是"a little strategy"泛用形容 |
| `defensive` | 1 | 就是那句推迟句 |
| `odds` | 2 | **新增假朋友**：牌型家族名 `odds (13579)`，指单数牌不是概率 |
| `win` / `winning` | 10 | 多为社交场景句（谁赢了大牌、赢家得塑料小鸭），及 rules 篇 `When Nobody Wins` 流局机制 |
| `improve your game` / `commit to a hand` / `pick a hand` / `read the table` | **0** | 零覆盖 |

**结论：真 clean，可以写。**

## 4. 选题理由与源帖证据

**选题入口是本站自己写下的一句推迟句。** `how-to-teach-mahjong-to-beginners` 正文里逐字列着第一课不该教的东西：*"strategy about defensive discarding, and any discussion of which hands are statistically stronger"*。**被本站主动推迟的话题，就是一个本站已确认存在、却尚未覆盖的搜索意图。**（08-17 的三人局篇也是这样来的，两次实例，已升级为方法写进 `references/keyword-research.md`。）

源帖（MJTI 3,642 帖，62 条检索命中，取高互动；**是直接证据不是邻近证据**）：

| 互动 / 评论 | 内容 | 用在哪 |
| --- | --- | --- |
| **404 / 98** [链接](https://www.facebook.com/groups/MahJonggThatsIt/permalink/25517967587821413/) | open play 中高级桌，一位玩家先亮 Ws 的 pung，几轮后又亮 8 craks 的 pung，最后打成 wall game，"另外两人的挫败感肉眼可见" | **开篇场景 + 全文立意**，把「输」具体化成一个可教的动作 |
| **373 / 210** [链接](https://www.facebook.com/groups/MahJonggThatsIt/permalink/27786663127618503/) | "这算好策略还是没风度，还是两者都是？"（扣住领先者需要的花牌） | 「防守就是留心」一节。**210 条评论没有共识，这个没有共识本身就是结论**，并导流礼仪篇 |
| **298 / 155** [链接](https://www.facebook.com/groups/MahJonggThatsIt/permalink/27580046711613480/) | 从对手的 kong + 6 张花反推出只可能是两条牌型之一，据此避开某些弃牌 | 「你的亮牌是一句所有人都读得懂的话」一节 |
| **239 / 96** [链接](https://www.facebook.com/groups/MahJonggThatsIt/permalink/27039198785698278/) | 一月入门的新手：第一轮该不该叫花牌亮 FFF？"我觉得太早了" | 「晚定，定了就定死」一节 |
| **230 / 56** [链接](https://www.facebook.com/groups/MahJonggThatsIt/permalink/25903893025895532/) | "一个人练麻将……单练对我的 Charleston 和对牌型卡的熟悉度帮助很大"，并用 neighborhoods 称呼牌型家族 | 练习一节 + 产品连接；`neighborhoods` 一词直接采用 |
| **92 / 67** [链接](https://www.facebook.com/groups/MahJonggThatsIt/permalink/25755541684064001/) | "刚发到 13 张牌时怎么理牌？"（花左、风箭 joker 右、数牌居中升序） | 「每周用同一种方式理牌」一节 |
| **1,095 / 274** [链接](https://www.facebook.com/groups/MahJonggThatsIt/permalink/26701600912791402/) | 逐年发攻防思路的玩家："完全不是规定性的，牌流和运气各人不同" | 结尾一段，也是全文口径依据（不给必胜法） |

另用 125/26（用自己需要的花换别人亮出的 joker）与 90/24（还没定牌型就亮了 kong）两条作补充。

## 5. 红线处理

- **事实过期**（本轮最需小心的一项，也是 08-17 暂缓 `american mahjong strategy` 的原因）：通篇**不写任何具体牌型、不写任何分值**；标题、第三段、结尾三处明写牌型卡逐年重发；源帖里的「2026 年卡花牌很重」**刻意抽象成「今年的牌型卡」**，不写年份不写结论。全文讲的是理牌 / 按家族读卡 / 何时亮牌 / 亮牌暴露什么 / 何时花 joker 这五类**不依赖具体牌型的判断**。
- **赌博措辞**：无 bet / wager / stakes / payout / odds。wall game 一节不写任何计分与输赢结算。
- **竞品**：证据里出现的 Miss Mahjong、Mahjong4Friends、Sunday Mahjong、Mahjong Atelier、MJTI 等**全部抽象成「一位玩家」「一个在线平台」**，发帖人姓名未写入正文。
- **产品事实**：2026-08-30 实查线上产品页 —— 160 张（154 在玩 + 6 空白备用）、carved acrylic、0.87"W × 1.25"H × 0.6"D、珊瑚橙牌背、拉链袋 + 说明手册 + 4 张快速参考卡、180 天保修。用 `carved`。未提 NMJL 牌型卡随盒附送。
- **两条对自己不利的话**（刻意保留）：① 盒里没有 racks / pushers / mat；② **「雕刻牌面对牌型卡毫无帮助。牌好读只消掉『这是什么牌』那一次停顿，消不掉『该拿它怎么办』那一次，而后者才是整个游戏。」**

## 6. 内链目标（全部实查 PUB=True，四篇草稿一条没链）

| 目标 | 锚点位置 | 备注 |
| --- | --- | --- |
| `how-to-play-american-mahjong-beginners-guide` | 读卡一节 | |
| `american-mahjong-rules` | 叫牌/亮牌机制 | |
| `mahjong-etiquette` | 防守争议 | **`--full` 报入站 0** |
| `3-player-mahjong` | 三个人时的练习桌 | **`--full` 报入站 0** |
| `mahjong-lessons` | 宁可有人教 | **`--full` 报入站 0** |
| `/products/monets-garden` | 在家练习一节 | 产品链接 |

**一次动作把 `--full` 的三条 internal-links MED 全部补掉。**

## 7. 质量闸门结果

`shopify_article.py create` 全部通过，**未使用 `--force`**：无被禁标题短语、无 AI 腔命中、meta title 49 字符、meta desc 138 字符、有产品链接、有站内文章链接、无占位符、有 FAQ、锚点全部可解析、U+FFFD = 0。`verify` 复核 `isPublished: False`。

## 8. ⚠️ 站点问题（`--full` 本轮 5 条 HIGH，比上轮多 3 条）

**新增的三条是发布流程造成的**：`3-player-mahjong` / `mahjong-etiquette` / `mahjong-lessons` 已于 08-29 发布，**但都没有配封面图**。缺图在草稿上只是 MED，一旦发布就升为 HIGH（Article 结构化数据缺 `image`，Google Article 富媒体结果拿不到，og:image 退回站点 logo）。

**当前 `PUB=True 且 IMG=NO` 的完整清单（四篇，都需要补图）**：
1. `american-mahjong-rules`（连续第七轮报告）
2. `3-player-mahjong`
3. `mahjong-etiquette`
4. `mahjong-lessons`

**另一条 HIGH（连续第二轮）**：`american-mahjong-rules` 的 TOC 里 `#cheat-sheet` 指向不存在的 id（TOC 16 条 vs 12 个 id），读者点了不跳转。**按硬规则未擅自修复**，修复只需对该文跑 `shopify_article.py toc` 并显式传 `--published`，**等你确认后再动**。

其余：4 条缺图 MED（均为待发布草稿，属正常）、1 条 thin-content MED（`how-to-host-a-cozy-mahjong-night-at-home` 604 词）、1 条封面图缺 alt、2 篇 meta title 超 60 字符、1 篇 meta desc 166 字符、3 篇无 tags、1 条作者名不一致（`Averill` / `The Averill Team` / `Averill Mahjong` 三种并存）。

## 9. ⚠️ 台账漂移（已修正）

云端仓库的 `seo-state/` 只有一次提交，台账最后更新停在 08-26，但实查发现站上已有 `mahjong-etiquette`（1,634 词，08-29 发布），而台账里它还躺在候选池 —— **说明某一轮产出后台账没有 push 回仓库**。本轮已把它补登进「已占用主关键词」并从候选池移除。本轮所有产物已 commit + push。

## 10. 你的待办

1. **配封面图**（发布的前置步骤，不是并列项）。避开这几个已知配色错误的素材：`premium-gift-box.jpg`、`branded-carrying-bag.jpg`、`instruction-manual.jpg`、`four-rules-reference-cards.jpg`、`full-tile-set-monets-garden.jpg`
2. **审阅正文**（下方有完整中文对照翻译）
3. **手动发布**
4. 顺带处理积压：上面第 8 节那四篇已发布但缺封面图的文章 + `american-mahjong-rules` 的坏锚点（需你确认后我才动已发布文章）

---

# 英文正文 + 完整中文对照翻译（逐句）

## H1 / 标题

**How to Win at Mahjong: Habits That Outlast Any Year's Card**

> 怎样赢下一局麻将：比任何一年的牌型卡都活得久的几个习惯

## 开篇

**At an open play session, a woman watched the player to her right call a discard and expose a pung of winds.**

> 在一次公开牌局上，一位女士看着右手边的玩家叫走一张弃牌，亮出了一副风牌的 pung。

**A few turns later the same player called again and exposed a pung of eight craks.**

> 几轮之后，同一个人又叫了一次牌，亮出一副八万的 pung。

**Two exposures, and no line on the card holds both.**

> 两次亮牌，而牌型卡上没有任何一条牌型能同时容下它们。

**The hand ran down to the wall, nobody declared, and the frustration at that table, as she put it afterward, was palpable.**

> 那一局一路打到牌墙见底，没有人叫胡，用她事后的话说，那桌上的挫败感肉眼可见。

**That table did not lose to luck.**

> 那一桌不是输给了运气。

**It lost to an exposure made three turns too early.**

> 是输给了一次早了三轮的亮牌。

**Anyone asking how to win at mahjong once the rules have stopped being the problem is really asking about that gap, the one between knowing what a pung is and knowing when a pung costs you the hand.**

> 当规则已经不再是障碍，还在问怎样赢下一局麻将的人，其实问的是那道缝：知道 pung 是什么，和知道一副 pung 什么时候会让你输掉这一局，中间隔着的那道缝。

**American mahjong makes the question harder than it should be, because the National Mah Jongg League reissues its card every year and the specific hands move with it.**

> 美式麻将把这个问题弄得比本该的更难，因为 National Mah Jongg League 每年重发一次牌型卡，具体的牌型也跟着变。

**Advice built on this year's lines expires next spring.**

> 建立在今年这些牌型上的建议，明年春天就过期了。

**What follows is the part that does not move: how you hold your rack, how you read the card, when you commit, and what your own tiles are telling everyone else at the table.**

> 下面写的是不会变的那部分：你怎么理牌、怎么读牌型卡、什么时候定下来，以及你自己的牌正在向同桌其他人说些什么。

## H2 · Sort your rack the same way every week（每周用同一种方式理牌）

**One player asked the groups how she should organize the thirteen tiles she is dealt, and sixty-seven people answered.**

> 一位玩家在群里问，刚发到手的十三张牌该怎么理，六十七个人回了她。

**Her own system puts flowers to the left, winds and dragons and jokers to the right, and the number tiles between them in ascending order by suit.**

> 她自己的做法是：花牌放左边，风牌、箭牌和 joker 放右边，数牌摆在中间，按花色升序排列。

**The replies argued about the order.**

> 回帖的人对顺序吵得很热闹。

**Almost nobody argued about the principle.**

> 几乎没有人质疑这件事本身。

**The order matters less than the repetition.**

> 顺序其实没有「重复」重要。

**When your rack looks the same at the start of every hand, you stop reading it and start seeing it, and the holes in it announce themselves without effort.**

> 当你的牌架每一局开始时都长成同一个样子，你就不再是在「读」它，而是在「看」它，缺口会自己跳出来，不需要你费力去找。

**Sort once at the deal, then sort again after the Charleston, because that is the moment your hand changes shape.**

> 发牌后理一次，Charleston 传牌结束后再理一次，因为那正是你这手牌变形的时刻。

## H2 · Learn the card in families, not line by line（按家族读牌型卡，不要一条一条背）

**New players try to memorize the card.**

> 新手想把牌型卡背下来。

**Experienced ones learn where to look.**

> 老手学的是该往哪儿看。

**The hands are grouped into families, and most players settle into two or three they return to.**

> 牌型是按家族分组的，多数玩家最后都会固定回到其中两三组。

**A woman a few months into the game listed hers as any like numbers, consecutive runs, and winds and dragons, and called them her favorite neighborhoods, which is a better word for it than sections.**

> 一位入门几个月的女士说她的是 any like numbers、consecutive runs 和 winds and dragons，并把它们叫作自己最喜欢的「街区」，这个词比「分区」贴切得多。

**Knowing your neighborhoods gives you something concrete to do in the first ten seconds after the deal.**

> 知道自己的街区在哪，能让你在发牌后的头十秒有件具体的事可做。

**You check two families instead of scanning every line.**

> 你只看两个家族，而不是把每一条牌型都扫一遍。

**It also survives the annual reissue, since the lines move each year but the families largely stay put.**

> 这个办法也扛得住每年换卡，因为牌型每年在动，家族基本不动。

**If the card itself is still the wall you keep hitting, our beginner's guide to American mahjong walks through how it is laid out.**

> 如果牌型卡本身还是你反复撞上的那堵墙，我们的《美式麻将新手指南》里讲了它是怎么排布的。

## H2 · Choose late, then commit clearly（晚一点再定，定了就定清楚）

**A player who started in January posted a hand for review.**

> 一位一月才开始打的玩家发帖请大家帮她复盘一手牌。

**After the Charleston she held five flowers, six evens across two suits, and two jokers.**

> Charleston 结束时，她手上有五张花、两门花色里六张偶数牌，还有两张 joker。

**On the first round someone discarded a flower.**

> 第一轮就有人打出一张花。

**Should she have called it and exposed three flowers that early?**

> 她该不该叫下来、那么早就亮出三张花？

**She decided it was too soon.**

> 她当时判断太早了。

**Ninety-six people weighed in, and the thread was less about the flower than the shape of the decision.**

> 九十六个人参与讨论，而整个帖子谈的与其说是那张花牌，不如说是这个决定的形状。

**The frame worth carrying: hold two candidate hands through the Charleston and into the first turns, and treat your first exposure as the moment flexibility ends.**

> 值得带在身上的框架是：让两个候选牌型一起走过 Charleston 并进入前几轮，然后把你的第一次亮牌当作灵活性终结的那一刻。

**Before you call a tile, ask what the call closes off, not only what it opens.**

> 叫牌之前先问一句：这一叫关掉了什么，而不只是打开了什么。

**Another newer player asked whether a kong she exposed before settling on a hand could still be steered toward a different line, which is the same question arriving too late.**

> 另一位新手问，她在还没定牌型时就亮出的一副 kong，还能不能往别的牌型上带，那是同一个问题，只是来得太晚了。

**The mechanics of calling and exposing are set out in our American mahjong rules reference.**

> 叫牌与亮牌的具体机制，写在我们的《美式麻将规则》参考页里。

## H2 · Your exposures are a sentence the table reads（你的亮牌是一句全桌都读得懂的话）

**Return to the winds and the eight craks.**

> 回到那副风牌和那副八万。

**Two exposures that cannot live on one line, and every attentive player at that table knew it.**

> 两次亮牌不可能落在同一条牌型上，桌上每个留心的人都看出来了。

**Reading exposures is ordinary practice: one player described watching an opponent expose a kong of two craks and then lay down six flowers, worked out that only two lines could hold both, and told her table what to stop discarding.**

> 读别人的亮牌是很平常的做法：一位玩家说她看着对手亮出一副二万的 kong，接着又摆下六张花，她推断出只有两条牌型能同时容下这两样，于是提醒同桌不要再打某些牌。

**She noted the group was simply working on defensive play.**

> 她特意说明，她们只是在练防守而已。

**So before you expose, read your own exposure the way the others will read it.**

> 所以在你亮牌之前，先用别人会用的读法，读一遍你自己的亮牌。

**Sometimes the tile is worth the information you hand over.**

> 有时候那张牌值得你交出去的那点信息。

**Early in a hand it usually is not, because the same tile tends to come around again and your neighbors will remember the pung long after you have abandoned the line.**

> 但在一局的早期通常不值得，因为同一张牌往往还会再出现，而在你早就放弃那条牌型很久之后，邻座还记得你亮过那副 pung。

## H2 · Defense is mostly paying attention（防守大半就是留心）

**A player asked the groups whether holding back a flower she knew the leader needed was good strategy or poor sportsmanship.**

> 一位玩家在群里问：明知领先的人要那张花却扣着不打，这算好策略还是没风度。

**Two hundred and ten comments later there was no consensus, which is the finding.**

> 两百一十条评论过后仍然没有共识，而这本身就是结论。

**Defensive play sits in the space your table defines rather than in any rulebook, so it is worth knowing where your group stands before you lean on it.**

> 防守打法落在你这一桌自己划定的空间里，而不在任何规则书上，所以在你依赖它之前，值得先弄清自己这一群人怎么看。

**Our piece on mahjong etiquette covers how those unwritten agreements usually get settled.**

> 我们那篇讲麻将礼仪的文章，写了这些不成文的约定通常是怎么定下来的。

**The defensive habits nobody disputes are smaller.**

> 没有人有异议的那些防守习惯，都要小得多。

**Notice which tiles stop being discarded.**

> 留意哪些牌开始没人打了。

**Late in a hand, prefer a tile you have already seen twice over one nobody has touched.**

> 一局后段，宁可打一张你已经见过两次的牌，也不要打一张谁都没碰过的。

**Slow down when a player has three exposures and a quiet rack, because that is the table telling you something out loud.**

> 当某个人已经亮了三副牌而牌架又很安静时，把速度放慢，因为那是牌桌在大声告诉你一些事。

## H2 · Jokers buy flexibility, so spend them late（joker 买的是灵活性，所以要晚点花）

**One player described trading a flower she needed for a joker sitting in someone's exposure, reasoning that a joker does more work later.**

> 一位玩家说，她会用一张自己也需要的花牌，去换别人亮牌里的那张 joker，理由是 joker 在后面能干更多活。

**That is a fair trade to consider, and it points at the general rule: a joker is worth most while your hand is still undecided, and worth least once your line is fixed and only one tile is missing.**

> 这笔交换值得考虑，它也指向一条通则：当你这手牌还没定下来时，joker 的价值最高；一旦牌型已定、只差一张牌，它的价值最低。

**Hold them through the ambiguity.**

> 在还没想清楚的那段时间里，先握住它们。

**Spend them on the tiles that are genuinely scarce for you, not on the first gap you can fill.**

> 把它们花在对你来说真正稀缺的牌上，而不是花在第一个能填上的缺口上。

## H2 · A wall game is a result, not a failure（流局是一种结果，不是一次失败）

**The story this article opened with ends in a wall game, and most tables read that as twenty wasted minutes.**

> 本文开头那个故事以流局收场，多数牌桌会把它读成白白浪费的二十分钟。

**It is not.**

> 并不是。

**A hand where nobody declares is a hand where you fed nobody, and over a long night that shows up in the count.**

> 没有人叫胡的一局，也是你没有喂给任何人的一局，而在一个漫长的夜晚里，这是会算进总账的。

**Some of the best playing you will ever do looks, from the outside, like nothing happened at all.**

> 你这辈子打得最好的一些牌，从外面看，就像什么都没发生过。

## H2 · What to practice between game nights（两次牌局之间该练什么）

**A player a few months into the game posted a photo of a solo session at her own table and said practicing alone had done more for her Charleston and her card familiarity than anything else she tried.**

> 一位入门几个月的玩家发了一张自己一个人在牌桌前练牌的照片，说单练对她的 Charleston 和对牌型卡的熟悉度，比她试过的任何别的办法都管用。

**It is the least glamorous advice here and the one with the shortest path to results.**

> 这是本文里最不好看的一条建议，也是见效路径最短的一条。

**Deal yourself thirteen tiles, find the two closest lines, decide what you would pass, discard one, and start over.**

> 给自己发十三张牌，找出最接近的两条牌型，想好你会传出什么，打掉一张，然后重来。

**Ten minutes, twice a week.**

> 十分钟，一周两次。

**If three of you are around on a given evening, a three-handed adaptation gives you a live table instead of a drill, and if you would rather be walked through it by a person, a class shortens the whole process.**

> 如果某个晚上正好有三个人在，一套三人打法能把练习变成一张真牌桌；而如果你更希望有个人带着你走一遍，上课能把整个过程缩短。

**Practice is also where the set on your table starts to matter.**

> 练习也是牌本身开始产生影响的地方。

**The Monet's Garden set holds 160 tiles, 154 in play plus six blank spares, with carved acrylic faces at 0.87 in W by 1.25 in H by 0.6 in D and coral-orange backs.**

> Monet's Garden 这副共 160 张牌，其中 154 张在局中使用，另有六张空白备用牌，牌面为雕刻亚克力，尺寸 0.87 英寸宽 × 1.25 英寸高 × 0.6 英寸厚，牌背为珊瑚橙色。

**It ships with a zippered pouch, an instruction booklet, and four quick reference cards, which is the detail that matters at a practice table: everyone has one in front of them rather than passing a single card around the rack.**

> 随盒附拉链收纳袋、说明手册和四张快速参考卡，而最后这一项正是练习桌上真正起作用的细节：每个人面前都有一张，不必把同一张卡在牌架之间传来传去。

**Two honest limits.**

> 两条老实话。

**Racks, pushers and a mat are not in the box.**

> 牌架、推牌器和牌垫不在盒子里。

**And carved faces do nothing for the card.**

> 还有，雕刻牌面对牌型卡毫无帮助。

**A readable tile removes the pause where you are working out what you are holding.**

> 一张好读的牌，消掉的是「我手上这是什么牌」那一次停顿。

**It does not remove the pause where you decide what to do with it, and that second pause is the entire game.**

> 它消不掉「该拿它怎么办」那一次停顿，而后面这一次停顿，才是整个游戏。

## H2 · FAQ

**Should I pick my hand during the Charleston or after it?**

> 我该在 Charleston 期间就定牌型，还是等它结束之后？

**Neither, exactly.**

> 严格说来，两者都不是。

**Most steady players narrow to two candidate families during the Charleston, pass toward both, and let the first several draws break the tie.**

> 多数打得稳的玩家会在 Charleston 期间把范围收到两个候选家族，传牌时朝这两个方向同时靠，然后让开局的头几张摸牌来打破平局。

**Deciding before the passing ends means you pass away tiles you will want back.**

> 在传牌结束前就定下来，意味着你会把之后想要回来的牌传出去。

**Deciding much after it means you spend turns with no direction at all.**

> 拖到传牌结束很久才定，意味着你会有好几轮完全没有方向。

**Is it poor manners to hold a tile another player needs?**

> 扣着别人需要的牌不打，算失礼吗？

**Groups genuinely differ.**

> 各个群体的看法是真的不一样。

**Some treat it as normal defensive play, others read it as unfriendly at a social table, and the same question has run for hundreds of comments without settling.**

> 有些人把它当作正常的防守，有些人觉得在社交性质的牌桌上这样做不友好，同一个问题吵了几百条评论也没有定论。

**The safe move is to ask your group how it sees the matter early, ideally before the situation arrives.**

> 稳妥的做法是早点问清你这一群人怎么看，最好在这种局面出现之前。

**Does playing alone or online actually help my table game?**

> 一个人练或者在线上打，对我在真牌桌上的表现真的有帮助吗？

**It helps unevenly.**

> 帮助是不均匀的。

**Solo and online play build card familiarity and speed, which are real gains.**

> 单练和线上对局能练出对牌型卡的熟悉度和速度，这是实打实的收获。

**What they do not build is reading live exposures and the timing of calls, since a screen sorts and prompts for you.**

> 它们练不出来的是读现场的亮牌，以及叫牌的时机，因为屏幕会替你理牌、替你提示。

**Treat them as drills between game nights rather than as substitutes for a table.**

> 把它们当成两次牌局之间的练习，而不是牌桌的替代品。

## 收尾

**None of this makes a win arrive on schedule.**

> 这些都不能让胡牌按时到来。

**Tile flow is tile flow, and one player who posts her tips every year is careful to say her advice is in no way prescriptive.**

> 牌流就是牌流，一位每年都发一次心得的玩家特意说明，她的建议完全不是规定性的。

**What these habits do is make sure that when the hand does come to you, you are not three turns into the wrong line and holding an exposure that says so to everyone at the table.**

> 这些习惯能做到的，是保证当那手牌真的来到你面前时，你没有在一条错的牌型上走了三轮，也没有亮着一副把这件事告诉全桌的牌。
