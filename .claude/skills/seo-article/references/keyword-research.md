# Keyword Research

## 数据源优先级

### 1. Google Ads Keyword Planner（首选）

通过 NotFair MCP 的 `getKeywordIdeas`。真实美国搜索量 + 竞争指数 + 出价区间，**比 Ahrefs actor 更权威**，且不消耗 Apify 额度。

```
ToolSearch: select:mcp__2e8f9e05-b07f-4c54-a352-28d40aa7f4b8__getKeywordIdeas
调用：keywords=[最多20个种子], geoTargetIds=["2840"]（美国）, pageSize=50
```

返回 `avgMonthlySearches` / `competition` / `competitionIndex` / `lowTopOfPageBid` / `highTopOfPageBid`。

**注意**：返回的 `averageCpc` 常为 0，用 `lowTopOfPageBid`/`highTopOfPageBid` 代替。`competitionIndex` 是**广告竞争度**，不等于 SEO 难度（Ahrefs KD），两者不可混用比较。

新站选题优先看 `competitionIndex` 低的：index ≤30 属于容易拿的。

### 2. 复用历史关键词库

之前 Ahrefs actor 跑出的真实 KD 数据：
- （本地历史关键词库，云端不可用）`Documents\Codex6-07-05\wo-y\outputsverill-blog-seo-2026-07-09-live\seo_keyword_bank.csv`
- （本地历史关键词库，云端不可用）`Documents\Codex6-07-17
ew-chat\outputsverill-blog-seo-2026-07-17-live\seo_keyword_bank.csv`

已知锚点：`mahjong set` 37,000/月 KD 64；`mahjong tiles` 34,000/月 KD 47；`american mahjong set` 700/月 KD 54–66；`mahjong gifts` 1,200/月；`luxury mahjong set` 600/月 KD 58。

### 3. Apify（当前不可用）

`averill-blog-seo-operator/scripts/run_weekly.py` 会调 `apify/facebook-groups-scraper` + `burbn/ahrefs-keyword-explorer`。
**2026-08-07 状态：额度耗尽**，报 `platform-feature-disabled: Monthly usage hard limit exceeded`。Token 在 `fb-group-shopify-seo/secrets/apify_token.json`。充值后可恢复。

## 社群需求证据（不消耗任何额度）

本地已有 MJTI 数据集，样本远大于一次 7 天抓取：

`seo-state/fb-discussions.csv`（仓库内，即原来的 mjti_design_accessory_discussions.csv）
3,642 行，2025-11-01 起，含帖子链接、互动数、评论数、图片数、摘录、matched_keywords。

**读取注意**：CSV 表头是中文且带 BOM，用 `encoding='utf-8-sig'`；打印时用 `sys.stdout.reconfigure(encoding='utf-8',errors='replace')`，云端 Linux 是 UTF-8，这一条主要是历史留痕，但保留 `utf-8-sig` 读法（BOM 必须剥掉）。列位置：`cols[4]`=互动数、`cols[5]`=评论数、`cols[7]`=图片数、`cols[8]`=帖子链接、`cols[10]`=摘录。

话题分布（`primary_topic`）：

| 话题 | 帖数 | 均互动 | 均评论 |
| --- | --- | --- | --- |
| tile_design_readability | 952 | 102.9 | 42.2 |
| accessory_storage | 929 | 98.0 | 39.5 |
| buying_matching | 595 | 67.7 | 26.8 |
| tile_theme_pattern | 532 | 110.4 | 51.0 |
| mat_table_surface | 464 | 92.5 | 34.0 |
| quality_risk | 170 | 118.2 | 47.8 |

其他本地资产：`mjti_storage_pain_posts.csv`、`mjti_tile_back_side_report.xml`、`mjti_strategy_topic_stats.csv`。

## 已验证的关键词量（Google Ads，美国，2026-08-07 实拉）

**尺寸/可读性簇**（已被 `mahjong-tile-size-readability` 占用）
acrylic mahjong tiles 1,900 / mahjong tile size 880 / mahjong tile dimensions 880 / large mahjong tiles 880 / big mahjong tiles 880 / standard mahjong tile size 390 / large tile mahjong set 210 / extra large mahjong tiles 170 / xl mahjong tiles 140 / large print mahjong tiles 110 / easy to read mahjong tiles 40 / how to choose a mahjong set 20

**配件簇**（已被 `mahjong-accessories-guide` 占用）
mah jongg tile bags 4,400 / mahjong bag for tiles 4,400 / mahjong accessories 3,600 / mahjong racks and pushers 2,400（含 3 个同量变体）/ mahjong wooden racks 1,600 / mah jongg pushers 1,300 / mahjong table cover 1,000 / acrylic mahjong racks 590 / mahjong tile holders 480 / mahjong carrying cases 390 / mahjong trays 320 / mahjong keychain 390 / mahjong coin purse 260 / magnetic mahjong tiles 210

**低竞争信息类簇（高价值，但已被新手指南覆盖，见台账否决记录）**
how many tiles in american mahjong 1,300（competitionIndex **25**）/ how many flowers in american mahjong 1,000（index **5**）/ how many tiles in an american mah jongg set 390 / how many tiles in american mahjong set 390 / how many tiles in an american mahjong set 170 / how many tiles are in an american mahjong set 90

**其他已见**：linda li mah jongg set 1,300（竞品品牌词，不做）/ bamboo mahjong set 170 / full size mahjong set 110

## 已验证的关键词量（Google Ads，美国，2026-08-08 实拉）

**教学簇**（`how-to-teach-mahjong-to-beginners` 已占用主词）
how to teach mahjong 260（index **62** MEDIUM）/ how to teach mah jongg 260（同量同 index，是同一词的变体）/ learn american mahjong 170（index 71）/ learn how to play american mahjong 170（index 58）/ learn american mahjong online 90（index **24** LOW，全簇最低）/ learn to play american mahjong online 20（index 29）

**牌垫桌面簇**（整簇 index 100，且与配件篇 MED 重叠，已否决）
mahjong mat / mah jongg mats 27,100 / mahjong tablecloth 1,600 / mahjong table cover 1,000 / mahjong table mat 880 / best mahjong mat 590 / mahjong table topper 320 / mahjong playing mat 260

**vintage / antique 簇**（整簇 index 100，二手估值意图，无转化关系，已否决）
vintage mahjong set 1,900 / antique mahjong set 1,300 / vintage mahjong game set 1,300 / antique mahjong tiles 880 / vintage mahjong tiles 880 / vintage mahjong sets for sale 1,000 / vintage mahjong set value 50（index 89）

**设计簇**（量小且 index 满格，只够做现有设计篇的补充段落）
personalized mah jongg sets 1,600 / designer mahjong sets 1,000 / unique mahjong tiles 390 / mahjong tile designs 170（index 99）/ mahjong tile patterns 20

## 坑：`avgMonthlySearches` 返回 null 不等于「零搜索」

**现象**：`mahjong tile back designs`、`mahjong set worth`、`mahjong playing surface` 这类种子词返回 `avgMonthlySearches: null` + `competition: "UNSPECIFIED"`，而不是 0。

**根因**：Keyword Planner 对样本量不足的词不给量级，只在结果里回显种子词本身。这**不代表没人搜**，只代表它不在 Planner 的可报告阈值内。

**检测方法**：看 `competition` 字段。返回 `UNSPECIFIED` 且 `competitionIndex: null` 就是没有数据，不要写成「0/月」记进台账。

**修复/防护**：改用同簇的近义词做代理判断（例：`mahjong tile back designs` 无数据 → 看 `mahjong tile designs` 170/index 99 → 判定整簇不值得单独成篇）。台账里标「待拉」的候选词很多属于这一类，拉不出数不是失败，是可以直接据此否决的信号。

## 已验证的关键词量（Google Ads，美国，2026-08-10 实拉）

**价格/成本簇**（`why-are-mahjong-sets-so-expensive` 已占用主词）
buy mahjong set 590 / mahjong game price 320 / why are mahjong sets so expensive 260（index 100，**蚕食 clean**）/ mahjong set price 260 / mahjong set cost 260 / buy mahjong set near me 140 / how much does a mahjong set cost 110（index 100，**蚕食 clean**）/ mahjong table cost 50 / mahjong tiles price 20 / mahjong set buying guide 10（index 98）

**图案/符号簇**（整簇蚕食 MED，方向已关闭，见台账否决表）
flower tiles mahjong 1,600 / mahjong characters 1,300 / mahjong symbol 880 / flowers mahjong 590 / mahjong characters 1-9 等变体 480 / chinese characters in mahjong 480 / mahjong character numbers 390 / flower mahjong tile 320 / flowers in mahjong 320（index **12** LOW，但蚕食 HIGH）/ mahjong symbols meaning 260（index 45）/ mahjong flower and season tiles 210 / mahjong flower tiles meaning 90（index **4**，蚕食 MED）/ what do mahjong tiles mean 70 / season tiles mahjong 70

**选购入口簇**（几乎全部蚕食或量太小）
american mahjong set for beginners 210（index 61，蚕食 **HIGH**）/ a beginners guide to american mah jongg 480（index 79）/ how to choose a mahjong set 20（index 99）/ what to look for in a mahjong set 10 / mahjong set buying guide 10

## 坑：文章语料变密后，蚕食检查会对整个词族系统性报 MED

**现象**（2026-08-10）：`mahjong symbols meaning`、`mahjong tile symbols`、`what do mahjong tiles mean`、`mahjong flower tiles` 四个不同角度的候选词，全部报 MED，且命中的是同一批 4 篇文章。连 `mahjong set price` 也报 MED（命中 4 篇）。看起来像「站上什么都写过了」，实际不是。

**根因**：脚本剔除 generic 词后，剩下的判别词高频落在 `tile`/`tiles`/`flower`/`set`/`meaning` 上。站上 8 篇里有 5 篇是 tile 密集内容，任一篇的 FAQ 或 H2 里几乎必然出现这些词，于是「判别词 in body」轻松达到 50–100%，触发 MED。这是**语料密度导致的判别力衰减**，不是真实的意图重叠：`mahjong-gifts-game-night-hosts` 因为有一个小节叫 “Small Accessories Can Carry a Lot of Meaning”，就命中了 `mahjong symbols meaning`。

**检测方法**：看命中项的 `closest existing heading/question`。若那条 heading 与候选词的**搜索意图**明显无关（只是共享了一个泛词），且 `title/meta 0%`、`exact phrase x0`，那是判别力衰减而非真重叠。反之若 heading 直接回答了候选词（例：`flowers in mahjong` 命中 “8 Flowers, and 8 Jokers”，heading 100%），那是真重叠，必须换角度。

**修复/防护**：
1. 不要因为一个 MED 就放弃整个方向。换成**不含站上高频名词**的同义表达再测一次。本次 `mahjong set price`（MED）→ `why are mahjong sets so expensive`（clean）就是同一意图换词后通过的。
2. 若整族换词都过不了，说明这个方向该走「在现有文章加 FAQ 条目」而不是新开页。
3. 长期看这是新增文章的天花板信号。站上 tile 密集文章越多，新词越难 clean，应转向合并与优化现有文章。

## 坑：competitionIndex 100 不等于不能做

**现象**：价格/成本簇几乎全是 `HIGH index 100`，按「新站优先低 index」的规则会被整簇排除，但候选池已经没有低 index 且蚕食 clean 的词了。

**根因**：`competitionIndex` 衡量的是**广告主竞价拥挤度**。零售商会对所有带购买意图的词出价，包括 `why are mahjong sets so expensive` 这种纯问句。它与自然结果的排名难度是两件事，问句式信息意图的自然结果里排的通常是内容页而不是商品页。

**检测方法**：看词形。问句（why / how much / what）+ 无品牌词 = 信息意图，高 index 主要来自广告侧。名词短语（`buy mahjong set`、`acrylic mahjong tiles`）= 交易意图，高 index 同时反映自然端竞争，应交给产品页。

**修复/防护**：低 index 优先仍然成立，但当低 index 词全部蚕食时，**可以接受问句式的高 index 词**，前提是蚕食 clean 且能给出竞争对手给不出的内容（本次是真实制造成本结构 + 社群证据）。在台账里写明接受理由，不要让下次的自己以为规则被随意破坏了。

## 选关键词的判断顺序

1. 跑 `audit_blog.py --cannibalize "<候选词>"`，HIGH 或 MED 就换角度或改为在现有文章加 FAQ
2. 查 `state/topic-ledger.md` 的否决记录，避免重复踩同一个坑
3. 拉 `getKeywordIdeas` 确认量级与竞争度
4. 确认有 MJTI 社群证据支撑（否则是纯搜索量投机）
5. 确认能自然连到产品页

**交易型大词**（如 `acrylic mahjong tiles`、`mahjong set`）不做文章主关键词，应由产品页或集合页承接，文章里作次关键词与内链锚文本。

## 已验证的关键词量（Google Ads，美国，2026-08-12 实拉）

**人群/处境簇（本次新开，全部低竞争）**
mahjong for seniors 2,900（index **30** LOW，**蚕食 clean**，已占用）/ free mahjong for seniors 1,300（index 29，在线游戏意图，否决）/ mahjong terms 720（index **13** LOW，蚕食 clean，候选）/ mahjong group 390（index **3**，全表最低，候选）/ mahjong solitaire for seniors 320（index 19，在线游戏意图，否决）/ mahjong etiquette 90（index **7** LOW，蚕食 clean，候选）/ senior center mahjong 30（index 9）/ mahjong for elderly 10（index 30）

**对比簇**
difference between chinese and american mahjong 880（index **22** LOW，但蚕食 **HIGH**，新手指南已有同名 FAQ）/ difference between american and chinese mahjong sets 70（index 76）

**计分簇（否决：事实风险 + 赌博措辞红线）**
mahjong scoring / mahjong points / mahjong rules scoring 均 1,000（index 13 LOW）/ mahjong score cards 880（index 100）/ japanese mahjong scoring 320（index 0）/ mahjong scoring chart 320

**桌子簇（整簇 index 100，且 `mahjong table size` 蚕食 HIGH，否决）**
mahjong table 22,200 / automatic mahjong table 9,900 / foldable mahjong table 6,600 / mahjong board 4,400 / mahjong table size 与 mahjong table dimension 均 720 / best size table for mahjong 140

**旅行簇（交易型，且无对应产品，否决）**
travel mah jongg set 8,100 / travel mahjong 1,300 / mini travel mahjong set 880 / travel american mahjong set 480

**NMJL 卡簇**
national mah jongg league card 14,800（index **37** MEDIUM，量极大，值得单独评估）/ american mah jongg league card 260 / american mahjong score cards 260

## 方法：品类词枯竭时，改按「人群与处境」找词

**现象**（2026-08-12）：台账在 2026-08-08 与 08-10 连续两次得出「候选池见底」的结论，理由是所有候选词都报 MED/HIGH。但同一天换一批种子词重拉，立刻拿到 4 个低竞争且蚕食 clean 的词，其中一个是 2,900/月 index 30。

**根因**：此前的选题种子全部来自 MJTI 的六个 `primary_topic` 分类，而那六类都是按**器物**划分的（tile / accessory / mat / theme / buying / quality）。器物词天然共享 `tile`/`set`/`flower` 这些名词，而站上已有 5 篇 tile 密集文章，判别词必然撞车。这不是关键词池枯竭，是**种子词维度单一**。

**检测方法**：如果连续两轮候选词的蚕食报告命中的都是同一批文章，且命中的判别词都是同几个名词，那是种子维度问题，不是池子问题。

**修复/防护**：换一个正交的维度出种子词。已验证有效的维度：
1. **人群**：seniors、elderly、beginners、kids、lefties
2. **处境/场合**：etiquette、finding a group、senior center、travel、club
3. **身体条件**：eyesight、vision、arthritis、color vision
这些词的判别词（`seniors`/`etiquette`/`group`）站上完全没有语料，天然避开蚕食。MJTI 数据集也支持这种检索：不要只按 `primary_topic` 列过滤，直接对 `cols[10]` 摘录做跨话题正则检索，本次用 senior/elderly/eyesight/grandma 等词命中 131 帖。

## 坑：搜索量里混着完全不同的意图，Planner 不会告诉你

**现象**：`mahjong for seniors` 报 2,900/月 LOW index 30，看起来是个绝佳的商业词。但同簇里 `free mahjong for seniors` 有 1,300、`mahjong solitaire for seniors` 有 320。

**根因**：「老年人 + 麻将」这个组合在美国有两个完全不重叠的需求：一个是买实体美式麻将牌，一个是找免费的在线麻将消消乐（solitaire）。Keyword Planner 只报量，不拆意图，头部词 `mahjong for seniors` 两种意图都吃。

**检测方法**：拿主关键词加上 `free`、`online`、`solitaire`、`app`、`download` 做前后缀再拉一次。如果这些变体有可观的量，说明头部词的意图是混的，实际可承接的比例要打折。

**修复/防护**：
1. 不要按报出来的量做流量预期，在台账里写明折扣估计**并标注这是判断不是测量**。
2. 用标题做意图过滤。本次标题写 `Setting Up a Table`，明确指向实体牌桌，让找消消乐的人不点进来。误点进来的人会秒跳出，反而拉低页面指标。
3. 这条不构成否决理由。意图混杂的词只要还有一部分是买家意图，且竞争度低、蚕食 clean，仍然值得做。


## 坑：同名手游/App 会把一个词的量整个买断

**现象**（2026-08-14）：`mahjong club` 报 4,400/月、竞争 LOW index 7，是当轮所有候选里量最大且竞争最低的组合，看上去应该直接做主关键词。

**根因**：同一次 `getKeywordIdeas` 返回里躺着 `mahjong club app` 480、`mahjong club online` 720、`gamovation mahjong club` 140、`mahjong club solitaire game` 390。Mahjong Club 是一款手机消消乐 App 的产品名。头部词 4,400 的主体是在找那个 App 的人，跟实体美式麻将牌没有关系。这跟上一条「意图混杂」不同：那条是两种真实需求共用一个词，这条是**一个品牌名恰好等于一个通用词**，头部词实际上被那个品牌占了。

**检测方法**：拿到任何量级异常好而竞争异常低的词，先扫同一次返回里的兄弟词。出现下列任一模式就要怀疑是 App/游戏品牌名：
- 兄弟词里有 `<候选词> app` / `<候选词> online` / `<候选词> download` 且量不小
- 兄弟词里出现你不认识的公司名前缀（本次是 `gamovation`）
- 兄弟词里出现 `solitaire`、`pogo`、`free`、平台名

**修复/防护**：降为次关键词，不要作主关键词、不要进 meta title、不要进 slug。本次 `mahjong club` 只在正文里自然出现。**不要因为这条就否掉整个方向**：同簇的 `mahjong club near me` 1,000 / index 4 是真实的找局意图，没有被 App 污染，因为没人会给一个手机 App 加「near me」。

## 坑：「near me」词的量是真的，但那个位置拿不到

**现象**（2026-08-14）：找局簇里 `mah jongg groups near me` 1,300 / index 7、`mahjong club near me` 1,000 / index 4、`where to play mahjong near me` 480 / index 6，整簇约 3,500/月，竞争指数全部低于 10。数字看起来是台账开始以来最好的一簇。

**根因**：`near me` 是本地意图。Google 对这类查询在首屏上半部分给地图包、Meetup 的本地页、本地 Facebook 群。一个全国性的品牌博客不是一个「地点」，进不了那一层。而且这批人里相当一部分拿到本地链接就走了，根本不点内容页。

**为什么竞争指数会那么低**：`competitionIndex` 反映广告主出价竞争。这批词几乎没人投，正说明广告主判断它的即时商业价值低。低竞争在这里既是机会信号，也是一个警告，不要只读前半句。

**检测方法**：候选词里含 `near me`、`in <城市>`、`local`，或者兄弟词大量出现这些后缀，就按本地意图处理。

**修复/防护**：
1. **不要把 `near me` 词作主关键词**，主词取去掉本地限定后的头部词（本次取 `mahjong group` 390 / index 5），`near me` 变体只作次关键词自然出现在正文和 FAQ 里。
2. 文章必须为「找不到本地局的人」提供下一步动作，否则你既接不住本地意图、也没接住任何别的意图。本次的做法是把文章主体写成「怎么自己开一个」，FAQ 里那条 `How do I find a mahjong group near me?` 明确说「找一周还没有，那就自己开」，把死流量接成活意图。
3. 在审阅包里写明预期要打折以及打折的理由，**并标注这是判断不是测量**。

## 坑：几个写法报同一个量，那是一个量桶不是几个词（2026-08-17）

**现象**：拉三人局簇时，`3 player mahjong`、`3 people mahjong`、`3 person mahjong` 三个词**都报 1,600 / LOW / index 13**，连 CPC 出价区间都逐位相同。看起来像是三个各 1,600 的词，加起来 4,800。

**根因**：Keyword Planner 把语义等价的写法归到同一个分组里报同一个聚合值，不是三次独立测量。同值 + 同竞争指数 + 同出价区间三项全同，就是同一个桶的强信号。历史上 `mahjong strategy` 与 `mah jongg strategies` 同报 1,300、`american mahjong practice` 与 `american mah jongg practice` 同报 1,000，都是同一现象。

**检测方法**：在返回的 JSON 里按 `avgMonthlySearches` 分组。**如果两个词的 avgMonthlySearches、competitionIndex、lowTopOfPageBid、highTopOfPageBid 四项全部相同，按一个词计。**

**修复/防护**：算簇容量时先去重再相加，审阅包里写的是**去重后**的数。本次三人局簇去重后约 1,600 + 390 + 50 + 20 = 2,060，不是把三个 1,600 加进去的 4,800。**给用户报虚高的簇容量，会让后续所有投入产出判断跟着错，这是会传导的错误。**

## 已验证的关键词量（Google Ads，美国，2026-08-17 实拉）

| 关键词 | 月量 | 竞争 | index | 处理 |
| --- | --- | --- | --- | --- |
| 3 player mahjong / 3 people mahjong / 3 person mahjong | 1,600（**同一个量桶，按一个算**） | LOW | 13 | **本次主关键词** |
| 3 player mahjong rules | 390 | LOW | 12 | 次关键词 |
| 3 player mahjong set up | 50 | LOW | 20 | 次关键词 |
| american mahjong with 3 players | 30 | LOW | 13 | 次关键词 |
| american mahjong rules for 3 players | 20 | LOW | 11 | 次关键词（原样写进 FAQ） |
| 3 handed mahjong | 40 | LOW | 13 | 次关键词 |
| how many jokers in mahjong | 880 | LOW | 5 | **否决，真重叠** |
| can you use a joker in a pair for mahjong | 480 | LOW | 1 | **否决，真重叠**（rules 篇有逐字同名 FAQ） |
| mahjong joker rules / mah jongg joker rules | 260 | LOW | 5 | **否决，真重叠**（rules 篇有 H2 `Joker Rules`） |
| mahjong strategy / mah jongg strategies | 1,300（同一个量桶） | LOW | 26 | 暂缓，事实过期风险 |
| american mahjong strategy / american mah jongg strategies | 210（同一个量桶） | LOW | 24 | 暂缓 |
| mahjong terms | 720 | LOW | 15 | 仍在候选池，clean 复核通过 |
| mahjong etiquette | 110 | LOW | 9 | 仍在候选池 |
| charleston mahjong | 1,300 | HIGH | 100 | 未评估，竞争满格 |
| mahjong tournament | 720 | LOW | 1 | 未评估，可能是赛事查询意图（本地/日期），转化承接存疑 |
| american mahjong practice | 1,000 | LOW | 13 | 未评估，疑似找 App/在线练习意图 |

**joker 簇的教训值得单独记**：约 2,000/月、竞争指数全簇 1–7，是本台账见过最诱人的数字组合，但站上 `american-mahjong-rules` 已经把它占满了。**低竞争 + 高量 + 站内已覆盖 = 该去扩写旧文，不是新开页。** 数字好看不构成写新页的理由。

## 已验证的关键词量（Google Ads，美国，2026-08-20 实拉）

**锦标赛簇（本次新开方向，整簇竞争指数 0–6，是台账见过最低的两簇之一）**

| 关键词 | 月量 | 竞争 | index | 处理 |
| --- | --- | --- | --- | --- |
| mahjong tournament | 720 | LOW | **1** | **本次主关键词** |
| mahjong tournament near me | 480 | LOW | 3 | 次关键词，按 near me 规则只进 FAQ |
| destination mah jongg tournaments | 260 | LOW | 0 | 次关键词（周末场 / 邮轮场） |
| mah jongg tournament | 170 | LOW | 1 | 次关键词 |
| mahjong competition | 170 | LOW | 6 | 次关键词，单独查蚕食 clean |
| mahjong fever tournaments | 140 | LOW | 0 | **剔除，是主办方品牌名** |
| american mah jongg tournament | 110 | LOW | 0 | 次关键词 |
| mah jongg tournaments near me | 70 | LOW | 4 | 本地意图 |
| american mahjong tournament | 30 | LOW | 2 | 次关键词 |
| mahjong tournament online / online mahjong tournament | 20（同一个量桶） | LOW | 3 | 无关意图 |

**去重且剔除品牌名后约 2,030/月**，但 `near me` 两条 550 与 `destination` 260 是本地/找活动意图接不住，可承接的信息型部分保守估计 **400–700/月，这是判断不是测量**。

**保养/清洁簇（2026-08-20 新拉，正文实证零覆盖，已进候选池）**
how to clean mahjong tiles 110（index **9**）/ how to clean mah jongg tiles 110（**与主词同桶**）/ how to wash mahjong tiles 30（index 6）/ how do you clean mahjong tiles 10 / how to clean ivory mahjong tiles 10 / how to clean yellow mahjong tiles 10（index 0）/ how to store mahjong tiles 20（**HIGH index 100**，配件篇已有同名 FAQ，否决）/ mahjong tile care 与 yellowed mahjong tiles **无数据 UNSPECIFIED**
去重后簇容量约 170/月。量小，但判别词在站上零实质语料。

**练习簇（否决：App / 在线对局意图）**
american mahjong practice 与 american mah jongg practice 均 1,000（同一个量桶，index 13）/ american mahjong practice app 590（index **1**）/ free american mahjong practice 20 / 另有 practice 2019–2022 一批年份变体
**判定依据**：`app` 变体 590 且 index 1，加上一整排年份变体，说明主体在找练习软件而不是实体牌内容。与 travel 簇同理否决。

**人数/角色簇（本轮关闭）**
5 player mahjong 20（index 11，量太小）/ mahjong bettor 与 mah jongg bettor 均 90（同一个量桶，**HIGH index 67**，且 bettor 措辞贴近赌博红线）
2026-08-17 候选池里「五人局 / bettor 角色」这一条至此正式关闭。

**术语簇（脚本 clean 但正文实证为真重叠，改扩写旧文）**
mahjong terms 720（index 15）/ mahjong lingo 50（index 20）/ mahjong english terms 10（UNSPECIFIED）/ mahjong terms cantonese 与 mahjong terms tagalog 各 10
详见 seo-audit-checklist.md 的「坑：脚本报 clean 也可能是假阴性」。

**礼仪簇（仍在候选池）**
mahjong etiquette 110（index **9**，2026-08-20 复核仍 clean）/ mah jongg etiquette 10（index 15）
注：08-12 记的是 90，本次实拉 110，量级会小幅漂移，以最近一次为准。

## 方法：低竞争指数要分辨是「机会」还是「广告主认为不值钱」

**现象**（2026-08-20）：锦标赛簇竞争指数 0 到 6，比组局簇还低，量还有 720。按「新站优先低 index」的规则，这是本台账开始以来数字最漂亮的组合之一。

**根因**：`competitionIndex` 只反映广告主竞价拥挤度。它低有两种完全不同的成因，必须分辨：
1. **广告主还没发现**（真机会）。
2. **广告主发现了，判定这批人不会买东西**（假机会）。找活动、找场次、查日期的人，看完就走了。

锦标赛簇属于两者混合：informational 那一层是真机会（没人为「第一次参赛该注意什么」投广告，但这批人确实在买牌练习）；`near me` 与 `destination` 那一层是假机会（找活动的人不会顺手下单）。

**检测方法**：把簇里的词按「查完就走 / 查完要买东西」分两堆，看量集中在哪一堆。含 `near me`、城市名、年份、`online`、`app`、主办方或产品品牌名的，归到「查完就走」。

**修复/防护**：主关键词取信息型的头部词，本地与找活动的变体只作 FAQ 并给出下一步动作（本次那条 `How do I find a mahjong tournament near me?` 的答案是「先在你已经在的群里问，找不到说明你还没进那个圈子」，并导向组局篇）。在审阅包里按两堆分别报量，不要报一个合计数。

## 已验证的关键词量（Google Ads，美国，2026-08-25 实拉）

**两人局簇（本次主方向，去重后约 5,110/月，是台账见过最大的一簇）**

| 关键词 | 月量 | 竞争 | index | 处理 |
| --- | --- | --- | --- | --- |
| 2 player mahjong / 2 person mahjong / 2 player mahjong game / 2 player mahjong games | 2,900（**四个写法同一个量桶**） | LOW | 29 | **本次主关键词** |
| 2 person mahjong rules / 2 player mahjong rules | 1,000（同桶） | LOW | 16 | 次关键词 |
| mahjong for two players | 880 | MEDIUM | 39 | 次关键词（**独立桶**） |
| 2 player american mahjong | 70 | LOW | 16 | 次关键词 |
| 2 handed mah jongg / two handed mah jongg | 50（同桶） | LOW | 9 | 次关键词 |
| 2 handed mahjong | 40 | LOW | 9 | 次关键词 |
| playing mahjong with two people | 40 | LOW | 15 | 次关键词 |
| 2 people mahjong | 30 | MEDIUM | 38 | 次关键词 |
| 2 player mahjong how to play | 30 | LOW | 6 | 次关键词 |
| american mahjong for 2 players | 20 | MEDIUM | 42 | 次关键词 |
| mah jongg for two players | 20 | MEDIUM | 41 | 次关键词 |
| 2 player mahjong online | 140 | LOW | 3 | **剔除**，在线意图 |
| 2 player mahjong app | 30 | LOW | 9 | **剔除**，App 意图 |
| 2 player riichi mahjong | 30 | LOW | 0 | **剔除**，日式 |

**开局/摆桌簇（整簇否决：真重叠，rules 篇有 H2 逐字叫 `Setup`）**
how to set up mahjong / how to set up a mahjong game / how to set up mahjong game 720（同一个量桶，index 16）/ mahjong wall 480（index 46）/ mahjong wall setup 210（index 46）/ mahjong dealing 260（index 30）/ mahjong dealing rules 170（index 37）/ how to set up mahjong tiles 170（index 33）/ mahjong deal 170（**HIGH index 100**）/ how to deal mahjong tiles 140（index 20）/ dealing mahjong 140（index 24）/ mahjong east wind 110（index 63）/ how to set up american mahjong 90（index 32）/ mahjong seating 40（**HIGH index 71**）/ who goes first in mahjong 30（index 8）/ how to build mahjong wall 20（index 5）
**数字很好（720 / index 16），但站上已被 `american-mahjong-rules` 的 `Setup` 一节和新手指南的 `Setting Up` 一节完全占满。这是「低竞争 + 有量 + 站内已覆盖 = 去扩写旧文」的第二个实例（第一个是 08-17 的 joker 簇）。**

**NMJL 牌型卡簇（否决：导航型意图，08-12「值得单独评估」的待办至此关闭）**
national mahjongg league 22,200（**HIGH index 76**）/ national mah jongg league card 与 mah jongg league cards 14,800（同桶，LOW index 31）/ national mah jongg league 与 mah jongg league 12,100（index 60）/ www nationalmahjonggleague org order online 1,900（**index 100**）/ nationalmahjonggleague org cards 1,000（**index 100**）/ national mah jongg 590（index 94）/ how to read mahjong card 320（index 33）/ national mah jongg card 260（index 100）
**判定依据**：三个含 `nationalmahjonggleague org` 的站内导航词合计近 3,000/月且 index 全部 92–100，说明头部 14,800 的主体是**要去 NMJL 官网买当年牌型卡的人**。这不是内容意图，是导航意图，第三方博客接不住。叠加牌型卡逐年更新的事实过期风险，整簇关闭。

**牌型簇（否决：竞争高 + 事实逐年过期）**
mahjong hands 1,900（**HIGH index 88**）/ all mahjong winning hands 110（**index 91**）/ all mahjong hands 40（index 35）/ 另有 2021–2022 年份变体一批（各 10 或 0）
年份变体的存在本身就是**事实过期风险的信号**：这类词每年重新洗牌，写死的页面会逐年贬值。

**礼仪簇（复核仍 clean，本次未采用）**
mahjong etiquette 110（index **9**，08-12 / 08-20 / 08-25 三次均 clean，本次已加正文实证）/ mah jongg etiquette 10（index 15）
其余礼仪类种子（`mahjong table manners`、`mahjong rules for guests`、`mahjong group etiquette`、`what to bring to mahjong`、`how to be a good mahjong player`、`first time playing mahjong`）**全部 UNSPECIFIED 无数据**，说明这个方向天花板就是 110 那一个词。

## 方法：意图污染检查要看「兄弟词的绝对量」，不是有没有兄弟词（2026-08-25 细化）

08-12 定的检测方法是「主词加 free / online / solitaire / app / download 再拉一次」。**本次补一条判读标准：拉出来之后怎么判。**

三个实例并排：

| 主词 | 量 | 污染兄弟词 | 判定 |
| --- | --- | --- | --- |
| `mahjong for seniors` | 2,900 | `free mahjong for seniors` **1,300**、`mahjong solitaire for seniors` 320 | **重度污染**，可承接三到五成 |
| `mahjong club` | 4,400 | `mahjong club app` 480、`mahjong club online` 720、`gamovation mahjong club` 140 | **被同名 App 买断**，降为次关键词 |
| `2 player mahjong` | 2,900 | `free 2 player mahjong` **无数据**、`2 player mahjong solitaire` **无数据**、`2 player mahjong download` **无数据**、app 仅 30、online 仅 140 | **几乎无污染**，折扣可打得很轻 |

**判读标准**：把污染兄弟词的量加总，除以主词的量。
- **> 30%**：重度污染，按三到五成折算（seniors 那次是 1,620/2,900 ≈ 56%）。
- **5%–30%**：中度，折两成左右。
- **< 5%**：可以基本按报出的量规划（本次是 170/2,900 ≈ 5.9%，其中 140 还是 online 这种边缘意图）。
- **兄弟词返回 UNSPECIFIED 无数据是最强的干净信号**：说明连 Planner 都凑不出这个组合的样本，那个意图基本不存在。

**注意这条只筛「同词根的其他意图」，筛不掉「`mahjong` 一词在美国大众语境里本身就常指消消乐」这层底噪。**后者无法用 Planner 测量，只能在审阅包里写明是判断不是测量。

## 候选池会「过期低估」，不只是「过期失效」（2026-08-26 新增）

**现象**：台账候选池里记着 `where to learn mahjong near me` 390 / index 4。本轮按这个方向去实拉整簇，发现同一个读者处境下的非本地头词是 `mahjong lessons` **3,600 / index 7**，量级大 9 倍，竞争同样低。**候选池那条本身没错，但它严重低估了这个方向的价值。**

**根因**：候选池记的是「上次拉词时用的那个措辞碰巧命中的结果」，不是「这个方向的最优词」。上次是用 `where to learn` 这个措辞拉的，Keyword Planner 就只在那个措辞的邻域里返回结果。**同一个读者处境换成 `lessons` / `classes` 去拉，返回的是完全另一批词。**

**此前记录的失效模式都是反向的**（上次 clean 这次蚕食了，见台账 08-20 与 08-25）。「过期低估」是新的一类，且更隐蔽：它不会报错，只会让你写一篇量级小一个数量级的文章而毫不知情。

**检测方法**：从候选池取词时，**先把该词的读者处境翻译成 2 到 3 种别的措辞，各拉一次 `getKeywordIdeas`**，再决定用哪个当主词。本轮生效的具体做法：把「我想找个人教我」分别写成 `where to learn mahjong` / `learn to play mahjong` / `mahjong lessons` / `mahjong classes` 放进同一次调用的 `keywords` 数组。

**防护**：台账「用前必须做」原本是两条（拉量级、跑蚕食），**现在是三条**：
1. 把处境翻译成 2–3 种措辞，整簇重拉，选量级最大的非本地词作主词
2. 拉 `getKeywordIdeas` 确认量级与竞争度
3. 跑 `--cannibalize` 复核，且脚本两种结论都要回正文实证

## 配额会耗尽（2026-08-26 新增）

**现象**：同一轮里第二次调用 `getKeywordIdeas` 返回 `8 RESOURCE_EXHAUSTED: Resource has been exhausted (e.g. check quota)`，第一次调用正常返回 50 条。

**根因**：Google Ads API 的 Keyword Planner 有独立配额，与 GAQL 查询不共享。并发两次调用更容易触发。

**检测方法**：错误字符串里有 `RESOURCE_EXHAUSTED`。**不是参数错误，重试即可**。

**修复/防护**：
- **一次调用里把 `keywords` 数组塞满（上限 20 个种子词）**，比分多次调用划算得多。本轮 4 个种子词一次就拿回了整个找课簇 50 条。
- 触发后隔一会儿单发一次通常就能成功（本轮第二次单发 `mahjong etiquette` 正常返回）。
- **不要为了「更干净」把种子词拆成多次调用**，那正好是最容易耗尽配额的用法。

## 第三条找词路径：站上自己写下的「推迟句」（2026-08-30 升级为方法，两次实例）

**现象**：候选池见底、按品类与按人群两条路径都拉不出新词时，`how to win at mahjong` **1,600/月 index 13** 这样量级不小、竞争不高、蚕食干净的词却一直没被发现。

**根因**：前两条路径都是从站外找（品类名、人群名），而这个词的线索**一直写在本站正文里**。`how-to-teach-mahjong-to-beginners` 逐字列着第一课不该教的东西：`strategy about defensive discarding, and any discussion of which hands are statistically stronger`。作者当时是为了收窄那篇的范围，**但这句话同时也是一条声明：这个主题真实存在、本站承认它重要、本站还没写它。**

**第二个实例（回溯）**：08-17 的 `3 player mahjong` 1,600/index 13 同样来自一句推迟句 —— 新手指南写着 "three-player table variants exist, but learn the four-player game first"。当时只当成蚕食实证的旁证，没意识到它是找词入口。

**检测方法**：把全部正文落盘（含草稿），正则搜推迟句式：
```
exists,? but | but learn .* first | not the first | skip .* for now | worth learning later
| once you | after you .* comes | is a topic for | beyond the scope | we are not covering
| should not (teach|cover) | leave .* for another
```
命中的每一句，把**被推迟的那个话题**当作 `getKeywordIdeas` 的种子词。

**为什么这条路径的蚕食天然干净**：本站之所以推迟它，就是因为本站没写它。推迟句本身只有一两句话，不构成覆盖（与 08-26 「一个从句不构成覆盖」同一条判据）。

**顺序建议**：候选池取词 → 按处境重拉 2–3 种措辞（08-26 那条） → 都不理想时走本条。

## 新增假朋友（2026-08-30，打法判断簇）

| 词 | 在本站的真实含义 | 会误伤哪类候选词 |
| --- | --- | --- |
| `odds`（新手指南 ×2） | 牌型家族名 `odds (13579)`，指**单数牌**，不是概率 | 任何含 odds / chances 的打法类候选词 |
| `strategy`（新手指南开头） | "a little strategy, a lot of conversation" 的**泛用形容词** | `mahjong strategy` 簇 |
| `win` / `winning`（10 处，跨 5 篇） | 多为**社交场景句**（谁赢了大牌、赢家得一个塑料小鸭、赢家奖品），以及 rules 篇的 `When Nobody Wins` 流局机制 | `how to win` 簇（本轮实证的主要工作量） |
