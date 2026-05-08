#!/usr/bin/env python3
"""
Dreaming - Workspace Memory Consolidation Script
每晚 22:17 运行，对 Kimi Claw 的工作区进行"做梦"式整理。

核心理念（来自 Anthropic Dreaming）：
- Memory 让 Agent 在工作中记住学到了什么
- Dreaming 让 Agent 在工作间隙想明白这些经验意味着什么
- 一个是即时学习，一个是反思整理

原则：
1. 永不修改原始数据——所有整理结果写入新文件
2. 删除操作标记为通知，不自动执行
3. 输出一份"梦境报告"，呈现发现的模式和洞察
"""

import os
import re
import json
import hashlib
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from pathlib import Path

WORKSPACE = Path("/root/.openclaw/workspace")
MEMORY_DIR = WORKSPACE / "memory"
DREAMING_LOG = MEMORY_DIR / f".dreaming_{datetime.now().strftime('%Y%m%d')}.md"
DELETE_NOTIFY = MEMORY_DIR / f".cleanup_delete_notify_{datetime.now().strftime('%Y%m%d')}"

# ============ 工具函数 ============
def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}")

def read_file_safe(path, max_lines=500):
    """安全读取文件，限制行数"""
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.readlines()[:max_lines]
    except Exception as e:
        return [f"[读取失败: {e}]"]

def extract_todos(content_lines):
    """从文本中提取 TODO 项"""
    todos = []
    for line in content_lines:
        line = line.strip()
        if line.startswith('- [ ]') or line.startswith('- [x]'):
            todos.append(line)
        elif re.search(r'TODO|待办|待处理', line, re.I) and len(line) < 200:
            todos.append(line)
    return todos

def extract_topics(content_lines):
    """提取文本中的主题关键词（简单启发式）"""
    topics = []
    for line in content_lines:
        # 匹配 ## 标题
        m = re.match(r'^#+\s+(.+)', line)
        if m:
            topics.append(m.group(1).strip())
        # 匹配粗体强调
        for match in re.finditer(r'\*\*(.+?)\*\*', line):
            topics.append(match.group(1).strip())
    return topics

# ============ Level 1: 物理整理（安全扫描） ============
def scan_physical_clutter():
    """扫描物理层面的冗余，只报告不删除"""
    clutter = {
        "empty_dirs": [],
        "old_downloads": [],
        "duplicate_basenames": [],
        "orphaned_files": []
    }
    
    # 1. 空目录
    for root, dirs, files in os.walk(WORKSPACE / "keyword_library"):
        for d in dirs:
            full_path = Path(root) / d
            if d.startswith('_'):
                continue
            try:
                if not any(full_path.iterdir()):
                    clutter["empty_dirs"].append(str(full_path.relative_to(WORKSPACE)))
            except:
                pass
    
    # 2. 过期下载文件（>7天）
    downloads = WORKSPACE / "downloads"
    if downloads.exists():
        for f in downloads.iterdir():
            if f.is_file():
                age = datetime.now() - datetime.fromtimestamp(f.stat().st_mtime)
                if age > timedelta(days=7):
                    clutter["old_downloads"].append({
                        "path": str(f.relative_to(WORKSPACE)),
                        "age_days": age.days,
                        "size": f.stat().st_size
                    })
    
    # 3. 检测 keyword_library 中同名不同目录的文件（潜在的重复）
    file_map = defaultdict(list)
    for root, dirs, files in os.walk(WORKSPACE / "keyword_library"):
        for fname in files:
            if fname.endswith(('.xlsx', '.csv', '.json', '.md')):
                file_map[fname].append(Path(root) / fname)
    
    for fname, paths in file_map.items():
        if len(paths) > 1 and not fname.startswith('.'):
            # 计算 MD5 看是否真重复
            hashes = {}
            for p in paths:
                try:
                    h = hashlib.md5(p.read_bytes()).hexdigest()
                    hashes.setdefault(h, []).append(str(p.relative_to(WORKSPACE)))
                except:
                    pass
            if len(hashes) > 1:
                # 同名但内容不同——可能是版本迭代
                clutter["duplicate_basenames"].append({
                    "name": fname,
                    "locations": [str(p.relative_to(WORKSPACE)) for p in paths]
                })
    
    return clutter

# ============ Level 2: Memory 提炼 ============
def consolidate_memories():
    """分析 daily memory 文件，提炼长期价值"""
    daily_files = sorted([f for f in MEMORY_DIR.glob("*.md") if re.match(r'\d{4}-\d{2}-\d{2}', f.name)])
    
    if not daily_files:
        return None
    
    recent_files = daily_files[-14:]  # 最近两周
    
    all_todos = []
    all_topics = []
    cross_session_patterns = Counter()
    
    for f in recent_files:
        lines = read_file_safe(f, max_lines=300)
        content = ''.join(lines)
        
        todos = extract_todos(lines)
        all_todos.extend(todos)
        
        topics = extract_topics(lines)
        all_topics.extend(topics)
        
        # 检测重复主题（跨 session 出现 >=2 次）
        for t in set(topics):
            cross_session_patterns[t] += 1
    
    # 找出高频主题（跨多天出现）
    recurring_topics = {k: v for k, v in cross_session_patterns.items() if v >= 2 and len(k) > 3}
    
    # 找出未完成的 TODO
    undone = [t for t in all_todos if t.startswith('- [ ]')]
    done = [t for t in all_todos if t.startswith('- [x]')]
    
    return {
        "period": f"{recent_files[0].name.replace('.md','')} ~ {recent_files[-1].name.replace('.md','')}",
        "daily_count": len(recent_files),
        "total_todos": len(all_todos),
        "undone_todos": undone,
        "done_todos": done,
        "recurring_topics": dict(recurring_topics.most_common(20)),
        "all_topics_sample": list(set(all_topics))[:30]
    }

# ============ Level 3: 知识库模式发现 ============
def analyze_knowledge_patterns():
    """分析 keyword_library 和 skills 中的跨类目模式"""
    lib = WORKSPACE / "keyword_library"
    categories = [d.name for d in lib.iterdir() if d.is_dir() and not d.name.startswith('_')]
    
    # 检测活跃类目（有最近更新）
    active_categories = []
    for cat_dir in lib.iterdir():
        if not cat_dir.is_dir() or cat_dir.name.startswith('_'):
            continue
        # 检查最近7天是否有文件修改
        recent = False
        for f in cat_dir.rglob('*'):
            if f.is_file():
                age = datetime.now() - datetime.fromtimestamp(f.stat().st_mtime)
                if age < timedelta(days=7):
                    recent = True
                    break
        if recent:
            active_categories.append(cat_dir.name)
    
    # 检查 skills 目录
    skills_dir = WORKSPACE / "skills"
    skills = [d.name for d in skills_dir.iterdir() if d.is_dir()] if skills_dir.exists() else []
    
    # 检查 rufus/ 下的方法论更新
    rufus_dir = WORKSPACE / "rufus"
    rufus_files = [f.name for f in rufus_dir.iterdir()] if rufus_dir.exists() else []
    
    return {
        "total_categories": len(categories),
        "active_categories_7d": active_categories,
        "inactive_categories": [c for c in categories if c not in active_categories],
        "skills_count": len(skills),
        "skills_list": skills,
        "rufus_files": rufus_files
    }

# ============ Level 4: 生成梦境报告 ============
def generate_dreaming_report(clutter, memory, patterns):
    """生成梦境报告——呈现发现的模式和洞察"""
    
    report = f"""# 🌙 Dreaming Report — {datetime.now().strftime('%Y-%m-%d %H:%M')}

> *"Memory 让你记住学到了什么。Dreaming 让你想明白这些经验意味着什么。"*

---

## 一、物理层扫描（只看不删）

"""
    
    # 物理冗余
    if clutter["empty_dirs"]:
        report += "### 空目录\n"
        for d in clutter["empty_dirs"][:10]:
            report += f"- `{d}`\n"
        report += "\n"
    
    if clutter["old_downloads"]:
        report += "### 过期下载文件（>7天）\n"
        report += "| 文件 | 年龄 | 大小(字节) |\n"
        report += "|------|------|-----------|\n"
        for item in clutter["old_downloads"][:10]:
            report += f"| `{item['path']}` | {item['age_days']}天 | {item['size']} |\n"
        report += "\n> ⚠️ 以上文件**建议删除**，但我不会自动执行。请告诉我是否清理。\n\n"
    
    if clutter["duplicate_basenames"]:
        report += "### 同名不同内容的文件（版本迭代信号）\n"
        for dup in clutter["duplicate_basenames"][:5]:
            report += f"- **{dup['name']}** 出现在 {len(dup['locations'])} 个位置\n"
            for loc in dup['locations']:
                report += f"  - `{loc}`\n"
        report += "\n> 💡 可能是同一类目的多版本词表，考虑归档旧版本。\n\n"
    
    # Memory 层
    if memory:
        report += f"""## 二、Memory 层提炼（{memory['period']}）

### 跨 Session 模式

最近 {memory['daily_count']} 天的 daily memory 中，以下主题反复出现：

"""
        for topic, count in list(memory['recurring_topics'].items())[:10]:
            report += f"- **{topic}** — 在 {count} 天中出现\n"
        
        report += "\n### TODO 追踪\n\n"
        report += f"- 总 TODO: {memory['total_todos']} 项\n"
        report += f"- 已完成: {len(memory['done_todos'])} 项\n"
        report += f"- 待完成: {len(memory['undone_todos'])} 项\n\n"
        
        if memory['undone_todos']:
            report += "**未完成的 TODO（建议关注）：**\n\n"
            for todo in memory['undone_todos'][:10]:
                report += f"- {todo}\n"
            report += "\n"
        
        report += "### 建议写入 MEMORY.md 的信号\n\n"
        report += "以下主题在多天内反复出现，可能值得提升到长期记忆：\n\n"
        for topic, count in list(memory['recurring_topics'].items())[:5]:
            if count >= 3:
                report += f"- [ ] `{topic}` — 出现 {count} 次\n"
        report += "\n"
    
    # 知识库模式
    if patterns:
        report += f"""## 三、知识库模式发现

### 类目活跃度
- 总类目数: {patterns['total_categories']}
- 最近7天活跃类目: {len(patterns['active_categories_7d'])}

"""
        if patterns['active_categories_7d']:
            report += "活跃类目:\n"
            for cat in patterns['active_categories_7d']:
                report += f"- `{cat}`\n"
            report += "\n"
        
        if patterns['inactive_categories']:
            report += "沉默类目（超过7天无更新）:\n"
            for cat in patterns['inactive_categories']:
                report += f"- `{cat}`\n"
            report += "\n"
        
        report += f"""### Skills 状态
- 已注册 Skills: {patterns['skills_count']} 个
- 列表: {', '.join(patterns['skills_list'][:10])}

### Rufus 方法论
- 文件: {', '.join(patterns['rufus_files'])}

"""
    
    # 洞察层
    report += """## 四、今晚的梦（洞察）

"""
    
    # 生成简单洞察
    insights = []
    
    if memory and len(memory['undone_todos']) > len(memory['done_todos']):
        insights.append("TODO 堆积速度超过完成速度，可能需要一次集中清理。")
    
    if patterns and len(patterns['active_categories_7d']) > 3:
        insights.append(f"最近同时推进 {len(patterns['active_categories_7d'])} 个类目，注意资源分散。")
    
    if clutter["duplicate_basenames"]:
        insights.append("发现同名多版本文件，建议建立版本命名规范（如 V1/V2/日期后缀）。")
    
    if not insights:
        insights.append("工作区状态良好，无明显模式异常。")
    
    for insight in insights:
        report += f"- {insight}\n"
    
    report += """
---

## 五、明日建议

1. **查看未完成的 TODO** — 是否有可以批量处理的任务
2. **归档旧版本词表** — 特别是 keyword_library 中的重复文件
3. **更新 MEMORY.md** — 将跨天出现的主题提炼为长期记忆

---

*这是一个 Dreaming 报告。所有整理建议都是「只读分析」，原始数据未被修改。*
*如果有删除建议，会在下方单独标记。*
"""
    
    return report

# ============ 删除通知 ============
def write_delete_notification(clutter):
    """写入删除通知标记"""
    items = []
    
    for d in clutter["empty_dirs"]:
        items.append(f"空目录: {d}")
    
    for item in clutter["old_downloads"]:
        items.append(f"过期下载: {item['path']} ({item['age_days']}天)")
    
    if items:
        with open(DELETE_NOTIFY, 'w', encoding='utf-8') as f:
            f.write(f"Dreaming 删除建议 — {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write("=" * 50 + "\n\n")
            for item in items:
                f.write(f"- {item}\n")
        log(f"已创建删除通知: {DELETE_NOTIFY}")
        return True
    return False

# ============ 主流程 ============
def main():
    log("=" * 50)
    log("🌙 Dreaming 开始 — Workspace Memory Consolidation")
    log("=" * 50)
    
    # Level 1
    log("Level 1: 扫描物理层...")
    clutter = scan_physical_clutter()
    log(f"  发现空目录: {len(clutter['empty_dirs'])}, 过期下载: {len(clutter['old_downloads'])}, 同名文件: {len(clutter['duplicate_basenames'])}")
    
    # Level 2
    log("Level 2: 提炼 Memory...")
    memory = consolidate_memories()
    if memory:
        log(f"  分析 {memory['daily_count']} 天记忆, 总 TODO: {memory['total_todos']}, 跨天主题: {len(memory['recurring_topics'])}")
    else:
        log("  未发现 daily memory 文件")
    
    # Level 3
    log("Level 3: 发现知识库模式...")
    patterns = analyze_knowledge_patterns()
    log(f"  类目: {patterns['total_categories']}, 活跃: {len(patterns['active_categories_7d'])}, Skills: {patterns['skills_count']}")
    
    # Level 4
    log("Level 4: 生成梦境报告...")
    report = generate_dreaming_report(clutter, memory, patterns)
    
    # 保存报告
    with open(DREAMING_LOG, 'w', encoding='utf-8') as f:
        f.write(report)
    log(f"梦境报告已保存: {DREAMING_LOG}")
    
    # 删除通知（只标记，不执行）
    notified = write_delete_notification(clutter)
    if notified:
        log("已标记待删除项目，请确认后处理")
    
    # 同时输出到 stdout（cron 日志）
    print("\n" + "=" * 50)
    print(report)
    
    log("🌙 Dreaming 结束")
    log("=" * 50)

if __name__ == "__main__":
    main()
