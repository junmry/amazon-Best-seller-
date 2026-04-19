#!/bin/bash
# 金融考试报名提醒脚本

echo "========================================"
echo "📢 金融从业资格考试报名提醒"
echo "========================================"
echo ""

# 获取当前日期
current_date=$(date +%Y-%m-%d)
echo "当前日期: $current_date"
echo ""

# 考试信息
echo "📅 2026年考试计划："
echo ""
echo "【期货从业】- 统考: 5月16日"
echo "   └─ 预计报名时间: 4月中下旬"
echo "   └─ 报名网站: www.cfachina.org"
echo ""
echo "【基金从业】- 统考: 5月23日、11月28日"  
echo "   └─ 预计报名时间: 考前1个月"
echo "   └─ 报名网站: www.amac.org.cn"
echo ""
echo "【证券从业】- 统考: 6月27日、9月19日"
echo "   └─ 预计报名时间: 考前1个月"
echo "   └─ 报名网站: www.sac.net.cn"
echo ""

echo "========================================"
echo "⚠️  重要提醒"
echo "========================================"
echo ""
echo "1. 机位有限，先报先得，额满即止"
echo "2. 建议报名开启当天尽早报名"
echo "3. 准备好: 身份证、学历证明、电子照片"
echo "4. 缴费成功才算报名完成"
echo ""
echo "📚 备考资料已整理至:"
echo "   /root/.openclaw/workspace/finance_exam_plan_2026.md"
echo ""
