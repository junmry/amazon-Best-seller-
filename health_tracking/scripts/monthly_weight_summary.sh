#!/bin/bash
# 月度体重趋势汇总 - 每月1号 09:00

YEAR=$(date +%Y)
MONTH=$(date +%m)
LAST_MONTH=$(date -d "last month" +%m 2>/dev/null || echo "12")

WEIGHT_FILE="/root/.openclaw/workspace/health_tracking/weight/${YEAR}-${LAST_MONTH}.csv"

echo "📊 ${LAST_MONTH}月体重趋势汇总"
echo "======================="
echo ""

if [ ! -f "$WEIGHT_FILE" ]; then
    echo "⚠️ 上月无体重记录"
    echo ""
    echo "提示: 每天21:55我会提醒你记录体重"
    exit 0
fi

# 统计
echo "📈 数据统计"
echo ""

# 读取数据计算
TOTAL=$(tail -n +2 "$WEIGHT_FILE" | wc -l)
if [ "$TOTAL" -eq 0 ]; then
    echo "⚠️ 记录为空"
    exit 0
fi

# 提取体重数值
WEIGHTS=$(tail -n +2 "$WEIGHT_FILE" | cut -d',' -f2 | sort -n)
MIN=$(echo "$WEIGHTS" | head -1)
MAX=$(echo "$WEIGHTS" | tail -1)
FIRST=$(echo "$WEIGHTS" | head -1)
LAST=$(echo "$WEIGHTS" | tail -1)

# 计算平均值
SUM=0
COUNT=0
for w in $WEIGHTS; do
    SUM=$(echo "$SUM + $w" | bc)
    COUNT=$((COUNT + 1))
done
AVG=$(echo "scale=1; $SUM / $COUNT" | bc)

# 变化
CHANGE=$(echo "scale=1; $LAST - $FIRST" | bc)

echo "   记录天数: ${TOTAL}天"
echo "   平均体重: ${AVG}kg"
echo "   最低体重: ${MIN}kg"
echo "   最高体重: ${MAX}kg"
echo "   月初体重: ${FIRST}kg"
echo "   月末体重: ${LAST}kg"

if (( $(echo "$CHANGE > 0" | bc -l) )); then
    echo "   月度变化: +${CHANGE}kg 📈"
elif (( $(echo "$CHANGE < 0" | bc -l) )); then
    echo "   月度变化: ${CHANGE}kg 📉"
else
    echo "   月度变化: 0kg ➡️"
fi

echo ""
echo "📋 详细记录:"
echo "$WEIGHTS" | head -5
echo "... (${TOTAL}条记录)"
echo ""
echo "文件: $WEIGHT_FILE"
