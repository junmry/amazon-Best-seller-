#!/usr/bin/env python3
import pandas as pd

# 差异化版本 - 按尺寸和人群定制

final_titles = [
    # ========== ORANGE ==========
    # 2S系列 - 小户型/公寓/年轻人
    ("XS-W5656S00091", "Orange", "2S", 'KEIKI 68.5" Loveseat Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Small Apartment Living Room Furniture Space with Ergonomic Curved Design and Contemporary Home Studio Style, Orange'),
    ("XS-W5656S00093", "Orange", "2S+1O", 'KEIKI 68.5" Loveseat Sectional with Chaise Ottoman Teddy Fleece, Plush Comfortable Perfect for Compact Apartment Living Room Furniture with Ergonomic Curved Design and Modern Home Style, Orange'),
    ("XS-W5656S00094", "Orange", "2S+2O", 'KEIKI 68.5" Modular Loveseat with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Perfect for Small Space Living Room Furniture with Ergonomic Curved Design and Home Studio Style, Orange'),
    
    # 3S系列 - 中等家庭/标准住宅
    ("XS-W5656S00095", "Orange", "3S", 'KEIKI 98.2" Oversized Couch Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Spacious Family Living Room Furniture Space with Ergonomic Curved Design and Home Studio Style, Orange'),
    ("XS-W5656S00097", "Orange", "3S+1O", 'KEIKI 98.2" Sectional Couch with Ottoman Teddy Fleece, Plush Comfortable Perfect for Family Living Room Furniture Space with Ergonomic Curved Design and Modern Home Style, Orange'),
    ("XS-W5656S00099", "Orange", "3S+2O", 'KEIKI 98.2" Modular Sectional with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Perfect for Medium Family Living Room Furniture with Ergonomic Curved Design and Home Studio Style, Orange'),
    
    # 4S系列 - 大家庭/大空间/娱乐
    ("XS-W5656S00101", "Orange", "4S", 'KEIKI 129.1" Large Sectional Teddy Fleece Fabric, Plush Comfortable Soft Cozy Perfect for Large Family Living Room Furniture Space with Ergonomic Curved Design and Home Entertainment Style, Orange'),
    ("XS-W5656S00103", "Orange", "4S+1O", 'KEIKI 129.1" Large Sectional with Chaise Ottoman Teddy Fleece, Plush Comfortable Cozy Perfect for Large Living Room Furniture Space with Ergonomic Curved Design and Modern Home Style, Orange'),
    ("XS-W5656S00105", "Orange", "4S+2O", 'KEIKI 129.1" Modular Sectional with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Cozy Perfect for Generous Family Living Room Furniture with Ergonomic Curved Design and Home Style, Orange'),
    
    # ========== GREEN ==========
    # 2S系列
    ("XS-W5656S00076", "Green", "2S", 'KEIKI 68.5" Loveseat Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Small Apartment Living Room Furniture Space with Ergonomic Curved Design and Contemporary Home Studio Style, Green'),
    ("XS-W5656S00077", "Green", "2S+1O", 'KEIKI 68.5" Loveseat Sectional with Chaise Ottoman Teddy Fleece, Plush Comfortable Perfect for Compact Apartment Living Room Furniture with Ergonomic Curved Design and Modern Home Style, Green'),
    ("XS-W5656S00079", "Green", "2S+2O", 'KEIKI 68.5" Modular Loveseat with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Perfect for Small Space Living Room Furniture with Ergonomic Curved Design and Home Studio Style, Green'),
    
    # 3S系列
    ("XS-W5656S00081", "Green", "3S", 'KEIKI 98.2" Oversized Couch Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Spacious Family Living Room Furniture Space with Ergonomic Curved Design and Home Studio Style, Green'),
    ("XS-W5656S00083", "Green", "3S+1O", 'KEIKI 98.2" Sectional Couch with Ottoman Teddy Fleece, Plush Comfortable Perfect for Family Living Room Furniture Space with Ergonomic Curved Design and Modern Home Style, Green'),
    ("XS-W5656S00086", "Green", "3S+2O", 'KEIKI 98.2" Modular Sectional with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Perfect for Medium Family Living Room Furniture with Ergonomic Curved Design and Home Studio Style, Green'),
    
    # 4S系列
    ("XS-W5656S00088", "Green", "4S", 'KEIKI 129.1" Large Sectional Teddy Fleece Fabric, Plush Comfortable Soft Cozy Perfect for Large Family Living Room Furniture Space with Ergonomic Curved Design and Home Entertainment Style, Green'),
    ("XS-W5656S00090", "Green", "4S+1O", 'KEIKI 129.1" Large Sectional with Chaise Ottoman Teddy Fleece, Plush Comfortable Cozy Perfect for Large Living Room Furniture Space with Ergonomic Curved Design and Modern Home Style, Green'),
    ("XS-W5656S00092", "Green", "4S+2O", 'KEIKI 129.1" Modular Sectional with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Cozy Perfect for Generous Family Living Room Furniture with Ergonomic Curved Design and Home Style, Green'),
    
    # ========== CAMEL ==========
    # 2S系列
    ("XS-W5656S00096", "Camel", "2S", 'KEIKI 68.5" Loveseat Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Small Apartment Living Room Furniture Space with Ergonomic Curved Design and Contemporary Home Studio Style, Camel'),
    ("XS-W5656S00098", "Camel", "2S+1O", 'KEIKI 68.5" Loveseat Sectional with Chaise Ottoman Teddy Fleece, Plush Comfortable Perfect for Compact Apartment Living Room Furniture with Ergonomic Curved Design and Modern Home Style, Camel'),
    ("XS-W5656S00100", "Camel", "2S+2O", 'KEIKI 68.5" Modular Loveseat with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Perfect for Small Space Living Room Furniture with Ergonomic Curved Design and Home Studio Style, Camel'),
    
    # 3S系列
    ("XS-W5656S00102", "Camel", "3S", 'KEIKI 98.2" Oversized Couch Teddy Fleece Fabric, Plush Comfortable Soft Perfect for Spacious Family Living Room Furniture Space with Ergonomic Curved Design and Home Studio Style, Camel'),
    ("XS-W5656S00104", "Camel", "3S+1O", 'KEIKI 98.2" Sectional Couch with Ottoman Teddy Fleece, Plush Comfortable Perfect for Family Living Room Furniture Space with Ergonomic Curved Design and Modern Home Style, Camel'),
    ("XS-W5656S00106", "Camel", "3S+2O", 'KEIKI 98.2" Modular Sectional with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Perfect for Medium Family Living Room Furniture with Ergonomic Curved Design and Home Studio Style, Camel'),
    
    # 4S系列
    ("XS-W5656S00107", "Camel", "4S", 'KEIKI 129.1" Large Sectional Teddy Fleece Fabric, Plush Comfortable Soft Cozy Perfect for Large Family Living Room Furniture Space with Ergonomic Curved Design and Home Entertainment Style, Camel'),
    ("XS-W5656S00108", "Camel", "4S+1O", 'KEIKI 129.1" Large Sectional with Chaise Ottoman Teddy Fleece, Plush Comfortable Cozy Perfect for Large Living Room Furniture Space with Ergonomic Curved Design and Modern Home Style, Camel'),
    ("XS-W5656S00109", "Camel", "4S+2O", 'KEIKI 129.1" Modular Sectional with 2 Ottomans Teddy Fleece, Comfortable Plush Soft Cozy Perfect for Generous Family Living Room Furniture with Ergonomic Curved Design and Home Style, Camel'),
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
print("=" * 100)
print("差异化版本 - 按尺寸人群定制 (185-190字符)")
print("=" * 100)

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

# 差异化统计
print("\n" + "=" * 100)
print("差异化关键词分布")
print("=" * 100)

apartment = [r for r in results if "Apartment" in r["Title"]]
family = [r for r in results if "Family" in r["Title"]]
entertainment = [r for r in results if "Entertainment" in r["Title"]]

print(f"\n2S系列 (小户型/公寓): {len(apartment)}个")
print(f"  关键词: Apartment, Compact, Small Space")
print(f"  人群: 单身/情侣/租房年轻人")

print(f"\n3S系列 (中等家庭): {len(family) - len(entertainment)}个")
print(f"  关键词: Family, Spacious, Medium")
print(f"  人群: 三口之家/标准住宅")

print(f"\n4S系列 (大家庭/娱乐): {len(entertainment)}个")
print(f"  关键词: Family, Large, Generous, Entertainment")
print(f"  人群: 大家庭/别墅/社交需求")

# 保存
df = pd.DataFrame(results)
output = "/root/.openclaw/workspace/KEIKI_OGC_标题_差异化版.xlsx"
df.to_excel(output, index=False)
print(f"\n✓ 已保存: {output}")

# 样本对比
print("\n" + "=" * 100)
print("样本对比 (同一颜色不同尺寸)")
print("=" * 100)

for size in ["2S", "3S", "4S"]:
    r = [x for x in results if x["Color"] == "Orange" and x["Size"] == size][0]
    print(f"\n{size} ({r['Length']}字符):")
    print(r['Title'])
