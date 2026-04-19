#!/bin/bash
# 创建健康追踪Cron任务
# 在终端运行此脚本

echo "正在创建健康追踪定时任务..."
echo ""

# 检查openclaw命令
if ! command -v openclaw &> /dev/null; then
    echo "❌ openclaw 命令未找到"
    exit 1
fi

echo "1. 创建每日饮食推荐 (10:35)"
openclaw cron create \
  --name "每日饮食推荐" \
  --schedule "35 10 * * *" \
  --payload '{"kind":"agentTurn","content":"基于我的健康档案（身高182cm，不吃辣），查看最新体重记录，计算BMI，然后推荐今日三餐食谱。从health_tracking/nutrition_db.md中选取合适选项。"}' \
  --sessionTarget main

echo ""
echo "2. 创建每日体重提醒 (21:55)"
openclaw cron create \
  --name "每日体重提醒" \
  --schedule "55 21 * * *" \
  --payload '{"kind":"agentTurn","content":"询问用户今日体重，并记录到health_tracking/weight/current.csv。格式：日期,体重(kg),备注。然后回复确认已记录。"}' \
  --sessionTarget main

echo ""
echo "3. 创建月度体重汇总 (每月1号09:00)"
openclaw cron create \
  --name "月度体重汇总" \
  --schedule "0 9 1 * *" \
  --payload '{"kind":"agentTurn","content":"读取上月的体重记录(health_tracking/weight/YYYY-MM.csv)，计算平均/最高/最低体重，计算月度变化，生成趋势汇总报告发给用户。"}' \
  --sessionTarget main

echo ""
echo "✅ 任务创建完成"
echo ""
echo "查看所有任务: openclaw cron list"
