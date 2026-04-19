#!/bin/bash
# Amazon Analytics Learning System Runner
# 每日自动学习亚马逊和统计学知识

cd /root/.openclaw/workspace

echo "=========================================="
echo "🎓 启动每日学习系统"
echo "=========================================="
echo ""

# 运行学习脚本
python3 /root/.openclaw/workspace/scripts/learn_daily.py

# 检查运行结果
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 学习完成，正在更新技能索引..."
    
    # 可选：提交到git（如果配置了）
    if [ -d ".git" ]; then
        git add -A knowledge/ skills/amazon-analytics/
        git commit -m "📚 Daily learning update: $(date +%Y-%m-%d)" 2>/dev/null || true
    fi
    
    echo "✅ 所有任务完成!"
else
    echo "❌ 学习过程出错，请检查日志"
    exit 1
fi
