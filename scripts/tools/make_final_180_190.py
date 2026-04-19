#!/usr/bin/env python3
"""
KEIKI 泰迪绒沙发标题 - 最终版 180-190字符
搜索量优化 + 格式正确
"""

import pandas as pd

titles_final = [
    # Beige 系列
    ("XS-W5656S00073", "Beige", "2S", 'KEIKI 68.5" Cozy Neutral Loveseat Sofa Teddy Fleece Fabric Couch, Compact 2-Seat Design with Deep Cloud-Like Comfort Perfect for Living Room Lounging, Beige'),
    ("XS-W5656S00075", "Beige", "2S+1O", 'KEIKI 68.5" Warm Elegant Loveseat Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Ergonomic Curved Design Ideal for Bedroom Comfort and Relaxation, Beige'),
    ("XS-W5656S00078", "Beige", "2S+2O", 'KEIKI 68.5" Soft Inviting Modular Loveseat Teddy Fleece Fabric Couch with 2 Storage Ottomans, Plush Cushion Support Designed for Apartment Living Space, Beige'),
    ("XS-W5656S00080", "Beige", "3S", 'KEIKI 98.2" Modern Beige Oversized Couch Teddy Fleece Fabric, Spacious 3-Seat Design with Luxurious Lounging Experience Perfect for Your Home Studio Space, Beige'),
    ("XS-W5656S00082", "Beige", "3S+1O", 'KEIKI 98.2" Elegant Cream Sectional Sofa Teddy Fleece Fabric Couch with Storage Ottoman, Ultimate Relaxation Design for Modern Office Environment, Beige'),
    ("XS-W5656S00084", "Beige", "3S+2O", 'KEIKI 98.2" Cozy Neutral Modular Sectional Teddy Fleece Fabric Couch with 2 Ottomans, Deep Cloud-Like Comfort Perfect for Living Room Relaxation Time, Beige'),
    ("XS-W5656S00085", "Beige", "4S", 'KEIKI 129.1" Warm Elegant Large Sectional Teddy Fleece Fabric Couch, Generous 4-Seat Design with Ergonomic Curved Design Ideal for Bedroom Comfort Zone, Beige'),
    ("XS-W5656S00087", "Beige", "4S+1O", 'KEIKI 129.1" Soft Inviting Large Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Plush Cushion Support Designed for Apartment Living Comfort, Beige'),
    ("XS-W5656S00089", "Beige", "4S+2O", 'KEIKI 129.1" Modern Beige Modular Sectional Teddy Fleece Fabric Couch with 2 Storage Ottomans, Luxurious Lounging Experience Perfect for Home Studio, Beige'),
    # Orange 系列
    ("XS-W5656S00091", "Orange", "2S", 'KEIKI 68.5" Bold Vibrant Loveseat Sofa Teddy Fleece Fabric Couch, Compact 2-Seat Design with Ultimate Relaxation Design for Modern Office Furniture Style, Orange'),
    ("XS-W5656S00093", "Orange", "2S+1O", 'KEIKI 68.5" Retro Statement Loveseat Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Deep Cloud-Like Comfort Perfect for Living Room Relaxation, Orange'),
    ("XS-W5656S00094", "Orange", "2S+2O", 'KEIKI 68.5" Warm Energetic Modular Loveseat Teddy Fleece Fabric Couch with 2 Ottomans, Ergonomic Curved Design Ideal for Bedroom Comfort and Style, Orange'),
    ("XS-W5656S00095", "Orange", "3S", 'KEIKI 98.2" Stylish Orange Oversized Couch Teddy Fleece Fabric, Spacious 3-Seat Design with Plush Cushion Support Designed for Apartment Living Space, Orange'),
    ("XS-W5656S00097", "Orange", "3S+1O", 'KEIKI 98.2" Designer Citrus Sectional Sofa Teddy Fleece Fabric Couch with Storage Ottoman, Luxurious Lounging Experience Perfect Addition to Your Home Studio, Orange'),
    ("XS-W5656S00099", "Orange", "3S+2O", 'KEIKI 98.2" Bold Vibrant Modular Sectional Teddy Fleece Fabric Couch with 2 Ottomans, Ultimate Relaxation Design Ultimate Modern Office Furniture Piece, Orange'),
    ("XS-W5656S00101", "Orange", "4S", 'KEIKI 129.1" Retro Statement Large Sectional Teddy Fleece Fabric Couch, Generous 4-Seat Design with Deep Cloud-Like Comfort Perfect for Living Room Relaxation, Orange'),
    ("XS-W5656S00103", "Orange", "4S+1O", 'KEIKI 129.1" Warm Energetic Large Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Ergonomic Curved Design Ideal for Bedroom Comfort Zone, Orange'),
    ("XS-W5656S00105", "Orange", "4S+2O", 'KEIKI 129.1" Stylish Orange Modular Sectional Teddy Fleece Fabric Couch with 2 Storage Ottomans, Plush Cushion Support Designed for Apartment Living Space, Orange'),
    # Green 系列
    ("XS-W5656S00076", "Green", "2S", 'KEIKI 68.5" Fresh Natural Loveseat Sofa Teddy Fleece Fabric Couch, Compact 2-Seat Design with Luxurious Lounging Experience Perfect Addition to Your Home Studio, Green'),
    ("XS-W5656S00077", "Green", "2S+1O", 'KEIKI 68.5" Botanical Organic Loveseat Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Ultimate Relaxation Design Ultimate Modern Office Furniture, Green'),
    ("XS-W5656S00079", "Green", "2S+2O", 'KEIKI 68.5" Calming Green Modular Loveseat Teddy Fleece Fabric Couch with 2 Ottomans, Deep Cloud-Like Comfort Perfect for Living Room Relaxation Time, Green'),
    ("XS-W5656S00081", "Green", "3S", 'KEIKI 98.2" Serene Forest Oversized Couch Teddy Fleece Fabric, Spacious 3-Seat Design with Ergonomic Curved Design Ideal for Bedroom Comfort and Relaxation, Green'),
    ("XS-W5656S00083", "Green", "3S+1O", 'KEIKI 98.2" Nature Inspired Sectional Sofa Teddy Fleece Fabric Couch with Storage Ottoman, Plush Cushion Support Designed for Apartment Living Space, Green'),
    ("XS-W5656S00086", "Green", "3S+2O", 'KEIKI 98.2" Fresh Natural Modular Sectional Teddy Fleece Fabric Couch with 2 Ottomans, Luxurious Lounging Experience Perfect Addition to Your Home Studio, Green'),
    ("XS-W5656S00088", "Green", "4S", 'KEIKI 129.1" Botanical Organic Large Sectional Teddy Fleece Fabric Couch, Generous 4-Seat Design with Ultimate Relaxation Design Ultimate Modern Office Furniture, Green'),
    ("XS-W5656S00090", "Green", "4S+1O", 'KEIKI 129.1" Calming Green Large Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Deep Cloud-Like Comfort Perfect for Living Room Relaxation, Green'),
    ("XS-W5656S00092", "Green", "4S+2O", 'KEIKI 129.1" Serene Forest Modular Sectional Teddy Fleece Fabric Couch with 2 Storage Ottomans, Ergonomic Curved Design Ideal for Bedroom Comfort Zone, Green'),
    # Camel 系列
    ("XS-W5656S00096", "Camel", "2S", 'KEIKI 68.5" Classic Sophisticated Loveseat Sofa Teddy Fleece Fabric Couch, Compact 2-Seat Design with Plush Cushion Support Designed for Apartment Living Space, Camel'),
    ("XS-W5656S00098", "Camel", "2S+1O", 'KEIKI 68.5" Timeless Elegant Loveseat Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Luxurious Lounging Experience Perfect Addition to Your Home Studio, Camel'),
    ("XS-W5656S00100", "Camel", "2S+2O", 'KEIKI 68.5" Premium Camel Modular Loveseat Teddy Fleece Fabric Couch with 2 Storage Ottomans, Ultimate Relaxation Design Ultimate Modern Office Furniture, Camel'),
    ("XS-W5656S00102", "Camel", "3S", 'KEIKI 98.2" Heritage Warm Oversized Couch Teddy Fleece Fabric, Spacious 3-Seat Design with Deep Cloud-Like Comfort Perfect for Living Room Relaxation Time, Camel'),
    ("XS-W5656S00104", "Camel", "3S+1O", 'KEIKI 98.2" Refined Tan Sectional Sofa Teddy Fleece Fabric Couch with Storage Ottoman, Ergonomic Curved Design Ideal for Bedroom Comfort and Style, Camel'),
    ("XS-W5656S00106", "Camel", "3S+2O", 'KEIKI 98.2" Classic Sophisticated Modular Sectional Teddy Fleece Fabric Couch with 2 Ottomans, Plush Cushion Support Designed for Apartment Living Space, Camel'),
    ("XS-W5656S00107", "Camel", "4S", 'KEIKI 129.1" Timeless Elegant Large Sectional Teddy Fleece Fabric Couch, Generous 4-Seat Design with Luxurious Lounging Experience Perfect Addition to Home Studio, Camel'),
    ("XS-W5656S00108", "Camel", "4S+1O", 'KEIKI 129.1" Premium Camel Large Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Ultimate Relaxation Design Ultimate Modern Office Furniture Style, Camel'),
    ("XS-W5656S00109", "Camel", "4S+2O", 'KEIKI 129.1" Heritage Warm Modular Sectional Teddy Fleece Fabric Couch with 2 Storage Ottomans, Deep Cloud-Like Comfort Perfect for Living Room Relaxation, Camel'),
]

# 创建DataFrame并计算长度
df = pd.DataFrame(titles_final, columns=['SKU', 'Color', 'Size', 'Title'])
df['Length'] = df['Title'].str.len()

# 统计
print("=" * 90)
print("KEIKI 泰迪绒沙发标题 - 最终版 180-190字符")
print("=" * 90)

lengths = df['Length'].tolist()
print(f"\n总标题: {len(df)}")
print(f"字符范围: {min(lengths)} - {max(lengths)}")
print(f"平均: {sum(lengths)/len(lengths):.1f}")
print(f"唯一: {len(set(df['Title']))}/{len(df)}")

# 检查问题
short = df[df['Length'] < 180]
long = df[df['Length'] > 190]

if len(short) > 0:
    print(f"\n⚠️ 太短({len(short)}个):")
    for _, row in short.iterrows():
        print(f"  {row['SKU']} ({row['Color']} {row['Size']}): {row['Length']}字符")
        
if len(long) > 0:
    print(f"\n⚠️ 太长({len(long)}个):")
    for _, row in long.iterrows():
        print(f"  {row['SKU']} ({row['Color']} {row['Size']}): {row['Length']}字符")
        print(f"    {row['Title']}")

# 显示全部
print("\n" + "=" * 90)
print("全部标题")
print("=" * 90)
for _, row in df.iterrows():
    status = "✓" if 180 <= row['Length'] <= 190 else ("短" if row['Length'] < 180 else "长")
    print(f"\n【{row['Color']} | {row['Size']}】{status} ({row['Length']})")
    print(f"{row['Title']}")

# 保存
output = "/root/.openclaw/workspace/KEIKI_泰迪绒沙发_标题_最终版.xlsx"
df.to_excel(output, index=False)
print(f"\n\n✓ 已保存: {output}")
