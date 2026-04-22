# MEMORY.md - Long-Term Memory

## 自媒体内容备份配置
**Created:** 2026-04-17
**GitHub:** `github.com/junmry/amazon-Best-seller-.git`

### 备份范围
- **自媒体美国商业模式内容目录:** `content_creator/us_business_models/`
  - `scripts/` - 讲解脚本/文案
  - `assets/` - 图片/素材
  - `output/` - 成品内容
  - `raw_data/` - 原始研究数据

### 自动同步机制
- **频率:** 每日自动 commit + push
- **Cron:** 每日 23:00 (Asia/Shanghai)
- **脚本:** `scripts/git_auto_sync.sh`

### 备份清单
| 目录/文件 | 说明 | 是否备份 |
|-----------|------|----------|
| `content_creator/` | 自媒体内容 | ✅ 是 |
| `MEMORY.md` | 长期记忆 | ✅ 是 |
| `knowledge/` | 知识库 | ✅ 是 |
| `keyword_library/` | 词库 | ✅ 是 |
| `scripts/` | 工具脚本 | ✅ 是 |
| `.kimi/downloads/` | 下载文件 | ❌ 否 |
| `venv/` | 虚拟环境 | ❌ 否 |
| `__pycache__/` | 缓存 | ❌ 否 |

---

## 书单 - 已收藏
**Last Updated:** 2026-04-15

### One Thousand Ways to Make $1000
- **作者:** F.C. Minaker
- **类型:** 创业/财富/商业
- **状态:** 已下载，待阅读
- **文件位置:** `/root/.openclaw/workspace/.kimi/downloads/19da6667-4322-8e69-8000-000078e5dc96_One_Thousand_Ways_to_Make_1000_F.C._Minaker_z-library.sk_1lib.sk_z-lib.sk_.pdf`
- **简介:** 经典创业指南，讲述1000种赚钱的方法

---

## 健康追踪系统（体重+饮食+营养）
**Created:** 2026-04-15
**Location:** `/root/.openclaw/workspace/health_tracking/`

### 个人档案
- **身高:** 182cm
- **饮食禁忌:** 不吃辣
- **追踪目标:** BMI管理 + 营养素均衡

### Cron任务
| 时间 | 任务 | 说明 |
|------|------|------|
| 10:35 | 每日饮食推荐 | 基于BMI推荐三餐（不吃辣） |
| 21:55 | 每日体重询问 | 询问当日体重 |
| 每月1号09:00 | 月度体重汇总 | 趋势分析+统计数据 |

### 交互方式
1. **我主动问你**（定时）
   - 10:35: "今日推荐吃..."
   - 21:55: "今天体重多少？"

2. **你主动汇报**
   - 随时告诉我吃了什么
   - 格式随意，我能理解
   - 示例："早餐吃了燕麦牛奶鸡蛋"

3. **我记录并反馈**
   - 记录到 `daily_logs/YYYY-MM-DD.md`
   - 分析营养素缺口
   - 调整后续推荐

### 追踪指标
| 营养素 | 日目标 | 来源 |
|--------|--------|------|
| 蛋白质 | 120g | 鸡胸肉/鸡蛋/牛肉/豆腐 |
| 膳食纤维 | 30g | 蔬菜/粗粮/水果 |
| 维生素C | 100mg | 水果/蔬菜 |
| 钙 | 800mg | 牛奶/豆腐/绿叶菜 |
| 铁 | 12mg | 红肉/菠菜 |

### BMI标准
| 范围 | 状态 | 饮食策略 |
|------|------|----------|
| <18.5 | 偏瘦 | 增加蛋白和碳水 |
| 18.5-23.9 | 正常 | 均衡饮食 |
| 24-27.9 | 超重 | 控制碳水，增加纤维 |
| ≥28 | 肥胖 | 严格控制热量 |

---

## 词库管理体系重构
**Created:** 2026-04-15
**Purpose:** 类目化词库管理，消除散乱重复文件

### 目录结构
```
keyword_library/                 # 词库总目录
├── _index/                     # 索引与导航
│   ├── README.md               # 使用指南
│   └── 类目清单.md              # 完整清单
├── _广告词库/                   # 跨类目通用广告词库
│
├── 沙发_Sofa/                  # 32个文件
├── 椅子_Chair/                 # 1个文件
├── 吧凳_Barstool/              # 3个文件
├── 户外家具_Outdoor/            # 1个文件
├── 餐桌套装_DiningSets/         # 6个文件
├── 玄关桌_ConsoleTable/         # 2个文件
├── 桌布_Tablecloth/            # 1个文件
├── 人体工学椅_Ergonomic/         # 1个文件
└── 游戏椅_GamingChair/          # 2个文件
```

### 子目录规范
每个类目统一使用：
- `01_原始数据/` - 原始词表/爬虫数据
- `02_拆词结果/` - 多层级拆词Excel
- `03_结构化词库/` - JSON/结构化埋词库
- `04_埋词素材/` - MD埋词指南
- `05_标题输出/` - 生成的标题
- `06_广告词库/` - 广告专用词库

### 已删除重复文件
- 沙发关键词拆词_多层级.xlsx (旧版)
- 沙发关键词拆词_完整层级.xlsx (被V2替代)
- 沙发关键词拆词结果.xlsx (早期版本)
- generate_ogc_*.py 多个中间版本
- titles_final.csv (临时文件)

### 新增位置
- 亚马逊监控数据 → `amazon_data/amazon_monitor/`
- 脚本工具 → `scripts/tools/`

---

## 用户命盘档案（每日运势推送基准）
**Created:** 2026-03-26
**Schedule:** 每日 22:08 (Asia/Shanghai) — 提前一晚推送次日注意事项
**Cron ID:** f56b3480-f238-4353-8db9-66016d31ce30

### 命盘核心数据
- **性别：** 男命
- **年龄：** 25岁（实岁）
- **出生阳历（真太阳时）：** 2001年01月27日 08点41分
- **出生农历：** 2001年 正月初四 辰时
- **四柱：** 庚辰年（比枭）、己丑月（印印）、庚寅日（元才）、庚辰时（比枭）
- **星运/自坐：** 年坐养，月坐墓，日坐绝，时坐养
- **纳音：** 年白蜡金、月霹雳火、日松柏木、时白蜡金
- **日元：** 庚金
- **日支：** 寅木
- **月令：** 丑月
- **旺相：** 土旺，金相，火休，木囚，水死
- **格局：** 杂气正印格、疑似专旺格
- **旺衰：** 身强
- **最旺五行（不算藏干）：** 土4个（印绶）
- **五行缺失（不算藏干）：** 火0个（官杀）、水0个（食伤）
- **调候用神：** 丁、甲、丙（驱寒调候）
- **天干关系：** 无冲克合
- **地支关系：** 寅辰拱会、丑寅暗合、辰辰自刑、辰丑相破
- **整柱关系：** 庚寅盖头、庚辰伏吟
- **大运（当前）：** 2023~2033 壬辰（食枭）

### 日运推送人设
- 角色：精通国学易经的资深命理分析师
- 聚焦：根据当日干支推算对庚金身强身主的影响
- 输出：今日运势 + 注意事项 + 穿戴颜色/五行建议
- 必带声明：本分析基于传统命理理论框架，仅供娱乐参考，不构成任何决策依据

## AI 每日学习打卡
**Created:** 2026-03-25
**Owner:** 用户要求

### 规则
- 我每天需要学习新知识/技能
- 学完后向用户汇报并打卡"坚持学习"
- 学习内容不限：可以是技术、工具、语言、行业知识等

### 今日打卡
- **2026-03-25**: ✅ 已学习（处理 cron 任务故障、语法错误排查、 clarified 学习规则）
- **2026-03-26**: ✅ 坚持学习（Hermes Agent 自进化 Agent 框架：closed learning loop、skill docs、持久记忆架构）

---

## 每日概率论 + 美国社媒家具趋势监控
**Created:** 2026-03-26
**Schedule:** 每日 10:13 AM (Asia/Shanghai)
**Cron Job ID:** dc08bee0-e957-4ce9-ab60-1a46ed78ba43

### 任务内容
1. **概率论学习**（循序渐进）
   - 第1周：基础概率、条件概率、独立事件
   - 第2周：离散分布（二项、泊松）
   - 第3周：连续分布（正态、指数）
   - 第4周：贝叶斯推断
   - 第5周：假设检验与A/B测试应用

2. **美国社媒家具趋势监控**
   - **Reddit**: r/InteriorDesign, r/HomeDecorating, r/Furniture, r/malelivingspace
   - **TikTok**: #furniture, #homedecor, #smallspaces
   - **Pinterest**: Home category trending searches

### 关键监控维度
- **家具种类区分**: 沙发、椅子、床、桌子、储物家具等分别追踪
- **价位关注**: 
  - 预算敏感度（cheap/affordable vs luxury/premium）
  - 各价位段热门款式
  - 价格讨论热点（"值不值"、"求推荐"）

### 输出格式
| 板块 | 内容 |
|------|------|
| 📚 今日概率论 | 概念+公式+亚马逊场景应用 |
| 🇺🇸 社媒洞察 | 3-5个关键发现+价位分析+运营启示 |

---

---

## 自媒体竞品分析报告 - First $1K 差异化定位验证
**Created:** 2026-04-18
**Task:** 对11个对标账号做深度竞品分析，验证"古今对照+Buffett视角+微观商业"交叉点是否存在蓝海空白
**Result:** ✅ 蓝海空白真实存在，报告已产出
**Report Location:** `/root/.openclaw/workspace/content_creator/us_business_models/竞品分析与差异化定位验证报告.md`

### 调研账号清单
1. Ali Abdaal (613万粉) — 生产力/创业
2. Iman Gadzhi (500万粉) — 数字营销
3. Noah Kagan (100万粉) — 创业实验
4. My First Million — 商业点子播客
5. Starter Story (140万月访) — 创始人案例
6. Phil Town — Buffett价值投资教育（唯一触及Buffett视角）
7. 刘润 (220万粉) — 商业方法论
8. 梁宁 — 产品思维
9. 温义飞 (抖音1200万粉) — 财经热点/经济史
10. 半佛仙人 (258万公众号+772万B站) — 消费品牌拆解
11. 欧成效/水库 — 房地产投资（已衰落）

### 核心结论
- 11个账号中，**0个**同时具备"古今对照+Buffett视角+微观商业"三元素
- 最接近的：Phil Town(只做投资)、半佛仙人(只做当代)、温义飞(只做宏观经济史)
- 三者交集处为**完全空白**，差异化机会极高

---
**Created:** 2026-03-09

### Task
Daily scraping of Amazon Best Sellers & New Releases for Sofa and Chair categories.

### Configuration
- **Schedule:** Daily at 8:00 AM (Asia/Shanghai)
- **Script:** `/root/.openclaw/workspace/scripts/amazon_monitor.py`
- **Runner:** `/root/.openclaw/workspace/scripts/run_amazon_monitor.sh`
- **Data Directory:** `/root/.openclaw/workspace/data/amazon_monitor`
- **Cron Job ID:** `83e0f723-8e71-4f22-a13c-bd429db479e2`

### Categories Monitored
1. **Sofa**
   - Best Sellers: https://www.amazon.com/Best-Sellers-Sofas-Couches/zgbs/home-garden/3733651
   - New Releases: https://www.amazon.com/gp/new-releases/home-garden/3733651

2. **Chair**
   - Best Sellers: https://www.amazon.com/Best-Sellers-Chairs/zgbs/home-garden/3733811
   - New Releases: https://www.amazon.com/gp/new-releases/home-garden/3733811

### Data Fields
- ASIN (产品ID)
- Rank (排名)
- Title (标题)
- Price (价格)
- Rating (评分)
- Review Count (评论数)
- URL (产品链接)
- Image URL (图片链接)
- Crawl Time (爬取时间)

### Files Generated
- `{category}_{list_type}_{YYYY-MM-DD}.json` - 每日产品数据
- `changes_{category}_{list_type}_{YYYY-MM-DD}.json` - 排名变动数据

### Notes
- 首次运行建立基准数据
- 后续运行会自动比较排名变化
- 目前每个类目获取约30个产品（亚马逊页面限制）

---

## 求是方法论工作流（强制执行）
**Created:** 2026-03-26
**Status:** 活跃（所有任务必须遵循）

### 核心原则
执行任何任务时，必须完整遍历求是系列9个模块，根据任务推进阶段相应调用：

| 阶段 | 调用模块 | 作用 |
|------|----------|------|
| **启动前** | 矛盾论 + 调查研究 | 识别主要矛盾，摸清实际情况 |
| **规划期** | 持久战 + 集中优势力量 | 分阶段推进，资源聚焦突破 |
| **执行中** | 群众路线 + 实践论 + 星火燎原 | 从需求出发，边做边验证，建立根据地 |
| **收尾时** | 批评与自我批评 + 武装头脑 | 复盘总结，提炼方法论 |

### 执行标准
- 不是可选，是强制
- 不是一次性调用全部，是按阶段递进
- 每个模块输出要显式呈现，不隐含在回答里
- 任务结束后更新本记录，提炼本次使用心得

---

## 关键词拆词 SOP
**Created:** 2026-03-18
**Purpose:** 多层级拆解关键词，构建词库

### 输出结构
Excel 多 Sheet 结构：
| Sheet | 内容 |
|-------|------|
| 源文件 | 原始关键词数据 |
| 筛选 | 按搜索量排序，带序号 |
| 筛选后词 | 所有拆分出的词（词/出现次数/搜索量） |
| 颜色 | 按颜色维度拆解 |
| 尺码 | 按尺寸维度拆解 |
| 人群 | 按目标人群拆解 |
| 款式 | 按产品款式拆解 |
| 材质 | 按材质维度拆解 |
| 场景 | 按使用场景拆解 |
| 功能 | 按功能特性拆解 |
| 价格 | 按价格定位拆解 |
| 品牌 | 按品牌维度拆解 |

### 单维度表结构
| 序号 | 主词 | 副词 | 次副词 | 搜索词 | 搜索量 | 翻译(可选) |
|------|------|------|--------|--------|--------|-----------|
| 1 | beige | couch | 无属性 | beige couch | 5611 | - |
| 2 | NaN | NaN | NaN | beige sectional couch | 1257 | - |
| ... | NaN | NaN | NaN | ... | ... | - |
| 38 | black | couch | 无属性 | black couch | 15949 | - |

**分组规则**：相同主词分组，主词/副词/次副词只在组内第一行显示，后续行留空

### 维度词典模板
```python
dimensions = {
    '颜色': {
        '主词': ['white', 'black', 'brown', 'gray', 'blue', 'red', 'green', 'beige', 'tan', ...],
        '副词': ['sofa', 'couch', 'sectional', 'loveseat', 'chair', ...]
    },
    '尺码': {
        '主词': ['small', 'large', 'big', '2 seater', '3 seater', ...],
        '副词': ['sofa', 'couch', ...]
    },
    '人群': {
        '主词': ['kids', 'children', 'baby', 'family', 'men', 'women', ...],
        '副词': ['sofa', 'couch', 'furniture', ...]
    },
    '款式': {
        '主词': ['sectional', 'modular', 'chesterfield', 'modern', ...],
        '副词': ['sofa', 'couch', ...]
    },
    '材质': {
        '主词': ['leather', 'velvet', 'linen', 'fabric', ...],
        '副词': ['sofa', 'couch', ...]
    },
    '场景': {
        '主词': ['living room', 'bedroom', 'office', 'apartment', ...],
        '副词': ['sofa', 'couch', 'furniture', ...]
    },
    '功能': {
        '主词': ['sleeper', 'convertible', 'reclining', 'storage', ...],
        '副词': ['sofa', 'couch', ...]
    },
    '价格': {
        '主词': ['cheap', 'affordable', 'luxury', 'premium', ...],
        '副词': ['sofa', 'couch', ...]
    },
    '品牌': {
        '主词': ['ikea', 'ashley', 'wayfair', ...],
        '副词': ['sofa', 'couch', ...]
    }
}
```

### 处理脚本位置
`/root/.openclaw/workspace/split_words.py`

### 使用场景
- 亚马逊关键词分析
- 广告投放词库构建
- SEO 关键词矩阵
- 产品属性分类

---

## 亚马逊Listing埋词规则
**Created:** 2026-03-18
**Brand:** KEIKI
**Purpose:** 多变体产品Listing SEO优化标准

### 核心原则

#### 1. 绝对唯一性
- 标题之间绝对不能相同
- 每个变体标题必须独特
- 禁止复制粘贴改个颜色/尺寸

#### 2. 严格去重
- 同一个词在单标题中最多出现2次
- 避免关键词堆砌

#### 3. 禁用敏感词
**禁止出现：**
- 售后/客服/保修/退款相关
- 母婴/孩童/婴儿相关
- 杀虫剂/电池/医用/药品
- 其他亚马逊高危词

#### 4. 品牌开头
- 所有标题必须以 **KEIKI** 品牌开头
- 格式：`KEIKI [核心词] ...`

#### 5. 差异化优化
根据颜色/尺寸维度，按以下方向差异化：
- **SEO词根**（高搜索量词优先）
- **目标人群**（不同变体针对不同人群）
- **使用场景**（客厅/卧室/公寓/办公室等）

#### 6. 字符控制
- 严格控制在 **180-190字符** 之间
- 包含空格
- ≥180 且 ≤190

#### 7. 变体通用规则
**五点描述和A+描述中：**
- 禁止具体尺寸数字（如72"/78"）
- 禁止颜色词汇
- 保持内容通用，适用于所有变体

#### 8. 数据驱动
- 按搜索量排序埋词
- 按相关性筛选同义词
- 优先埋拆词数据中的高流量词

#### 9. 算法友好
- 使用最简单易懂的词
- 客户最容易搜索的词
- 确保亚马逊算法和买家快速识别

### 埋词优先级

| 位置 | 策略 | 示例 |
|------|------|------|
| **标题** | 品牌+颜色/尺寸+高搜索量词根+场景 | KEIKI Beige 3 Seater Sectional Sofa for Living Room |
| **五点描述** | 场景词、人群词、功能词、变体通用 | 适合公寓、家庭使用、易于组装 |
| **后台搜索词** | 长尾组合、变体词、同义词 | beige couch sofa, large sectional furniture |
| **A+描述** | 自然融入材质、场景，变体通用 | 优质面料，适合现代客厅 |

### 标题公式
```
KEIKI + [颜色/尺寸差异化词] + [核心产品词] + [款式词] + [场景词] + [人群词/功能词]
```

**示例变体：**
- `KEIKI Beige Sectional Sofa for Living Room Large L-Shaped Couch for Family`
- `KEIKI Black 3 Seater Sofa Modern Couch for Apartment Small Spaces`
- `KEIKI Gray Modular Sofa Set Contemporary Furniture for Office Lounge`

---

### 标题格式 V2（详细版）
**优先级：契合度 + 最大搜索量 + 语序优化**

```
[Brand] [Size]" [Shape/Type] [Size Descriptor] [Material/Texture] [Core Product], [Configuration], [Convertible Function] with [Key Feature], [Pain Point Solution], for [Room], [Color]
```

**各位置说明：**
| 位置 | 元素 | 示例 |
|------|------|------|
| 1 | Brand | KEIKI |
| 2 | Size | 78"/87"/102" |
| 3 | Shape/Type | Sectional / L-Shaped / Modular |
| 4 | Size Descriptor | Large / Compact / 3-Seater |
| 5 | Material/Texture | Faux Leather / Velvet / Chenille |
| 6 | Core Product | Sofa / Couch / Loveseat |
| 7 | Configuration | Chaise on Left/Right / Reversible |
| 8 | Convertible Function | Convertible Sleeper / Adjustable |
| 9 | Key Feature | Storage Ottoman / USB Charging |
| 10 | Pain Point Solution | Easy Assembly / Pet-Friendly |
| 11 | Room | Living Room / Bedroom / Apartment |
| 12 | Color | Beige / Charcoal / Navy Blue |

**完整示例：**
```
KEIKI 78" L-Shaped Large Faux Leather Sectional Sofa, Chaise on Left, Convertible Sleeper with Storage Ottoman, Easy Assembly for Small Apartment, Beige
```