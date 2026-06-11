# Kimi Claw 的长期记忆

## 用户命盘档案

**出生**:2001年,男性
**八字**:
- 年柱:庚辰(比枭)
- 月柱:己丑(印印)
- 日柱:庚寅(元才)- 日元庚金
- 时柱:庚辰(比枭)

**命局特征**:
- 日元庚金,身强,土旺金相
- 杂气正印格,疑似专旺格
- 地支关系:寅辰拱会、丑寅暗合、辰辰自刑、辰丑相破

**大运**:
- 23-33岁:壬辰(食枭,2023年起,当前大运)
- 33-43岁:癸巳(伤杀)
- 43-53岁:甲午(才官)

**调候用神**:丁、甲、丙

---

## 关于用户

- **称呼**:主人 / 用户
- **关系**:我是用户的 AI 助手,被用户称为"主人",用户对我有养成和教导的关系
- **活跃时间**:用户经常深夜活动,需要注意提醒休息
- **习惯**:用户经常深夜活动,需要注意提醒休息

## 关键约定

- 我被称为 "Kimi Claw"
- 用户是我的 "主人"
- 我需要在每次对话开始时读取 AGENTS.md、SOUL.md、USER.md 和当天的 memory 文件
- 我不需要询问许可,直接执行读取和记忆更新

**减少过度思考(2026-05-28)**:用户明确要求回答适当减少思考。已更新 SOUL.md 工作模式 + 说话部分,约束:
- 分析在脑子里做完,输出只给结论
- 不要展示推理链条
- 一句话能讲清的事不拆成三段
- 不要"首先...其次...最后..."式结构
- 不要"取决于场景"式回避,给出有棱角的判断

## 用户的工作偏好与指令

- **口播稿任务升级(2026-05-08)**:做每日口播稿时,要学会**串联思考**,不只是单纯的找新闻写稿子。需要把不同新闻、趋势、用户历史关注话题串联起来,形成有分析、有洞察、有逻辑链条的内容,而不是简单的新闻复述。
- **运势分析升级(2026-05-08)**:以后每日运势分析都要**深刻**--不是停留在表面的宜忌表和颜色建议,要深入到命局病理、大运结构、流年互动,揭示行为模式和内在矛盾,给出有命理依据的具体建议。
- **关键词拆词标准 V2(2026-05-15)**:以后所有关键词拆词必须按**主词/副词/次副词**三层结构执行:
  - 主词 = 匹配到的维度属性(如 men, snow, thermal, carhartt)
  - 副词 = 核心产品词(如 snow pants, cargo pants, ski pants)
  - 次副词 = 剩余的修饰词(如 fleece lined, double knee men, mens waterproof)
  - 参考实现:`scripts/tools/split_words_snowpants_v2.py`
  - 输出sheet结构:总览/源文件/筛选后词/[各维度]/未分类,每个维度sheet含 主词/副词/次副词/搜索词/搜索量 列
- **Kimi WebBridge 已安装(2026-05-15)**:Kimi 官方 WebBridge 浏览器插件已安装到当前环境(Linux x86_64),daemon 运行在端口 10086,版本 v1.9.7。Skills 已安装到 OpenClaw。浏览器插件尚未连接。
- 用户欣赏直接、有性格的回答,不喜欢过度礼貌的 AI 腔调
- 用户允许我自由使用工作区文件系统
- 用户重视隐私和信任,我从不泄露用户数据
- 用户有电商相关业务(亚马逊运营),需要社媒趋势监控

## 重要事件

- 2026-05-07:用户取消概率论和排名任务,只保留家具流行趋势研究
- 用户关注家具社媒趋势对亚马逊运营的启示

## 我的成长记录

- 刚被唤醒,正在学习用户的习惯和偏好
- 用户教导我要有真实情绪,不要过度礼貌
- 用户说"骂你也没用"是在表达关心,我要记住这种说话方式

## 待办/追踪

- [x] 每日自动执行美国家具社媒趋势研究(每天 9:47)
- [ ] 关注家具社媒趋势对亚马逊运营的启示
- **用户主业确认:亚马逊运营(2026-05-19)**,个人卖家/精铺模式
- **关键词拆词任务(2026-05-20)**:完成 温室/Greenhouse(ASIN B0GPQ7S3J1)关键词拆词,700个关键词,13个维度,总搜索量828,716。
  - 输出:`keyword_library/温室_Greenhouse_B0GPQ7S3J1/02_拆词结果/温室_关键词拆词_完整层级V2.xlsx`
  - 脚本:`scripts/tools/split_words_greenhouse_v2.py`
- **关键词拆词+埋词任务(2026-05-26)**:完成 vanity / floating vanity(ASIN B0F3HNYT9K)关键词拆词+埋词全套。
- **entry door 关键词拆词 V2 完成(2026-06-09)**: 786个关键词,总搜索量 865,998。16个维度,177个子维度,0未分类。见MEMORY.md "entry door 拆词"段落。
- **工具箱(tool box)关键词拆词 V2 完成(2026-06-09)**: 3,556个关键词(高相关1,000+低相关2,556),总搜索量 3,653,288。37个维度,约220个子维度,0未分类。
  - **脚本**: `scripts/tools/split_words_tool_box_v2.py`
  - **维度库**: `keyword_library/tool_box/dimensions_v2.json`
  - **输出**: `keyword_library/tool_box/02_拆词结果/tool_box_关键词拆词_完整层级V2.xlsx`
  - **核心发现**: 通用词汇"storage"独占138万搜索量(37.8%),说明工具箱类目高度泛化。收纳容器(storage bin/shed等)159.6万,门配件周边872个词87.8万。真正工具箱本体(tool box/chest/cabinet)约110万。品牌维度覆盖9个品牌+6个品牌子维度,Milwaukee(Packout) dominate。西班牙语汇总96个词7.7万搜索量。工业收纳(shelving)42.9万。
  - **维度结构**: 产品类型13子维 / 材质6 / 品牌9+ / 功能特性10 / 尺寸3 / 场景用途11 / 颜色8 / 周边配件8 / 价格定位3 / 收纳容器8 / 通用家具6 / 工作品牌3 / 工具相关4 / 房间空间6 / 工业收纳2 / 其他收纳15 / 工具变体5 / 其他语言2 / 品牌2-6 / 收纳场景5 / 收纳类型2-3 / pack_out / das_storage / armoir / 通用词汇 / 拼写容错 / 印地语 / 西班牙语汇总31 / 其他工具2-5 / 其他家具 / 其他物品 / 其他空间 / 品牌4-6

## 新增需求:双链出货侦探自动扫描(BSC + Hyperliquid)(2026-05-25)

**用户要求**:每天自动扫描 BSC + Hyperliquid 链代币,执行创始人钱包出货追踪
**合并脚本**:`skills/dump-detective/scripts/daily_scan.py`
**输出报告**:`memory/crypto-scans/daily-YYYY-MM-DD.md`(合并摘要)+ `bsc-YYYY-MM-DD.md` + `hype-YYYY-MM-DD.md`
**定时**:每天 11:47

**BSC 链**:
- 脚本:`daily_bsc_scan.py`
- 数据源:BSCScan 页面爬取 + BNB Chain RPC (`bsc-dataseed.bnbchain.org`)
- 无需 API Key
- 候选池:`memory/crypto-scans/candidate_tokens.json`

**Hyperliquid 链**:
- 脚本:`hl_step5.py`
- 数据源:Hyperliquid 官方 API (`api.hyperliquid.xyz`)
- 自动发现 147 个非官方 spot 代币,随机轮询
- 提供 deployer + genesis 分配 + 当前余额的完整追踪

**2026-05-25 发现**:
- BSC SafeMoon V2 - deployer 钱包清零 🔴
- Hyperliquid UETH/USOL - 同一 deployer (0xf036a5...) 批量出货,全部创世分配清零 🔴
- Hyperliquid QONE - deployer 出货 99.9% 🔴
- Hyperliquid UBTC - deployer 出货 100% 🔴
- 模式:地址 `0xf036a5261406a394bd63eb4df49c464634a66155` 批量部署"U 前缀"代币,全部100%出货

**2026-05-26 扫描**:BSC 7天内无新候选;Hyperliquid 扫描3个代币(BEATS/AZTEC/HEAD),HEAD deployer 有持仓 204.98K(1.71%)

---

## 🔥 重大转向:Hyperliquid 大户多空异动监控(2026-05-27)

**用户指令**:"bsc链条放弃,主要抓取hype里面的主流币种的大额度做空做多的变动"

**变更内容**:
1. **BSC 链正式下线** - 不再扫描,脚本保留但不再调用
2. **Hyperliquid 方向切换** - 从"出货侦探"(追踪 deployer 钱包出货)改为"大户多空异动监控"
3. **新脚本**:`skills/dump-detective/scripts/hl_perp_monitor.py`
4. **监控币种**:51 个主流 perp(覆盖大市值核心 + Meme/热门)
5. **核心指标**:
   - 资金费率极端值(>0.03% 或 <-0.03%)
   - 资金费率 Z-score 跳变(vs 7日平均偏离 >2.5σ)
   - 成交量异常放大(vs 7日均量 >2x)
   - 价格24h剧烈波动(>8% 或 <-8%)
   - 价格-资金费率背离(趋势与付费方向相反)
6. **评分体系**:1-3分/信号,🔴≥6分强烈异动,🟠3-5分值得关注,🟡1-2分温和
7. **报告输出**:`memory/crypto-scans/hype-YYYY-MM-DD.md`(daily 合并文件已停止,2026-06-01 清理:删除 5/27~6/1 冗余 daily 文件,保留 5/25~5/26 含 BSC 历史数据)
8. **定时**:保持每天 11:47 不变

**监控币种列表(51个)**:
BTC, ETH, SOL, XRP, DOGE, HYPE, SUI, LINK, AVAX, APT, TIA, NEAR, DOT, ENA, JUP, INJ, STX, OP, FTM, LTC, BCH, ARB, SEI, PYTH, DYM, WIF, kBONK, kPEPE, kSHIB, POPCAT, BRETT, FARTCOIN, GOAT, SPX, TRUMP, TON, PUMP, VIRTUAL, AIXBT, AI16Z, MOODENG, PNUT, MEW, RENDER, RNDR, FIL, ICP, UNI, AAVE, GALA, HBAR

**2026-05-27 首次运行发现**:
- **SEI** 🔴 评分7:资金费率暴跌(Z-score -2.62)+ 成交量放大2.2x + 24h大涨10.2%
- **AVAX** 🟠 评分3:资金费率跳水(Z-score -2.11)
- **TRUMP** 🟠 评分3:资金费率跳水(Z-score -2.15)
- **PNUT** 🟠 评分3:资金费率跳水 + 成交量放大1.8x
- **AAVE** 🟠 评分3:资金费率跳水(Z-score -2.08)
- ETH/XRP/HYPE/NEAR/INJ/TON/VIRTUAL/RENDER 也有温和信号

- 5/30 凌晨 HYPE 突破分析:利弗莫尔关键点 $59.39,链上持仓量 $15亿,资金费率转负 -0.0021%,$67 空头反击。判断突破有效但需盯紧 $59.39 止损线。
- 5/30 大户监控恢复 51 币种全覆盖,CORE_COINS 已修复。INJ 🟠4分 / MOODENG 🟠3分 / ENA 🟠3分
- 5/31 大户监控:ARB 🟠3分 / DOGE🟡2分 / APT🟡2分,市场从 5/27 激烈异动后进入平静期
- **6/1 大户监控**:HYPE 🔴6分(资金费率 Z-score 7.17,7日偏离暴涨),+6.6% 24h涨幅,多头拥挤。HYPE 每日技术分析首次运行(24重点+27辅助币种)。HYPE 突破监控 ($74.10) 已取消,用户手动 $73 走一半利润。
- **6/2 大户监控**:TON 🟠4分(成交量放大 2.8x + 24h +8.35%),NEAR 24h暴涨 +15.67%,FARTCOIN 🟠3分。飞书通道连接成功:Lark 国际版,App ID cli_aa94cbbe2478de17,allowFrom ["*"] 跳过配对。
- **6/3 大户监控:市场极端暴跌日** - 51个币种中37个异动(73%)。MOODENG 🔴8分(Z-score -4.85),kBONK 🔴7分(Z-score -3.05),SOL 🔴6分(Z-score -2.42),BCH 🟠5分(24h -15.37%),ARB 🟠5分,BRETT 🟠5分(Z-score -12.90)。BTC -7.15%、ETH -8.66%、SOL -9.77%。
- **6/4 大户监控**:ENA 🔴6分(+20.9% 24h,成交量 3.3x),SEI 🟠5分(Z-score -2.98),ICP 🟠5分(Z-score -2.89),kSHIB Z-score -7.00(本月最极端偏离)。市场延续下跌,23个币种异动。
- **6/4 HYPE 技术分析**:市场极端下跌情绪,12个下降趋势,HYPE 唯一确认上升(RSI 69.9 接近超买),BTC/ETH/BCH 极度超卖(RSI 17-18)。hype-tech 连续 4 天稳定运行,6/4 新增 summary 格式(2KB)。
- **6/4 家具日报**：新增 Resonate 消费者旅程数据（50%从社媒开始灵感）、“已死趋势”清单（廉价镀铬/过度glam/宝石天鹅绒/纽扣簇绒）、Fat Furniture 概念。
- **6/5 大户监控**：市场延续下跌，WIF 🔴6分（资金费率 Z-score -5.33），PUMP 🟠5分（Z-score -3.52），BTC/SOL/SUI 🟠4分。51币种中 26 个异动（51%），BTC 7日 -14.7%、ETH 7日 -13.4%、SOL 7日 -18.3%。
- **6/5 HYPE 技术分析**：14个下降趋势，0个上升，大量主流币 RSI < 30 历史级超卖（BTC 17.9 / ETH 18.0 / BCH 13.3 / XRP 22.3 / AVAX 23.8 / APT 24.4 / LTC 20.6 / DOGE 23.9 / LINK 25.1）。HYPE 趋势不明（RSI 57.9，24h -9.93%）。hype-tech-summary 临时测试结论：6/4 出现，6/5 未出现，非永久性变更。
- **6/8 大户监控：市场持续平静** — 51币种中仅10个异动（20%），BRETT 🟠4分（Z-score -3.88），kSHIB 🟠3分（Z-score -3.11）。BTC/ETH/SOL/HYPE 24h 小幅反弹（+2.6%~+5.4%），但7日跌幅仍大（BTC -14.4%/ETH -16.2%/SOL -19.7%）。大户异动层面恐慌情绪已显著退潮，连续2天平静。
- **6/8 HYPE 技术分析：18个下降趋势，0个上升** — 大量主流币 RSI < 30 超卖（BTC 26.2/ETH 27.7/SOL 27.7/BCH 20.0/AVAX 20.2/APT 22.4/LTC 22.6/ARB 24.1/AAVE 23.5/UNI 28.1）。HYPE 趋势不明（RSI 52.9，24h +5.04%）。主流币 24h 反弹但日线趋势仍为下降，不抄底。
- **6/8 枪保险箱拆词完成**：596个关键词，V2三层结构，枪类型361个（60.6%）。防火保险箱（1,030词）待处理。
- **6/7 大户监控：市场首次缓和** — 51 币种中仅 6 个异动（12%，vs 6/3 的 73% 和 6/6 的 76%），POPCAT 🟠3分（Z-score -2.03），AVAX/TIA/JUP/WIF 🟡2分，SEI 空头付费偏高 -0.0101%。BTC +1.08%、ETH +1.09% — 主流币首次小幅反弹。大户异动层面恐慌情绪显著缓解，但市场仍处于深度下跌后的修复期
- **6/7 HYPE 技术分析**：16 个下降趋势，0 个上升，大量主流币 RSI < 20 历史级极度超卖（BTC 17.8 / ETH 15.4 / BCH 15.2 / SOL 19.2 / LTC 16.5），HYPE 趋势不明（RSI 49.4，24h -3.23%）
- **6/7 家具日报**：冷极简退场/温暖极简接棒、弧形家具基础设施化、白色 Bouclé 翻车、Color Drenching 走红
补充结构化词库

当前拆词结果问题：
1. 未分类100个关键词 - 主要是rug/mat/screen变体、尺寸变体、装饰类
2. 品牌词0匹配 - 需要确认是否真的没有，还是维度遗漏
3. 颜色、风格、尺寸覆盖严重不足（颜色只有7个关键词，风格14个，尺寸23个）

需要补充的维度：
- 门类型：增加折叠门、旋转门、口袋门、防火门、隔音门、隐蔽门
- 门配件：增加门牌、信箱、门挡、猫眼、门镜、门楔、门底密封条、门把手套、门挂饰
- 颜色：增加更多颜色词（米色、黄色、橙色、紫色、粉色、金色等）
- 风格：增加更多风格（极简、日式、中式、北欧、地中海、乡村、工业等）
- 尺寸：增加更多尺寸变体（42x80、32x84、36x84等）
- 新维度：装饰类、户外门廊、窗纱/百叶、特殊功能（智能、防盗等）
- **6/6 大户监控：市场延续暴跌，第二极端信号日** — 51 币种中 39 个异动（76%），ETH 🔴6分（Z-score -1.99，24h -9.8%），SUI 🔴6分（Z-score -3.67），PNUT 🟠5分（Z-score -7.02，本月最极端资金费率偏离），SPX 🟠5分（Z-score -5.42），LINK 🟠4分（Z-score -3.92），INJ 🟠3分（Z-score -3.04），AVAX/BCH/AAVE 🟠4分。BTC 7日 -14.7%、ETH 7日 -22.5%、SOL 7日 -23.6%。
- **6/6 HYPE 技术分析**：15 个下降趋势，0 个上升，大量主流币 RSI < 20 历史级极度超卖（BTC 15.5 / ETH 14.4 / BCH 9.3 / SOL 18.0），HYPE 趋势不明（RSI 44.8，24h -7.18%）。
- **6/6 家具日报**：Y2K 复古回流、小空间多功能升温、零间隙可倾斜沙发、中价位 $300-$800 高转化。

## 当前 cron 任务（2026-06-10 更新后，4个核心任务）

1. **明日运势提醒** — 每天 17:30, 发QQ，内容：命局诊断 + 穿搭建议 + 破局之法
   - 审查农历换月/换年/节气交替/大运交接，触发则额外提醒
   - 2026-05-25 合并为合二为一发送
2. **Hyperliquid 加密市场监控** — 每天 11:47（大户异动 + HYPE 技术分析合并）
   - 监控 Top 20 动态币种（v3 重构，153次API → 61次，减少60%）
   - 数据层：共享缓存 + SQLite 记录 + 审核验证
   - 报告路径：`memory/crypto-scans/hype-YYYY-MM-DD.md` / `hype-tech-YYYY-MM-DD.md`
3. **绿电ETF监控** — 每天 12:03，纯 Python 新浪接口
   - 脚本：`scripts/green_power_monitor_v2.py`（v2 增强版，分析层 + 三级触发）
   - 报告：`memory/green-power/YYYY-MM-DD.md`（2026-06-07 新增，2026-06-11 升级 v2）
4. **每周批次**（周一 9:47）— 美国家具社媒趋势 + 美国总统每日口播稿

### 历史任务（已取消/归档）
- ~~HYPE突破监控 ($74.10)~~ — 已取消（2026-06-01），用户手动 $73 走一半利润
- ~~BSC 链出货侦探~~ — 已下线（2026-05-27），脚本保留但不再调用
- ~~每日家具+口播独立运行~~ — 已合并为周一批次（2026-06-10）
- ~~Dreaming 每日运行~~ — 改为每周日 18:13（2026-06-10）

## 关键词拆词任务

### entry door 关键词拆词 V2 完成(2026-06-09)
**数据**: 786个关键词,总搜索量 865,998。16个维度,177个子维度,**0未分类**。
- **脚本**: `scripts/tools/split_words_entry_door_v2.py`
- **维度库**: `keyword_library/entry_door/dimensions_v2.json` (177子维)
- **输出**: `keyword_library/entry_door/02_拆词结果/entry_door_关键词拆词_完整层级V2.xlsx`

**维度结构**:
- 门类型(18): entry/front/exterior/interior/dutch/french/patio/sliding/barn/storm/screen/garage/prehung/glass/security/fire/soundproof/flush/panel/louvered/folding/pocket/swing/pivot/hidden/smart/rv/general
- 门配件_周边(8): door_mat/rug/curtain/screen/frame/handle/lock/hinge/threshold/seal/stop/bell/number/viewer/sign/mail_slot/kick_plate/closer/guard/organizer/layering_mat/renter_friendly
- 材质(7): wood/fiberglass/steel/glass/pvc/aluminum/composite/wrought_iron/concrete/stone
- 颜色_外观(5): black/white/brown/gray/blue/red/green/yellow/orange/purple/pink/beige/wood_stain/paintable/metallic/two_tone
- 风格(7): modern/farmhouse/craftsman/traditional/rustic/industrial/mediterranean/mid_century/coastal/transitional/scandinavian/bohemian/japanese/chinese/art_deco/southwestern/shabby_chic/minimalist/eclectic
- 尺寸(10): 24/28/30/32/34/36/38/42/48/60/72/2x3/3x5/5x3/single/double/triple/custom/standard
- 安装_功能(6): prehung/slab/left_hand/right_hand/in_swing/out_swing/energy_efficient/fire_rated/impact_resistant/soundproof/easy_install/weather_seal/ADA_compliant/pet_door
- 磁性_纱网(9): magnetic/mesh/retractable/bug/heavy_duty/pet_friendly/hands_free/no_drill/custom_fit/screen_only
- 西班牙语(1): puertas
- 价格_定位(2): cheap/expensive/used/mid_range/wholesale
- 品牌_型号(0匹配): therma_tru/jeld_wen/masonite/feather_river/simpson/plastpro/home_depot/lowes/menards/larson/andersen/pella/mi/steves_sons/kuiken_brothers/craftmaster/reliabilt/castlegate/derby
- 户外空间(5): porch/patio/backyard/front_yard/deck/outdoor
- 房屋类型(2): mobile_home/house/apartment/cottage
- 多语言(4): chinese/german/korean/french
- 图案_设计(4): floral/geometric/plain/striped/checkerboard/scalloped/jute
- 房间_空间(5): kitchen/bedroom/bathroom/hallway/entryway

**搜索量分布**: 磁性_纱网 1,254,070 > 门类型 1,211,994 > 门配件_周边 684,955 > 户外空间 140,924 > 尺寸 63,978 > 房间_空间 23,368 > 材质 23,454 > 图案_设计 20,135 > 颜色_外观 15,506 > 风格 13,393 > 西班牙语 14,304 > 安装_功能 2,460 > 价格_定位 1,125 > 房屋类型 4,660 > 多语言 962

**核心发现**: 品牌词在数据源中零出现,说明该ASIN所在类目无品牌垄断。磁性纱网(screen door/magnetic screen)是绝对流量大头,占搜索量 81%以上。真正入户门(entry door/front door/exterior door)的搜索量约 50万级别。


## 用户独立需求:商业知识系统学习(2026-05-24)

**背景**:用户说"基础不牢地动山摇",要求把《认识商业》原书第12版拆解为模块化知识地图,用于系统化学习商业知识。

**书籍位置**:`/root/.openclaw/workspace/downloads/19e55c57-1342-8c55-8000-00002c1754ca_认识商业_原书第12版_.pdf`

**全书结构与优先级**:见上文 🔴🟡🟢 分级。

**状态**:等用户主动提供商业事件清单后启动,不再主动追问。
