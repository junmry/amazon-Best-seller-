#!/usr/bin/env python3
"""
生成Listing分析报告Excel
"""

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import re
from collections import Counter, defaultdict

# 读取数据
file_path = '/root/.openclaw/workspace/.kimi/downloads/19d6ff19-0f12-8922-8000-000077c456ec_BSR_Conversation-Sets_Current_-100-US-20260409.xlsx'
df = pd.read_excel(file_path, sheet_name='US')

titles = df['Product Title'].dropna().astype(str).tolist()
bullets = df['Bullet Points'].dropna().astype(str).tolist()

stopwords = {'and', 'the', 'for', 'with', 'of', 'in', 'to', 'a', 'an', 'is', 'are', 'was', 'were', 
             'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 
             'could', 'should', 'may', 'might', 'must', 'shall', 'can', 'need', 'dare', 'ought', 
             'used', 'at', 'on', 'by', 'from', 'as', 'into', 'through', 'during', 'before', 
             'after', 'above', 'below', 'up', 'down', 'out', 'off', 'over', 'under', 'again', 
             'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 
             'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 
             'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'just', 'don', 'now', '|', '-', '&', ','}

output_path = '/root/.openclaw/workspace/Conversation_Sets_Listing分析报告.xlsx'

with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    
    # Sheet 1: 数据概览
    overview_data = {
        '指标': ['分析产品数', '平均评分', '平均评论数', '平均价格', '平均标题长度', '150-200字符占比'],
        '数值': [
            len(df),
            f"{df['Rating'].mean():.2f}",
            f"{df['Ratings'].mean():.0f}",
            f"${df['Price($)'].mean():.2f}",
            f"{sum(len(t) for t in titles)/len(titles):.0f} 字符",
            f"{sum(1 for t in titles if 150 <= len(t) <= 200) / len(titles) * 100:.1f}%"
        ]
    }
    pd.DataFrame(overview_data).to_excel(writer, sheet_name='数据概览', index=False)
    
    # Sheet 2: 标题高频词
    all_title_words = []
    for title in titles:
        words = re.findall(r'\b[a-zA-Z]+\b', title.lower())
        all_title_words.extend([w for w in words if w not in stopwords and len(w) > 2])
    word_counter = Counter(all_title_words)
    
    title_words_df = pd.DataFrame([
        {'排名': i+1, '关键词': word, '出现次数': count, '占比': f'{count/len(titles)*100:.1f}%'}
        for i, (word, count) in enumerate(word_counter.most_common(50))
    ])
    title_words_df.to_excel(writer, sheet_name='标题高频词TOP50', index=False)
    
    # Sheet 3: 五点高频词
    all_bullet_words = []
    for bullet in bullets:
        words = re.findall(r'\b[a-zA-Z]+\b', bullet.lower())
        all_bullet_words.extend([w for w in words if w not in stopwords and len(w) > 2])
    bullet_counter = Counter(all_bullet_words)
    
    bullet_words_df = pd.DataFrame([
        {'排名': i+1, '关键词': word, '出现次数': count, '占比': f'{count/len(bullets)*100:.1f}%'}
        for i, (word, count) in enumerate(bullet_counter.most_common(50))
    ])
    bullet_words_df.to_excel(writer, sheet_name='五点高频词TOP50', index=False)
    
    # Sheet 4: 卖点类型分析
    selling_point_types = {
        '材质工艺': ['rattan', 'wicker', 'pe', 'steel', 'frame', 'durable', 'sturdy', 'weather', 'resistant', 'waterproof', 'uv', 'rust', 'aluminum', 'iron', 'wood', 'teak'],
        '舒适体验': ['comfortable', 'cushion', 'soft', 'padding', 'thick', 'cozy', 'relax', 'seat', 'seating', 'ergonomic'],
        '空间场景': ['patio', 'outdoor', 'garden', 'backyard', 'balcony', 'porch', 'deck', 'yard', 'lawn', 'terrace'],
        '安装使用': ['easy', 'assemble', 'assembly', 'install', 'installation', 'quick', 'simple', 'tools', 'manual', 'instruction'],
        '设计款式': ['modern', 'classic', 'elegant', 'stylish', 'design', 'beautiful', 'fashion', 'contemporary', 'traditional'],
        '功能用途': ['conversation', 'chat', 'relax', 'entertain', 'dining', 'lounge', 'rest', 'gathering', 'party'],
        '包装服务': ['warranty', 'service', 'customer', 'support', 'package', 'packaging', 'delivery', 'shipping', 'guarantee']
    }
    
    selling_point_stats = []
    for sp_type, keywords in selling_point_types.items():
        title_count = sum(1 for t in titles if any(kw in t.lower() for kw in keywords))
        bullet_count = sum(1 for b in bullets if any(kw in b.lower() for kw in keywords))
        selling_point_stats.append({
            '卖点类型': sp_type,
            '标题覆盖数': title_count,
            '标题覆盖率': f'{title_count/len(titles)*100:.1f}%',
            '五点覆盖数': bullet_count,
            '五点覆盖率': f'{bullet_count/len(bullets)*100:.1f}%',
            '相关关键词': ', '.join(keywords[:5]) + '...'
        })
    
    pd.DataFrame(selling_point_stats).to_excel(writer, sheet_name='卖点类型分析', index=False)
    
    # Sheet 5: 件套数分布
    numbers_in_titles = []
    for title in titles:
        nums = re.findall(r'\d+\s*(?:piece|pieces|pc|pcs|seater|seat)', title.lower())
        if nums:
            numbers_in_titles.extend(nums)
    number_counter = Counter(numbers_in_titles)
    
    piece_df = pd.DataFrame([
        {'件套数': num, '出现次数': count, '占比': f'{count/len(titles)*100:.1f}%'}
        for num, count in number_counter.most_common(15)
    ])
    piece_df.to_excel(writer, sheet_name='件套数分布', index=False)
    
    # Sheet 6: 场景词分析
    scene_words = ['patio', 'outdoor', 'garden', 'backyard', 'balcony', 'porch', 'deck', 'yard']
    scene_stats = []
    for word in scene_words:
        title_count = sum(1 for t in titles if word in t.lower())
        bullet_count = sum(1 for b in bullets if word in b.lower())
        scene_stats.append({
            '场景词': word,
            '标题出现数': title_count,
            '标题占比': f'{title_count/len(titles)*100:.1f}%',
            '五点出现数': bullet_count,
            '五点占比': f'{bullet_count/len(bullets)*100:.1f}%'
        })
    
    pd.DataFrame(scene_stats).to_excel(writer, sheet_name='场景词分析', index=False)
    
    # Sheet 7: 优秀案例
    df['综合得分'] = df['Rating'] * 0.3 + (df['Ratings']/df['Ratings'].max()) * 0.4 + (1 - (df['#']-1)/99) * 0.3
    top_listings = df.nlargest(10, '综合得分')
    
    top_listings_data = []
    for idx, row in top_listings.iterrows():
        top_listings_data.append({
            'BSR排名': row['#'],
            '品牌': row['Brand'],
            '价格': f"${row['Price($)']}",
            '评分': row['Rating'],
            '评论数': row['Ratings'],
            '标题': row['Product Title'],
            '标题长度': len(row['Product Title']),
            '五点': str(row['Bullet Points'])[:500] + '...' if len(str(row['Bullet Points'])) > 500 else str(row['Bullet Points'])
        })
    
    pd.DataFrame(top_listings_data).to_excel(writer, sheet_name='优秀案例TOP10', index=False)
    
    # Sheet 8: 完整数据
    df.to_excel(writer, sheet_name='完整数据', index=False)

print(f'✅ 分析报告生成完成！')
print(f'📁 文件路径: {output_path}')
