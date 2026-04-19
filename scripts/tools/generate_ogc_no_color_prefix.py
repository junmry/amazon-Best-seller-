#!/usr/bin/env python3
import pandas as pd

# 首位无颜色版 - 全部185-190字符

final_titles = [
    # Orange - 2S达标, 2S+1O减词, 2S+2O加词
    ("XS-W5656S00091", "Orange", "2S", 'KEIKI 68.5" Loveseat Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Small Modern Living Room Furniture Space with Ergonomic Curved Design and Contemporary Home Studio Style, Orange'),
    ("XS-W5656S00093", "Orange", "2S+1O", 'KEIKI 68.5" Loveseat Sectional with Chaise Ottoman Teddy Fleece, Plush Comfortable Perfect for Small Living Room Furniture with Ergonomic Curved Design and Modern Home Studio Style, Orange'),
    ("XS-W5656S00094", "Orange", "2S+2O", 'KEIKI 68.5" Modular Loveseat with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Perfect for Compact Living Room Furniture Space with Ergonomic Curved Design and Home Studio Style, Orange'),
    ("XS-W5656S00095", "Orange", "3S", 'KEIKI 98.2" Oversized Couch Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Spacious Modern Living Room Furniture with Ergonomic Curved Design and Home Style, Orange'),
    ("XS-W5656S00097", "Orange", "3S+1O", 'KEIKI 98.2" Sectional Couch with Ottoman Teddy Fleece, Plush Comfortable Perfect for Spacious Living Room Furniture with Ergonomic Curved Design and Modern Home Studio Style, Orange'),
    ("XS-W5656S00099", "Orange", "3S+2O", 'KEIKI 98.2" Modular Sectional with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Perfect for Medium Living Room Furniture Space with Ergonomic Curved Design and Home Studio Style, Orange'),
    ("XS-W5656S00101", "Orange", "4S", 'KEIKI 129.1" Large Sectional Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Large Modern Living Room Furniture with Ergonomic Curved Design and Home Style, Orange'),
    ("XS-W5656S00103", "Orange", "4S+1O", 'KEIKI 129.1" Large Sectional with Chaise Ottoman Teddy Fleece, Plush Comfortable Perfect for Large Living Room Furniture with Ergonomic Curved Design and Modern Home Style, Orange'),
    ("XS-W5656S00105", "Orange", "4S+2O", 'KEIKI 129.1" Modular Sectional with 2 Ottomans Teddy Fleece, Comfortable Plush Perfect for Generous Living Room Furniture Space with Ergonomic Curved Design and Home Studio Style, Orange'),
    
    # Green
    ("XS-W5656S00076", "Green", "2S", 'KEIKI 68.5" Loveseat Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Small Modern Living Room Furniture Space with Ergonomic Curved Design and Contemporary Home Studio Style, Green'),
    ("XS-W5656S00077", "Green", "2S+1O", 'KEIKI 68.5" Loveseat Sectional with Chaise Ottoman Teddy Fleece, Plush Comfortable Perfect for Small Living Room Furniture with Ergonomic Curved Design and Modern Home Studio Style, Green'),
    ("XS-W5656S00079", "Green", "2S+2O", 'KEIKI 68.5" Modular Loveseat with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Perfect for Compact Living Room Furniture Space with Ergonomic Curved Design and Home Studio Style, Green'),
    ("XS-W5656S00081", "Green", "3S", 'KEIKI 98.2" Oversized Couch Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Spacious Modern Living Room Furniture with Ergonomic Curved Design and Home Style, Green'),
    ("XS-W5656S00083", "Green", "3S+1O", 'KEIKI 98.2" Sectional Couch with Ottoman Teddy Fleece, Plush Comfortable Perfect for Spacious Living Room Furniture with Ergonomic Curved Design and Modern Home Studio Style, Green'),
    ("XS-W5656S00086", "Green", "3S+2O", 'KEIKI 98.2" Modular Sectional with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Perfect for Medium Living Room Furniture Space with Ergonomic Curved Design and Home Studio Style, Green'),
    ("XS-W5656S00088", "Green", "4S", 'KEIKI 129.1" Large Sectional Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Large Modern Living Room Furniture with Ergonomic Curved Design and Home Style, Green'),
    ("XS-W5656S00090", "Green", "4S+1O", 'KEIKI 129.1" Large Sectional with Chaise Ottoman Teddy Fleece, Plush Comfortable Perfect for Large Living Room Furniture with Ergonomic Curved Design and Modern Home Style, Green'),
    ("XS-W5656S00092", "Green", "4S+2O", 'KEIKI 129.1" Modular Sectional with 2 Ottomans Teddy Fleece, Comfortable Plush Perfect for Generous Living Room Furniture Space with Ergonomic Curved Design and Home Studio Style, Green'),
    
    # Camel
    ("XS-W5656S00096", "Camel", "2S", 'KEIKI 68.5" Loveseat Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Small Modern Living Room Furniture Space with Ergonomic Curved Design and Contemporary Home Studio Style, Camel'),
    ("XS-W5656S00098", "Camel", "2S+1O", 'KEIKI 68.5" Loveseat Sectional with Chaise Ottoman Teddy Fleece, Plush Comfortable Perfect for Small Living Room Furniture with Ergonomic Curved Design and Modern Home Studio Style, Camel'),
    ("XS-W5656S00100", "Camel", "2S+2O", 'KEIKI 68.5" Modular Loveseat with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Perfect for Compact Living Room Furniture Space with Ergonomic Curved Design and Home Studio Style, Camel'),
    ("XS-W5656S00102", "Camel", "3S", 'KEIKI 98.2" Oversized Couch Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Spacious Modern Living Room Furniture with Ergonomic Curved Design and Home Style, Camel'),
    ("XS-W5656S00104", "Camel", "3S+1O", 'KEIKI 98.2" Sectional Couch with Ottoman Teddy Fleece, Plush Comfortable Perfect for Spacious Living Room Furniture with Ergonomic Curved Design and Modern Home Studio Style, Camel'),
    ("XS-W5656S00106", "Camel", "3S+2O", 'KEIKI 98.2" Modular Sectional with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Perfect for Medium Living Room Furniture Space with Ergonomic Curved Design and Home Studio Style, Camel'),
    ("XS-W5656S00107", "Camel", "4S", 'KEIKI 129.1" Large Sectional Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Large Modern Living Room Furniture with Ergonomic Curved Design and Home Style, Camel'),
    ("XS-W5656S00108", "Camel", "4S+1O", 'KEIKI 129.1" Large Sectional with Chaise Ottoman Teddy Fleece, Plush Comfortable Perfect for Large Living Room Furniture with Ergonomic Curved Design and Modern Home Style, Camel'),
    ("XS-W5656S00109", "Camel", "4S+2O", 'KEIKI 129.1" Modular Sectional with 2 Ottomans Teddy Fleece, Comfortable Plush Perfect for Generous Living Room Furniture Space with Ergonomic Curved Design and Home Studio Style, Camel'),
]

# 验证
results = []
for sku, color, size, title in final_titles:
    actual_len = len(title)
    results.append({
        "SKU": sku,
        "Color": color,
        "Size": size,
        "Title": title,
        "Length": actual_len
    })

# 统计
print("=" * 90)
print("首位无颜色版 - 最终标题 (185-190字符)")
print("=" * 90)

lengths = [r["Length"] for r in results]
in_range = [r for r in results if 185 <= r["Length"] <= 190]
short = [r for r in results if r["Length"] < 185]
long = [r for r in results if r["Length"] > 190]

print(f"\n总标题: {len(results)}")
print(f"字符范围: {min(lengths)} - {max(lengths)}")
print(f"平均: {sum(lengths)/len(lengths):.1f}")
print(f"符合185-190: {len(in_range)}/{len(results)}")

for color in ["Orange", "Green", "Camel"]:
    color_results = [r for r in results if r["Color"] == color]
    ok = [r for r in color_results if 185 <= r["Length"] <= 190]
    print(f"{color}: 达标 {len(ok)}/9")

if short:
    print(f"\n⚠️ 太短({len(short)}个):")
    for r in short:
        print(f"  {r['Color']} {r['Size']}: {r['Length']}")
        
if long:
    print(f"\n⚠️ 太长({len(long)}个):")
    for r in long:
        print(f"  {r['Color']} {r['Size']}: {r['Length']}")

# 保存
df = pd.DataFrame(results)
output = "/root/.openclaw/workspace/KEIKI_OGC_标题_最终版.xlsx"
df.to_excel(output, index=False)
print(f"\n✓ 已保存: {output}")

# 样本
print("\n" + "=" * 90)
print("样本")
print("=" * 90)
for color in ["Orange", "Green", "Camel"]:
    r = [x for x in results if x["Color"] == color][0]
    print(f"\n{color} 2S ({r['Length']}字符):")
    print(r['Title'])
