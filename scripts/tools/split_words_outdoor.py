#!/usr/bin/env python3
import pandas as pd
import re
from collections import defaultdict

# 读取户外家具关键词文件
file_path = '/root/.openclaw/workspace/.kimi/downloads/19d6fecc-d3d2-8dc2-8000-000020ffc7a9_variantExtendKeyword_jjktraqhcsi1775699208038_1775699221086.xlsx'
df = pd.read_excel(file_path, header=1)  # 第1行是表头

# 获取关键词和搜索量
keywords = df['关键词'].dropna().astype(str).tolist()
volumes = df['搜索量'].fillna(0).astype(int).tolist()

print(f'共读取 {len(keywords)} 个关键词')
print(f'前5个关键词: {keywords[:5]}')
print(f'前5个搜索量: {volumes[:5]}')

# 定义各维度词典 - 针对户外家具场景优化
dimensions = {
    '颜色': {
        '主词': ['white', 'black', 'brown', 'gray', 'grey', 'blue', 'red', 'green', 'beige', 'tan', 'cream', 'ivory', 
                'pink', 'purple', 'yellow', 'orange', 'navy', 'teal', 'turquoise', 'burgundy', 'maroon', 'charcoal', 'gray'],
        '副词': ['patio', 'furniture', 'wicker', 'rattan', 'outdoor', 'set', 'sofa', 'sectional', 'table', 'chair']
    },
    '尺码': {
        '主词': ['small', 'large', 'big', 'mini', 'compact', 'oversized', 'tiny', '2 piece', '3 piece', '4 piece', '5 piece', '6 piece', '7 piece',
                'two piece', 'three piece', 'four piece', 'five piece', 'six piece', 'seven piece',
                '4 piece', '5 piece', '6 piece', '7 piece', 'modular'],
        '副词': ['patio', 'furniture', 'set', 'wicker', 'rattan', 'outdoor', 'sofa', 'sectional']
    },
    '人群': {
        '主词': ['kids', 'kid', 'children', 'child', 'baby', 'toddler', 'family', 'pet', 'dog', 'cat', 
                'boys', 'boy', 'girls', 'girl', 'adult', 'senior', 'teen'],
        '副词': ['patio', 'furniture', 'set', 'outdoor', 'wicker', 'rattan']
    },
    '款式': {
        '主词': ['sectional', 'l shape', 'l shaped', 'modular', 'corner', 'chaise', 'conversation', 
                'loveseat', 'chesterfield', 'mid century', 'modern', 'traditional', 
                'classic', 'vintage', 'rustic', 'farmhouse', 'tufted', 'recliner', 'sleeper'],
        '副词': ['patio', 'furniture', 'set', 'outdoor', 'wicker', 'rattan']
    },
    '材质': {
        '主词': ['wicker', 'rattan', 'resin wicker', 'pe wicker', 'metal', 'aluminum', 'wood', 'teak', 'plastic', 'acacia', 'steel'],
        '副词': ['patio', 'furniture', 'set', 'outdoor', 'sectional', 'sofa']
    },
    '场景': {
        '主词': ['outdoor', 'patio', 'garden', 'backyard', 'porch', 'deck', 'balcony', 'terrace', 'gazebo', 'pool', 'lawn', 'yard'],
        '副词': ['furniture', 'set', 'wicker', 'rattan', 'sectional', 'sofa']
    },
    '功能': {
        '主词': ['sleeper', 'convertible', 'folding', 'reclining', 'swivel', 'storage', 'adjustable', 'stackable'],
        '副词': ['patio', 'furniture', 'set', 'outdoor', 'sofa', 'sectional']
    },
    '价格': {
        '主词': ['cheap', 'affordable', 'budget', 'discount', 'luxury', 'premium', 'expensive'],
        '副词': ['patio', 'furniture', 'set', 'outdoor', 'wicker', 'rattan']
    },
    '品牌': {
        '主词': ['ikea', 'ashley', 'wayfair', 'amazon', 'walmart', 'target', 'aoxun', 'devoko', 'homall', 'yaheetech'],
        '副词': ['patio', 'furniture', 'set', 'outdoor', 'wicker', 'rattan']
    },
    '产品类型': {
        '主词': ['furniture set', 'sectional', 'sofa set', 'dining set', 'bistro set', 'lounge set', 'conversation set', 'seating set'],
        '副词': ['patio', 'outdoor', 'wicker', 'rattan', 'garden']
    }
}

def extract_dimension_data(keywords, volumes, dim_config):
    """提取某个维度的数据，按主词-副词层级组织，主词分组显示"""
    # 按主词分组存储
    groups = defaultdict(list)
    
    for main_word in dim_config['主词']:
        main_word_lower = main_word.lower()
        for kw, vol in zip(keywords, volumes):
            kw_lower = kw.lower()
            if main_word_lower in kw_lower:
                # 判断副词
                副词 = ''
                次副词 = '无属性'
                for sub_word in dim_config['副词']:
                    if sub_word in kw_lower:
                        副词 = sub_word
                        break
                if not 副词:
                    副词 = 'furniture'
                
                groups[main_word].append({
                    '副词': 副词,
                    '次副词': 次副词,
                    '搜索词': kw,
                    '搜索量': vol
                })
    
    # 按搜索量排序每个主词组内的数据
    for main_word in groups:
        groups[main_word].sort(key=lambda x: -x['搜索量'])
    
    # 构建最终结果，主词只在第一行显示
    results = []
    idx = 1
    for main_word in sorted(groups.keys()):
        items = groups[main_word]
        for i, item in enumerate(items):
            results.append({
                '序号': idx,
                '主词': main_word if i == 0 else None,  # 只在第一行显示主词
                '副词': item['副词'] if i == 0 else None,  # 只在第一行显示副词
                '次副词': item['次副词'] if i == 0 else None,
                '搜索词': item['搜索词'],
                '搜索量': item['搜索量']
            })
            idx += 1
    
    return results

# 创建Excel writer
output_path = '/root/.openclaw/workspace/户外家具关键词拆词_完整层级V2.xlsx'

with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    
    # 1. 源文件
    df.to_excel(writer, sheet_name='源文件', index=False)
    
    # 2. 筛选 - 按搜索量排序
    df_sorted = df.sort_values('搜索量', ascending=False).reset_index(drop=True)
    df_sorted.insert(0, '序号', range(1, len(df_sorted) + 1))
    df_sorted.to_excel(writer, sheet_name='筛选', index=False)
    
    # 3. 筛选后词 - 所有拆分出的词
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
    
    # 4-13. 各维度
    total_count = 0
    for dim_name, dim_config in dimensions.items():
        data = extract_dimension_data(keywords, volumes, dim_config)
        if data:
            dim_df = pd.DataFrame(data)
            dim_df.to_excel(writer, sheet_name=dim_name, index=False)
            total_count += len(data)
            print(f'  {dim_name}: {len(data)} 条')

print(f'\n✅ 拆词完成！')
print(f'📁 文件保存至: {output_path}')
print(f'📊 总维度条目: {total_count}')
