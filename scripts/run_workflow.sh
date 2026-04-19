#!/bin/bash
# 拆词工作流主控脚本
# Usage: ./run_workflow.sh [关键词文件] [BSR文件]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="$WORKSPACE_DIR/拆词工作流输出"

echo "=========================================="
echo "  关键词拆词自动化工作流"
echo "=========================================="
echo ""

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

# 检查依赖
check_dependency() {
    if ! command -v "$1" &> /dev/null; then
        echo "❌ 缺少依赖: $1"
        echo "   请安装: pip3 install $2"
        exit 1
    fi
}

echo "🔍 检查依赖..."
check_dependency python3 "python3"

# 检查Python包
python3 -c "import pandas" 2>/dev/null || {
    echo "❌ 缺少Python包: pandas"
    echo "   请安装: pip3 install pandas openpyxl"
    exit 1
}

python3 -c "import openpyxl" 2>/dev/null || {
    echo "❌ 缺少Python包: openpyxl"
    echo "   请安装: pip3 install openpyxl"
    exit 1
}

echo "   ✓ 依赖检查通过"
echo ""

# 处理关键词文件
if [ -n "$1" ] && [ -f "$1" ]; then
    KEYWORD_FILE="$1"
    echo "📊 处理关键词文件: $KEYWORD_FILE"
    python3 "$SCRIPT_DIR/keyword_pipeline.py" "$KEYWORD_FILE" "$OUTPUT_DIR/关键词分析"
    echo ""
fi

# 处理BSR文件
if [ -n "$2" ] && [ -f "$2" ]; then
    BSR_FILE="$2"
    echo "📊 处理BSR文件: $BSR_FILE"
    python3 "$SCRIPT_DIR/bsr_analyzer.py" "$BSR_FILE" "$OUTPUT_DIR/BSR分析"
    echo ""
fi

# 生成汇总报告
echo "📋 生成工作流汇总..."

SUMMARY_FILE="$OUTPUT_DIR/工作流汇总_$(date +%Y%m%d_%H%M).md"

cat > "$SUMMARY_FILE" << EOF
# 拆词工作流汇总报告

**生成时间**: $(date "+%Y-%m-%d %H:%M:%S")  
**工作目录**: $WORKSPACE_DIR

---

## 本次处理文件

EOF

if [ -n "$KEYWORD_FILE" ]; then
    echo "- **关键词文件**: $KEYWORD_FILE" >> "$SUMMARY_FILE"
fi

if [ -n "$BSR_FILE" ]; then
    echo "- **BSR文件**: $BSR_FILE" >> "$SUMMARY_FILE"
fi

cat >> "$SUMMARY_FILE" << EOF

---

## 输出文件列表

### 关键词分析
\`\`\`
$(find "$OUTPUT_DIR/关键词分析" -type f -name "*.xlsx" -o -name "*.md" 2>/dev/null | head -20)
\`\`\`

### BSR分析
\`\`\`
$(find "$OUTPUT_DIR/BSR分析" -type f -name "*.xlsx" 2>/dev/null | head -20)
\`\`\`

---

## 下一步操作

1. **查看Excel文件**: 打开生成的 .xlsx 文件查看详细拆词结果
2. **阅读分析报告**: 查看 .md 报告获取洞察和建议
3. **提取埋词**: 根据"高价值词"sheet和"洞察摘要"sheet提取埋词清单
4. **制作Listing**: 参考BSR分析的"标题公式建议"制作标题和五点

---

## 快速参考

### 标题结构公式
```
[Brand] + [核心产品词] + [with + 核心功能] + [附加功能] + [for 场景] + (颜色)
```

### 五点描述结构
1. **舒适度** - ergonomic, support, comfortable
2. **材质** - leather, fabric, foam, quality
3. **功能** - adjustable, footrest, massage, swivel
4. **耐用性** - durable, heavy duty, stable
5. **售后** - easy assembly, warranty, service

### 埋词优先级
- **标题**: 高搜索量 + 短词 (20-40字符)
- **五点**: 中长尾词 + 场景词
- **后台**: 所有维度词 + 变体词

---

*本报告由拆词工作流自动生成*
EOF

echo "   ✓ 汇总报告: $SUMMARY_FILE"
echo ""

echo "=========================================="
echo "  工作流完成!"
echo "=========================================="
echo ""
echo "📁 输出目录: $OUTPUT_DIR"
echo ""
echo "生成的文件:"
find "$OUTPUT_DIR" -type f \( -name "*.xlsx" -o -name "*.md" \) -exec ls -lh {} \; | awk '{print "  -", $9, "(" $5 ")"}'
echo ""
echo "💡 提示: 查看 $SUMMARY_FILE 获取完整汇总"
