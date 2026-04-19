#!/usr/bin/env python3
"""
关键词拆词自动化流水线
使用: python3 keyword_pipeline.py <输入.xlsx> [输出目录]
"""

import pandas as pd
import re
import sys
import os
from collections import defaultdict, Counter
from datetime import datetime

# 维度词典
DIMENSIONS = {
    '颜色': ['white', 'black', 'red', 'blue', 'green', 'pink', 'purple', 'yellow', 
            'orange', 'brown', 'grey', 'gray', 'beige', 'tan', 'silver', 'gold', 
            'camo', 'camouflage', 'teal', 'navy', 'ivory', 'cream'],
    
    '尺码': ['big', 'tall', 'large', 'small', 'compact', 'wide', 'narrow',
            '72', '78', '84', '96', '102', '120',
            '350', '400', '300', '330', '500', 'lbs', 'lb', 'pound',
            '2 seater', '3 seater', '4 seater', 'loveseat', 'sectional'],
    
    '人群': ['adults', 'kids', 'children', 'baby', 'teen', 'teenager', 
            'boy', 'girl', 'men', 'women', 'man', 'woman', 
            'gamer', 'gamers', 'student', 'kid', 'child', 'family'],
    
    '款式': ['gaming', 'racing', 'ergonomic', 'office', 'computer', 'desk', 
            'executive', 'task', 'swivel', 'rocking', 'recliner', 'reclining',
            'high back', 'mid back', 'low back', 'racing style', 
            'modern', 'contemporary', 'classic', 'vintage', 'industrial'],
    
    '材质': ['leather', 'fabric', 'mesh', 'velvet', 'linen', 'faux', 
            'pu', 'pvc', 'suede', 'cloth', 'canvas', 'nylon', 
            'polyester', 'synthetic', 'microfiber', 'chenille', 'boucle'],
    
    '场景': ['home', 'office', 'bedroom', 'living room', 'game room', 
            'studio', 'work', 'pc', 'computer desk', 'apartment', 
            'dorm', 'study', 'library', 'conference', 'waiting room'],
    
    '功能': ['massage', 'heated', 'heating', 'cooling', 'lumbar', 'support', 
            'footrest', 'adjustable', 'recline', 'reclining', 'swivel', 
            'rolling', 'wheels', 'armrest', 'headrest', 'pillow', 
            'cushion', 'spring', 'pocket', 'storage', 'cup holder',
            'usb', 'charging', 'led', 'rgb', 'folding', 'convertible'],
    
    '价格': ['cheap', 'affordable', 'budget', 'economy', 'value',
            'expensive', 'luxury', 'premium', 'high end', 'designer',
            'sale', 'deal', 'discount', 'clearance', 'under', 'below',
            'dollar', 'price', 'cost'],
    
    '品牌': ['ikea', 'amazon basics', 'yaheetech', 'homall', 'gtplayer',
            'dowinx', 'n-gen', 'ngen', 'razer', 'secretlab', 'herman miller',
            'steelcase', 'haworth', 'humanscale', 'branch', 'autonomous']
}

def clean_keyword(keyword):
    """清洗关键词"""
    if pd.isna(keyword):
        return ""
    return str(keyword).strip().lower()

def extract_words(text):
    """提取所有单词"""
    text = re.sub(r'[^\w\s]', ' ', str(text).lower())
    return [w for w in text.split() if len(w) > 2]

def match_dimension(keyword, dim_words):
    """判断关键词属于哪个维度"""
    keyword_lower = keyword.lower()
    matches = []
    for word in dim_words:
        pattern = rf'\b{re.escape(word)}\b'
        if re.search(pattern, keyword_lower):
            matches.append(word)
    return matches

def analyze_keywords(input_file, output_dir):
    """主分析流程"""
    print(f"📊 正在分析: {input_file}")
    
    # 读取数据
    df = pd.read_excel(input_file)
    original_cols = df.columns.tolist()
    
    # 自动识别列名
    keyword_col = None
    volume_col = None
    for col in original_cols:
        col_lower = str(col).lower()
        if any(k in col_lower for k in ['关键词', 'keyword', 'search term']):
            keyword_col = col
        if any(v in col_lower for v in ['搜索量', 'volume', 'search volume', 'sv']):
            volume_col = col
    
    if not keyword_col:
        keyword_col = original_cols[0]
    if not volume_col and len(original_cols) > 1:
        volume_col = original_cols[1]
    
    print(f"   识别列: 关键词={keyword_col}, 搜索量={volume_col}")
    
    # 清洗数据
    df = df[df[keyword_col].notna()].copy()
    if volume_col:
        df = df[df[volume_col] > 0].copy()
        df = df.sort_values(volume_col, ascending=False).reset_index(drop=True)
    
    total_keywords = len(df)
    print(f"   有效关键词: {total_keywords} 条")
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = os.path.join(output_dir, f"拆词结果_{timestamp}.xlsx")
    
    # 创建Excel写入器
    writer = pd.ExcelWriter(output_file, engine='openpyxl')
    
    # ===== Sheet 1: 源文件 =====
    df['序号'] = range(1, len(df) + 1)
    cols_order = ['序号'] + original_cols
    df[cols_order].to_excel(writer, sheet_name='源文件', index=False)
    print("   ✓ 生成: 源文件")
    
    # ===== Sheet 2: 筛选（按搜索量排序） =====
    if volume_col:
        df_filter = df[['序号', keyword_col, volume_col]].copy()
        if '翻译' in original_cols:
            df_filter['翻译'] = df['翻译']
    else:
        df_filter = df[['序号', keyword_col]].copy()
    df_filter.to_excel(writer, sheet_name='筛选', index=False)
    print("   ✓ 生成: 筛选")
    
    # ===== Sheet 3: 筛选后词（所有拆分出的词） =====
    all_words = []
    for idx, row in df.iterrows():
        kw = clean_keyword(row[keyword_col])
        vol = row[volume_col] if volume_col else 0
        words = extract_words(kw)
        for w in words:
            all_words.append({
                '词': w,
                '搜索词': kw,
                '搜索量': vol
            })
    
    word_df = pd.DataFrame(all_words)
    if len(word_df) > 0:
        word_stats = word_df.groupby('词').agg({
            '搜索词': 'count',
            '搜索量': 'sum'
        }).reset_index()
        word_stats.columns = ['词', '出现次数', '总搜索量']
        word_stats['平均搜索量'] = (word_stats['总搜索量'] / word_stats['出现次数']).round(0)
        word_stats = word_stats.sort_values('总搜索量', ascending=False).reset_index(drop=True)
        word_stats['序号'] = range(1, len(word_stats) + 1)
        word_stats = word_stats[['序号', '词', '出现次数', '总搜索量', '平均搜索量']]
        word_stats.to_excel(writer, sheet_name='筛选后词', index=False)
        print("   ✓ 生成: 筛选后词")
    
    # ===== 各维度Sheet =====
    def create_dimension_sheet(dim_name, keywords):
        result = []
        
        for target_word in keywords:
            pattern = rf'\b{re.escape(target_word)}\b'
            mask = df[keyword_col].astype(str).str.contains(pattern, case=False, na=False, regex=True)
            matched = df[mask].copy()
            
            if len(matched) == 0:
                continue
            
            # 按搜索量排序
            if volume_col:
                matched = matched.sort_values(volume_col, ascending=False).reset_index(drop=True)
            
            # 添加主词行
            total_vol = matched[volume_col].sum() if volume_col else 0
            first_row = {
                '序号': len(result) + 1,
                '主词': target_word,
                '副词': '',
                '次副词': '',
                '搜索词': matched.iloc[0][keyword_col],
                '搜索量': matched.iloc[0][volume_col] if volume_col else 0,
                '分组总搜索量': total_vol
            }
            if '翻译' in original_cols:
                first_row['翻译'] = matched.iloc[0].get('翻译', '')
            result.append(first_row)
            
            # 添加后续行（主词留空）
            for i in range(1, min(len(matched), 100)):  # 限制每词最多100条
                row_data = {
                    '序号': len(result) + 1,
                    '主词': '',
                    '副词': '',
                    '次副词': '',
                    '搜索词': matched.iloc[i][keyword_col],
                    '搜索量': matched.iloc[i][volume_col] if volume_col else 0,
                    '分组总搜索量': ''
                }
                if '翻译' in original_cols:
                    row_data['翻译'] = matched.iloc[i].get('翻译', '')
                result.append(row_data)
        
        return pd.DataFrame(result)
    
    # 生成各维度sheet
    for dim_name, keywords in DIMENSIONS.items():
        df_dim = create_dimension_sheet(dim_name, keywords)
        if len(df_dim) > 0:
            df_dim.to_excel(writer, sheet_name=dim_name, index=False)
            print(f"   ✓ 生成: {dim_name} ({len(df_dim)} 行)")
    
    # ===== Sheet: 高价值词 =====
    if volume_col:
        # 筛选搜索量适中的高价值词
        high_value = df[(df[volume_col] >= 1000) & (df[volume_col] <= 50000)].copy()
        high_value = high_value.sort_values(volume_col, ascending=False).head(200)
        
        # 标记类型
        def tag_keyword_type(kw):
            kw_lower = str(kw).lower()
            tags = []
            if any(w in kw_lower for w in ['cheap', 'budget', 'affordable', 'under', 'sale']):
                tags.append('价格敏感')
            if any(w in kw_lower for w in ['pink', 'white', 'black', 'purple', 'red']):
                tags.append('颜色明确')
            if any(w in kw_lower for w in ['big', 'tall', 'large', 'small']):
                tags.append('尺寸明确')
            if any(w in kw_lower for w in ['massage', 'heated', 'footrest', 'lumbar']):
                tags.append('功能明确')
            if any(w in kw_lower for w in ['adults', 'kids', 'gamer']):
                tags.append('人群明确')
            return ','.join(tags) if tags else '通用'
        
        high_value['标签'] = high_value[keyword_col].apply(tag_keyword_type)
        high_value['埋词建议'] = high_value[keyword_col].apply(
            lambda x: '标题' if len(str(x)) < 30 else ('五点' if len(str(x)) < 80 else '后台')
        )
        
        cols = ['序号', keyword_col, volume_col, '标签', '埋词建议']
        if '翻译' in original_cols:
            cols.insert(3, '翻译')
        high_value[cols].to_excel(writer, sheet_name='高价值词', index=False)
        print("   ✓ 生成: 高价值词")
    
    # ===== Sheet: 洞察摘要 =====
    insights = []
    
    # 整体统计
    insights.append(['统计项', '数值', '说明'])
    insights.append(['总关键词数', total_keywords, '去重后有效数据'])
    if volume_col:
        total_volume = df[volume_col].sum()
        avg_volume = df[volume_col].mean()
        insights.append(['总搜索量', f"{total_volume:,}", '所有关键词搜索量之和'])
        insights.append(['平均搜索量', f"{avg_volume:.0f}", '单关键词平均搜索量'])
        insights.append(['Top 10占比', f"{df.head(10)[volume_col].sum()/total_volume*100:.1f}%", '头部集中度'])
    
    insights.append(['', '', ''])
    insights.append(['维度', 'Top关键词', '总搜索量/占比', '建议'])
    
    # 各维度Top词
    for dim_name, keywords in DIMENSIONS.items():
        top_word = None
        top_volume = 0
        for word in keywords:
            pattern = rf'\b{re.escape(word)}\b'
            mask = df[keyword_col].astype(str).str.contains(pattern, case=False, na=False, regex=True)
            matched = df[mask]
            if volume_col and len(matched) > 0:
                vol = matched[volume_col].sum()
                if vol > top_volume:
                    top_volume = vol
                    top_word = word
        
        if top_word and volume_col:
            pct = top_volume / total_volume * 100
            insights.append([
                dim_name, 
                top_word, 
                f"{top_volume:,} ({pct:.1f}%)",
                '核心必埋' if pct > 10 else '建议埋入'
            ])
    
    pd.DataFrame(insights).to_excel(writer, sheet_name='洞察摘要', index=False, header=False)
    print("   ✓ 生成: 洞察摘要")
    
    # 保存
    writer.close()
    print(f"\n✅ 完成! 输出文件: {output_file}")
    
    # 生成文本报告
    report_file = os.path.join(output_dir, f"拆词报告_{timestamp}.md")
    generate_report(df, keyword_col, volume_col, report_file, total_keywords)
    print(f"✅ 报告文件: {report_file}")
    
    return output_file, report_file

def generate_report(df, keyword_col, volume_col, report_file, total_keywords):
    """生成Markdown报告"""
    report = f"""# 关键词拆词分析报告

**分析时间**: {datetime.now().strftime("%Y-%m-%d %H:%M")}  
**数据来源**: {total_keywords} 条关键词

---

## 一、整体概况

"""
    
    if volume_col:
        total_vol = df[volume_col].sum()
        avg_vol = df[volume_col].mean()
        top10_vol = df.head(10)[volume_col].sum()
        
        report += f"""
| 指标 | 数值 |
|:-----|:-----|
| 总关键词数 | {total_keywords} |
| 总搜索量 | {total_vol:,} |
| 平均搜索量 | {avg_vol:.0f} |
| Top 10占比 | {top10_vol/total_vol*100:.1f}% |
| 中位数搜索量 | {df[volume_col].median():.0f} |
"""
    
    report += "\n## 二、搜索量 TOP 20\n\n"
    report += "| 排名 | 关键词 | 搜索量 | 类型 |\n"
    report += "|:----:|:-------|:------:|:-----|\n"
    
    for i in range(min(20, len(df))):
        row = df.iloc[i]
        kw = str(row[keyword_col])[:40]
        vol = row[volume_col] if volume_col else 0
        
        # 判断类型
        kw_lower = str(row[keyword_col]).lower()
        if any(w in kw_lower for w in ['chair', 'sofa', 'couch']):
            kw_type = '产品词'
        elif any(w in kw_lower for w in ['cheap', 'under', 'budget']):
            kw_type = '价格词'
        elif any(w in kw_lower for w in ['pink', 'white', 'black']):
            kw_type = '颜色词'
        else:
            kw_type = '属性词'
        
        report += f"| {i+1} | {kw} | {vol:,} | {kw_type} |\n"
    
    report += "\n## 三、各维度Top词\n\n"
    
    for dim_name, keywords in DIMENSIONS.items():
        report += f"### {dim_name}\n\n"
        report += "| 关键词 | 出现次数 | 总搜索量 | 平均搜索量 |\n"
        report += "|:-------|:--------:|:--------:|:----------:|\n"
        
        dim_data = []
        for word in keywords:
            pattern = rf'\b{re.escape(word)}\b'
            mask = df[keyword_col].astype(str).str.contains(pattern, case=False, na=False, regex=True)
            matched = df[mask]
            if len(matched) > 0:
                count = len(matched)
                total = matched[volume_col].sum() if volume_col else 0
                avg = total / count if count > 0 else 0
                dim_data.append((word, count, total, avg))
        
        # 按总搜索量排序，取前10
        dim_data.sort(key=lambda x: x[2], reverse=True)
        for word, count, total, avg in dim_data[:10]:
            report += f"| {word} | {count} | {total:,} | {avg:.0f} |\n"
        
        report += "\n"
    
    report += """## 四、埋词建议

### 标题必埋词
"""
    
    # 找出高频高搜索量的词
    if volume_col:
        top_for_title = df[df[keyword_col].str.len() < 40].head(10)
        for i, row in top_for_title.iterrows():
            report += f"- {row[keyword_col]} ({row[volume_col]:,})\n"
    
    report += """
### 五点描述关键词
"""
    
    if volume_col:
        top_for_bullet = df[(df[keyword_col].str.len() >= 20) & (df[keyword_col].str.len() < 80)].head(10)
        for i, row in top_for_bullet.iterrows():
            report += f"- {row[keyword_col]} ({row[volume_col]:,})\n"
    
    report += """
### 后台Search Terms
"""
    
    # 收集所有维度词
    all_dim_words = []
    for words in DIMENSIONS.values():
        all_dim_words.extend(words)
    
    report += f"```\n{', '.join(all_dim_words[:50])}\n```\n"
    
    report += f"""

---
*报告由关键词拆词流水线自动生成*
"""
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 keyword_pipeline.py <输入.xlsx> [输出目录]")
        print("Example: python3 keyword_pipeline.py 游戏椅关键词.xlsx 输出/")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "拆词输出"
    
    if not os.path.exists(input_file):
        print(f"❌ 文件不存在: {input_file}")
        sys.exit(1)
    
    analyze_keywords(input_file, output_dir)
