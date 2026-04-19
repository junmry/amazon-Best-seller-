#!/usr/bin/env python3
import pandas as pd

# 基础标题（152-169字符）
base_titles = [
    ("XS-W5656S00073", "Beige", "2S", 'KEIKI 68.5" Cozy Neutral Loveseat Sofa Teddy Fleece Fabric Couch, Compact 2-Seat Design with Deep Cloud-Like Comfort'),
    ("XS-W5656S00075", "Beige", "2S+1O", 'KEIKI 68.5" Warm Elegant Loveseat Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Ergonomic Curved Design'),
    ("XS-W5656S00078", "Beige", "2S+2O", 'KEIKI 68.5" Soft Inviting Modular Loveseat Teddy Fleece Fabric Couch with 2 Storage Ottomans, Plush Cushion Support'),
    ("XS-W5656S00080", "Beige", "3S", 'KEIKI 98.2" Modern Beige Oversized Couch Teddy Fleece Fabric, Spacious 3-Seat Design with Luxurious Lounging Experience'),
    ("XS-W5656S00082", "Beige", "3S+1O", 'KEIKI 98.2" Elegant Cream Sectional Sofa Teddy Fleece Fabric Couch with Storage Ottoman, Ultimate Relaxation Design'),
    ("XS-W5656S00084", "Beige", "3S+2O", 'KEIKI 98.2" Cozy Neutral Modular Sectional Teddy Fleece Fabric Couch with 2 Ottomans, Deep Cloud-Like Comfort'),
    ("XS-W5656S00085", "Beige", "4S", 'KEIKI 129.1" Warm Elegant Large Sectional Teddy Fleece Fabric Couch, Generous 4-Seat Design with Ergonomic Curved Design'),
    ("XS-W5656S00087", "Beige", "4S+1O", 'KEIKI 129.1" Soft Inviting Large Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Plush Cushion Support'),
    ("XS-W5656S00089", "Beige", "4S+2O", 'KEIKI 129.1" Modern Beige Modular Sectional Teddy Fleece Fabric Couch with 2 Storage Ottomans, Luxurious Lounging Experience'),
    ("XS-W5656S00091", "Orange", "2S", 'KEIKI 68.5" Bold Vibrant Loveseat Sofa Teddy Fleece Fabric Couch, Compact 2-Seat Design with Ultimate Relaxation Design'),
    ("XS-W5656S00093", "Orange", "2S+1O", 'KEIKI 68.5" Retro Statement Loveseat Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Deep Cloud-Like Comfort'),
    ("XS-W5656S00094", "Orange", "2S+2O", 'KEIKI 68.5" Warm Energetic Modular Loveseat Teddy Fleece Fabric Couch with 2 Ottomans, Ergonomic Curved Design'),
    ("XS-W5656S00095", "Orange", "3S", 'KEIKI 98.2" Stylish Orange Oversized Couch Teddy Fleece Fabric, Spacious 3-Seat Design with Plush Cushion Support'),
    ("XS-W5656S00097", "Orange", "3S+1O", 'KEIKI 98.2" Designer Citrus Sectional Sofa Teddy Fleece Fabric Couch with Storage Ottoman, Luxurious Lounging Experience'),
    ("XS-W5656S00099", "Orange", "3S+2O", 'KEIKI 98.2" Bold Vibrant Modular Sectional Teddy Fleece Fabric Couch with 2 Ottomans, Ultimate Relaxation Design'),
    ("XS-W5656S00101", "Orange", "4S", 'KEIKI 129.1" Retro Statement Large Sectional Teddy Fleece Fabric Couch, Generous 4-Seat Design with Deep Cloud-Like Comfort'),
    ("XS-W5656S00103", "Orange", "4S+1O", 'KEIKI 129.1" Warm Energetic Large Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Ergonomic Curved Design'),
    ("XS-W5656S00105", "Orange", "4S+2O", 'KEIKI 129.1" Stylish Orange Modular Sectional Teddy Fleece Fabric Couch with 2 Storage Ottomans, Plush Cushion Support'),
    ("XS-W5656S00076", "Green", "2S", 'KEIKI 68.5" Fresh Natural Loveseat Sofa Teddy Fleece Fabric Couch, Compact 2-Seat Design with Luxurious Lounging Experience'),
    ("XS-W5656S00077", "Green", "2S+1O", 'KEIKI 68.5" Botanical Organic Loveseat Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Ultimate Relaxation Design'),
    ("XS-W5656S00079", "Green", "2S+2O", 'KEIKI 68.5" Calming Green Modular Loveseat Teddy Fleece Fabric Couch with 2 Ottomans, Deep Cloud-Like Comfort'),
    ("XS-W5656S00081", "Green", "3S", 'KEIKI 98.2" Serene Forest Oversized Couch Teddy Fleece Fabric, Spacious 3-Seat Design with Ergonomic Curved Design'),
    ("XS-W5656S00083", "Green", "3S+1O", 'KEIKI 98.2" Nature Inspired Sectional Sofa Teddy Fleece Fabric Couch with Storage Ottoman, Plush Cushion Support'),
    ("XS-W5656S00086", "Green", "3S+2O", 'KEIKI 98.2" Fresh Natural Modular Sectional Teddy Fleece Fabric Couch with 2 Ottomans, Luxurious Lounging Experience'),
    ("XS-W5656S00088", "Green", "4S", 'KEIKI 129.1" Botanical Organic Large Sectional Teddy Fleece Fabric Couch, Generous 4-Seat Design with Ultimate Relaxation Design'),
    ("XS-W5656S00090", "Green", "4S+1O", 'KEIKI 129.1" Calming Green Large Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Deep Cloud-Like Comfort'),
    ("XS-W5656S00092", "Green", "4S+2O", 'KEIKI 129.1" Serene Forest Modular Sectional Teddy Fleece Fabric Couch with 2 Storage Ottomans, Ergonomic Curved Design'),
    ("XS-W5656S00096", "Camel", "2S", 'KEIKI 68.5" Classic Sophisticated Loveseat Sofa Teddy Fleece Fabric Couch, Compact 2-Seat Design with Plush Cushion Support'),
    ("XS-W5656S00098", "Camel", "2S+1O", 'KEIKI 68.5" Timeless Elegant Loveseat Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Luxurious Lounging Experience'),
    ("XS-W5656S00100", "Camel", "2S+2O", 'KEIKI 68.5" Premium Camel Modular Loveseat Teddy Fleece Fabric Couch with 2 Storage Ottomans, Ultimate Relaxation Design'),
    ("XS-W5656S00102", "Camel", "3S", 'KEIKI 98.2" Heritage Warm Oversized Couch Teddy Fleece Fabric, Spacious 3-Seat Design with Deep Cloud-Like Comfort'),
    ("XS-W5656S00104", "Camel", "3S+1O", 'KEIKI 98.2" Refined Tan Sectional Sofa Teddy Fleece Fabric Couch with Storage Ottoman, Ergonomic Curved Design'),
    ("XS-W5656S00106", "Camel", "3S+2O", 'KEIKI 98.2" Classic Sophisticated Modular Sectional Teddy Fleece Fabric Couch with 2 Ottomans, Plush Cushion Support'),
    ("XS-W5656S00107", "Camel", "4S", 'KEIKI 129.1" Timeless Elegant Large Sectional Teddy Fleece Fabric Couch, Generous 4-Seat Design with Luxurious Lounging Experience'),
    ("XS-W5656S00108", "Camel", "4S+1O", 'KEIKI 129.1" Premium Camel Large Sectional Teddy Fleece Fabric Couch with Chaise Ottoman, Ultimate Relaxation Design'),
    ("XS-W5656S00109", "Camel", "4S+2O", 'KEIKI 129.1" Heritage Warm Modular Sectional Teddy Fleece Fabric Couch with 2 Storage Ottomans, Deep Cloud-Like Comfort'),
]

# 扩展词组（约40-45字符，确保总长180-190）
extensions = [
    "Perfect for Your Living Room Space and Home Relaxation",
    "Ideal for Bedroom Comfort Zone and Ultimate Relaxation", 
    "Designed for Apartment Living Style and Modern Comfort",
    "Ultimate Home Studio Furniture with Premium Lounging Experience",
    "Premium Modern Office Lounging with Ergonomic Design Support"
]

# 颜色
colors = ["Beige", "Orange", "Green", "Camel"]

def build_final_title(base, color, idx):
    """组合成完整标题"""
    ext = extensions[idx % 5]
    full = f"{base} {ext}, {color}"
    return full

# 生成
results = []
for i, (sku, color, size, base) in enumerate(base_titles):
    idx = i % 5
    title = build_final_title(base, color, idx)
    length = len(title)
    results.append({
        "SKU": sku,
        "Color": color,
        "Size": size,
        "Title": title,
        "Length": length
    })

# 统计
print("=" * 90)
print("KEIKI 泰迪绒沙发标题 - 180-190字符最终版")
print("=" * 90)

lengths = [r["Length"] for r in results]
print(f"\n总标题: {len(results)}")
print(f"字符范围: {min(lengths)} - {max(lengths)}")
print(f"平均: {sum(lengths)/len(lengths):.1f}")
print(f"唯一: {len(set(r['Title'] for r in results))}/{len(results)}")

# 检查问题
short = [r for r in results if r["Length"] < 180]
long = [r for r in results if r["Length"] > 190]

if short:
    print(f"\n⚠️ 太短({len(short)}个):")
    for r in short[:5]:
        print(f"  {r['SKU']}: {r['Length']}字符")
        
if long:
    print(f"\n⚠️ 太长({len(long)}个):")
    for r in long[:5]:
        print(f"  {r['SKU']}: {r['Length']}字符")

# 显示全部
print("\n" + "=" * 90)
print("全部标题")
print("=" * 90)
for r in results:
    status = "✓" if 180 <= r["Length"] <= 190 else ("短" if r["Length"] < 180 else "长")
    print(f"\n【{r['Color']} | {r['Size']}】{status} ({r['Length']})")
    print(f"{r['Title']}")

# 保存
df = pd.DataFrame(results)
output = "/root/.openclaw/workspace/KEIKI_泰迪绒沙发_标题_最终版.xlsx"
df.to_excel(output, index=False)
print(f"\n\n✓ 已保存: {output}")
