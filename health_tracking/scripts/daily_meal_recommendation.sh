#!/bin/bash
# 今日饮食推荐 - 10:35
# 基于BMI和营养素缺口推荐

echo "🍽️ 今日饮食推荐"
echo "时间: $(date '+%Y-%m-%d %a')"
echo ""

# 读取最新体重计算BMI
LATEST_WEIGHT=$(tail -1 /root/.openclaw/workspace/health_tracking/weight/current.csv 2>/dev/null | cut -d',' -f2)
if [ -z "$LATEST_WEIGHT" ]; then
    echo "⚠️ 暂无体重记录，请先用标准体重参考"
    LATEST_WEIGHT=75
fi

HEIGHT=1.82
BMI=$(echo "scale=1; $LATEST_WEIGHT / ($HEIGHT * $HEIGHT)" | bc)

echo "📊 当前数据"
echo "   体重: ${LATEST_WEIGHT}kg"
echo "   身高: 182cm" 
echo "   BMI: ${BMI}"
echo ""

# BMI判断
if (( $(echo "$BMI < 18.5" | bc -l) )); then
    echo "⚠️ BMI偏低，建议增加蛋白质和碳水化合物摄入"
    GOAL="增重"
elif (( $(echo "$BMI >= 18.5 && $BMI < 24" | bc -l) )); then
    echo "✅ BMI正常，保持均衡饮食"
    GOAL="维持"
elif (( $(echo "$BMI >= 24 && $BMI < 28" | bc -l) )); then
    echo "⚠️ BMI超重，建议控制碳水、增加膳食纤维"
    GOAL="减重"
else
    echo "⚠️ BMI肥胖，建议严格控制热量、增加运动"
    GOAL="减脂"
fi

echo ""
echo "🥗 今日推荐食谱（不吃辣）"
echo ""
echo "【早餐】8:00-9:00"
echo "   选项1: 燕麦牛奶 + 水煮蛋 + 苹果"
echo "   选项2: 全麦面包 + 花生酱 + 牛奶"
echo ""
echo "【午餐】12:00-13:00"
echo "   选项1: 番茄炒蛋 + 米饭 + 清炒时蔬"
echo "   选项2: 香煎鸡胸肉 + 杂粮饭 + 西兰花"
echo ""
echo "【晚餐】18:00-19:00"
echo "   选项1: 豆腐汤 + 杂粮馒头 + 凉拌黄瓜"
echo "   选项2: 清蒸鱼 + 蒸南瓜 + 清炒芥蓝"
echo ""
echo "【加餐】15:00或21:00（如饿）"
echo "   坚果一小把 / 酸奶 / 香蕉"
echo ""
echo "---"
echo "📝 吃完后告诉我你吃了什么"
echo "   我会记录并分析营养素缺口"
