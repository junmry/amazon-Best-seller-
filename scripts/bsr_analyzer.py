#!/usr/bin/env python3
"""
BSR竞品分析自动化脚本
使用: python3 bsr_analyzer.py <BSR.xlsx> [输出目录]
"""

import pandas as pd
import re
from collections import Counter
import sys
import os
from datetime import datetime

def extract_words(text):
    """提取单词"""
    text = re.sub(r'[^\w\s]', ' ', str(text).lower())
    return [w for w in text.split() if len(w) > 2]

def analyze_titles(titles):
    """分析标题词频"""
    all_words = []
    for title in titles:
        all_words.extend(extract_words(title))
    return Counter(all_words)

def analyze_bsr(input_file, output_dir):
    """主分析流程"""
    print(f"📊 正在分析BSR: {input_file}")
    
    # 读取数据
    xl = pd.ExcelFile(input_file)
    sheet_name = xl.sheet_names[0]
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    
    print(f"   数据行数: {len(df)}")
    
    # 自动识别列名
    col_mapping = {}
    for col in df.columns:
        col_lower = str(col).lower()
        if any(k in col_lower for k in ['title', '标题', 'product title']):
            col_mapping['title'] = col
        if any(k in col_lower for k in ['bullet', '五点', 'point']):
            col_mapping['bullet'] = col
        if any(k in col_lower for k in ['brand', '品牌']):
            col_mapping['brand'] = col
        if any(k in col_lower for k in ['price', '价格', '$']):
            col_mapping['price'] = col
        if any(k in col_lower for k in ['rating', '评分', 'star']):
            col_mapping['rating'] = col
        if any(k in col_lower for k in ['review', '评论']):
            col_mapping['reviews'] = col
        if any(k in col_lower for k in ['bsr', 'rank', '排名']):
            col_mapping['bsr'] = col
    
    print(f"   识别列: {col_mapping}")
    
    # 创建输出
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = os.path.join(output_dir, f"BSR分析_{timestamp}.xlsx")
    
    writer = pd.ExcelWriter(output_file, engine='openpyxl')
    
    # ===== Sheet 1: 源数据 =====
    df.to_excel(writer, sheet_name='源数据', index=False)
    print("   ✓ 生成: 源数据")
    
    # ===== Sheet 2: TOP 20标题 =====
    if 'title' in col_mapping:
        top20 = df.head(20).copy()
        cols = []
        for key in ['bsr', 'brand', 'title', 'price', 'rating', 'reviews']:
            if key in col_mapping:
                cols.append(col_mapping[key])
        if cols:
            top20[cols].to_excel(writer, sheet_name='TOP20标题', index=False)
            print("   ✓ 生成: TOP20标题")
    
    # ===== Sheet 3: 标题词频分析 =====
    if 'title' in col_mapping:
        titles = df[col_mapping['title']].dropna().tolist()
        word_freq = analyze_titles(titles)
        
        # 排除常见停用词
        stop_words = {'and', 'the', 'with', 'for', 'from', 'that', 'this', 'have', 'has', 
                      'had', 'was', 'were', 'are', 'you', 'your', 'our', 'all', 'can'}
        
        word_data = []
        for word, count in word_freq.most_common(100):
            if word not in stop_words and not word.isdigit():
                pct = count / len(titles) * 100
                word_data.append({
                    '单词': word,
                    '频次': count,
                    '出现率': f"{pct:.1f}%",
                    '埋词建议': '必埋' if pct > 50 else ('建议' if pct > 20 else '可选')
                })
        
        pd.DataFrame(word_data).to_excel(writer, sheet_name='标题词频', index=False)
        print("   ✓ 生成: 标题词频")
        
        # 维度分析
        dimensions = {
            '颜色': ['white', 'black', 'red', 'blue', 'green', 'pink', 'purple', 'brown', 'beige'],
            '材质': ['leather', 'fabric', 'mesh', 'velvet', 'linen', 'faux', 'pu', 'suede'],
            '功能': ['footrest', 'lumbar', 'support', 'headrest', 'massage', 'adjustable', 'reclining'],
            '场景': ['office', 'home', 'gaming', 'desk', 'computer'],
            '人群': ['adults', 'kids', 'men', 'women', 'gamer']
        }
        
        dim_results = []
        for dim_name, keywords in dimensions.items():
            for kw in keywords:
                count = sum(1 for t in titles if kw in t.lower())
                if count > 0:
                    pct = count / len(titles) * 100
                    dim_results.append({
                        '维度': dim_name,
                        '关键词': kw,
                        '出现次数': count,
                        '占比': f"{pct:.1f}%",
                        '优先级': '高' if pct > 50 else ('中' if pct > 20 else '低')
                    })
        
        dim_df = pd.DataFrame(dim_results)
        dim_df = dim_df.sort_values(['维度', '占比'], ascending=[True, False])
        dim_df.to_excel(writer, sheet_name='维度分析', index=False)
        print("   ✓ 生成: 维度分析")
    
    # ===== Sheet 4: 五点分析 =====
    if 'bullet' in col_mapping:
        bullets = df[col_mapping['bullet']].dropna().tolist()
        
        # 提取五点主题
        themes = {
            '舒适度': ['comfort', 'comfortable', 'cozy', 'soft', 'ergonomic', 'support'],
            '材质': ['leather', 'fabric', 'foam', 'quality', 'material', 'durable'],
            '功能': ['adjustable', 'recline', 'massage', 'footrest', 'swivel', 'lumbar'],
            '安装': ['assembly', 'assemble', 'install', 'easy', 'instruction', 'manual'],
            '售后': ['warranty', 'service', 'support', 'replace', 'guarantee']
        }
        
        theme_results = []
        all_bullet_text = ' '.join([str(b).lower() for b in bullets])
        
        for theme_name, keywords in themes.items():
            total = 0
            for kw in keywords:
                total += all_bullet_text.count(kw)
            if total > 0:
                theme_results.append({
                    '主题': theme_name,
                    '总提及次数': total,
                    '平均每产品': f"{total/len(bullets):.1f}",
                    '五点位置建议': ['第1点', '第2点', '第3点', '第4点', '第5点'][len(theme_results) % 5]
                })
        
        pd.DataFrame(theme_results).to_excel(writer, sheet_name='五点主题', index=False)
        print("   ✓ 生成: 五点主题")
    
    # ===== Sheet 5: 价格分布 =====
    if 'price' in col_mapping:
        df_price = df[df[col_mapping['price']].notna()].copy()
        if len(df_price) > 0:
            price_col = col_mapping['price']
            
            # 价格区间统计
            bins = [0, 50, 100, 150, 200, 300, 500, 1000]
            labels = ['$0-50', '$50-100', '$100-150', '$150-200', '$200-300', '$300-500', '$500+']
            
            df_price['价格区间'] = pd.cut(df_price[price_col], bins=bins, labels=labels)
            price_dist = df_price['价格区间'].value_counts().sort_index()
            
            price_data = []
            for interval, count in price_dist.items():
                avg_bsr = df_price[df_price['价格区间'] == interval][col_mapping.get('bsr', df_price.columns[0])].mean() if 'bsr' in col_mapping else 0
                price_data.append({
                    '价格区间': interval,
                    '产品数量': count,
                    '占比': f"{count/len(df_price)*100:.1f}%",
                    '平均BSR': f"{avg_bsr:.0f}"
                })
            
            pd.DataFrame(price_data).to_excel(writer, sheet_name='价格分布', index=False)
            print("   ✓ 生成: 价格分布")
    
    # ===== Sheet 6: 品牌分析 =====
    if 'brand' in col_mapping:
        brand_col = col_mapping['brand']
        brand_stats = df[brand_col].value_counts().head(20)
        
        brand_data = []
        for brand, count in brand_stats.items():
            brand_df = df[df[brand_col] == brand]
            avg_price = brand_df[col_mapping['price']].mean() if 'price' in col_mapping else 0
            avg_rating = brand_df[col_mapping['rating']].mean() if 'rating' in col_mapping else 0
            
            brand_data.append({
                '品牌': brand,
                'BSR产品数': count,
                '平均价格': f"${avg_price:.2f}" if avg_price > 0 else '-',
                '平均评分': f"{avg_rating:.1f}" if avg_rating > 0 else '-'
            })
        
        pd.DataFrame(brand_data).to_excel(writer, sheet_name='品牌分析', index=False)
        print("   ✓ 生成: 品牌分析")
    
    # ===== Sheet 7: 洞察摘要 =====
    insights = []
    insights.append(['分析项', '数值', '洞察'])
    insights.append(['BSR样本数', len(df), '竞品分析样本量'])
    
    if 'title' in col_mapping:
        avg_title_len = df[col_mapping['title']].str.len().mean()
        insights.append(['平均标题长度', f"{avg_title_len:.0f}字符", '建议控制在150-200字符'])
    
    if 'price' in col_mapping:
        avg_price = df[col_mapping['price']].mean()
        min_price = df[col_mapping['price']].min()
        max_price = df[col_mapping['price']].max()
        insights.append(['平均价格', f"${avg_price:.2f}", f'价格区间 ${min_price:.0f}-${max_price:.0f}'])
    
    if 'rating' in col_mapping:
        avg_rating = df[col_mapping['rating']].mean()
        insights.append(['平均评分', f"{avg_rating:.1f}", '4.3+为优秀水平'])
    
    if 'reviews' in col_mapping:
        avg_reviews = df[col_mapping['reviews']].mean()
        insights.append(['平均评论数', f"{avg_reviews:.0f}", '评论积累程度'])
    
    insights.append(['', '', ''])
    insights.append(['标题公式建议', '', ''])
    insights.append(['Brand', '+', '品牌名'])
    insights.append(['核心词', '+', 'Gaming/Computer Chair'])
    insights.append(['功能', '+', 'with Footrest/Lumbar Support'])
    insights.append(['场景', '+', 'for Office/Gaming'])
    insights.append(['颜色', '', '(Black/White)'])
    
    pd.DataFrame(insights).to_excel(writer, sheet_name='洞察摘要', index=False, header=False)
    print("   ✓ 生成: 洞察摘要")
    
    # 保存
    writer.close()
    print(f"\n✅ 完成! 输出文件: {output_file}")
    
    return output_file

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 bsr_analyzer.py <BSR.xlsx> [输出目录]")
        print("Example: python3 bsr_analyzer.py BSR_Gaming_Chair.xlsx 分析输出/")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "BSR分析输出"
    
    if not os.path.exists(input_file):
        print(f"❌ 文件不存在: {input_file}")
        sys.exit(1)
    
    analyze_bsr(input_file, output_dir)
