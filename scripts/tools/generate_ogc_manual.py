#!/usr/bin/env python3
import pandas as pd

# 手动精确编写27个标题，确保185-190字符

# 手工优化的标题列表
manual_titles = [
    # Orange (XS-W5656S00091 - 00109)
    ("XS-W5656S00091", "Orange", "2S", 'KEIKI 68.5" Bold Vibrant Loveseat Teddy Fleece, Cushion Comfort Perfect for Your Modern Living Room Furniture Space with Ergonomic Curved Design and Home Style, Orange'),
    ("XS-W5656S00093", "Orange", "2S+1O", 'KEIKI 68.5" Retro Warm Loveseat Sectional with Chaise Ottoman Teddy Fleece, Cushion Comfort Perfect for Living Room with Ergonomic Curved Design and Modern Home Studio Style, Orange'),
    ("XS-W5656S00094", "Orange", "2S+2O", 'KEIKI 68.5" Energetic Stylish Modular Loveseat with 2 Ottomans Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Home Studio Style, Orange'),
    ("XS-W5656S00095", "Orange", "3S", 'KEIKI 98.2" Bold Vibrant Oversized Couch Teddy Fleece, Cushion Comfort Perfect for Your Modern Living Room Furniture Space with Ergonomic Curved Design and Home Style, Orange'),
    ("XS-W5656S00097", "Orange", "3S+1O", 'KEIKI 98.2" Retro Warm Sectional Couch with Ottoman Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Modern Home Style, Orange'),
    ("XS-W5656S00099", "Orange", "3S+2O", 'KEIKI 98.2" Energetic Stylish Modular Sectional with 2 Ottomans Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Home Style, Orange'),
    ("XS-W5656S00101", "Orange", "4S", 'KEIKI 129.1" Bold Vibrant Large Sectional Teddy Fleece Fabric, Cushion Comfort Perfect for Your Modern Living Room Furniture Space with Ergonomic Curved Design and Home Style, Orange'),
    ("XS-W5656S00103", "Orange", "4S+1O", 'KEIKI 129.1" Retro Warm Large Sectional with Chaise Ottoman Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Modern Home Style, Orange'),
    ("XS-W5656S00105", "Orange", "4S+2O", 'KEIKI 129.1" Energetic Stylish Modular Sectional with 2 Ottomans Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Home Style, Orange'),
    
    # Green (XS-W5656S00076 - 00092)
    ("XS-W5656S00076", "Green", "2S", 'KEIKI 68.5" Fresh Natural Loveseat Teddy Fleece, Cushion Comfort Perfect for Your Modern Living Room Furniture Space with Ergonomic Curved Design and Home Style, Green'),
    ("XS-W5656S00077", "Green", "2S+1O", 'KEIKI 68.5" Botanical Organic Loveseat Sectional with Chaise Ottoman Teddy Fleece, Cushion Comfort Perfect for Living Room with Ergonomic Curved Design and Modern Home Studio Style, Green'),
    ("XS-W5656S00079", "Green", "2S+2O", 'KEIKI 68.5" Calming Serene Modular Loveseat with 2 Ottomans Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Home Studio Style, Green'),
    ("XS-W5656S00081", "Green", "3S", 'KEIKI 98.2" Fresh Natural Oversized Couch Teddy Fleece, Cushion Comfort Perfect for Your Modern Living Room Furniture Space with Ergonomic Curved Design and Home Style, Green'),
    ("XS-W5656S00083", "Green", "3S+1O", 'KEIKI 98.2" Botanical Organic Sectional Couch with Ottoman Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Modern Home Style, Green'),
    ("XS-W5656S00086", "Green", "3S+2O", 'KEIKI 98.2" Calming Serene Modular Sectional with 2 Ottomans Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Home Style, Green'),
    ("XS-W5656S00088", "Green", "4S", 'KEIKI 129.1" Fresh Natural Large Sectional Teddy Fleece Fabric, Cushion Comfort Perfect for Your Modern Living Room Furniture Space with Ergonomic Curved Design and Home Style, Green'),
    ("XS-W5656S00090", "Green", "4S+1O", 'KEIKI 129.1" Botanical Organic Large Sectional with Chaise Ottoman Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Modern Home Style, Green'),
    ("XS-W5656S00092", "Green", "4S+2O", 'KEIKI 129.1" Calming Serene Modular Sectional with 2 Ottomans Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Home Style, Green'),
    
    # Camel (XS-W5656S00096 - 00109)
    ("XS-W5656S00096", "Camel", "2S", 'KEIKI 68.5" Classic Heritage Loveseat Teddy Fleece, Cushion Comfort Perfect for Your Modern Living Room Furniture Space with Ergonomic Curved Design and Home Style, Camel'),
    ("XS-W5656S00098", "Camel", "2S+1O", 'KEIKI 68.5" Timeless Elegant Loveseat Sectional with Chaise Ottoman Teddy Fleece, Cushion Comfort Perfect for Living Room with Ergonomic Curved Design and Modern Home Studio Style, Camel'),
    ("XS-W5656S00100", "Camel", "2S+2O", 'KEIKI 68.5" Sophisticated Refined Modular Loveseat with 2 Ottomans Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Home Studio Style, Camel'),
    ("XS-W5656S00102", "Camel", "3S", 'KEIKI 98.2" Classic Heritage Oversized Couch Teddy Fleece, Cushion Comfort Perfect for Your Modern Living Room Furniture Space with Ergonomic Curved Design and Home Style, Camel'),
    ("XS-W5656S00104", "Camel", "3S+1O", 'KEIKI 98.2" Timeless Elegant Sectional Couch with Ottoman Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Modern Home Style, Camel'),
    ("XS-W5656S00106", "Camel", "3S+2O", 'KEIKI 98.2" Sophisticated Refined Modular Sectional with 2 Ottomans Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Home Style, Camel'),
    ("XS-W5656S00107", "Camel", "4S", 'KEIKI 129.1" Classic Heritage Large Sectional Teddy Fleece Fabric, Cushion Comfort Perfect for Your Modern Living Room Furniture Space with Ergonomic Curved Design and Home Style, Camel'),
    ("XS-W5656S00108", "Camel", "4S+1O", 'KEIKI 129.1" Timeless Elegant Large Sectional with Chaise Ottoman Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Modern Home Style, Camel'),
    ("XS-W5656S00109", "Camel", "4S+2O", 'KEIKI 129.1" Sophisticated Refined Modular Sectional with 2 Ottomans Teddy Fleece, Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Home Style, Camel'),
]

# 验证并调整
results = []
for sku, color, size, title in manual_titles:
    length = len(title)
    results.append({
        "SKU": sku,
        "Color": color,
        "Size": size,
        "Title": title,
        "Length": length
    })

# 输出
print("=" * 90)
print("Orange/Green/Camel 标题 - 手工优化 (185-190字符)")
print("=" * 90)

lengths = [r["Length"] for r in results]
in_range = [r for r in results if 185 <= r["Length"] <= 190]
short = [r for r in results if r["Length"] < 185]
long = [r for r in results if r["Length"] > 190]

print(f"\n总标题: {len(results)}")
print(f"字符范围: {min(lengths)} - {max(lengths)}")
print(f"平均: {sum(lengths)/len(lengths):.1f}")
print(f"符合185-190: {len(in_range)}/{len(results)}")

if short:
    print(f"\n⚠️ 太短({len(short)}个):")
    for r in short:
        print(f"  {r['Color']} {r['Size']}: {r['Length']}字符")
        
if long:
    print(f"\n⚠️ 太长({len(long)}个):")
    for r in long:
        print(f"  {r['Color']} {r['Size']}: {r['Length']}字符")

# 各颜色统计
for color in ["Orange", "Green", "Camel"]:
    color_results = [r for r in results if r["Color"] == color]
    color_lengths = [r["Length"] for r in color_results]
    color_ok = [r for r in color_results if 185 <= r["Length"] <= 190]
    print(f"\n{color}: 范围 {min(color_lengths)}-{max(color_lengths)}, 达标 {len(color_ok)}/9")

# 检查禁用词
print("\n" + "=" * 90)
print("禁用词检查")
print("=" * 90)

forbidden = ["storage", "ultimate", "premium", "luxurious"]
issues = []
for r in results:
    title_lower = r["Title"].lower()
    found = [w for w in forbidden if w in title_lower]
    if found:
        issues.append((r, found))

if issues:
    print(f"⚠️ 发现{len(issues)}个问题")
else:
    print("✓ 无禁用词")

# 显示样本
print("\n" + "=" * 90)
print("样本标题")
print("=" * 90)
for color in ["Orange", "Green", "Camel"]:
    print(f"\n【{color}】")
    samples = [r for r in results if r["Color"] == color][:3]
    for r in samples:
        status = "✓" if 185 <= r["Length"] <= 190 else f"✗{r['Length']}"
        print(f"  {r['Size']} {status}: {r['Title']}")

# 保存
df = pd.DataFrame(results)
output = "/root/.openclaw/workspace/KEIKI_OGC_标题_手工版.xlsx"
df.to_excel(output, index=False)
print(f"\n\n✓ 已保存: {output}")
