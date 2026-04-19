#!/bin/bash
# Amazon Monitor Wrapper Script
# 设置环境并运行监控脚本

cd /root/.openclaw/workspace

# 创建数据目录
mkdir -p /root/.openclaw/workspace/data/amazon_monitor

# 检查并安装依赖（如需要）
python3 -c "import requests, bs4" 2>/dev/null || pip3 install --break-system-packages requests beautifulsoup4 -q 2>/dev/null

# 运行监控脚本
python3 /root/.openclaw/workspace/scripts/amazon_monitor.py 2>&1
