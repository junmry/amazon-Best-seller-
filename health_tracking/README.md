# 体重和营养追踪系统

## 目录结构
```
health_tracking/
├── profile.json              # 个人档案（身高182cm、饮食禁忌等）
├── nutrition_db.md           # 食物营养数据库 + 推荐食谱
├── weight/
│   ├── current.csv           # 当月体重记录
│   └── YYYY-MM.csv           # 历史月度记录
├── nutrition/
│   └── YYYY-MM-DD.json       # 每日营养摄入记录
├── daily_logs/
│   └── YYYY-MM-DD.md         # 每日饮食汇报日志
└── scripts/
    ├── daily_weight_reminder.sh      # 21:55体重提醒
    ├── daily_meal_recommendation.sh  # 10:35饮食推荐
    └── monthly_weight_summary.sh     # 每月1号体重汇总
```

## 使用流程

### 1. 体重记录（每天21:55）
- 我主动问你："今天体重多少？"
- 你回复数字（如：75.5）
- 我记录到 `weight/current.csv`

### 2. 饮食推荐（每天10:35）
- 基于：身高182cm + 昨日体重 → 计算BMI
- 结合：营养素缺口分析
- 输出：早/午/晚三餐推荐（不吃辣）

### 3. 饮食汇报（用户主动）
- 你随时告诉我吃了什么
- 格式："早餐：燕麦+鸡蛋+牛奶"
- 我记录并分析营养素摄入

### 4. 营养分析
追踪指标：
| 营养素 | 日目标 | 状态 |
|--------|--------|------|
| 蛋白质 | 120g | 正常/不足/过量 |
| 膳食纤维 | 30g | 正常/不足 |
| 维生素C | 100mg | 正常/不足 |
| 钙 | 800mg | 正常/不足 |
| 铁 | 12mg | 正常/不足 |

### 5. 月度汇总（每月1号09:00）
- 上月体重趋势图
- 平均/最高/最低体重
- 月度变化量
- 饮食营养达标率

## BMI参考标准
| BMI范围 | 状态 | 饮食建议 |
|---------|------|----------|
| <18.5 | 偏瘦 | 增加蛋白质和碳水 |
| 18.5-23.9 | 正常 | 均衡饮食 |
| 24-27.9 | 超重 | 控制碳水、增加纤维 |
| ≥28 | 肥胖 | 严格控制热量 |

## Cron任务配置

```bash
# 每日体重提醒 21:55
openclaw cron create --name "每日体重提醒" --schedule "55 21 * * *" --command "health_tracking/scripts/daily_weight_reminder.sh"

# 每日饮食推荐 10:35（与10:13概率论任务错开）
openclaw cron create --name "每日饮食推荐" --schedule "35 10 * * *" --command "health_tracking/scripts/daily_meal_recommendation.sh"

# 月度体重汇总 每月1号09:00
openclaw cron create --name "月度体重汇总" --schedule "0 9 1 * *" --command "health_tracking/scripts/monthly_weight_summary.sh"
```

## 数据格式

### 体重记录 (weight/current.csv)
```csv
date,weight_kg,note
2026-04-15,75.5,
2026-04-16,75.2,
```

### 营养记录 (nutrition/YYYY-MM-DD.json)
```json
{
  "date": "2026-04-15",
  "meals": {
    "breakfast": [{"food": "燕麦", "amount": 50, "unit": "g"}],
    "lunch": [],
    "dinner": [],
    "snack": []
  },
  "totals": {
    "protein_g": 25,
    "fiber_g": 8,
    "vitamin_c_mg": 45,
    "calcium_mg": 200,
    "iron_mg": 3
  }
}
```
