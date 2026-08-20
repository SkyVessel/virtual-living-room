# Product Select Report · 2026-08-19

## Pipeline Quality

| Metric | Value | Status |
|--------|-------|--------|
| HORIZON windows found | 9 | ok — 5 `golden`, 2 `early`, 1 `early_golden`, 1 `early`/high-risk |
| DEPTH pain points found | 5 | ok — 全部带真实日期引用 (r/self 2026-02, App Store 2026-05, r/homeowners 2025-07 等) |
| CRAFT candidates evaluated | 12 | ok — 每项跑 7 项检查 |
| CRAFT kill rate | 92% | `too_strict` (被 2026 敌对市场证据证明合理) |
| Data freshness | evidence 2026-01 至 2026-08 | ok — 覆盖 LLM 价格战、GPT-Realtime-2、Poke 3 天 10K→100K |
| Evidence density | 2+ URLs per claim | ok (上游声明; 个别数字未二次核验, 标记为"未复核的上游断言") |

**目标画像**: Consumer (B2C) · AI 全栈 · 15h/周 · <$50/月 · 无现成受众 · 无营销预算

---

## Top Recommendation: Plant Care App(自适应浇水提醒,免费基础版)

> 靠"真正记得住、不淹死植物"的差异化提醒,打进植物养护这个有真实付费意愿、但头部体验普遍被吐槽的细分市场。先验证、后写码。

### Why now (HORIZON)
- **On-device AI (golden)** 是唯一可复用窗口: Core AI 开放开源模型本地推理 (AFM 3 20B), Android AICore + Gemma 4。自适应提醒可完全本地推理,零服务器成本——支撑 "free basics" 楔子,并把 "静态时间表" 差异做成隐私卖点。
- LLM 价格战 (~1000-2000 LLM sessions/$1) 让"根据光照/湿度/品种动态生成浇灌方案"的单用户成本趋近于零。
- 2026 年 3 个同质竞品 (Sprout 免费、Frond 免费、Greenroot £14.99 预售) 证明**这个楔子已被证实有人想占**,窗口正在被占满——现在不做,6 个月后更难。

### Who needs this (DEPTH)
- 每周频率痛点,强度 5/10(该面板中最弱,但用户真实)。
- 直接引语: *"£70 a year just to be reminded to water my pothos. Are you kidding me?"* (App Store 2026-05); *"I've been reading that Planta is not so good about reminding you to water your plants and can cause you to overwater them. Are there any other better apps?"* (r/houseplants)。
- 7,585 条评论分析显示: 基础功能被 paywall、提醒失效、**静态计划导致过度浇水**是三大重复抱怨。"提醒无效"是被引用的真实缺口。

### Why you can win (CRAFT)
- 唯一通过全部 7 项检查的候选 (`survival_score 5/10`): 可单人实现、成本 <$50/月、无平台依赖、无需受众即可启动。
- 差异化明确: 自适应(光照/品种/上水时间) vs 头部"静态提醒";本地推理 → 免费基础版可持续。
- 验证路径最便宜: Greenroot 模型(一次性预售落地页) + r/houseplants 帖子 + DM 20 位植物主人,2 周内完成,写码前先拿到付费信号。

### Why this might fail (Devil's Advocate)
1. **最可能失败方式**: 你进入的是 **2026 年已被 3+ 全新对手占位的 land-grab**(Sprout/Frond 免费 + Greenroot 预售)。你没有受众,对方有发行惯性。落地页可能拿到 0-50 个预售——r/houseplants 今年已见过同类发布,**新品疲劳** + 社区对"提醒类应用"不信任(过度浇水抱怨 → 对任何提醒 app 都怀疑)。你写码 3 个月,Greenroot 先发货,差异点被抄走。
2. **可能错了的假设**: (a) "自适应提醒值得付费"从未被验证——抱怨可能只是"想要免费",而非"想要更聪明的提醒";(b) £70/年太贵的用户,不代表愿意为任何东西付费;(c) r/houseplants 的可触达性被高估了。
3. **build→don't build 翻转信号**: 落地页 2 周内**转化率 <5% 或预售 <20 单**(自然 Reddit 流量),或 DM 20 位植物主人后 <30% 表示会换掉现有工具 → 停止。
4. **反驳**: 下行成本极低——最坏情况是 15-25 小时 + ~$30,不是半年。失败引用的是被明确引用的痛点("会淹死植物"),不是发明需求。"先验证后写码"意味着**杀信号先于任何真实开发成本触发**。

### Action Plan
| Phase | Timeline | What to do | Success signal |
|---|---|---|---|
| Week 1 | 落地页 + 渠道测试 | 单页(free basics 承诺 + "自适应不淹死植物"钩子) + 预售按钮; r/houseplants 2-3 帖(先回答/贡献,再带链接); DM 20 位植物主人 | >20 预售 or >5% 落地页转化 |
| Week 2-4 | 最小 MVP | 品种库(前 50 常见植物) + 天气/位置感知的浇水计划 + 每周推送(Telegram/Bot 短信即可,不做 app) + "上次浇水""光照评估" | 50 活跃用户,30 日留存 >25% |
| 3-month | 目标 | 300 活跃用户;免费层自然传播(每周分享卡片); ≥5% 转付费订阅或 5% 一次性解锁 | 月度订阅收入 >$50(覆盖成本即过线) |
| Kill signal | 任意时点 | 落地页失败; 或 MVP 后 30 日留存 <10% | 立刻停,转 #2 路线 |

---

## Recommendation #2: AI Dinner Decision-Maker("今晚吃什么"决策消除器,条件复活)

> 痛感全场最高 (8/10,每日触发) + LLM 价格战把单次成本打到趋零,但**必须先解决 CRAFT 杀掉它的那个问题:没有受众**。这是"先建受众、再写码"的路线。

### Why now (HORIZON)
- **LLM price war (golden)**: 1000-2000 LLM sessions/$1,"个性化晚餐决策 + 购物清单 + 菜谱"每次成本趋近于零,毛利结构天然成立。
- **Realtime voice (golden)**: $0.017-0.034/分钟,语音是留存最高的模态——"语音问、语音答"的晚餐助手终于便宜到可以 ToC。
- 反信号: **ChatGPT/Gemini 语音已经免费在做这件事**——价格战让巨头更有动机覆盖这个用例,这正是 CRAFT 判定平台风险的理由。

### Who needs this (DEPTH)
- 每日频率、强度 8/10(全部 5 个痛点中最高)。
- 引语: *"Feels like every single day around 5pm my brain has to solve this puzzle... Ended up ordering takeout for the third time this week"* (r/self 2026-02)。
- 数据: 60% 千禧/Gen Z 是家庭餐食规划唯一负责人,26% 报告压力;用户每周花 $60-100 在 HelloFresh 上就是为了外包这个决策。**现有 app 全是菜谱管理器,不是决策消除器**——决策疲劳是真空缺。

### Why you can win (CRAFT)
- 面板评分在各候选中**数字最高 (6.20/10)**,全部来自痛感强度与窗口时机。
- CRAFT 的杀掉理由**不是需求或技术,而是发行**——可修复: revive 条件是"先建立食物内容受众,或做带自有数据护城河的 chat-native 形态"。
- 每日高频 hook = 订阅留存的前提条件,全 5 个痛点里只有它和 parental control 是每日级。

### Why this might fail (Devil's Advocate)
1. **最可能失败方式**: 没有食物内容受众,App Store 的"晚餐决策"搜索位被菜谱巨头占据。更致命的是——用户点外卖不是因为缺一个"决策器",而是因为**累 + 做饭摩擦真实存在**。"解决 what"不解决"will"。你做一个模型套壳,而巨头免费送同样的能力,且这能力只会越来越便宜。
2. **可能错了的假设**: HelloFresh 类比。HelloFresh 卖的是**生鲜物流(重资产护城河)**,不是决策。用它论证"用户为决策付 $60-100/周"是过度解读——用户付钱是因为菜到家了,不是因为"不用想了"。
3. **build→don't build 翻转信号**: r/tonightsdinner、r/cooking 发 3 条有机帖,2 周内 <50 预售注册或 <200 深度参与用户 → 不写码。做食物短内容 4-8 周无起色 → 视为发行路径证伪。
4. **反驳**: 痛感 8/10 + 每日触发是全部候选中**唯一能支撑长期订阅的心智模型**;CRAFT 的 kill 是"发行策略错误",不是"产品不存在"。若接受时间线从"一个月上线"变成"先养 2 个月受众",LLM 成本趋零让单人完全可承担。但这是**显式的时间换空间交易**,不是白送的升级。

### Action Plan
| Phase | Timeline | What to do | Success signal |
|---|---|---|---|
| Week 1 | 受众可行性验证(不写码) | r/cooking、r/tonightsdinner 发 3 条有内容的决策类帖子; 同时注册 TikTok/小红书食物账号发 3-5 条"AI 帮你解决晚餐"短内容 | 3 帖合计 >50 深度评论; 任一内容 >500 播放/展示 |
| Week 2-4 | 受众构建(4-8 周为主路径) | 每周 3-5 条内容; 同时做 chat-native 原型(Telegram Bot 即可):"问它今晚吃什么" | 受众粉丝 >500 或单帖 >5K 触达; 原型 >200 会话、30 日回访 >30% |
| 3-month | 目标 | 单一食物小众(如"上班族快手健康晚餐")站稳; 订阅转化 >5%; 单用户单月成本 <$0.10 | 500 付费前活跃用户 |
| Kill signal | 任意时点 | 4 周内容冷启动 0 信号(粉丝 <100) → 受众先行路径证伪; 或原型 30 日留存 <15% | 停,转 #3 或回到 #1 |

---

## Recommendation #3: Forgotten-Subscription Finder(免银行登录的订阅漏检器,条件复活)

> 单位经济全场最好(人均每月多付 $133、低估 2.5 倍;持续监控 = 天然订阅),但**整个方向押在 Google Gmail API 的审批政策上**——这是你无法控制的闸门。

### Why now (HORIZON)
- 无专属 golden window;可搭 **LLM 价格战**的车——邮件语义分类("这是订阅吗、涨价了吗、还用过吗")单封成本趋零。
- **Messaging-native agents (early_golden)** 是潜在形态: 发现结果主动推给用户,切中 home-maintenance 的 "bot 直接发消息" 教训。

### Who needs this (DEPTH)
- 月度频率、强度 6/10;引用数据: 人均订阅支出 $133/月,自我低估 2.5 倍。
- 需求真实且被验证过: Rocket Money ($100M+ 营收) 证明付费意愿,但它的**银行登录信任门槛**是真痛点。`gap = 免银行登录地发现被遗忘的订阅` 成立。supply gap 5/10。

### Why you can win (CRAFT)
- CRAFT 的杀掉理由是**技术可行性 (Gmail API verification)** 而非需求/发行——属于"政策闸门型"kill,比"需求不存在型"更接近可复活。
- revive 条件: (a) Gmail API 受限 scope 变得可申请; (b) 做成**持续监控服务**而非一次性扫描。
- 隐私叙事 + 成本叙事("替你找还回来的钱")是 5 个痛点里**最具体的 ROI 故事**。

### Why this might fail (Devil's Advocate)
1. **最可能失败方式**: Google 的 OAuth 受限 scope 审批对单人开发者是硬墙(这**正是** CRAFT 杀掉它的原因);个人 Gmail scope 通常要求审核、业务资质,<$50/月预算下大概率拿不到。就算拿到,**免银行登录但要求全邮箱读取权限**——你用更深的信任问题替换了 Rocket Money 的信任问题。分类不准(把促销邮件误判成订阅)会瞬间摧毁信任。Rocket Money 已占据品类与"省钱"心智。
2. **可能错了的假设**: 用户愿意把邮箱读权限交给一个未知开发者。隐私用户 (r/privacy、r/personalfinance) 可能买单,但主流用户不会——你进入的是比银行登录更难卖的信任谈判。
3. **build→don't build 翻转信号**: **Gmail API 受限 scope 申请被拒** → 一票否决,不写任何代码;scope 获批后落地页 2 周 <30 注册 → 停。
4. **反驳**: 这是"如果你能拿到 key,就能赢"的方向。$133/月漏损 + 持续监控 = 最健康的订阅模型之一。但闸门在 Google 手里——**必须先验证 scope,后验证产品**,顺序反了就是浪费。

### Action Plan
| Phase | Timeline | What to do | Success signal |
|---|---|---|---|
| Week 1 | 政策验证(唯一不可跳过项) | 提交 Gmail API 受限 scope 申请; 同时做落地页("发现你的订阅漏检,不看你的银行") + r/privacy/r/personalfinance 帖 | scope 获批; 落地页 2 周 >30 注册 |
| Week 2-4 | MVP(仅当 scope 通过) | 只做**发现**: 邮件扫描 + LLM 分类 + 周报; 不做取消代办。单用户运行 | 100 用户完成扫描,40% 识别出 ≥1 个被遗忘订阅 |
| 3-month | 目标 | 持续监控订阅化 ($3-5/月); 单用户月均找回 >$20 | 300 付费用户或 MRR >$1000 |
| Kill signal | 任意时点 | scope 被拒; 或扫描准确率导致 30 日留存 <20% | 停,止损在政策墙前 |

---

## Recommendation #4(备选,篇幅从简): Home Maintenance Bot(条件复活)

- 矩阵得分 4.55。痛感 6/10,"$6 滤网 → $4000 维修"是全场最具体的 ROI 故事,r/homeowners 真实需求("记住定期维护 + 追踪保修",2025-07 引语)。
- CRAFT 杀掉于**留存**(月频工具,无 app 可开的 bot 短信模型是唯一差异化——所有在位者都是 app)。但 **r/homeowners 禁止自推广**,发行路径几乎被封死。
- 翻转信号: 纯文本落地页 100 waitlist + 短信原型 40% 回复率 + 30 日留存 >30%,否则即 kill。不满足"无 app"前提就不要做——否则退化成又一个无留存的月历 app。

---

## Ranking Matrix(透明披露)

| Candidate | Pain 25% | Supply 20% | Window 20% | CRAFT 20% | Fit 15% | **Total** |
|---|---|---|---|---|---|---|
| **#1 Plant care** | 5 (1.25) | 3 (0.60) | 4 (0.80) | 5 (1.00) | 7 (1.05) | **4.70** |
| #2 Dinner | 8 (2.00) | 5 (1.00) | 8 (1.60) | 2 (0.40) | 8 (1.20) | **6.20** |
| #3 Forgotten subs | 6 (1.50) | 5 (1.00) | 5 (1.00) | 2 (0.40) | 7 (1.05) | **4.95** |
| #4 Home maintenance | 6 (1.50) | 4 (0.80) | 4 (0.80) | 2 (0.40) | 7 (1.05) | **4.55** |
| (参考) Parental control | 7 (1.75) | 3 (0.60) | 3 (0.60) | 1 (0.20) | 4 (0.60) | **3.75** |

**诚实说明**: 按矩阵裸分,#2 晚餐决策 (6.20) **高于** #1 (4.70)。#1 仍排第一,是因为矩阵无法表达**硬闸门**: 晚餐决策的 kill 是一个"前置条件"(必须先生成受众),这个前置条件在用户现有约束(无受众、15h/周)下**无法在构建窗口内兑现**;而 #1 是唯一"现在、无受众、下周就能发货"的候选。**排名规则 (survivor #1) 反映的是"可执行性优先",不是"需求强度优先"**。如果你愿意花 4-8 周先养受众,则 #2 的期望值可能反超——这是本报告最重要的隐性结论。

---

## Opportunity Cost Analysis

选择 #1(plant care)意味着放弃:

- **放弃 #2 晚餐决策(最高天花板)**: 痛感 8/10、每日 hook、唯一支撑长期订阅的心智。代价是**显式的**: 要么你现在用 4-8 周养食物受众(这是 CRAFT 给它的唯一复活前提),要么接受它永远只是"巨头语音助手的免费功能"。植物方向的上行被同质竞品压到 ~2-3x,而晚餐如果发行做对,可能是 10x+。
- **放弃 #3 订阅漏检(最优单位经济)**: 若 Gmail 政策墙在 6 个月内打开,它会是一个 $100M+ 品类的干净切入位。但你把决定权交给了 Google,这是你无法对冲的风险。
- **时间成本才是真代价**: 你 15h/周、<$50/月,只能并行维持一条主路线 + 一条验证副线。#1 的最大优势不是它的上限,而是**它的失败也便宜** (15-25 小时)。选 #1 ≠ 永远放弃 #2——只要在 #1 的验证期 (2 周) 内观察 r/cooking 类内容的冷启动信号,你可以**把 #2 的受众验证当作 #1 的并行副线**,让机会成本自然摊薄。

---

## Killed Directions(Reference)

| Direction | Failed Check | Reason | Could revive if... |
|---|---|---|---|
| AI dinner decision-maker | Distribution | 无受众,巨头语音助手免费覆盖 | 先建食物内容受众; 或 chat-native + 自有数据护城河 |
| Forgotten-subscription finder | Technical feasibility | Gmail API 验证墙(个人 scope 难获批) | Gmail 受限 scope 开放 + 做持续监控服务(见 #3) |
| Home maintenance tracker | Retention | 月频工具留不住 | bot 短信化(无 app 可开) + 拥有房主受众(见 #4) |
| Parental control layer | Technical feasibility | OS 沙箱,单人做不了 | Apple 开放 Screen Time API(极不可能)或 Android+路由器(范围太大) |
| Voice-native companion | Platform/regulatory risk | Character.AI/Replika 反弹 + 监管 | 合规的成人小众(老年陪伴、哀伤支持) + 严格护栏 |
| Voice dinner coach | Platform risk | ChatGPT voice 已免费覆盖 | 独特硬件/上下文,或拥有烹饪受众 |
| Personalized AI music | Retention | 一次性礼物, LTV $3-5 | 订阅捆绑,或自有病毒 TikTok 模板 |
| WhatsApp/Telegram AI agent | Platform risk | Poke 被 Cognition 收购; Apple Messages for Business; Meta 禁 WhatsApp 聊天机器人 | Telegram 上超垂直场景 + 存储数据切换成本 |
| On-device private journaling | Platform risk | Apple Journal 占住轨道 | Apple 12+ 月不给 Journal 加 AI + 差异化工作流 |
| Voice-native private journal | Platform risk | 同平台风险 | 监管利基 + 契约式隐私 |
| AI personalized pet videos | Retention | 一次性新奇, LTV $5 | 每月宠物健康用例 + 自有发行 |

---

## Verdict on the Pipeline / The Honest Question

**92% 杀光率意味着什么?** 三条可能解释:

1. **2026 年消费者 AI 没有蓝海了** — **不成立**。DEPTH 找到了 5 个真实、有引语、有数据支撑的痛点,其中晚餐决策强度 8/10。痛点是真实的。
2. **约束条件在杀人** — **这是主因**。逐个看 11 个被杀: 要么被**融资巨头占位**(Character.AI、ChatGPT voice、Rocket Money、Apple Journal),要么被**平台政策封死**(Gmail API、OS 沙箱、Apple 轨道、Meta 封 WhatsApp bot),要么死于**发行依赖**(你无受众)。HORIZON 的 9 个窗口里 5 个标 `golden`——但"窗口"是给有渠道的人看的。对"单人 + 无受众 + 15h/周 + <$50/月"来说,每个 golden 窗口的**进场费都是受众**,而这正是你唯一没有的资产。
3. **CRAFT 过于保守** — 部分成立但不该被推翻。92% 里只有 1-2 个(dinner、subs)属于"条件可复活"而非"确实该死",说明 kill rate 大致合理。它给每个 killed 方向都写了 revive 条件,这比一杀了之更有用。

**建议: 走 (a),同时内置一半的 (c)。**

- **(a) Plant care 验证先行**: 唯一"下周就能测、失败只要 20 小时"的路径,也是唯一不需要任何前置资产就能跑的实验。用 2 周落地页 + 预收单完成 Go/No-Go。
- **在 #1 的验证窗口内并行做 #2 的受众冷启动测试**(r/cooking 3 帖 + 5 条短内容)——成本近乎为零,却能把"是否需要换路线"的信息提前拿到。
- **(c) 战略真相,现在就该接受**: 本报告最硬的一条证据是——**你的杀手不是技术也不是创意,是发行**。2026 年每个可见窗口都被融资方或新进入者占据,对无受众的 solo dev 而言,最可复制的"护城河"是**一个你养出来的小受众**。所以无论选哪条路线,把"每周 2-3 小时内容"写进你的常规预算。这不会立刻解决 2026 的竞争,但它会把下一个 SELECTOR 报告的排名顺序从"可执行性优先"改回"需求强度优先"——那时 #2 晚餐决策就是 #1。

**一句话总结**: 先花 2 周、20 小时验证植物应用(失败也便宜);同时用零成本测晚餐受众的冷启动信号;然后把"养受众"这件事从可选项升级为必做项——因为杀掉 92% 候选的不是市场,是你的约束。

---

## Raw Data Appendix

<details><summary>HORIZON — All Windows</summary>

```json
{
  "windows": [
    {"name": "LLM price war", "label": "golden", "evidence": "GPT-5.6 Luna -80%; Gemini 3.7 Flash $0.75/$3.75; ~1000-2000 LLM sessions per $1"},
    {"name": "Realtime voice / speech-to-speech", "label": "golden", "evidence": "GPT-Realtime-2 May 2026; $0.017-0.034/min; voice = highest-retention modality"},
    {"name": "Companion app vulnerability", "label": "golden", "evidence": "Character.AI free-tier backlash (8 Reddit threads >2000 upvotes); Replika 2.0 lobotomized backlash; category spend $328M H1 2026 (+30% QoQ); caveat: regulatory risk"},
    {"name": "On-device AI", "label": "golden", "evidence": "Apple Private Cloud Compute free (<2M downloads); Core AI for open models on-device (AFM 3 20B); Android AICore + Gemma 4; iOS 27/macOS 27 only"},
    {"name": "AI video cheap", "label": "golden", "evidence": "Veo 3.1 Lite $0.03-0.05/sec, $0.25-0.60 per 5-sec clip; Sora API shuts down Sep 24 2026"},
    {"name": "FLUX.2 cheap image editing", "label": "golden", "evidence": "4B Apache-2.0; ~$0.014-0.03/image; sub-0.5s; editing is first-class cheap API"},
    {"name": "AI music API", "label": "early", "evidence": "MiniMax Music 3.0 $0.15/5-min track; Suno exploring API; ElevenLabs Music API; personalized songs"},
    {"name": "Messaging-native AI agents", "label": "early_golden", "evidence": "Poke $300M valuation, text-your-AI-friend, 10K->100K users in 3 days on a Reddit post; Telegram Bot API 10.1"},
    {"name": "Tiny on-device agentic models", "label": "early", "evidence": "Cactus Needle 2 (45M params, 500-1500 tok/s on RPi); high risk"}
  ]
}
```
</details>

<details><summary>DEPTH — All Pain Points</summary>

```json
{
  "pains": [
    {
      "name": "Dinner decision fatigue", "frequency": "daily", "intensity": 8,
      "evidence": "5pm decision paralysis -> takeout; 60% Millennials/Gen Z solely responsible for meal planning; 26% report stress; $60-100/wk HelloFresh; existing apps are recipe managers NOT decision eliminators; supply 5/10",
      "quote": "\"Feels like every single day around 5pm my brain has to solve this puzzle... Ended up ordering takeout for the third time this week\" (r/self, 2026-02)"
    },
    {
      "name": "Forgotten subscriptions", "frequency": "monthly", "intensity": 6,
      "evidence": "$133/mo avg in subs, underestimates 2.5x; Rocket Money $100M+ revenue requires bank login (trust barrier); manual trackers don't discover anything; gap = find forgotten subs WITHOUT bank login; supply 5/10"
    },
    {
      "name": "Plant care reminders", "frequency": "weekly", "intensity": 5,
      "evidence": "Planta/Greg/PictureThis paywall basics £35-70/yr, broken reminders, static schedules overwater plants; 7,585 review analysis shows same complaints; millions pay despite complaints; supply 3/10 (weakest)",
      "quotes": [
        "\"£70 a year just to be reminded to water my pothos. Are you kidding me?\" (App Store review, 2026-05)",
        "\"I've been reading that Planta is not so good about reminding you to water your plants and can cause you to overwater them. Are there any other better apps?\" (r/houseplants)"
      ]
    },
    {
      "name": "Home maintenance tracking", "frequency": "monthly", "intensity": 6,
      "evidence": "$6 HVAC filter -> $4,000+ repair; no single source of truth for a home; flood of new entrants, NONE has traction; r/homeowners blocks self-promotion; supply 4/10",
      "quote": "\"Mostly to remember to schedule maintenance, but tracking warrantees would be helpful too.\" (r/homeowners, 2025-07)"
    },
    {
      "name": "Parental control / screen time", "frequency": "daily", "intensity": 7,
      "evidence": "Kids bypass every app in minutes; Apple Screen Time = 'confusing corporate spreadsheet'; Qustodio/Bark/OurPact rage reviews; strong demand but technically HARD (OS sandboxing); supply 3/10 but low solvability",
      "quote": "\"My son worked out the hack within minutes - he turned the WiFi off, then back on... I want my money back\" (Qustodio App Store review, 2025-09)"
    }
  ]
}
```
</details>

<details><summary>CRAFT — Full Analysis</summary>

```json
{
  "method": "12 candidates, 7 checks each, 11 killed = 92% kill rate",
  "survivor": {
    "name": "Plant care app, free basics + adaptive reminders",
    "type": "execution play", "survival_score": 5,
    "notes": "Passed all 7 checks. Eroded to ~2-3x (no clean 10x) on Ten-X. Distribution only marginal. 'Crowded land-grab, not a blue ocean'.",
    "competitors": ["Greenroot (one-time £14.99, solo dev pre-ordering)", "Sprout (free, on-device, Feb 2026)", "Frond (free, on-device, June 2026)", "Lily ($2.99/mo, 4.8★)", "Growli ($44.99/yr)", "Sprig ($24.99/yr)"],
    "risk": "'free plant care' wedge occupied by 3+ fresh 2026 entrants",
    "validation": "pre-order landing page (Greenroot model) + Reddit posts in r/houseplants + DM 20 plant owners"
  },
  "killed": [
    {"direction": "AI dinner decision-maker", "failed_check": "Distribution", "revive": "build food content audience first, or ship chat-native with proprietary data moat"},
    {"direction": "Forgotten-subscription finder", "failed_check": "Technical feasibility (Gmail API verification)", "revive": "Gmail API scope becomes accessible + become ongoing monitor service"},
    {"direction": "Home maintenance tracker", "failed_check": "Retention", "revive": "bot texts the user (no app to open) + owns homeowners audience"},
    {"direction": "Parental control layer", "failed_check": "Technical feasibility (OS sandboxing)", "revive": "Apple opens Screen Time API (unlikely) or Android + router filtering (too big)"},
    {"direction": "Voice-native companion", "failed_check": "Platform/regulatory risk", "revive": "compliant adults-only niche (seniors companionship, grief support) with strict guardrails"},
    {"direction": "Voice dinner coach", "failed_check": "Platform risk (ChatGPT voice)", "revive": "unique hardware/context or owned cooking audience"},
    {"direction": "Personalized AI music", "failed_check": "Retention (one-time gift, LTV $3-5)", "revive": "recurring subscription bundle or owned viral TikTok template"},
    {"direction": "WhatsApp/Telegram AI agent", "failed_check": "Platform risk (Poke acquired by Cognition, Apple Messages for Business, Meta barred WhatsApp chatbots)", "revive": "hyper-specific vertical with stored-data switching costs on Telegram"},
    {"direction": "On-device private journaling", "failed_check": "Platform risk (Apple Journal owns rails)", "revive": "Apple leaves Journal without AI for 12+ months + differentiated workflow"},
    {"direction": "Voice-native private journal", "failed_check": "Platform risk", "revive": "regulated niche with contractual privacy"},
    {"direction": "AI personalized pet videos", "failed_check": "Retention (one-time novelty, LTV $5)", "revive": "recurring monthly pet-wellness use case with owned distribution"}
  ],
  "final_assessment": "Given the evidence, near-total kill is warranted... the 2026 consumer market is uniquely hostile — every timing window is owned or contested by a funded giant or a flood of fresh entrants. If the user wants to build regardless, the plant-care play is the only defensible bet and should be validated with a pre-order page before any code."
}
```
</details>

---

*Generated by Product Select v1.0 · 2026-08-19*
*This is a telescope, not a steering wheel. Read the failure modes before deciding.*