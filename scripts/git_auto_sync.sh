#!/bin/bash
# Git 自动同步脚本 - 每日备份自媒体内容

REPO_DIR="/root/.openclaw/workspace"
LOG_FILE="/root/.openclaw/workspace/memory/git_sync.log"

# 进入仓库
cd "$REPO_DIR" || exit 1

# 添加自媒体相关内容
git add content_creator/ 2>/dev/null
git add MEMORY.md 2>/dev/null
git add knowledge/ 2>/dev/null
git add keyword_library/ 2>/dev/null
git add scripts/*.py 2>/dev/null
git add *.md 2>/dev/null

# 检查是否有变更
if git diff --cached --quiet; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 无变更，跳过同步" >> "$LOG_FILE"
    exit 0
fi

# 提交并推送
COMMIT_MSG="Auto sync: $(date '+%Y-%m-%d %H:%M:%S') Asia/Shanghai"
git commit -m "$COMMIT_MSG" >> "$LOG_FILE" 2>&1

if git push origin HEAD 2>> "$LOG_FILE"; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ 同步成功" >> "$LOG_FILE"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ❌ 同步失败" >> "$LOG_FILE"
fi
