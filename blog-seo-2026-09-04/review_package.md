# 审阅包 · /blogs/news/american-mahjong-rules 增补版(v2)

日期:2026-09-04 · 类型:**已发布文章的增补更新**(不是新文章)· 状态:**未上线,等店主一句"上"**

## 为什么改

GSC 近 28 天:1073 展示 / 4 点击 / 均位 11.6,是全站博客展示量最大的一篇,但排在首页末尾到第二页开头。SEO 日报的两条改法(改标题、加 FAQ/HowTo 结构化数据)都不成立:标题描述早已含 Charleston 与 printable cheat sheet;FAQ/HowTo 富摘要 Google 已停。真正的杠杆是**排名**:内容深度、回答页面被匹配到却没专节的长尾问题、把描述里承诺的"printable cheat sheet"真做出来、补站内链接。

## 改了什么(只增不删,既有段落原文保留)

| # | 位置 | 改动 | 针对的查询 / 问题 |
|---|---|---|---|
| 1 | At-a-Glance Cheat Sheet 段末 | 新增一段:PDF 下载入口(US letter 三页) | "american mahjong rules pdf";描述承诺兑现 |
| 2 | The Tiles 段末 | 修一句:160 张的多出部分是 2 张备用鬼牌 + 6 张空白(原文只说"spare blanks",且有 em dash) | 事实修正 |
| 3 | 新 H2「How Many Tiles Are in American Mahjong?」 | 4 段:152 在玩的拆解与桌上速算(4 面墙 × 19 叠 × 2);盒装 160 = 152 + 2 鬼牌备用 + 6 空白;空白几张、能否当鬼牌;中日式 136–144 张无鬼牌为何不能配美式牌型卡 | "how many tiles mahjong / for american mahjong / number of tiles / how many blanks"(该页被匹配到这些词却排 75–88 位) |
| 4 | Setup 段内新 H3「Dealing, step by step」 | 掷骰破墙、每轮 4 张三轮、East 取顶排第 1 和第 3 张、14 张开局、开局前数错重发 / 开局后数错死手 | "american mahjong how to deal"(位 10)、"american mahjong dealing" |
| 5 | Scoring 段末 | 加一句内链 → /blogs/news/how-to-win-at-mahjong | 站内链接 |
| 6 | Penalties 死手条目末 | 加一句内链 → /blogs/news/mahjong-etiquette | 站内链接 |
| 7 | Rules FAQ 新增 3 条 | 鬼牌几张(8 在玩 / 盒装 10);两人能否玩(可,通常去掉 Charleston;三人更完整 → 内链 /blogs/news/3-player-mahjong);有没有 PDF(有,链接) | "2 player american mahjong"、"how many blanks in american mahjong" |
| 8 | 结尾段 | **事实修正**:删掉"ships with the current Official Standard Hands and Rules card"(产品页 Set Includes 没有这张卡),改为 160 张牌 + 说明手册 + 4 张快速参考卡 + 拉链收纳袋,并说明当年牌型卡来自 NMJL 需另购 | 与产品页一致 |
| 9 | 全部 h3 补 id;TOC 用脚本重刷(新增 how-many-tiles 入 TOC) | 锚点校验通过 |

不改:meta title、meta description、slug、封面图、发布日期(更新时显式带 `--published --publish-date 2026-08-10T10:02:24Z`,避免 datePublished 被重置)。

## 数字

- 纯正文:约 1,300 → 约 1,650 词(参考型规则页,略超新文章 1,100–1,500 口径,合理)
- 新增内链 3 条(how-to-win / etiquette / 3-player,均为已发布文章)
- 既有 em dash 14 处为历史遗留未动;本次新增文字零 em dash

## PDF

- 文件:`blog-seo-2026-09-04/american-mahjong-rules-cheat-sheet.pdf`(3 页,US letter,105KB)
- 已上传 Shopify Files:https://cdn.shopify.com/s/files/1/0947/6161/5657/files/american-mahjong-rules-cheat-sheet.pdf?v=1788574732
- 源稿:`american-mahjong-rules-cheat-sheet.md`(改内容重生成:`make-pdf generate --no-confidential --no-chapter-breaks --page-size letter --margins 0.6in`)

## 新增英文段落 · 中文对照(逐句)

**[1] Printable version:** download the cheat sheet as a PDF (US letter, three pages: tile count, deal, Charleston, claims, jokers and payments). Print it once and keep it under your rack.
> 可打印版本:下载速查表 PDF(US letter 三页:牌数、发牌、Charleston、叫牌、鬼牌与支付)。打印一次,压在牌架下面。

**[2]** Boxes often count 160 tiles: the extras are two spare jokers and six blanks. The arithmetic is in how many tiles are in American mahjong below.
> 盒装常见 160 张:多出的是 2 张备用鬼牌和 6 张空白牌。算法见下文"美式麻将有多少张牌"。

**[3] How Many Tiles Are in American Mahjong?**
152 tiles are in play under National Mah Jongg League rules: 108 suit tiles (Bams, Craks and Dots, 1 through 9, four of each), 16 winds, 12 dragons, 8 flowers and 8 jokers. The quick check at the table: four walls of 19 stacks, two tiles high, is 152.
> 美式麻将有多少张牌?按全美麻将联盟规则,在玩的是 152 张:108 张花色牌(条、万、筒各 1 到 9,每张 4 枚)、16 张风牌、12 张箭牌、8 张花牌、8 张鬼牌。桌上速算:四面墙,每面 19 叠、两层高,正好 152。

Boxed sets usually hold 160. Monet's Garden, for example, ships 160 tiles: the 152 above plus two extra jokers and six blank spares, so a lost or chipped tile never retires the set. Some tables play with all ten jokers. Agree before the first hand, because it changes how often jokers appear.
> 盒装套装通常是 160 张。以莫奈花园为例,出厂 160 张:上述 152 张,外加 2 张备用鬼牌和 6 张空白备用牌,丢一张或磕坏一张不至于让整套牌报废。有些牌桌会把 10 张鬼牌全部用上,第一把之前先说好,因为这会改变鬼牌出现的频率。

How many blanks? Six in a 160-tile box. They stay out of play unless you are replacing a damaged tile, and a blank cannot be used as a joker.
> 空白牌几张?160 张的盒装有 6 张。除了替换坏牌,它们不参与对局,也不能当鬼牌用。

Why an imported set will not work: Chinese and Japanese sets run 136 to 144 tiles and have no jokers, no flowers in the American sense, and no room for the card's joker-based hands. American mahjong needs an American set.
> 为什么进口套装不能用:中式和日式套装 136 到 144 张,没有鬼牌,没有美式意义上的花牌,也容不下牌型卡上依赖鬼牌的牌型。玩美式麻将需要美式套装。

**[4] Dealing, step by step**
East rolls both dice. Count that many stacks from the right-hand end of East's wall and break the wall there; the deal starts from the break. Take tiles four at a time, three rounds each, so every player holds 12. East then takes the first and third tiles from the top row of the wall, and South, West and North each take one, in that order. East holds 14 and opens by discarding. If the count is wrong before the first discard, re-deal; once play has started, a wrong count is a dead hand (see penalties).
> 发牌步骤:东家掷两颗骰子,从东家这面墙的右端数相应的叠数,在那里破墙,从破口开始发牌。每次取四张,每人三轮,人手 12 张。然后东家取墙顶排的第 1 和第 3 张,南、西、北各取 1 张,按此顺序。东家持 14 张,打出一张开局。第一张打出前发现数错就重发;开局之后数错就是死手(见罚则)。

**[5]** Reading the card for the hands you can realistically make is a separate skill: see how to win at mahjong.
> 看牌型卡判断哪些牌型实际做得成,是另一项技能:见《怎样赢麻将》。

**[6]** How to call these moments without souring the table is covered in our mahjong etiquette guide.
> 这些时刻怎么开口又不坏了桌上气氛,见我们的《麻将礼仪指南》。

**[7a] How many jokers are in American mahjong?** Eight are in play under the League rules. Boxed sets often include ten, and the two extras are spares. If your table plays with all ten, say so before the deal.
> 美式麻将有几张鬼牌?联盟规则在玩 8 张。盒装常含 10 张,多出的 2 张是备用。如果你们桌上 10 张全用,发牌前先说明。

**[7b] Can two people play American mahjong?** Yes, and it is a good way to learn the card. Two-player tables keep the deal and the hands, and usually drop the Charleston or shrink it to one across pass. You lose the tension of three opponents discarding, which is why three players keeps more of the game: see our three-player mahjong guide.
> 两个人能玩美式麻将吗?能,而且是学牌型卡的好办法。两人局保留发牌和牌型,通常省掉 Charleston 或缩成一次对家互换。少了三个对手轮流打牌的张力,所以三人局保留的味道更多:见我们的《三人麻将指南》。

**[7c] Is there a printable PDF of these rules?** Yes. The at-a-glance cheat sheet is a three-page US letter PDF covering tile count, the deal, the Charleston, claims, jokers and payments. It is the same content as the table at the top of this page, formatted to print.
> 这些规则有可打印的 PDF 吗?有。速查表是三页 US letter 的 PDF,覆盖牌数、发牌、Charleston、叫牌、鬼牌和支付。内容与本页顶部的表格相同,排成适合打印的版式。

**[8]** ...ships with 160 engraved acrylic tiles, an instruction booklet, four quick-reference cards and a zippered storage bag. The current year's card comes from the National Mah Jongg League and is the only piece not in the box.
> ……出厂含 160 张雕刻亚克力牌、一本说明手册、四张快速参考卡和一个拉链收纳袋。当年的牌型卡由全美麻将联盟发行,是盒子里唯一没有的东西。

## 上线命令(店主说"上"之后执行;已发布文章必须显式 --published 并带原发布日期)

```
python .claude/skills/seo-article/scripts/shopify_article.py update \
  --id gid://shopify/Article/618480894249 \
  --body-file blog-seo-2026-09-04/american-mahjong-rules-v2.html \
  --published --publish-date 2026-08-10T10:02:24Z
python .claude/skills/seo-article/scripts/shopify_article.py verify --id gid://shopify/Article/618480894249
```

验证按手册顺序(Admin API 读回 → 渲染浏览器看锚点与 PDF 链接;不用 curl,有全页缓存)。

## 可选的第二步(排名杠杆里的"站内链接",另行决定)

给这篇加入站内链接的候选(均为已发布文章,各加一句自然引用即可):how-to-play-american-mahjong-beginners-guide(已有)、how-to-teach-mahjong-to-beginners、mahjong-lessons、how-to-win-at-mahjong、3-player-mahjong、mahjong-etiquette。首页或集合页导流需要改主题,暂不动。
