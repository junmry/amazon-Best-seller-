
# 沙发Listing埋词AI调用指南

## 文件说明

### 1. 沙发埋词库_结构化.json
**用途**: API/代码调用
**格式**: JSON
**结构**:
```
{
  "大沙发": {
    "场景": {
      "主词": [{"keyword": "xxx", "volume": 123, "term": "xxx"}],
      "副词": [...],
      "长尾词": [...]
    },
    "人群": {...},
    "尺码": {...},
    "款式": {...}
  },
  "小沙发": {...}
}
```

**Python调用示例**:
```python
import json

# 加载词库
with open('沙发埋词库_结构化.json', 'r', encoding='utf-8') as f:
    word_bank = json.load(f)

# 获取大沙发场景主词（按搜索量排序）
scene_keywords = word_bank['大沙发']['场景']['主词']
for kw in scene_keywords[:10]:
    print(f"{kw['keyword']}: {kw['volume']}")

# 组合标题
size = "大沙发"
dimension = "场景"
main_words = [w['keyword'] for w in word_bank[size][dimension]['主词'][:5]]
print("推荐主词:", main_words)
```

---

### 2. 沙发埋词库_Excel版.xlsx
**用途**: 人工查看/复制粘贴
**Sheet列表**:
- `埋词速查_大沙发` - 大沙发高频词（按搜索量排序）
- `埋词速查_小沙发` - 小沙发高频词
- `主词库` - 所有主词汇总
- `副词库` - 所有副词汇总

---

### 3. 沙发埋词库.json
**用途**: 简单词列表
**格式**: 纯词列表，每条带搜索量

---

## AI埋词Prompt模板

```
你是亚马逊Listing优化专家。请根据以下词库为产品撰写标题和五点描述。

【产品信息】
- 产品类型: {大沙发/小沙发}
- 颜色: {xxx}
- 材质: {xxx}
- 尺寸: {xxx}

【词库参考】
场景词: {从词库选取}
人群词: {从词库选取}
尺码词: {从词库选取}
款式词: {从词库选取}

【要求】
1. 标题180-190字符，品牌开头
2. 埋入高搜索量词（>1000优先）
3. 不重复用词（同词最多2次）
4. 五点描述禁止具体尺寸数字和颜色
5. 自然融入，不要堆砌

请输出:
1. 标题
2. 五点描述（英文）
3. 埋词清单（说明用了哪些词库的哪些词）
```

---

## 分类规则速查

| 维度 | 大沙发关键词 | 小沙发关键词 |
|------|-------------|-------------|
| 场景 | living room, family room, house | apartment, studio, bedroom, dorm |
| 尺码 | 3 seater+, large, big, 78"/87"/102" | 2 seater, small, compact, loveseat |
| 款式 | sectional, L-shaped, modular, chaise | loveseat, futon, sleeper, daybed |
| 人群 | adult, family, couple, guest | teen, student, single |
