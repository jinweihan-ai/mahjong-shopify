# 审阅包 · 2026-09-02

## 一句话结果

Shopify 草稿已建成（**未发布**），主题是「**为什么麻将现在这么火，以及要坐上一张牌桌需要什么**」。你下一步：配封面图 → 审阅 → 手动发布。

---

## 1. Shopify 草稿

| 项 | 值 |
| --- | --- |
| 文章 GID | `gid://shopify/Article/618647453993` |
| handle | `why-is-mahjong-so-popular` |
| 标题 (H1) | Why Is Mahjong So Popular, and What It Takes to Join a Table |
| **发布状态** | **isPublished: False**（Admin API 实查确认，线上 URL 返回 404，符合预期） |
| meta title | `Why Is Mahjong So Popular? \| Averill`（36 字符，≤60，以 ` \| Averill` 结尾 ✅） |
| meta description | 140 字符（在 120–160 区间 ✅） |
| tags | american mahjong, mahjong popularity, new players, getting started, game night |
| 封面图 | **无（等你配）** |
| 正文字数 | 纯正文 **1,500** 词（spec 上限 1,500）；create 脚本口径 1,638 |
| 锚点导航 | 8 links / 11 ids，全部可解析 ✅ |
| U+FFFD 乱码自检 | **0** ✅ |
| em dash | **0** ✅ |
| 本地文件 | `blog-seo-2026-09-02/why-is-mahjong-so-popular.html` |

---

## 2. 关键词（Google Ads Keyword Planner 实时数据，美国，2026-09-02 实拉）

**没有降级，本次是真实搜索量。**

**主关键词**：`why is mahjong so popular` — **480/月，竞争 LOW，competitionIndex 20**，出价区间仅 $0.020–$0.043。

**次关键词**：`mahjong popularity` 210 / index 7 · `mahjong trend` 170 / index 3 · `why is everyone playing mahjong` 40 / index 8 · `mahjong resurgence` 20 / index 1

**簇容量（已按同桶规则去重）约 930/月**，剔除了 `most popular mahjong` 20（HIGH index 88，交易意图）。

**意图污染检查（按 08-25 判读标准）**：三个探针 `why is mahjong popular in china`、`mahjong solitaire popular`、`is mahjong popular in america` **全部 UNSPECIFIED 无数据**，这是最强的干净信号。**但仍要打折**：裸词里一定混有查中国/日本麻将文化的人。**保守估计可承接 300–450/月，这是判断不是测量。**

### ⚠️ 本轮最重要的一条其实是「否决」

`is mahjong hard to learn` **3,600/月，竞争 LOW index 7** —— 这是台账开始以来「量级 × 低竞争」最诱人的组合之一（与你已发布的 `mahjong-lessons` 并列纪录）。**我没有写它，因为实证下去是三重真重叠**：

1. `mahjong-for-seniors` 有一条 FAQ 逐字叫 `Is American mahjong hard to learn later in life?`
2. `mahjong-lessons` 有一整段就是这个问题的答案：「American mahjong is not a difficult game to understand. The rules fit comfortably on a page. What makes it hard is doing all of it at speed...」
3. `how-to-teach-mahjong-to-beginners` 有 FAQ `How long does it take to learn American mahjong?`

新开一页会正面蚕食站上最好的关键词资产。**建议：下一轮不写新文章，改为扩写 `mahjong-lessons` 那一段 + 给两篇各加一条 FAQ，把这个约 4,400/月的簇接住。** 这比再写一篇新文章的收益高。

**其他本轮否决**：cheat sheet 整簇约 8,000（index 99–100，且意图是要 PDF 不是读文章，内容还逐年过期）· 老牌缺件整簇 2,140（候选池那条至此关闭）· `what are mahjong tiles made of` 590（真重叠 vs 清洁篇）· `games like mahjong` 590（意图是把读者送走）· `benefits of playing mahjong` 140（医疗宣称红线）。

---

## 3. 蚕食检查（强制项）

`audit_blog.py --cannibalize "why is mahjong so popular"` → **`no meaningful overlap - safe to target`**

因为判别词只剩一个 `popular`（单判别词按 08-17 规则不可直接采信），**已做正文实证**：19 篇正文（含 4 篇草稿）落盘，正则搜 20 个热度意图同义词。

- `popular` / `popularity` / `trend` / `resurgence` / `renaissance` / `comeback` / `surge` / `TikTok` / `instagram` / `social media` —— **全站零命中**
- 71 处命中**全部是假朋友**：`fad` 是正则撞上 `fade`（子串误命中）· `moment` 全部指「某个瞬间」· `everyone` 全部指「桌上其他人」· `hot ` 是 `shot`

**这是全台账最干净的一次蚕食检查之一。**

**⚠️ 一个需要你知情的风险，已刻意管理**：你 08-31 发布的 `history-of-mahjong` 有一节叫 `The revival you are already part of`，是站上唯一沾边的语料。管理做法：两篇时间轴刻意分开（历史篇答「从哪来」，本篇答「为什么现在、我怎么进去」，本篇通篇不写起源与年代），八个 H2 零重复，且**本篇主动链去历史篇**并写明分工，用内链声明层级而不是竞争。

---

## 4. 源帖证据（MJTI 3,642 帖，检索命中 228 条，取高互动）

| 互动 / 评论 | 内容 | 用在哪 |
| --- | --- | --- |
| **360 / 37** | 「本周末的华尔街日报上。不敢相信我三十五年前和姐妹们穿着睡衣、哄睡孩子之后玩的那个游戏，**现在成了全国的热潮**」 [链接](https://www.facebook.com/groups/MahJonggThatsIt/permalink/27045719768379513/) | **开篇场景与全文立意**。刊物名已抽象成「一份周末报纸」 |
| **1,172 / 171** | 「对这波麻将热里的**过度商业化和捞钱**感到震惊……**我们组 45 个人，每次都在本地图书馆免费打**」 [链接](https://www.facebook.com/groups/MahJonggThatsIt/permalink/27629984219953062/) | 「热潮里可以忽略的那部分」整节。金额已抽象成「像家具一样贵的牌」 |
| **514 / 188** | 「一张照片就让你连着几个月每天刷好几次 instagram、定三个闹钟、为了抢到这副牌焦虑」 [链接](https://www.facebook.com/groups/MahJonggThatsIt/permalink/27821085734176242/) | 「牌变成了一种设计语言」一节。**本篇独有，之前没用过** |
| **405 / 254** + **387 / 185** | 两条群购帖，都在更新「已售罄 / 我们把人家清空了」 [链接1](https://www.facebook.com/groups/MahJonggThatsIt/permalink/26367182069566623/) · [链接2](https://www.facebook.com/groups/MahJonggThatsIt/permalink/26788705387414287/) | 同一节第二条证据，说明不是个例 |
| **1,051 / 255** | 「🚨新玩家🚨这是我打美式麻将的第一年……我把牌型卡**自己做了颜色标记**」 [链接](https://www.facebook.com/groups/MahJonggThatsIt/permalink/27743647868586696/) | 「为什么第一个月之后人还在」。年份已抽象成「今年的牌型卡」 |
| **268 / 216** | 一位新人冲动买了刷屏款，到货发现划痕与发丝纹，客服说不是瑕疵 [链接](https://www.facebook.com/groups/MahJonggThatsIt/permalink/27267793099505511/) | 「买得太急」的判断标准。**已抽象成「一位新人」，未指名任何厂牌** |
| **454 / 58** | 「同事发了张她在课上的照片，我一下子就懂了……现在周一是『Mahjongg Mondays』」 [链接](https://www.facebook.com/groups/MahJonggThatsIt/permalink/26897584236526401/) | 「新牌桌在哪」一节 |

### 为什么选这个方向

台账里已验证的四条找词路径本轮全部走空：候选池两条都关闭了，按处境重拉的十个种子里最好的一个是真重叠，实物来历那条 08-31 已经用掉。**这次走的是第五条路径：看老玩家在惊讶什么。**

新人发帖只证明有新人，**老玩家发帖说「不敢相信」才证明发生了变化**。本轮的入口正是那条三十五年老玩家的帖子。

**量小还做的三个理由**（不要按 480 做流量预期）：
1. 竞争指数 20、出价只有 2 到 4 美分，广告主完全没在抢，新站有机会真排上去；
2. **这是站上唯一的漏斗顶层内容** —— 19 篇里其余 18 篇都默认读者已经决定要玩了，这一篇接的是「还在旁边看」的人；
3. 判别词零语料，蚕食天然干净。

---

## 5. 内链目标（7 篇 + 1 产品页，历次最多）

**七篇全部实查 `PUB=True`**，四篇草稿一条没链（草稿 URL 返回 404）。

| 目标 | 锚文本语境 |
| --- | --- |
| `history-of-mahjong` | 「更长的版本在我们写麻将从哪来的那篇」 |
| `how-to-win-at-mahjong` | 「读牌型卡与何时定牌」 |
| `how-to-play-american-mahjong-beginners-guide` | 「一手牌是怎么打完的」 |
| `mahjong-lessons` | 「怎么分辨认真的老师和赶场的老师」 |
| `how-to-start-a-mahjong-group` | 「找一个月没找到就自己开一个」 |
| `3-player-mahjong` | 「有人临时来不了就打三人局」 |
| `mahjong-tile-size-readability` | 「怎么判断牌的尺寸」 |
| **产品页** `/products/monets-garden` | 最后一节自然落点 |

**`--full` 报的三条 `internal-links` MED 一次全部补掉**：`how-to-win-at-mahjong`（入站 0）、`history-of-mahjong`（入站 0）、`3-player-mahjong`（入站 1）。下轮应自动消失。

---

## 6. 质量闸门结果

`shopify_article.py create` 内建闸门 **全部通过，未使用 `--force`**。

| 项 | 结果 |
| --- | --- |
| 标题无被禁短语 | ✅ |
| 无 AI 腔（`elevate your experience` 等 8 条） | ✅ |
| **em dash 数量** | **0** ✅ |
| 主关键词在 H1 / 前 100 词 / meta title / meta desc / slug | ✅（正文第 98 词处出现） |
| ≥1 产品链接 + ≥1 站内文章链接 | ✅ 1 + 7 |
| 锚点导航齐全且全部可解析 | ✅ 8 links / 11 ids |
| FAQ（3 条真实问题） | ✅ |
| meta title ≤60 且以 ` \| Averill` 结尾 | ✅ 36 字符 |
| meta desc 120–160 | ✅ 140 |
| 正文无 SEO 批注 / 大纲占位符 | ✅ |
| **U+FFFD 自检** | **0** ✅ |
| 产品事实与线上产品页一致 | ✅ 2026-09-02 WebFetch 实查 |
| 无竞品指名、无赌博措辞 | ✅ |

**产品事实实查结果**（本次没有凭记忆）：160 张牌 = 108 数牌 + 16 风 + 12 三元 + 8 花 + 10 joker + 6 空白备用，在玩 154；0.87"W × 1.25"H × 0.6"D；珊瑚橙牌背；拉链袋 + 说明手册 + 4 张快速参考卡 + 送礼包装；180 天保修。产品页仍写 `engraved floral artwork`，文章按 spec 统一用 `carved`。

**事实红线**：热度类文章最容易的写法是引市场规模与增长率，**全文一个统计数字都没有**。所有关于热度的断言要么是社群里可观察的行为（课满、售罄、新厂牌不断上线），要么明写是判断。不写具体年份、不写金额。

**三条对自己不利的话（刻意保留）**：
1. **第一天不要买牌** —— 课上有牌、群里有备用，等打到第二到第六次再说；
2. 盒里没有 racks / pushers / 牌垫，**也没有那张年卡**；
3. 「好读的牌只解决了这张桌上两个问题里较小的那个：它缩短『这是什么牌』的停顿，对『该拿它怎么办』的停顿毫无作用，而后者才是这个游戏。」

---

## 7. ⚠️ 站点问题（按硬规则只报告，未擅自修复）

`audit_blog.py --full` 报 22 条，**5 条 HIGH，与上轮持平（未新增也未减少）**：

| 级别 | 问题 | 状态 |
| --- | --- | --- |
| HIGH | `american-mahjong-rules` 缺封面图 | **连续第九轮** |
| HIGH | `3-player-mahjong` 缺封面图 | 连续第三轮 |
| HIGH | `mahjong-etiquette` 缺封面图 | 连续第三轮 |
| HIGH | `mahjong-lessons` 缺封面图 | 连续第三轮 |
| HIGH | `american-mahjong-rules` 锚点 `cheat-sheet` 指向不存在的 id（TOC 16 vs IDS 12） | 连续第四轮 |

**好消息**：你 08-31 发布的 `how-to-win-at-mahjong` 与 `history-of-mahjong` **都是带封面图发的**，说明 08-29 那次裸发的做法已经改掉了。**剩下这四条是存量不是增量。**

**建议（已连续三轮给出）：给这四篇补封面图的收益高于再写一篇新文章。** 缺图在草稿上只是 MED，一旦发布就升为 HIGH（Article 结构化数据缺 `image`，og:image 退回站点 logo，拿不到 Article rich result）。

其余：4 条缺图 MED 全是待发布草稿（属正常）· 1 条 thin-content MED（`how-to-host-a-cozy-mahjong-night-at-home` 604 词 vs 中位数 1,586）· 3 条 internal-links MED（**本篇已全部补掉**）· 3 条封面图缺 alt · 2 篇 meta title 问题 · 3 篇无 tags · 1 条作者名不一致（站上并存 `Averill` / `The Averill Team` / `Averill Mahjong`）。

`--full` 的 technical 实时检查因沙箱代理 403 未能执行，是环境限制不是站点问题。

---

## 8. 你的待办

1. **配封面图**。避开这几个已知配色错误的素材：`premium-gift-box.jpg` / `branded-carrying-bag.jpg` / `instruction-manual.jpg` / `four-rules-reference-cards.jpg` / `full-tile-set-monets-garden.jpg`。**顺手加 alt 文本**（站上已有 3 篇封面图没有 alt）。
2. **审阅正文**（下面第 9 节是逐句中文对照）。
3. **手动发布**。
4. **可选但建议**：给上面那 4 篇已发布文章补封面图，并修 `american-mahjong-rules` 的 `cheat-sheet` 坏锚点。

---

## 9. 英文正文 · 完整中文对照翻译（逐句）

### 标题
**Why Is Mahjong So Popular, and What It Takes to Join a Table**
> 为什么麻将现在这么火，以及坐上一张牌桌需要什么

### 开篇

> A woman in one of the large American mahjong communities posted a photograph of a weekend newspaper spread.

一位女士在某个大型美式麻将社群里发了一张周末报纸版面的照片。

> She has played for more than thirty-five years, mostly in pyjamas with three girlfriends after the children were asleep, and there was her quiet Tuesday habit written up as a national story.

她已经打了三十五年多，多数时候是穿着睡衣、哄睡孩子之后和三个姐妹一起打，而现在，她那个安静的周二习惯被写成了一则全国性的报道。

> Three hundred and sixty people reacted, and the replies mostly said the same thing: we were here the whole time, and now everyone is arriving at once.

三百六十个人点了反应，回复里说的基本是同一件事：我们一直都在这儿，现在所有人一下子全来了。

> So why is mahjong so popular, and what does it take to get a seat at one of these tables?

那么，为什么麻将现在这么火，以及要在这样一张牌桌上坐下来，究竟需要什么？

> The honest answer to the first has little to do with the tiles.

第一个问题的诚实答案，跟牌本身关系不大。

> The answer to the second is cheaper than the noise around the game suggests.

第二个问题的答案，比围绕这个游戏的那些喧嚣所暗示的要便宜得多。

### H2：The game did not change. The room did.
> 游戏没有变，变的是房间里的人。

> American mahjong plays the way it has played for decades.

美式麻将的打法和几十年前一样。

> Four seats, a wall, the Charleston, and a card of legal hands that the National Mah Jongg League reissues once a year.

四个座位、一堵牌墙、Charleston 传牌，以及一张由 National Mah Jongg League 每年重新发布一次的合法牌型卡。

> None of that was redesigned for new arrivals.

这些没有一样是为新来的人重新设计过的。

> What changed is who is sitting down, how they found each other, and how many companies now sell to them.

变的是谁在坐下来打、他们怎么找到彼此，以及现在有多少家公司在向他们卖东西。

> That matters if you are deciding whether to try it.

如果你正在犹豫要不要试试，这一点很重要。

> This is not a trend that will move on and leave you holding gear for an abandoned hobby.

这不是一阵过去之后、留你抱着一堆被抛弃爱好的装备的潮流。

> It is a game with a governing card and generations of players who will correct your Charleston within ninety seconds of your first mistake.

它是一个有权威牌型卡的游戏，而且有好几代玩家会在你第一次出错后的九十秒内纠正你的传牌。

> The crowd is new. The game is not.

人群是新的，游戏不是。

> There is a longer version of that in our piece on **where mahjong came from** and how American play grew a card of its own.

更长的版本在我们那篇写**麻将从哪来**、以及美式打法怎么长出自己那张牌型卡的文章里。

### H2：What is actually pulling people in
> 真正把人拉进来的是什么

> Three things come up again and again, and none of them is nostalgia.

有三件事反复出现，没有一件是怀旧。

> The first is that the game requires exactly four people in one room.

第一，这个游戏需要**正好四个人在同一个房间里**。

> That sounds like a constraint. In practice it is the appeal.

这听起来像个限制。实际上，它就是吸引力本身。

> A standing table is a commitment you make to three other people, on a repeating date, with no way to half-attend it from the sofa.

一张固定的牌桌，是你对另外三个人做出的承诺，落在一个重复的日期上，而且没法窝在沙发上半心半意地参加。

> People are not buying a tile game. They are buying a reason that friendship has to happen on Thursday.

人们买的不是一副牌。他们买的是一个「友情必须发生在周四」的理由。

> The second is the card.

第二是牌型卡。

> Because the League reissues it every year, the puzzle renews on a schedule, and a player of fifteen years and a player of fifteen weeks both spend part of each spring feeling lost.

因为 League 每年都会重发一次，这个谜题就按时更新，于是打了十五年的人和打了十五周的人，每年春天都有一段时间同样感到迷失。

> Few hobbies flatten their own hierarchy like that.

很少有爱好能这样把自己的等级差抹平。

> The third is that the tiles became a design language.

第三是牌本身变成了一种设计语言。

> One member wrote that a single photograph of an upcoming set had her checking a maker's feed several times a day for months and setting three alarms so she would not miss the preorder.

一位群友写道，仅仅一张即将发售的牌的照片，就让她连着好几个月每天刷好几次某个厂牌的动态，还定了三个闹钟，生怕错过预售。

> Five hundred people reacted.

五百个人点了反应。

> When a group posts a link to a well-priced set, the thread fills with "sold out" updates inside a day.

当群里发出一个价格不错的牌的链接，帖子里一天之内就会被「已售罄」的更新刷满。

> That is a design market, not a game hobby.

这是一个设计市场，不是一个游戏爱好。

### H2：The part of the boom worth ignoring
> 这波热潮里可以忽略的那部分

> One post put it plainly.

有一个帖子说得很直白。

> A long-time player wrote that she was shocked by the monetisation around the game: tile sets priced like furniture, membership parlours, paid everything.

一位老玩家写道，她被这个游戏周围的过度商业化震到了：贵得像家具一样的牌、会员制的麻将馆、什么都要收费。

> It drew more than eleven hundred reactions and one hundred and seventy comments, and the line people quoted back was the last one, where she mentioned that her own group is forty-five people who meet at a public library, for free, as often as they can.

那条帖子收到了一千一百多个反应和一百七十条评论，而人们反复引用的是最后那一句：她自己的那个局有四十五个人，在一家公共图书馆免费聚会，只要有机会就打。

> Both halves are true at once.

这两半同时都是真的。

> The expensive tier is entirely optional, and nothing about the game is gated behind it.

贵的那一层完全是可选的，这个游戏没有任何一部分被锁在它后面。

> The most common way to start is still a folding table, a borrowed set and somebody's aunt explaining the Charleston twice.

最常见的入门方式，仍然是一张折叠桌、一副借来的牌，还有某个人的姨妈把 Charleston 讲上两遍。

### H2：Why people stay after the first month
> 为什么第一个月之后人还在

> Popularity gets people to sit down once.

热度只能让人坐下来一次。

> What keeps them is that the game is hard in an unusually social way.

留住他们的，是这个游戏难得很特别，难在社交层面。

> The rules fit on a page. The card is the hard part, and it stays hard.

规则一页纸就写得下。难的是牌型卡，而且它一直难。

> You can watch people meeting that wall.

你能看到人们撞上那堵墙。

> A first-year player posted her own colour-coding system for this year's card, green for single-suit hands, a sticker for the odd-number section, because the printed grid refused to resolve for her.

一位打了不到一年的玩家发出了她自己给今年这张卡做的颜色标记系统：绿色代表只需要一门花色的牌型，单数那一栏贴一个贴纸，因为那张印出来的网格在她眼里就是化不开。

> It drew over a thousand reactions and two hundred and fifty comments, most asking for a photograph of the back.

那条帖子收到一千多个反应和两百五十条评论，多数人是在要一张背面的照片。

> A game people quit does not generate homework like that.

一个人们会放弃的游戏，不会催生出这样的作业。

> If you are months in and wondering why you never win, the answer is usually card fluency rather than luck, which we cover in our notes on **reading the card and when to commit**.

如果你已经打了几个月还在纳闷为什么总也赢不了，答案通常是对牌型卡的熟练度而不是运气，我们在**读牌型卡与何时定牌**那篇笔记里写了这个。

### H2：What you actually need to sit down
> 真正需要什么才能坐下来

> Three things, in this order.

三样东西，按这个顺序。

> The current card, which comes from the League rather than from any set maker.

当年的牌型卡，它来自 League，不来自任何一家做牌的。

> Everyone at your table plays from it, and it is reissued annually, so borrow a look at somebody's first.

你桌上每个人都照着它打，而且它每年重发一次，所以先借别人的看一眼。

> Three other people, the genuinely hard input.

另外三个人，这是真正难搞的那一项。

> And a set, eventually.

以及一副牌，最终。

> Not on day one.

不是第一天。

> This is the advice that gets skipped in a boom: you do not need tiles of your own to start.

这是热潮里最容易被跳过的一条建议：**你不需要自己有牌才能开始。**

> Classes supply sets and groups keep spares.

课上会提供牌，局里也会留备用的。

> Wait until you know the game has stuck, usually between the second and sixth session.

等到你确定这个游戏在你身上留住了再说，对多数人来说是第二次到第六次之间。

> If you have never seen a hand played through, our **beginner's guide to American mahjong** covers the shape of a turn.

如果你从没完整看过一手牌是怎么打完的，我们的**美式麻将新手指南**讲了一个回合的大致样子。

### H2：Where the new tables are
> 新的牌桌在哪里

> Almost nobody finds this game through a search.

几乎没有人是通过搜索找到这个游戏的。

> They find it because someone in their life posted a photograph.

他们找到它，是因为生活里的某个人发了一张照片。

> One member described twenty-five years of playing against a computer with nobody to teach her, then a coworker's photo from a beginner class.

一位群友描述过：二十五年里她一直在跟电脑打，没有人教她，然后她看到一位同事在入门课上拍的照片。

> Now her Mondays have a name.

现在她的周一有了名字。

> Check the parks and recreation catalogue, the library calendar and any open play session near you, because everyone in that room has already shown up for mahjong once.

去查一下当地的公园与康乐活动手册、图书馆的活动日历，以及你附近任何一场开放牌局，因为那个房间里的每个人都已经为麻将出现过一次了。

> A class is the fastest route in, and **what to look for in mahjong lessons** covers how to tell a careful teacher from a rushed one.

上课是最快的入口，**麻将课该看什么**那篇写了怎么分辨一位认真的老师和一位赶场的老师。

> If you look for a month and find nothing, the answer is to **start a group yourself**, which is how a good number of these tables began.

如果你找了一个月还是什么都没找到，答案就是**自己开一个局**，这波热潮里相当一部分牌桌就是这么开始的。

> Expect attendance to wobble for a season.

要预期出勤率会晃上一整季。

> Plenty of tables **play three-handed** when somebody cancels rather than lose the evening.

很多牌桌在有人临时取消时，宁可**打三人局**，也不愿意让整个晚上作废。

### H2：Choosing a set once you know it will stick
> 等你确定它会留下来之后，怎么挑一副牌

> The risk of buying inside a boom is buying quickly.

在热潮里买东西的风险，是买得太快。

> One newcomer posted that she had splurged on a much-photographed set and that it arrived with scuffing and hairline scratches she was told were normal.

一位新人发帖说，她狠心买了一副在网上被拍烂了的牌，到货发现有磨损和发丝般的划痕，而对方告诉她这是正常的。

> Two hundred and sixteen comments argued about whether that is true.

两百一十六条评论在争论这到底算不算正常。

> What to take from such a thread is not a verdict on any maker but a habit: ask how the face is made, and ask for photographs of the actual tiles in ordinary room light rather than a styled flat lay.

从这样一个帖子里该拿走的不是对某一家厂牌的判决，而是一个习惯：**问清楚牌面是怎么做出来的，并且要一张普通室内光线下实物牌的照片，而不是摆拍的平铺图。**

> Monet's Garden was drawn with that in mind.

Monet's Garden 就是照着这个思路画的。

> It is a 160 tile American set: 108 suit tiles, 16 winds, 12 dragons, 8 flowers, 10 jokers and 6 blank spares, leaving 154 in play.

它是一副 160 张的美式牌：108 张数牌、16 张风牌、12 张三元牌、8 张花牌、10 张 joker，以及 6 张空白备用牌，实际在玩的是 154 张。

> The faces are carved into the acrylic and filled with colour rather than printed on top, so the artwork keeps its edge through years of washing the tiles.

牌面是雕刻进亚克力里再填色的，不是印在表面的，所以图案在多年的洗牌之后仍然保持清晰的边缘。

> The backs are a single coral-orange, so a wall reads as a wall.

牌背是单一的珊瑚橙色，所以一堵牌墙看上去就是一堵牌墙。

> Each tile is 0.87" wide by 1.25" high by 0.6" deep, at the roomy end of the usual band, with more on judging that in our piece on **tile size and readability**.

每张牌宽 0.87 英寸、高 1.25 英寸、厚 0.6 英寸，处于常见区间里偏宽裕的一端，关于怎么判断这一点，我们在**牌的尺寸与可读性**那篇里写得更多。

> It arrives in gift-ready packaging with a zippered pouch, an instruction booklet and four quick reference cards, one per seat, and carries a 180-day warranty.

它以适合送礼的包装寄出，附带一个拉链收纳袋、一本说明手册和四张快速参考卡（每个座位一张），并提供 180 天保修。

> The full set is on the **Monet's Garden** page.

完整的这副牌在 **Monet's Garden** 页面上。

> Two limits before you buy anything, ours included.

在你买任何东西之前，有两条限制要说清楚，包括买我们的。

> Racks, pushers and a mat are not in the box, and neither is the annual card.

牌架、推牌器和牌垫不在盒子里，那张年度牌型卡也不在。

> And a readable tile solves the smaller of the two problems at this table: it shortens the pause where you work out what a tile is, and does nothing for the pause where you work out what to do with it.

而且，一张好读的牌只解决了这张桌上两个问题里较小的那个：它缩短你判断「这是什么牌」的那次停顿，对你判断「该拿它怎么办」的那次停顿毫无作用。

> That second pause is the game.

而第二次停顿才是这个游戏本身。

### H2：FAQ

**Q1: Is mahjong really more popular, or does it just feel that way from inside a group?**
> 麻将是真的变得更火了，还是只是你待在群里所以感觉如此？

> Both, and the second matters more than people admit, because community feeds amplify whatever is already in front of you.

两者都有，而且第二种成分比人们愿意承认的更重要，因为社群的信息流会放大任何已经出现在你眼前的东西。

> What is independently visible is that beginner classes fill, that new set makers keep launching, and that the long-time players are the ones expressing surprise.

可以独立观察到的是：入门课会满、新的做牌厂牌不断出现，以及**表示惊讶的是那些老玩家**。

> That last one usually signals a real shift.

最后那一条通常意味着确实发生了变化。

**Q2: Why is mahjong so popular with younger players now?**
> 为什么麻将现在在年轻玩家里这么受欢迎？

> It answers two things at once.

它一次回答了两件事。

> It is an unplugged, in-person standing date in a period when those are hard to schedule, and it photographs well, so it travels on the platforms younger players already use.

它是一个不插电的、面对面的固定约会，而这种约会在当下很难约成；同时它很上镜，所以能在年轻玩家本来就在用的平台上传播。

> The card supplies the difficulty that keeps it from being decorative.

牌型卡提供了难度，使它不至于沦为一件装饰品。

**Q3: Do I need to buy my own set to start?**
> 我需要自己买一副牌才能开始吗？

> No.

不需要。

> Classes and established groups almost always have sets, and borrowing for a month costs nothing while teaching you what you like in a tile.

课程和成熟的牌局几乎都有牌，借用一个月不花钱，同时还能让你搞清楚自己喜欢什么样的牌。

> Buy once you have a standing table, or once you are the one hosting it, because then the set is chosen for a real room rather than a maybe.

等你有了固定的牌桌，或者等你成了主持的那个人再买，因为那时候这副牌是为一个真实的房间挑的，而不是为一个「也许」挑的。

### 收尾

> If you have been watching this from the edge of somebody's Tuesday, the entry cost is lower than it looks.

如果你一直是在某个人的周二边上看着这一切，入场的成本比看上去要低。

> A card, three people willing to be bad at something together for a month, and a table you can leave set up.

一张牌型卡，三个愿意跟你一起在一件事上笨拙一个月的人，还有一张可以一直摆着不收的桌子。

> The tiles are the last decision, not the first.

牌是最后一个决定，不是第一个。
