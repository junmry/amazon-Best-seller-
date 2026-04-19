#!/usr/bin/env python3
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import re
from collections import defaultdict, Counter

# 读取关键词拓词文件
kw_file = '/root/.openclaw/workspace/.kimi/downloads/19d7133a-65b2-83dc-8000-0000e8e51f53_variantExtendKeyword_fzdjfremcnz1775720684719_1775720697854.xlsx'
df_kw = pd.read_excel(kw_file, header=1)

keywords = df_kw['关键词'].dropna().astype(str).tolist()
volumes = df_kw['搜索量'].fillna(0).astype(int).tolist()

print(f'共读取 {len(keywords)} 个关键词')

# 定义Sofa/Console Table维度词典
dimensions = {
    '产品词': {
        '主词': ['table', 'console', 'sofa', 'couch', 'entryway', 'hallway', 'foyer', 'entry'],
        '副词': ['table', 'console', 'sofa', 'couch']
    },
    '尺寸规格': {
        '主词': ['narrow', 'long', 'small', 'skinny', 'thin', 'slim', 'wide', 'large', 'tall', 'short',
                '5 inch', '6 inch', '7 inch', '8 inch', '9 inch', '10 inch', '11 inch', '12 inch',
                '36 inch', '40 inch', '47 inch', '55 inch', '60 inch', '70 inch', '78 inch', '80 inch', '100 inch'],
        '副词': ['table', 'console', 'sofa']
    },
    '场景位置': {
        '主词': ['behind', 'entryway', 'hallway', 'foyer', 'entry', 'living room', 'corridor', 'mudroom', 'porch'],
        '副词': ['sofa', 'couch', 'table', 'console']
    },
    '功能卖点': {
        '主词': ['power', 'outlet', 'usb', 'charging', 'storage', 'shelf', 'drawer', 'adjustable', 'outlets', 'station'],
        '副词': ['table', 'console', 'sofa']
    },
    '材质风格': {
        '主词': ['wood', 'metal', 'industrial', 'farmhouse', 'rustic', 'modern', 'contemporary', 'solid wood', 'oak', 'walnut'],
        '副词': ['table', 'console']
    },
    '结构设计': {
        '主词': ['tier', 'shelf', 'shelves', 'drawer', 'drawers', 'open', 'closed', 'glass', 'top'],
        '副词': ['table', 'console']
    },
    '使用人群': {
        '主词': ['small space', 'apartment', 'narrow space', 'tight space', 'compact'],
        '副词': ['table', 'console', 'sofa']
    }
}

def extract_dimension_data(keywords, volumes, dim_config):
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
                    副词 = 'table'
                
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
output_path = '/root/.openclaw/workspace/SofaConsoleTable_关键词拆词.xlsx'

with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    
    # 1. 源文件
    df_kw.to_excel(writer, sheet_name='源文件', index=False)
    
    # 2. 筛选 - 按搜索量排序
    df_sorted = df_kw.sort_values('搜索量', ascending=False).reset_index(drop=True)
    df_sorted.insert(0, '序号', range(1, len(df_sorted) + 1))
    df_sorted.to_excel(writer, sheet_name='筛选', index=False)
    
    # 3. 筛选后词 - 所有拆分出的词
    all_words = defaultdict(lambda: {'count': 0, 'volume': 0})
    for kw, vol in zip(keywords, volumes):
        words = re.findall(r'[a-z]+', kw.lower())
        for w in words:
            if len(w) > 2:
                all_words[w]['count'] += 1
                all_words[w]['volume'] += vol
    
    words_df = pd.DataFrame([
        {'词': w, '出现次数': stats['count'], '搜索量': stats['volume']}
        for w, stats in sorted(all_words.items(), key=lambda x: -x[1]['count'])
    ])
    words_df.to_excel(writer, sheet_name='筛选后词', index=False)
    
    # 4-10. 各维度
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

# 打印TOP词
print(f'\n=== TOP 20 高频词 ===')
for word, stats in sorted(all_words.items(), key=lambda x: -x[1]['count'])[:20]:
    print(f'  {word:20s}: 出现{stats["count"]:4d}次  搜索量{stats["volume"]:8d}')

print(f'\n=== TOP 20 高搜索量词 ===')
for word, stats in sorted(all_words.items(), key=lambda x: -x[1]['volume'])[:20]:
    print(f'  {word:20s}: 搜索量{stats["volume"]:8d}  出现{stats["count"]:4d}次')
