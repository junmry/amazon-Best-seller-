#!/usr/bin/env python3
"""
亚马逊Listing标题和五点拆解分析
分析维度：
1. 标题结构和关键词分布
2. 五点描述的卖点布局
3. 高频词汇统计
4. 竞品差异化策略
"""

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import re
from collections import Counter, defaultdict

# 读取数据
file_path = '/root/.openclaw/workspace/.kimi/downloads/19d6ff19-0f12-8922-8000-000077c456ec_BSR_Conversation-Sets_Current_-100-US-20260409.xlsx'
df = pd.read_excel(file_path, sheet_name='US')

print('=' * 80)
print('🎯 亚马逊 Conversation Sets 类目 Top 100  Listing 拆解分析')
print('=' * 80)

# ========== 基础数据统计 ==========
print(f'\n📊 数据概况')
print(f'   分析产品数: {len(df)}')
print(f'   平均评分: {df["Rating"].mean():.2f}')
print(f'   平均评论数: {df["Ratings"].mean():.0f}')
print(f'   平均价格: ${df["Price($)"].mean():.2f}')

# ========== 标题分析 ==========
print(f'\n{"="*80}')
print('📌 一、标题拆解分析')
print('=' * 80)

titles = df['Product Title'].dropna().astype(str).tolist()

# 1. 标题长度统计
title_lengths = [len(t) for t in titles]
print(f'\n1️⃣ 标题长度分布')
print(f'   平均长度: {sum(title_lengths)/len(title_lengths):.0f} 字符')
print(f'   最短: {min(title_lengths)} 字符')
print(f'   最长: {max(title_lengths)} 字符')
print(f'   150-200字符占比: {sum(1 for x in title_lengths if 150 <= x <= 200) / len(title_lengths) * 100:.1f}%')

# 2. 提取所有标题词汇（过滤停用词）
stopwords = {'and', 'the', 'for', 'with', 'of', 'in', 'to', 'a', 'an', 'is', 'are', 'was', 'were', 
             'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 
             'could', 'should', 'may', 'might', 'must', 'shall', 'can', 'need', 'dare', 'ought', 
             'used', 'at', 'on', 'by', 'from', 'as', 'into', 'through', 'during', 'before', 
             'after', 'above', 'below', 'up', 'down', 'out', 'off', 'over', 'under', 'again', 
             'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 
             'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 
             'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'just', 'don', 'now', '|', '-', '&', ','}

all_title_words = []
for title in titles:
    # 清洗并分词
    words = re.findall(r'\b[a-zA-Z]+\b', title.lower())
    all_title_words.extend([w for w in words if w not in stopwords and len(w) > 2])

# 统计高频词
word_counter = Counter(all_title_words)

print(f'\n2️⃣ 标题高频词 TOP 20')
for word, count in word_counter.most_common(20):
    percentage = count / len(titles) * 100
    print(f'   {word:20s} | 出现 {count:3d} 次 | 占比 {percentage:5.1f}%')

# 3. 标题结构分析
print(f'\n3️⃣ 标题结构特征')

# 分析标题开头的词
first_words = []
for title in titles:
    words = re.findall(r'\b[a-zA-Z]+\b', title)
    if words:
        first_words.append(words[0].lower())

first_word_counter = Counter(first_words)
print(f'\n   标题开头词 TOP 10:')
for word, count in first_word_counter.most_common(10):
    print(f'      {word}: {count} 次')

# 分析标题中包含的数值信息
numbers_in_titles = []
for title in titles:
    nums = re.findall(r'\d+\s*(?:piece|pieces|pc|pcs|seater|seat)', title.lower())
    if nums:
        numbers_in_titles.extend(nums)

number_counter = Counter(numbers_in_titles)
print(f'\n   标题中件套数分布:')
for num, count in number_counter.most_common(10):
    print(f'      {num}: {count} 次')

# ========== 五点分析 ==========
print(f'\n{"="*80}')
print('📌 二、五点描述拆解分析')
print('=' * 80)

bullets = df['Bullet Points'].dropna().astype(str).tolist()
print(f'\n   有效五点描述数: {len(bullets)} / {len(df)}')

# 1. 提取所有五点词汇
all_bullet_words = []
for bullet in bullets:
    words = re.findall(r'\b[a-zA-Z]+\b', bullet.lower())
    all_bullet_words.extend([w for w in words if w not in stopwords and len(w) > 2])

bullet_word_counter = Counter(all_bullet_words)

print(f'\n1️⃣ 五点高频词 TOP 20')
for word, count in bullet_word_counter.most_common(20):
    percentage = count / len(bullets) * 100
    print(f'   {word:20s} | 出现 {count:3d} 次 | 占比 {percentage:5.1f}%')

# 2. 五点卖点分类分析
print(f'\n2️⃣ 五点卖点类型分析')

# 定义卖点类型关键词
selling_point_types = {
    '材质工艺': ['rattan', 'wicker', 'pe', 'steel', 'frame', 'durable', 'sturdy', 'weather', 'resistant', 'waterproof', 'uv', 'rust', 'aluminum', 'iron', 'wood', 'teak'],
    '舒适体验': ['comfortable', 'cushion', 'soft', 'padding', 'thick', 'cozy', 'relax', 'seat', 'seating', 'ergonomic'],
    '空间场景': ['patio', 'outdoor', 'garden', 'backyard', 'balcony', 'porch', 'deck', 'yard', 'lawn', 'terrace'],
    '安装使用': ['easy', 'assemble', 'assembly', 'install', 'installation', 'quick', 'simple', 'tools', 'manual', 'instruction'],
    '设计款式': ['modern', 'classic', 'elegant', 'stylish', 'design', 'beautiful', 'fashion', 'contemporary', 'traditional'],
    '功能用途': ['conversation', 'chat', 'relax', 'entertain', 'dining', 'lounge', 'rest', 'gathering', 'party'],
    '包装服务': ['warranty', 'service', 'customer', 'support', 'package', 'packaging', 'delivery', 'shipping', 'guarantee']
}

# 统计每个卖点类型在五点中的出现频率
selling_point_stats = {}
for sp_type, keywords in selling_point_types.items():
    count = 0
    for bullet in bullets:
        bullet_lower = bullet.lower()
        if any(kw in bullet_lower for kw in keywords):
            count += 1
    selling_point_stats[sp_type] = count

print(f'\n   卖点类型覆盖度（有多少产品的五点包含该类型）:')
for sp_type, count in sorted(selling_point_stats.items(), key=lambda x: -x[1]):
    percentage = count / len(bullets) * 100
    bar = '█' * int(percentage / 5)
    print(f'   {sp_type:12s}: {count:3d}/{len(bullets)} ({percentage:5.1f}%) {bar}')

# 3. 分析典型的五点结构（取前5个产品的五点作为示例）
print(f'\n3️⃣ 典型五点结构示例（前3名产品）')
for i in range(min(3, len(df))):
    row = df.iloc[i]
    print(f'\n   🏆 BSR #{row["#"]} | {row["Brand"]} | ${row["Price($)"]} | ⭐{row["Rating"]} ({row["Ratings"]}评)')
    print(f'   标题: {row["Product Title"][:100]}...')
    print(f'   五点:')
    bullet_text = str(row['Bullet Points'])
    # 分割五点（通常以换行或"-"开头）
    points = re.split(r'\n|(?=\s*-\s*[A-Z])', bullet_text)
    for j, point in enumerate(points[:5], 1):
        point_clean = point.strip().replace('-', '').strip()
        if point_clean and len(point_clean) > 10:
            print(f'      {j}. {point_clean[:120]}...' if len(point_clean) > 120 else f'      {j}. {point_clean}')

# ========== 差异化策略分析 ==========
print(f'\n{"="*80}')
print('📌 三、竞品差异化策略分析')
print('=' * 80)

# 1. 品牌定位分析
print(f'\n1️⃣ 品牌定位词分析')
positioning_words = ['modern', 'classic', 'elegant', 'luxury', 'premium', 'budget', 'affordable', 'high-end', 'quality', 'cheap']
positioning_stats = {}
for word in positioning_words:
    count = sum(1 for t in titles if word in t.lower())
    positioning_stats[word] = count

for word, count in sorted(positioning_stats.items(), key=lambda x: -x[1]):
    if count > 0:
        print(f'   {word:15s}: {count} 个产品使用')

# 2. 材质强调分析
print(f'\n2️⃣ 材质强调策略')
material_words = {'pe rattan': 0, 'wicker': 0, 'rattan': 0, 'aluminum': 0, 'steel': 0, 'iron': 0, 'teak': 0, 'wood': 0, 'resin': 0}
for material in material_words:
    count = sum(1 for t in titles if material in t.lower())
    material_words[material] = count

for material, count in sorted(material_words.items(), key=lambda x: -x[1]):
    if count > 0:
        print(f'   {material:15s}: {count} 个产品在标题中强调')

# 3. 场景词分析
print(f'\n3️⃣ 场景定位词分析')
scene_words = ['patio', 'outdoor', 'garden', 'backyard', 'balcony', 'porch', 'deck', 'yard']
scene_stats = {}
for word in scene_words:
    title_count = sum(1 for t in titles if word in t.lower())
    bullet_count = sum(1 for b in bullets if word in b.lower())
    scene_stats[word] = {'title': title_count, 'bullet': bullet_count}

print(f'   {"场景词":15s} | {"标题":>8s} | {"五点":>8s}')
print(f'   {"-"*40}')
for word, stats in sorted(scene_stats.items(), key=lambda x: -(x[1]['title']+x[1]['bullet'])):
    print(f'   {word:15s} | {stats["title"]:>8d} | {stats["bullet"]:>8d}')

# ========== 优秀案例提取 ==========
print(f'\n{"="*80}')
print('📌 四、优秀Listing案例')
print('=' * 80)

# 综合评分筛选（评分高、评论多、BSR排名靠前）
df['综合得分'] = df['Rating'] * 0.3 + (df['Ratings']/df['Ratings'].max()) * 0.4 + (1 - (df['#']-1)/99) * 0.3
top_listings = df.nlargest(3, '综合得分')

print(f'\n🏆 综合表现最佳Top 3:')
for idx, row in top_listings.iterrows():
    print(f'\n   #{row["#"]} | {row["Brand"]} | ${row["Price($)"]} | BSR:{row["Category BSR"]} | ⭐{row["Rating"]} ({row["Ratings"]}评)')
    print(f'   标题: {row["Product Title"]}')
    print(f'   标题长度: {len(row["Product Title"])} 字符')
    
    # 提取标题关键词
    title_words = re.findall(r'\b[a-zA-Z]+\b', row['Product Title'].lower())
    title_keywords = [w for w in title_words if w not in stopwords and len(w) > 2]
    print(f'   核心词: {", ".join(title_keywords[:8])}')

print(f'\n{"="*80}')
print('✅ 分析完成！')
print('=' * 80)
