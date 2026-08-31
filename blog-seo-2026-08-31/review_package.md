# 审阅包 2026-08-31：The History of Mahjong, Told Through Its Tiles

## 一、Shopify 草稿

| 项 | 值 |
| --- | --- |
| 文章 GID | `gid://shopify/Article/618632544553` |
| handle | `history-of-mahjong` |
| 状态 | **isPublished: False**（verify 实查确认，线上 URL 返回 404，符合预期） |
| 标题 / H1 | The History of Mahjong, Told Through Its Tiles |
| meta title | `The History of Mahjong, Told Through Its Tiles \| Averill`（56 字符，≤60，以 ` \| Averill` 结尾） |
| meta description | `The history of mahjong, read through the tiles themselves: Chinese origins, the 1920s craze, the 1937 card, and how to date a set you inherited.`（144 字符，在 120–160 区间） |
| tags | mahjong history, mahjong origins, american mahjong, vintage mahjong sets |
| 作者 | Averill Mahjong |
| 字数 | 纯正文 **1,500 词**（spec 区间 1,100–1,500 的上限）；create 脚本口径 1,630 |
| 锚点导航 | 8 links / 11 ids，脚本校验通过 |
| 乱码自检 | U+FFFD = 0 |
| 封面图 | 无（等用户配） |

## 二、关键词（Google Ads Keyword Planner 实时数据，美国 geo 2840，2026-08-31 实拉，**未降级**）

**主关键词：`history of mahjong` 1,300/月，竞争 LOW，competitionIndex 19**
（`history mahjong` / `history of mah jongg` / `history of mahjong game` 四项指标逐位相同，按同桶规则算一个词）

次关键词（全部 LOW）：

| 词 | 月量 | index |
| --- | --- | --- |
| mahjong origin | **1,900** | **8** |
| when was mahjong invented | 590 | 6 |
| who invented mahjong | 320 | 6 |
| mahjong game history | 140 | 13 |
| history of american mahjong | 140 | 20 |
| mahjong game origin | 110 | 7 |
| mahjong origin country | 90 | 4 |
| american mahjong history | 70 | 17 |
| origin of mahjong game | 70 | 25 |
| mahjong country of origin | 50 | 0 |
| mahjong name meaning / mahjong jewish history / how did mahjong come to america / mahjong facts / why is it called mahjong / mahjong history wikipedia / mahjong originated from where | 10–30 各 | 0–14 |

**去重后簇容量约 4,900/月，竞争指数全簇 0–25**，是台账开始以来「量级 × 低竞争」组合最好的几次之一。

**为什么主词不取量更大的 `mahjong origin` 1,900**：该词作标题与 slug 都不自然（英文里没人把文章叫 "Mahjong Origin"），而 `history of mahjong` 是这个意图的自然头词，且两词的搜索结果高度重合。`mahjong origin` 已作次关键词写进正文首节、FAQ 第一条与 meta description（`Chinese origins`）。

**意图污染检查（按 08-25 的判读标准）：干净。** `mahjong solitaire history`、`national mah jongg league history`、`mahjong 1920s craze` 三个污染探针**全部 UNSPECIFIED 无数据**（最强的干净信号）。没有 app / free / download 兄弟词。

**但量级仍要打折，而且这次是另一种折扣。** 不是意图污染，是**转化距离**：查历史的人里有学生、写作业的、看完就走的。这批人不会当天下单。可承接的「手里有一副老牌、想弄明白它、进而可能买一副能打的」这一层，**保守估计 400–900/月，这是判断不是测量**。做它的三个理由：① 竞争指数 8–25，新站真有机会排上；② 站上完全零历史语料，是最后一块干净的大空白；③ 社群证据是历次里最直接的一类（见下）。

**本轮同时否决**：`mahjong tile racks` 590 / `mahjong racks and pushers` 2,400 / `mahjong mah jongg racks` 4,400 等整个 racks 簇，**全簇 HIGH index 100**，交易型意图，且配件篇已覆盖。`mahjong tradition` 1,300 MEDIUM 35（出价 0.32–2.34 明显偏商业，意图不明）不采用。`mahjong for arthritis` / `mahjong open play` / `left handed mahjong` / `how to host a mahjong tournament` 四个种子**一次拉词全部无数据返回**，这三个处境没有可测量的搜索需求。

## 三、蚕食检查

脚本：`audit_blog.py --cannibalize` 对 `history of mahjong` / `mahjong origin` / `who invented mahjong` **三次全部报 clean（exit 0）**。

**并按 08-20 升级后的规则做了正文实证**（脚本 clean 也可能是假阴性）：18 篇正文（含 5 篇草稿）落盘，正则搜 21 个历史意图同义词（histor / origin / invent / 1920s / 1930s / 1937 / dynasty / China / Chinese / Babcock / ancient / heritage / legend / Confucius / craze / century / tradition / imported / immigrant / Jewish / Shanghai / Ningbo）。

**全站命中 20 处，19 处是假朋友**：

- `tradition` / `traditional`（12 处，跨 6 篇）在本站全部指**桌规、牌垫材质、待客仪式**（"house traditions vary"、"felt is more traditional"、"become a tradition"），没有一处是历史。
- `1920s` 唯一一处在清洁篇，说的是 **bakelite / catalin 材料年代**，不是游戏史。
- `original`（2 处）是「原来的颜色」「原价」。
- `invented` 唯一一处在礼仪篇：`no rules invented as you go`。
- `century` 唯一一处是教学篇结尾的修辞。
- **`Babcock` / `Confucius` / `dynasty` / `craze` / `Shanghai` / `Ningbo` / `1937` / `Jewish` / `heritage` / `immigrant` 全部零命中。**

唯一一处实质邻近：新手指南有一个从句 `American mahjong grew out of the classic Chinese game in the 1920s`。**按 08-26 定的「一个从句不构成覆盖」判据，不构成重叠**，且那篇的意图是「怎么玩」，不回答「从哪来、谁发明的、怎么到美国的」。判定为**真 clean，可以写**。

## 四、社群证据（MJTI 3,642 帖，历史/继承/老牌 检索命中 218 条，精确检索 86 条，取高互动）

**这是直接证据不是邻近证据**：帖子里的人**逐字在问本文标题要回答的问题**。

1. **1,235 互动 / 177 评论** —— [帖子](https://www.facebook.com/groups/MahJonggThatsIt/permalink/25717773937840776/) 「这已经变成我掉进过的最疯的一次家族史兔子洞了……查下来这副牌属于我的高祖父（1899–1978），住在底特律」，还提到当年卖牌的百货公司。**开篇场景与 1920 年代那节的来源**。成文里**没有写出姓名与店名**，抽象成「一位群友」「大百货公司」。
2. **437 互动 / 227 评论** —— [帖子](https://www.facebook.com/groups/MahJonggThatsIt/permalink/27077406041877552/) 「在遗产拍卖买的，**有人知道这是哪一年的吗？花牌很多，一张 joker 都没有**，红色那几张现在算 joker 吗？」**逐字就是本文的搜索意图**，也是 joker 那一节的核心证据。
3. **269 互动 / 32 评论** —— [帖子](https://www.facebook.com/groups/MahJonggThatsIt/permalink/27027628153522008/) 「我妈给了我这副 1920 年代的美产牌……**没有 joker，我就拿我以为的空白牌做了 joker**」，评论里有人指出那些不是空白牌。
4. **184 互动 / 72 评论** —— [帖子](https://www.facebook.com/groups/MahJonggThatsIt/permalink/26433957099555786/) 一副中世纪老牌「**20 张花牌、6 张 joker、2 张空白**，配的说明册是 1964/65 版」。**成文「数字是移动靶」与「纸最能定年」两条结论的来源。**
5. **166 互动 / 68 评论** —— [帖子](https://www.facebook.com/groups/MahJonggThatsIt/permalink/26186165894334909/) 「我对麻将一无所知，只想弄明白我继承到的是什么。**有 152 张牌、2 颗骰子、5 个 rack**，看着像 bakelite」——「先数牌」那一节的来源。
6. **110 互动 / 49 评论** —— [帖子](https://www.facebook.com/groups/MahJonggThatsIt/permalink/27247233201561501/) 「我奶奶的牌，bakelite 仿象牙，**racks 上还带烟灰缸**」——材料定年那一节的细节。
7. **98 互动 / 67 评论** —— [帖子](https://www.facebook.com/groups/MahJonggThatsIt/permalink/27422391597378993/) 一副 1950 年代 bakelite 牌，「**没看到 joker**，有 28 张看着像花牌的，其中 4 张上面有个人像……**群里的历史学家们，我理解得对吗？**」

**为什么选这个方向**：候选池实质已空（唯一剩下的 `gentle tournament 专题` 未拉且大概率无量），按台账方法论走「第四条路径」——**从社群里「人手里那件实物的来历」找词**。这批帖子（218 条）此前从没被当成选题来源，因为它们分散在 vintage / storage / design 各个话题下，不属于 MJTI 的任何一个 `primary_topic`。而它们指向的搜索词簇（4,900/月、index 0–25）是站上最后一块完全没有语料的大空白。

## 五、内链与产品连接

内链 5 篇，**全部实查 `PUB=True`**（5 篇草稿一条没链，避免 404）：

| 目标 | 放在哪一节 | 备注 |
| --- | --- | --- |
| `mahjong-tile-size-readability` | 「牌面从来没有被统一过」 | — |
| `how-to-play-american-mahjong-beginners-guide` | 1937 年牌型卡那节 | — |
| `american-mahjong-rules` | 同上 | 该篇入站链接偏少 |
| `mahjong-lessons` | 「没有任何一副牌能解决牌型卡」 | **`--full` 报入站仅 1 的三篇之一** |
| `mahjong-etiquette` | 「带老牌去别人家先问一句」 | **`--full` 报入站仅 1 的三篇之一** |

产品链接 1 个：`/products/monets-garden`。

**产品连接是结构性的**：全文讲的是「老牌为什么对不上现在的牌型卡」，落点自然是**牌数配置**——8 张花、10 张 joker、6 张空白备用，正好是老牌缺的那三样。产品事实 2026-08-31 按线上产品页实查：160 张（108+16+12+8 花+10 joker+6 空白，在玩 154）、0.87"W × 1.25"H × 0.6"D、carved acrylic（产品页仍是 `engraved` 与 `printed with precision` 自相矛盾，按 spec 统一用 `carved`）、珊瑚橙牌背、拉链袋 + 说明手册 + 4 张快速参考卡、gift-ready、180 天保修。

**主动写了三条对自己不利的话**：① 「牌还在、看得清，就打它，换新牌不会让你打得更好」；② 「没有任何一副牌能解决牌型卡，那才是真正花时间的部分」，并把读者导向找课篇；③ 明写盒里**没有** racks / pushers / 牌垫，**也没有那张每年更新的牌型卡**（来自 League，不来自任何做牌的人）。

## 六、红线处理

- **事实**：全文没有给单一发明人或单一年份，写明「没有单一发明者、没有创立日期」。孔子说 / 三千年说**明写是 1920 年代的销售话术**。Joker 加入的具体年份**刻意不写**（只说「几十年后才进入美式打法」），避免写死一个有争议的年份。牌型卡逐年更新的事实写了两处。
- **赌博红线**：三花色的钱币来历是**设计史陈述**（铜钱、串钱、万），全文无 bet / wager / stakes / odds / 赌注措辞；社群证据里那条带 "betting wheel" 的帖子**刻意未采用**。
- **竞品与他人身份**：证据里出现的所有人名（高祖父姓名、捐牌者缩写）、店名（当年的百货公司）、厂牌（一家美国游戏公司、一家中世纪美国厂）**全部抽象**，无一写入正文。National Mah Jongg League 作为历史事实与牌型卡来源提及，**未暗示任何授权或关联**。
- **Monet**：仅作设计灵感，无美术馆 / 遗产管理方 / 授权暗示。
- **文化表述**：中国起源写得明确且尊重，美式变体写成「另一个版本」而不是「改良版」。

## 七、质量闸门

`shopify_article.py create` 内建闸门**一次通过，未用 `--force`**：

- 标题无被禁短语 ✅
- 无 AI 腔命中 ✅（另人工检查：全文 **em dash 0 个**、en dash 0 个）
- 主关键词在 H1 / 前 100 词 / meta title / meta desc / slug ✅
- 产品链接 1 + 站内文章链接 5 ✅
- 锚点 8 links / 11 ids 全部可解析 ✅
- FAQ 3 条 ✅
- U+FFFD = 0 ✅
- 纯正文 1,500 词，在区间内 ✅

## 八、站点问题（`--full` 本轮报 22 条，5 条 HIGH，与上轮持平，**按硬规则只报告未擅自修改**）

- **4 条缺封面图 HIGH（已发布文章）**：`american-mahjong-rules`（连续第八轮）、`3-player-mahjong`、`mahjong-etiquette`、`mahjong-lessons`（后三篇 08-29 发布时未配图，缺图在草稿上是 MED，一发布就升 HIGH：Article 结构化数据缺 `image`，og:image 退回站点 logo）。**这四篇补图是本轮最值得做的一件事，比新增文章收益高。**
- **1 条坏锚点 HIGH**：`american-mahjong-rules` 的 `cheat-sheet` 指向不存在的 id（TOC 16 条 vs 12 个 id），读者点了不跳。连续第三轮报告。
- 5 条缺图 MED 全部是待发布草稿（正常）、1 条 thin-content MED（`how-to-host-a-cozy-mahjong-night-at-home` 604 词）、3 条 internal-links MED（`3-player-mahjong` / `mahjong-lessons` / `mahjong-etiquette` 入站各 1，**本篇已各补 1，但要等本篇发布后才会计入**）。
- LOW：1 条封面图缺 alt、2 篇 meta title 超 60、1 篇 meta desc 166、3 篇无 tags、1 条作者名三种并存。
- `--full` 的 technical 实时检查因沙箱代理返回 403 未能执行（非站点问题）。

## 九、用户待办

1. **配封面图**（本篇主题是老牌与传承，画面上最合适的是整副牌铺开或牌背特写）。**避开这几个已知配色错误的素材**：`premium-gift-box.jpg`、`branded-carrying-bag.jpg`、`instruction-manual.jpg`、`four-rules-reference-cards.jpg`、`full-tile-set-monets-garden.jpg`。
2. **审阅正文**（下方有完整中文对照翻译）。
3. **手动发布**。
4. 顺手做的话：给上面 4 篇已发布文章补封面图（4 条 HIGH 一次清掉），修 `american-mahjong-rules` 的 `cheat-sheet` 锚点。
5. **发布 `how-to-clean-mahjong-tiles` 草稿后**，建议在本篇「继承的牌怎么定年」一节补一条指向它的内链——本轮因为它还是草稿（会 404）没有链，但它是本篇最自然的下一步。

---

# 完整中文对照翻译（逐句）

> 说明：左为英文原文段落，右为中文。标题为 H2 / H3。

**开篇**

> A set turns up at an estate sale in a hinged wooden case with a brass catch. The tiles are heavier than expected and slightly yellowed. There are more flower tiles than anyone can account for, and no jokers at all. The buyer photographs the lot, posts the pictures, and asks the question every inherited set eventually produces: does anyone know when this is from?

一副牌出现在一场遗产拍卖上，装在一个带黄铜搭扣的木质翻盖盒里。牌比想象中沉，微微泛黄。花牌多得没人说得清，而 joker 一张都没有。买家把整副牌拍下来，把照片发出去，问出了每一副继承来的牌最终都会引出的那个问题：有人知道这是哪一年的吗？

> That question is where the history of mahjong stops being an encyclopedia entry and becomes an object in your hands. Nearly every turn in the story left a mark on the tiles. The suits, the counts, the material, the missing jokers: each one is a date stamp if you can read it. What follows is the short version, told through pieces you can pick up.

正是在这个问题上，麻将的历史不再是一个百科词条，而变成了你手里的一件东西。这段历史几乎每一次转折都在牌上留下了痕迹。花色、数量、材质、缺失的 joker：只要你会读，每一项都是一个年代印记。下面是这段历史的简版，用你能拿起来的东西讲。

**H2：Where mahjong came from（麻将从哪里来）**

> Most accounts place the beginning in China in the second half of the 1800s, in the trading cities around Shanghai and Ningbo, with regional versions spreading quickly after. There is no single inventor and no founding date, which is the honest answer to who invented mahjong. What the game descends from is a family of Chinese playing cards, and that inheritance is still sitting on your rack.

多数说法把起点放在十九世纪后半叶的中国，在上海与宁波一带的通商城市，此后各地版本迅速扩散。**没有单一的发明人，也没有一个创立日期**，这就是「谁发明了麻将」这个问题的诚实答案。这个游戏承袭自一族中国纸牌，而那份继承至今就摆在你的牌架上。

> The three suits are denominations, not pictures. Dots were coins. Bams were strings of coins threaded together. Craks carry the character for ten thousand. Once you know the suits are money, the winds and dragons stop looking decorative and start looking structural.

三门花色是面额，不是图案。筒是铜钱。条是串起来的钱串。万带的是「万」这个字。一旦你知道花色其实是钱，风牌与箭牌就不再像装饰，而开始像结构。

> One story you can safely put down: the claim that Confucius invented the game, or that it is three thousand years old. That was sales copy written in the 1920s for buyers in the West. The tiles are old enough without it.

有一个说法你可以放心放下：孔子发明麻将，或者麻将有三千年历史。**那是 1920 年代为西方买家写的销售话术。** 牌本身已经够老了，不需要这个。

> Nothing about the faces was ever standardized by a governing body, then or now. That is why two sets on the same table can be so different to read, and why [tile size and face clarity](https://www.averillmahjong.com/blogs/news/mahjong-tile-size-readability) still come up at every table.

牌面从来没有被任何机构统一过，当年没有，现在也没有。这就是为什么同一张桌上的两副牌读起来会差那么多，也是为什么[牌的尺寸与牌面清晰度](https://www.averillmahjong.com/blogs/news/mahjong-tile-size-readability)在每一张牌桌上都还会被提起。

**H2：The 1920s, when the game crossed an ocean（1920 年代，游戏渡过一片海洋）**

> In 1920 an American businessman working in China, Joseph Babcock, published a short English rulebook, trimmed the game down for beginners, and registered the spelling Mah-Jongg. Sets followed the book. By 1923 they were arriving by the shipload, selling through the big department stores, and being copied by American manufacturers who could not import them fast enough.

1920 年，一位在中国工作的美国商人 Joseph Babcock 出版了一本简短的英文规则手册，把游戏为初学者做了删减，并注册了 Mah-Jongg 这个拼法。牌随着书一起来了。到 1923 年，牌已经是整船整船地到岸，在大百货公司里出售，还被那些进口速度跟不上的美国厂商仿造。

> You can still meet that year in a living room. One group member posted photographs of a case she had been given and then went digging, and a question about tiles turned into a family history: the set had belonged to her great great grandfather, born in 1899, who lived in Detroit and bought it during the boom. Her post drew 1,235 reactions and 177 comments, most from people with a similar box in a closet. A 1920s set is not a rare artifact. It is a household object from the year the whole country tried the same game at once.

那一年至今还能在某个客厅里遇上。一位群友发了她收到的那只盒子的照片，然后开始往下查，一个关于牌的问题变成了一段家族史：这副牌属于她 1899 年出生的高祖父，住在底特律，就是在那场热潮里买的。她那条帖子得到 1,235 个互动、177 条评论，大多数来自柜子里也有一只类似盒子的人。**1920 年代的牌不是稀有文物，它是那一年全国人一起玩同一个游戏时留下的家常物件。**

**H2：Why American play grew a card of its own（美式打法为什么长出了自己的牌型卡）**

> The craze cooled by the middle of the decade, but the tables did not disappear. Groups kept meeting in homes, adjusting the rules among themselves until the game needed a referee.

热潮在那个十年的中段冷下来，但牌桌没有消失。牌局继续在各家客厅里聚，规则也在各局内部不断被调整，直到这个游戏需要一个裁判。

> In 1937 a group of players in New York founded the National Mah Jongg League and printed one standard list of hands. A new card has come out every year since. That single decision is why American play feels the way it does: everyone at the table is building toward the same published hands, and those hands change annually, so experienced players spend each spring learning a new document. Our [beginner's guide to American mahjong](https://www.averillmahjong.com/blogs/news/how-to-play-american-mahjong-beginners-guide) walks through a first game, and the [rules reference](https://www.averillmahjong.com/blogs/news/american-mahjong-rules) covers the mechanics in order.

1937 年，一群纽约的玩家创立了 National Mah Jongg League，印出了一份统一的牌型清单。此后每年都会出一张新卡。**正是这一个决定，让美式打法有了今天的手感**：桌上每个人都在朝同一份公开的牌型努力，而那些牌型每年都变，所以老玩家每年春天都要重新学一份文件。我们的[美式麻将新手指南](https://www.averillmahjong.com/blogs/news/how-to-play-american-mahjong-beginners-guide)带你走一遍第一局，[规则参考](https://www.averillmahjong.com/blogs/news/american-mahjong-rules)则按顺序讲清机制。

**H2：Jokers are an American addition（Joker 是美国后加的）**

> The game those first sets were built for had no jokers. They came into American play decades later, and nobody went back to retrofit the boxes already in people's homes.

最早那批牌所服务的那个游戏里没有 joker。Joker 是几十年后才进入美式打法的，而没有人回过头去给已经在别人家里的盒子补装。

> This is the most common source of confusion in inherited sets. One buyer described her estate sale find as having lots of flowers and no jokers, and asked whether the red tiles were the jokers, in a post that drew 437 reactions and 227 comments. Another was given her mother's American made set from the 1920s, made jokers out of what she took to be blanks, and learned from the group that those blanks were not blanks. A third opened a bakelite set from the 1950s, counted 28 tiles that looked like flowers, noticed four carried a small figure, and asked the historians in the group whether she was reading it right.

这是继承来的牌里最常见的困惑来源。一位买家形容她在遗产拍卖上淘到的那副「花牌很多、没有 joker」，并问红色那几张是不是 joker，那条帖子得到 437 个互动、227 条评论。另一位拿到了母亲那副 1920 年代的美产牌，用她以为的空白牌做了 joker，后来才从群里得知那些空白牌并不是空白牌。第三位打开一副 1950 年代的 bakelite 牌，数出 28 张看着像花牌的，注意到其中四张上有个小人像，于是问群里的历史爱好者们她理解得对不对。

> None of those sets are incomplete. They were complete for a different version of the game.

**这几副牌都不是不完整。它们对另一个版本的游戏而言是完整的。**

**H2：How to read the age of a set you inherited（怎么读出你继承那副牌的年纪）**

> Start by counting. One member who had never played wrote that she was trying to work out what she had inherited, and reported 152 tiles, two dice, and five racks. That count alone narrows the era, because tile counts moved with the rules.

先数。一位从没打过牌的群友写道，她只是想弄明白自己继承到的是什么，报出来的是 152 张牌、2 颗骰子、5 个牌架。**光这个数字就能缩小年代范围**，因为牌数是随规则一起移动的。

> Then count the extras. Four flowers plus four seasons is a common older arrangement. A mid century set that surfaced in the group came with 20 flowers, six jokers, and two blanks, alongside a how to play booklet from 1964. Counts were a moving target for fifty years.

再数额外的那些。四张花加四张季是老牌常见的配置。群里出现过的一副中世纪老牌带着 20 张花、6 张 joker、2 张空白，还配着一本 1964 年的玩法说明册。**在长达五十年的时间里，这些数字都是移动靶。**

> Material gives you a rough decade. Bone and bamboo came first, in two pieces, which is why the oldest tiles show a seam. Early plastics such as bakelite and catalin carried the middle of the century, and one member's grandmother's set is bakelite tinted to imitate ivory, with ashtrays built into the racks. Acrylic and melamine came after.

材质能给你一个大概的十年区间。最早是骨面加竹背两片拼合，这就是为什么最老的牌能看到一条接缝。bakelite 与 catalin 这类早期塑料撑起了本世纪中段，一位群友的奶奶那副就是染成仿象牙色的 bakelite，牌架上还嵌着烟灰缸。亚克力与三聚氰胺是之后的事。

> Paper dates a set more precisely than anything else in the box: a booklet, a receipt, a store label inside the lid. One caution worth keeping is that age is not value. Most sets from the craze were mass produced, and the ones that matter are the ones with a name written inside the case.

**盒子里最能精确定年的是纸**：一本说明册、一张收据、盒盖内侧的商店标签。有一条提醒值得记住：**老不等于值钱**。那场热潮里的牌大多是量产的，真正要紧的是盒子里写着名字的那些。

**H2：What it takes to play an old set today（今天要用一副老牌打牌，需要什么）**

> An inherited set can come back to the table, and the group's own advice is consistent: play it if you can. The current card asks for eight flowers, jokers, and enough spare tolerance that losing one tile does not end the set's working life. Groups improvise with sticker jokers all the time, and nobody at a friendly table minds.

继承来的牌是可以回到牌桌上的，而且群里的建议相当一致：**能打就打它**。现在的牌型卡要求八张花、要有 joker，还要有足够的冗余，好让丢一张牌不至于终结这副牌的使用寿命。牌局里用贴纸做 joker 是常事，友谊局上没人会介意。

> Two honest limits. If the set has its tiles and you can read them, nothing about a newer set will make you play better. And no set solves the card, which is the part that takes real time. If reading a hand is what stands between you and a first game, a [class or a patient teacher](https://www.averillmahjong.com/blogs/news/mahjong-lessons) will do more than a purchase.

两条老实话。**第一，如果这副牌牌还齐、你也看得清，那么换一副新牌不会让你打得更好。第二，没有任何一副牌能解决牌型卡，而那才是真正花时间的部分。** 如果挡在你和第一局之间的是「读不懂一副牌型」，那么[一堂课或一位有耐心的老师](https://www.averillmahjong.com/blogs/news/mahjong-lessons)比买东西管用。

> A modern set helps when you want one built for the game as it is played now. [Monet's Garden](https://www.averillmahjong.com/products/monets-garden) was drawn for the current card: 160 tiles, 154 in play, with eight flowers, ten jokers, and six blank spares in the box, because tiles go missing over a decade of Tuesdays. Each tile measures 0.87 inches wide, 1.25 high, and 0.6 deep, with carved acrylic faces where the color sits down in the cut rather than on the surface, and coral orange backs. It ships gift ready in a zippered pouch with an instruction booklet and four quick reference cards, with a 180 day warranty. Not in the box: racks, pushers, a mat, and the annual card, which comes from the League rather than from any set maker.

新牌的用处在于：当你想要一副为「现在这样打」而做的牌。[Monet's Garden](https://www.averillmahjong.com/products/monets-garden) 就是照着现行牌型卡画的：160 张牌，其中 154 张在玩，盒里有八张花、十张 joker、六张空白备用，因为十年的周二打下来，牌是会丢的。每张牌 0.87 英寸宽、1.25 高、0.6 深，牌面是雕刻亚克力，颜色沉在刻痕里而不是浮在表面，牌背是珊瑚橙色。到货是可直接送礼的状态，含拉链收纳袋、说明手册、四张快速参考卡，附 180 天保修。**盒里没有的**：牌架、pusher、牌垫，以及那张每年更新的牌型卡——它来自 League，而不来自任何一家做牌的。

**H2：The revival you are already part of（你已经身在其中的这轮复兴）**

> The past decade has been the game's third act in America. New designers, younger tables, colors nobody would have printed in 1955, and closets giving up cases unopened since a grandmother stopped playing. Both at once, which is why one evening can hold a bakelite set and a modern one.

过去十年是这个游戏在美国的第三幕。新的设计者、更年轻的牌桌、1955 年没人会印的配色，以及一只只自从某位奶奶不再打牌后就没打开过、如今被交出来的盒子。两件事同时在发生，所以同一个晚上可以同时容下一副 bakelite 老牌和一副新牌。

> If you bring an antique set to somebody else's table, ask the host first. Some groups love it and some would rather everyone read the same faces, which is one of the small courtesies covered in our piece on [mahjong etiquette](https://www.averillmahjong.com/blogs/news/mahjong-etiquette).

如果你要把一副老牌带去别人家的牌桌，**先问一句主人**。有的局很喜欢，有的局更希望所有人读同一种牌面，这正是我们那篇[麻将礼仪](https://www.averillmahjong.com/blogs/news/mahjong-etiquette)里写到的小分寸之一。

**H2：FAQ**

**H3：Where did mahjong originate?（麻将起源于哪里？）**

> In China, most commonly traced to the second half of the 1800s in the region around Shanghai and Ningbo. It grew out of Chinese money suited playing cards, which is why the three suits are coins, strings of coins, and ten thousands rather than images.

在中国，最常见的追溯是十九世纪后半叶的上海与宁波一带。它由中国的钱纹纸牌演变而来，这就是为什么三门花色是铜钱、钱串和「万」，而不是图像。

**H3：When was mahjong invented, and by whom?（麻将是什么时候、由谁发明的？）**

> There is no single date or inventor. The game took shape gradually in the 1800s from earlier card games. The name most often attached to it in the United States belongs to the American who published the first widely sold English rulebook in 1920, which is a different thing from inventing it.

没有单一的日期，也没有单一的发明人。这个游戏是在 1800 年代从更早的纸牌游戏里逐渐成形的。在美国最常与它绑在一起的那个名字，属于 1920 年出版第一本畅销英文规则手册的那位美国人，**而那和「发明」是两回事**。

**H3：Can I play American mahjong with a set I inherited?（我能用继承来的牌打美式麻将吗？）**

> Often yes. Count the tiles, then check for eight flowers and for jokers. Sets from before mid century usually have no jokers, and players routinely sticker spare tiles to fill the gap. If the faces are readable and the count works, the set is playable.

多数情况下可以。先数牌，再看有没有八张花、有没有 joker。本世纪中叶以前的牌通常没有 joker，玩家们的常规做法是在多余的牌上贴贴纸补上。**只要牌面读得清、数目对得上，这副牌就能打。**

**结尾**

> Every set carries a version of this story. Some hold a receipt from 1923, some a booklet from 1964, some were made last year for a card that will be replaced next spring. They all end in the same place: four people, one table, and an afternoon that runs longer than anyone planned.

每一副牌都带着这个故事的一个版本。有的里面压着一张 1923 年的收据，有的夹着一本 1964 年的说明册，有的是去年才做的、为了一张明年春天就会被换掉的牌型卡。**它们最后都落在同一个地方：四个人、一张桌子，和一个比谁预想的都要长的下午。**
