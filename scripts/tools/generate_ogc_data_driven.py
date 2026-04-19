#!/usr/bin/env python3
import pandas as pd

# 高搜索量词库 (基于实际数据)
# couch: 273363, couches for living room: 179399, sectional couches: 122224
# sofa: 125242, loveseat: 32999, ottoman: 86212
# living room furniture: 63812, small couch: 24156, l shaped couch: 23974

final_titles = [
    # ========== ORANGE ==========
    # 2S系列 - 小户型/租房 (用 Small Couch + Loveseat)
    ("XS-W5656S00091", "Orange", "2S", 'KEIKI 68.5" 2 Seater Couch Teddy Fleece Fabric for Living Room, Small Loveseat Perfect for Apartment Space with Plush Comfortable Cushion and Ergonomic Curved Design, Orange'),
    ("XS-W5656S00093", "Orange", "2S+1O", 'KEIKI 68.5" 2 Seater Couch with Chaise Ottoman Teddy Fleece for Living Room, Small Loveseat Perfect for Apartment Space with Comfortable Cushion and Ergonomic Design, Orange'),
    ("XS-W5656S00094", "Orange", "2S+2O", 'KEIKI 68.5" 2 Seater Couch with 2 Ottomans Teddy Fleece for Living Room, Small Loveseat Perfect for Compact Apartment Space with Plush Comfortable Furniture, Orange'),
    
    # 3S系列 - 家庭 (用 3 Seater + Sectional)
    ("XS-W5656S00095", "Orange", "3S", 'KEIKI 98.2" 3 Seater Couch Teddy Fleece Fabric for Living Room, Sectional Sofa Perfect for Family Home Furniture Space with Plush Comfortable Cushion and Ergonomic Curved Design, Orange'),
    ("XS-W5656S00097", "Orange", "3S+1O", 'KEIKI 98.2" 3 Seater Couch with Ottoman Teddy Fleece for Living Room, Sectional Sofa Perfect for Family Home Furniture Space with Comfortable Cushion and Ergonomic Design, Orange'),
    ("XS-W5656S00099", "Orange", "3S+2O", 'KEIKI 98.2" 3 Seater Couch with 2 Ottomans Teddy Fleece for Living Room, Sectional Sofa Perfect for Family Home Furniture Space with Plush Comfortable Cushion, Orange'),
    
    # 4S系列 - 大空间 (用 Sectional Couch + Large)
    ("XS-W5656S00101", "Orange", "4S", 'KEIKI 129.1" Large Sectional Couch Teddy Fleece Fabric for Living Room, 4 Seater Sofa Perfect for Family Home Furniture Space with Plush Comfortable Cushion and Ergonomic Curved Design, Orange'),
    ("XS-W5656S00103", "Orange", "4S+1O", 'KEIKI 129.1" Large Sectional Couch with Chaise Ottoman Teddy Fleece for Living Room, 4 Seater Perfect for Family Home Furniture Space with Comfortable Cushion and Ergonomic Design, Orange'),
    ("XS-W5656S00105", "Orange", "4S+2O", 'KEIKI 129.1" Large Sectional Couch with 2 Ottomans Teddy Fleece for Living Room, Perfect for Family Home Furniture Space with Plush Comfortable Cushion and Ergonomic Design, Orange'),
    
    # ========== GREEN ==========
    ("XS-W5656S00076", "Green", "2S", 'KEIKI 68.5" 2 Seater Couch Teddy Fleece Fabric for Living Room, Small Loveseat Perfect for Apartment Space with Plush Comfortable Cushion and Ergonomic Curved Design, Green'),
    ("XS-W5656S00077", "Green", "2S+1O", 'KEIKI 68.5" 2 Seater Couch with Chaise Ottoman Teddy Fleece for Living Room, Small Loveseat Perfect for Apartment Space with Comfortable Cushion and Ergonomic Design, Green'),
    ("XS-W5656S00079", "Green", "2S+2O", 'KEIKI 68.5" 2 Seater Couch with 2 Ottomans Teddy Fleece for Living Room, Small Loveseat Perfect for Compact Apartment Space with Plush Comfortable Furniture, Green'),
    
    ("XS-W5656S00081", "Green", "3S", 'KEIKI 98.2" 3 Seater Couch Teddy Fleece Fabric for Living Room, Sectional Sofa Perfect for Family Home Furniture Space with Plush Comfortable Cushion and Ergonomic Curved Design, Green'),
    ("XS-W5656S00083", "Green", "3S+1O", 'KEIKI 98.2" 3 Seater Couch with Ottoman Teddy Fleece for Living Room, Sectional Sofa Perfect for Family Home Furniture Space with Comfortable Cushion and Ergonomic Design, Green'),
    ("XS-W5656S00086", "Green", "3S+2O", 'KEIKI 98.2" 3 Seater Couch with 2 Ottomans Teddy Fleece for Living Room, Sectional Sofa Perfect for Family Home Furniture Space with Plush Comfortable Cushion, Green'),
    
    ("XS-W5656S00088", "Green", "4S", 'KEIKI 129.1" Large Sectional Couch Teddy Fleece Fabric for Living Room, 4 Seater Sofa Perfect for Family Home Furniture Space with Plush Comfortable Cushion and Ergonomic Curved Design, Green'),
    ("XS-W5656S00090", "Green", "4S+1O", 'KEIKI 129.1" Large Sectional Couch with Chaise Ottoman Teddy Fleece for Living Room, 4 Seater Perfect for Family Home Furniture Space with Comfortable Cushion and Ergonomic Design, Green'),
    ("XS-W5656S00092", "Green", "4S+2O", 'KEIKI 129.1" Large Sectional Couch with 2 Ottomans Teddy Fleece for Living Room, Perfect for Family Home Furniture Space with Plush Comfortable Cushion and Ergonomic Design, Green'),
    
    # ========== CAMEL ==========
    ("XS-W5656S00096", "Camel", "2S", 'KEIKI 68.5" 2 Seater Couch Teddy Fleece Fabric for Living Room, Small Loveseat Perfect for Apartment Space with Plush Comfortable Cushion and Ergonomic Curved Design, Camel'),
    ("XS-W5656S00098", "Camel", "2S+1O", 'KEIKI 68.5" 2 Seater Couch with Chaise Ottoman Teddy Fleece for Living Room, Small Loveseat Perfect for Apartment Space with Comfortable Cushion and Ergonomic Design, Camel'),
    ("XS-W5656S00100", "Camel", "2S+2O", 'KEIKI 68.5" 2 Seater Couch with 2 Ottomans Teddy Fleece for Living Room, Small Loveseat Perfect for Compact Apartment Space with Plush Comfortable Furniture, Camel'),
    
    ("XS-W5656S00102", "Camel", "3S", 'KEIKI 98.2" 3 Seater Couch Teddy Fleece Fabric for Living Room, Sectional Sofa Perfect for Family Home Furniture Space with Plush Comfortable Cushion and Ergonomic Curved Design, Camel'),
    ("XS-W5656S00104", "Camel", "3S+1O", 'KEIKI 98.2" 3 Seater Couch with Ottoman Teddy Fleece for Living Room, Sectional Sofa Perfect for Family Home Furniture Space with Comfortable Cushion and Ergonomic Design, Camel'),
    ("XS-W5656S00106", "Camel", "3S+2O", 'KEIKI 98.2" 3 Seater Couch with 2 Ottomans Teddy Fleece for Living Room, Sectional Sofa Perfect for Family Home Furniture Space with Plush Comfortable Cushion, Camel'),
    
    ("XS-W5656S00107", "Camel", "4S", 'KEIKI 129.1" Large Sectional Couch Teddy Fleece Fabric for Living Room, 4 Seater Sofa Perfect for Family Home Furniture Space with Plush Comfortable Cushion and Ergonomic Curved Design, Camel'),
    ("XS-W5656S00108", "Camel", "4S+1O", 'KEIKI 129.1" Large Sectional Couch with Chaise Ottoman Teddy Fleece for Living Room, 4 Seater Perfect for Family Home Furniture Space with Comfortable Cushion and Ergonomic Design, Camel'),
    ("XS-W5656S00109", "Camel", "4S+2O", 'KEIKI 129.1" Large Sectional Couch with 2 Ottomans Teddy Fleece for Living Room, Perfect for Family Home Furniture Space with Plush Comfortable Cushion and Ergonomic Design, Camel'),
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
print("高搜索量词埋词版")
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
    for r in short[:5]:
        print(f"  {r['Color']} {r['Size']}: {r['Length']}")
        
if long:
    print(f"\n⚠️ 太长({len(long)}个):")
    for r in long[:5]:
        print(f"  {r['Color']} {r['Size']}: {r['Length']}")

# 保存
df = pd.DataFrame(results)
output = "/root/.openclaw/workspace/KEIKI_OGC_标题_数据驱动版.xlsx"
df.to_excel(output, index=False)
print(f"\n✓ 已保存: {output}")

# 样本
print("\n" + "=" * 100)
print("样本对比 (同一颜色不同尺寸)")
print("=" * 100)

for size in ["2S", "3S", "4S"]:
    r = [x for x in results if x["Color"] == "Orange" and x["Size"] == size][0]
    print(f"\n{size} ({r['Length']}字符):")
    print(r['Title'])
