#!/usr/bin/env python3
import pandas as pd

# 精确生成185-190字符标题

def generate_precise_title(color, size, sku_idx):
    # 尺寸配置
    size_configs = {
        "2S": ('68.5"', "Loveseat"),
        "2S+1O": ('68.5"', "Loveseat Sectional"),
        "2S+2O": ('68.5"', "Modular Loveseat"),
        "3S": ('98.2"', "Oversized Couch"),
        "3S+1O": ('98.2"', "Sectional Couch"),
        "3S+2O": ('98.2"', "Modular Sectional"),
        "4S": ('129.1"', "Large Sectional"),
        "4S+1O": ('129.1"', "Large Sectional"),
        "4S+2O": ('129.1"', "Modular Sectional")
    }
    
    ottoman_desc = {
        "2S": "",
        "2S+1O": " with Chaise Ottoman",
        "2S+2O": " with 2 Ottomans",
        "3S": "",
        "3S+1O": " with Ottoman",
        "3S+2O": " with 2 Ottomans",
        "4S": "",
        "4S+1O": " with Chaise Ottoman",
        "4S+2O": " with 2 Ottomans"
    }
    
    # 颜色形容词 - 不同长度版本
    color_adjs = {
        "Orange": {
            "short": ["Bold", "Warm", "Retro"],
            "medium": ["Vibrant", "Citrus", "Energetic"],
            "long": ["Bold Vibrant", "Retro Warm", "Energetic Stylish", "Designer Citrus", "Stylish Bold"]
        },
        "Green": {
            "short": ["Fresh", "Calm", "Natural"],
            "medium": ["Serene", "Forest", "Organic"],
            "long": ["Fresh Natural", "Botanical Organic", "Calming Serene", "Nature Inspired", "Forest Fresh"]
        },
        "Camel": {
            "short": ["Classic", "Elegant", "Refined"],
            "medium": ["Heritage", "Timeless", "Sophisticated"],
            "long": ["Classic Heritage", "Timeless Elegant", "Sophisticated Refined", "Heritage Classic", "Elegant Refined"]
        }
    }
    
    # 扩展词 - 按长度分级
    extensions = {
        "XS": [  # 155-165字符基础，用于+2O款
            "Teddy Fleece, Comfort for Living Room with Ergonomic Curved Design and Modern Home Style",
            "Teddy Fleece Fabric, Comfort for Living Room with Ergonomic Design and Home Studio Style",
            "Teddy Fleece, Comfort Perfect for Living Room with Ergonomic Design and Home Style",
        ],
        "S": [  # 165-175字符，用于+1O款
            "Teddy Fleece, Cushion Comfort for Living Room with Ergonomic Curved Design and Modern Home Studio Style",
            "Teddy Fleece Fabric, Cushion Comfort for Living Room with Ergonomic Design and Home Studio Style",
            "Teddy Fleece, Cushion Comfort Perfect for Living Room with Ergonomic Design and Home Style",
        ],
        "M": [  # 175-185字符，用于基础款
            "Teddy Fleece, Soft Cushion Comfort Perfect for Living Room with Ergonomic Curved Design and Modern Home Studio Style",
            "Teddy Fleece Fabric, Soft Cushion Comfort Perfect for Living Room with Ergonomic Design and Modern Home Studio Style",
            "Teddy Fleece, Cushion Comfort Perfect for Living Room Furniture with Ergonomic Curved Design and Home Style",
        ],
        "L": [  # 185-195字符，用于短基础款
            "Teddy Fleece Fabric Furniture, Soft Cushion Comfort Perfect for Living Room Space with Ergonomic Curved Design and Modern Home Studio Style",
            "Teddy Fleece, Soft Cushion Comfort Perfect for Your Living Room Furniture with Ergonomic Curved Design and Modern Home Studio Style",
            "Teddy Fleece Fabric, Plush Cushion Comfort Perfect for Living Room Space with Ergonomic Curved Design and Modern Home Studio Furniture Style",
        ]
    }
    
    # 根据尺寸选择扩展词组和形容词长度
    if "2O" in size:
        ext_list = extensions["XS"]
        adj_type = "long"
    elif "1O" in size:
        ext_list = extensions["S"]
        adj_type = "long"
    elif size in ["2S", "3S", "4S"]:
        # 基础款需要最长扩展词
        ext_list = extensions["L"]
        adj_type = "short"
    else:
        ext_list = extensions["M"]
        adj_type = "medium"
    
    dim, size_type = size_configs[size]
    ottoman = ottoman_desc[size]
    adj_list = color_adjs[color][adj_type]
    
    # 尝试所有组合找到185-190字符的标题
    best_title = None
    best_length = 0
    
    for adj in adj_list:
        for ext in ext_list:
            title = f'KEIKI {dim} {adj} {size_type}{ottoman} {ext}, {color}'
            length = len(title)
            
            if 185 <= length <= 190:
                return title, length
            
            # 记录最接近的
            if best_title is None or abs(187 - length) < abs(187 - best_length):
                best_title = title
                best_length = length
    
    return best_title, best_length


# 生成所有Orange/Green/Camel标题
sizes = ["2S", "2S+1O", "2S+2O", "3S", "3S+1O", "3S+2O", "4S", "4S+1O", "4S+2O"]
sku_starts = {"Orange": 91, "Green": 76, "Camel": 96}

results = []

for color in ["Orange", "Green", "Camel"]:
    for i, size in enumerate(sizes):
        sku = f"XS-W5656S00{sku_starts[color] + i:03d}"
        title, length = generate_precise_title(color, size, i)
        
        results.append({
            "SKU": sku,
            "Color": color,
            "Size": size,
            "Title": title,
            "Length": length
        })

# 输出统计
print("=" * 90)
print("Orange/Green/Camel 标题优化结果")
print("=" * 90)

lengths = [r["Length"] for r in results]
print(f"\n总标题: {len(results)}")
print(f"字符范围: {min(lengths)} - {max(lengths)}")
print(f"平均: {sum(lengths)/len(lengths):.1f}")

# 统计符合185-190的比例
in_range = [r for r in results if 185 <= r["Length"] <= 190]
print(f"符合185-190: {len(in_range)}/{len(results)} ({len(in_range)/len(results)*100:.0f}%)")

# 各颜色统计
for color in ["Orange", "Green", "Camel"]:
    color_results = [r for r in results if r["Color"] == color]
    color_lengths = [r["Length"] for r in color_results]
    color_in_range = [r for r in color_results if 185 <= r["Length"] <= 190]
    print(f"\n{color}: 范围 {min(color_lengths)}-{max(color_lengths)}, 平均 {sum(color_lengths)/len(color_lengths):.1f}, 达标 {len(color_in_range)}/9")

# 显示不达标的
short = [r for r in results if r["Length"] < 185]
long = [r for r in results if r["Length"] > 190]

if short:
    print(f"\n⚠️ 太短(<185): {len(short)}个")
    for r in short[:3]:
        print(f"  {r['Color']} {r['Size']}: {r['Length']}")
        
if long:
    print(f"\n⚠️ 太长(>190): {len(long)}个")
    for r in long[:3]:
        print(f"  {r['Color']} {r['Size']}: {r['Length']}")

# 检查禁用词
print("\n" + "=" * 90)
print("禁用词检查")
print("=" * 90)

forbidden_words = ["storage", "ultimate", "premium", "luxurious"]
has_forbidden = []

for r in results:
    title_lower = r["Title"].lower()
    found = [w for w in forbidden_words if w in title_lower]
    if found:
        has_forbidden.append((r, found))

if has_forbidden:
    print(f"⚠️ 发现禁用词({len(has_forbidden)}个):")
    for r, words in has_forbidden[:5]:
        print(f"  {r['Color']} {r['Size']}: {words}")
else:
    print("✓ 无禁用词 (Storage/Ultimate/Premium/Luxurious)")

# 显示样本
print("\n" + "=" * 90)
print("样本标题")
print("=" * 90)

for color in ["Orange", "Green", "Camel"]:
    print(f"\n【{color}】")
    color_results = [r for r in results if r["Color"] == color]
    for r in color_results[:3]:  # 显示前3个
        status = "✓" if 185 <= r["Length"] <= 190 else "✗"
        print(f"  {r['Size']} {status} ({r['Length']}字符): {r['Title']}")

# 保存
df = pd.DataFrame(results)
output = "/root/.openclaw/workspace/KEIKI_Orange_Green_Camel_标题_185-190.xlsx"
df.to_excel(output, index=False)
print(f"\n\n✓ 已保存: {output}")
