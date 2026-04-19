#!/usr/bin/env python3
import pandas as pd
import re
from collections import defaultdict

# 读取椅子关键词
input_path = '/root/openclaw/kimi/downloads/19d0a2b6-56b2-86b3-8000-0000caeb05b9_椅子关键词.xlsx'
df = pd.read_excel(input_path)
keywords = df['关键词'].dropna().astype(str).tolist()
volumes = df['搜索量'].fillna(0).astype(int).tolist()

# 定义椅子各维度词典
dimensions = {
    '颜色': {
        '主词': ['white', 'black', 'brown', 'gray', 'grey', 'blue', 'red', 'green', 'beige', 'tan', 'cream', 'ivory', 
                'pink', 'purple', 'yellow', 'orange', 'navy', 'teal', 'turquoise', 'burgundy', 'maroon', 'charcoal',
                'dark', 'light', 'natural', 'walnut', 'oak', 'espresso', 'mahogany'],
        '副词': ['chair', 'chairs', 'accent chair', 'armchair', 'recliner', 'furniture']
    },
    '尺码': {
        '主词': ['small', 'large', 'big', 'mini', 'compact', 'oversized', 'oversize', 'tiny', 
                'wide', 'narrow', 'tall', 'short', 'low', 'high',
                'single', 'double', 'queen', 'king', 'full'],
        '副词': ['chair', 'chairs', 'armchair', 'recliner', 'accent chair']
    },
    '人群': {
        '主词': ['kids', 'kid', 'children', 'child', 'baby', 'toddler', 'family', 'pet', 'dog', 'cat', 
                'boys', 'boy', 'girls', 'girl', 'men', 'man', 'women', 'woman', 'adult', 'senior', 'teen',
                'elderly', 'nursery', 'infant'],
        '副词': ['chair', 'chairs', 'furniture', 'armchair', 'recliner']
    },
    '款式': {
        '主词': ['accent', 'armchair', 'arm', 'wingback', 'wing', 'club', 'tub', 'slipper', 
                'recliner', 'reclining', 'rocking', 'rocker', 'glider', 'swivel', 
                'barrel', 'club', 'parsons', 'side', 'slipper', 'chaise', 'lounge',
                'mid century', 'modern', 'contemporary', 'traditional', 'classic', 
                'vintage', 'rustic', 'farmhouse', 'industrial', 'scandinavian',
                'tufted', 'upholstered', 'padded', 'cushioned', 'wingback'],
        '副词': ['chair', 'chairs']
    },
    '材质': {
        '主词': ['leather', 'velvet', 'linen', 'fabric', 'microfiber', 'suede', 'faux leather', 
                'pu leather', 'bonded leather', 'chenille', 'canvas', 'wicker', 'rattan',
                'wood', 'wooden', 'metal', 'plastic', 'acrylic', 'wrought iron'],
        '副词': ['chair', 'chairs', 'armchair', 'accent chair']
    },
    '场景': {
        '主词': ['living room', 'bedroom', 'dining', 'kitchen', 'office', 'desk', 'study', 
                'nursery', 'baby room', 'entryway', 'hallway', 'foyer', 'porch', 'patio',
                'outdoor', 'garden', 'balcony', 'deck', 'sunroom', 'reading', 'lounge',
                'waiting room', 'reception', 'lobby', 'conference', 'meeting',
                'apartment', 'studio', 'dorm', 'college', 'home'],
        '副词': ['chair', 'chairs', 'furniture', 'armchair', 'accent chair']
    },
    '功能': {
        '主词': ['reclining', 'recliner', 'rocking', 'rocker', 'glider', 'swivel', 'folding', 
                'foldable', 'stackable', 'adjustable', 'massage', 'heating', 'heated',
                'ergonomic', 'lumbar support', 'sleeper', 'convertible', 'storage',
                'with ottoman', 'with footrest', 'lift', 'power lift'],
        '副词': ['chair', 'chairs', 'armchair']
    },
    '价格': {
        '主词': ['cheap', 'affordable', 'budget', 'inexpensive', 'discount', 'sale', 
                'luxury', 'premium', 'designer', 'high end', 'expensive'],
        '副词': ['chair', 'chairs', 'furniture', 'armchair']
    },
    '品牌': {
        '主词': ['ikea', 'ashley', 'wayfair', 'amazon', 'walmart', 'target', 'herman miller'],
        '副词': ['chair', 'chairs']
    }
}

def extract_dimension_data(keywords, volumes, dim_config):
    """提取某个维度的数据，按主词-副词层级组织，主词分组显示"""
    groups = defaultdict(list)
    
    for main_word in dim_config['主词']:
        main_word_lower = main_word.lower()
        for kw, vol in zip(keywords, volumes):
            kw_lower = kw.lower()
            if main_word_lower in kw_lower:
                副词 = ''
                次副词 = '无属性'
                for sub_word in dim_config['副词']:
                    if sub_word in kw_lower:
                        副词 = sub_word
                        break
                if not 副词:
                    副词 = 'chair'
                
                groups[main_word].append({
                    '副词': 副词,
                    '次副词': 次副词,
                    '搜索词': kw,
                    '搜索量': vol
                })
    
    for main_word in groups:
        groups[main_word].sort(key=lambda x: -x['搜索量'])
    
    results = []
    idx = 1
    for main_word in sorted(groups.keys()):
        items = groups[main_word]
        for i, item in enumerate(items):
            results.append({
                '序号': idx,
                '主词': main_word if i == 0 else None,
                '副词': item['副词'] if i == 0 else None,
                '次副词': item['次副词'] if i == 0 else None,
                '搜索词': item['搜索词'],
                '搜索量': item['搜索量']
            })
            idx += 1
    
    return results

# 创建Excel writer
output_path = '/root/.openclaw/workspace/椅子关键词拆词_完整层级.xlsx'

with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    
    # 1. 源文件
    df.to_excel(writer, sheet_name='源文件', index=False)
    
    # 2. 筛选
    df_sorted = df.sort_values('搜索量', ascending=False).reset_index(drop=True)
    df_sorted.insert(0, '序号', range(1, len(df_sorted) + 1))
    df_sorted.to_excel(writer, sheet_name='筛选', index=False)
    
    # 3. 筛选后词
    all_words = defaultdict(lambda: {'count': 0, 'volume': 0})
    for kw, vol in zip(keywords, volumes):
        words = re.findall(r'[a-z]+', kw.lower())
        for w in words:
            if len(w) > 1:
                all_words[w]['count'] += 1
                all_words[w]['volume'] += vol
    
    words_df = pd.DataFrame([
        {'词': w, '出现次数': stats['count'], '搜索量': stats['volume']}
        for w, stats in sorted(all_words.items(), key=lambda x: -x[1]['count'])
    ])
    words_df.to_excel(writer, sheet_name='筛选后词', index=False)
    
    # 4-12. 各维度
    for dim_name, dim_config in dimensions.items():
        data = extract_dimension_data(keywords, volumes, dim_config)
        if data:
            dim_df = pd.DataFrame(data)
            dim_df.to_excel(writer, sheet_name=dim_name, index=False)

print(f'✅ 椅子关键词拆词完成！')
print(f'文件保存至: {output_path}')
print(f'\n📊 各维度统计:')
for dim_name, dim_config in dimensions.items():
    data = extract_dimension_data(keywords, volumes, dim_config)
    print(f'  {dim_name}: {len(data)} 条')
