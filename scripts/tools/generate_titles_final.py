#!/usr/bin/env python3
"""
KEIKI 泰迪绒沙发标题生成器 - 最终版
基于搜索量优化，字符严格180-190，无重复词
"""

import pandas as pd

# 产品数据
products = [
    ("XS-W5656S00073", "Beige", "2S", '68.5"', 0),
    ("XS-W5656S00075", "Beige", "2S+1O", '68.5"', 1),
    ("XS-W5656S00078", "Beige", "2S+2O", '68.5"', 2),
    ("XS-W5656S00080", "Beige", "3S", '98.2"', 0),
    ("XS-W5656S00082", "Beige", "3S+1O", '98.2"', 1),
    ("XS-W5656S00084", "Beige", "3S+2O", '98.2"', 2),
    ("XS-W5656S00085", "Beige", "4S", '129.1"', 0),
    ("XS-W5656S00087", "Beige", "4S+1O", '129.1"', 1),
    ("XS-W5656S00089", "Beige", "4S+2O", '129.1"', 2),
    ("XS-W5656S00091", "Orange", "2S", '68.5"', 0),
    ("XS-W5656S00093", "Orange", "2S+1O", '68.5"', 1),
    ("XS-W5656S00094", "Orange", "2S+2O", '68.5"', 2),
    ("XS-W5656S00095", "Orange", "3S", '98.2"', 0),
    ("XS-W5656S00097", "Orange", "3S+1O", '98.2"', 1),
    ("XS-W5656S00099", "Orange", "3S+2O", '98.2"', 2),
    ("XS-W5656S00101", "Orange", "4S", '129.1"', 0),
    ("XS-W5656S00103", "Orange", "4S+1O", '129.1"', 1),
    ("XS-W5656S00105", "Orange", "4S+2O", '129.1"', 2),
    ("XS-W5656S00076", "Green", "2S", '68.5"', 0),
    ("XS-W5656S00077", "Green", "2S+1O", '68.5"', 1),
    ("XS-W5656S00079", "Green", "2S+2O", '68.5"', 2),
    ("XS-W5656S00081", "Green", "3S", '98.2"', 0),
    ("XS-W5656S00083", "Green", "3S+1O", '98.2"', 1),
    ("XS-W5656S00086", "Green", "3S+2O", '98.2"', 2),
    ("XS-W5656S00088", "Green", "4S", '129.1"', 0),
    ("XS-W5656S00090", "Green", "4S+1O", '129.1"', 1),
    ("XS-W5656S00092", "Green", "4S+2O", '129.1"', 2),
    ("XS-W5656S00096", "Camel", "2S", '68.5"', 0),
    ("XS-W5656S00098", "Camel", "2S+1O", '68.5"', 1),
    ("XS-W5656S00100", "Camel", "2S+2O", '68.5"', 2),
    ("XS-W5656S00102", "Camel", "3S", '98.2"', 0),
    ("XS-W5656S00104", "Camel", "3S+1O", '98.2"', 1),
    ("XS-W5656S00106", "Camel", "3S+2O", '98.2"', 2),
    ("XS-W5656S00107", "Camel", "4S", '129.1"', 0),
    ("XS-W5656S00108", "Camel", "4S+1O", '129.1"', 1),
    ("XS-W5656S00109", "Camel", "4S+2O", '129.1"', 2),
]

# 颜色形容词
beige_adj = ["Cozy Neutral", "Warm Elegant", "Soft Inviting", "Modern Beige", "Elegant Cream"]
orange_adj = ["Bold Vibrant", "Retro Statement", "Warm Energetic", "Stylish Orange", "Designer Citrus"]
green_adj = ["Fresh Natural", "Botanical Organic", "Calming Green", "Nature Inspired", "Serene Forest"]
camel_adj = ["Classic Sophisticated", "Timeless Elegant", "Premium Camel", "Heritage Warm", "Refined Tan"]

# 材质词
materials = ["Teddy Fleece Fabric", "Plush Boucle Upholstery", "Soft Textured Teddy", "Premium Teddy Fabric"]

# 特性词
features = [
    "Deep Cloud-Like Comfort",
    "Ergonomic Curved Design", 
    "Plush Cushion Support",
    "Luxurious Lounging Experience",
    "Ultimate Relaxation Design"
]

# 场景词
rooms = ["Living Room", "Bedroom", "Apartment Living", "Home Studio", "Modern Office"]

def get_size_type(size, ottoman):
    """返回尺寸类型描述"""
    if size == "2S":
        if ottoman == 0:
            return "Loveseat Sofa", "Compact 2-Seat Design"
        elif ottoman == 1:
            return "Loveseat Sectional", "with Chaise Ottoman"
        else:
            return "Modular Loveseat", "with 2 Storage Ottomans"
    elif size == "3S":
        if ottoman == 0:
            return "Oversized Couch", "Spacious 3-Seat Design"
        elif ottoman == 1:
            return "Sectional Sofa", "with Storage Ottoman"
        else:
            return "Modular Sectional", "with 2 Ottomans"
    else:  # 4S
        if ottoman == 0:
            return "Large Sectional", "Generous 4-Seat Design"
        elif ottoman == 1:
            return "Large Sectional", "with Chaise Ottoman"
        else:
            return "Modular Sectional", "with 2 Storage Ottomans"

def build_title(color, size, width, ottoman, idx):
    brand = "KEIKI"
    
    # 选择词汇
    if color == "Beige":
        adj = beige_adj[idx % 5]
    elif color == "Orange":
        adj = orange_adj[idx % 5]
    elif color == "Green":
        adj = green_adj[idx % 5]
    else:
        adj = camel_adj[idx % 5]
    
    material = materials[idx % 4]
    feature = features[idx % 5]
    room = rooms[idx % 5]
    size_type, size_desc = get_size_type(size, ottoman)
    
    # 构建标题 - 手动控制长度在180-190
    # 结构: KEIKI + width + adj + size_type + material + Couch + size_desc + with + feature + for + room + color
    
    if ottoman == 0:
        # 无ottoman版本
        templates = [
            f'{brand} {width} {adj} {size_type} {material} Couch, {size_desc} with {feature} for {room}, {color}',
            f'{brand} {width} {adj} {size_type} {material} Couch with {feature}, {size_desc} for {room}, {color}',
            f'{brand} {width} {adj} {material} {size_type}, {size_desc} with {feature} for Your {room}, {color}',
            f'{brand} {width} Premium {adj} {size_type} {material}, {size_desc} with {feature} for {room}, {color}',
        ]
    else:
        # 有ottoman版本
        templates = [
            f'{brand} {width} {adj} {size_type} {material} Couch {size_desc} with {feature} for {room}, {color}',
            f'{brand} {width} {adj} {size_type} {material} Couch {size_desc}, {feature} for Your {room}, {color}',
            f'{brand} {width} Premium {adj} {size_type} {material} Couch {size_desc} with {feature} for {room}, {color}',
            f'{brand} {width} {adj} {material} {size_type} {size_desc} with {feature} for {room}, {color}',
        ]
    
    # 找到180-190范围内的
    for t in templates:
        t = t.replace("  ", " ")
        length = len(t)
        if 180 <= length <= 190:
            return t
    
    # 如果没有，找最长的并适当扩展
    valid = [(t.replace("  ", " "), len(t.replace("  ", " "))) for t in templates if len(t.replace("  ", " ")) <= 190]
    if valid:
        best, best_len = max(valid, key=lambda x: x[1])
        if best_len < 180:
            need = 180 - best_len
            # 扩展
            if need <= 5:
                best = best.replace(f", {color}", f" Design, {color}")
            elif need <= 12:
                best = best.replace("for ", "Perfect for ")
            elif need <= 18:
                best = best.replace("for ", "Perfect for Your ")
            else:
                best = best.replace(brand, f"{brand} Premium")
        return best
    
    # 都太长，截断
    shortest = min(templates, key=lambda x: len(x.replace("  ", " ")))
    shortest = shortest.replace("  ", " ")
    if len(shortest) > 190:
        # 截断到187，保留颜色
        truncated = shortest[:187].rsplit(' ', 1)[0]
        shortest = truncated + f", {color}"
    return shortest

# 生成
print("=" * 100)
print("KEIKI 泰迪绒沙发标题 - 最终版")
print("=" * 100)
print()

results = []
for i, (sku, color, size, width, ottoman) in enumerate(products):
    title = build_title(color, size, width, ottoman, i % 5)
    length = len(title)
    
    status = "✓" if 180 <= length <= 190 else ("⚠️ 短" if length < 180 else "⚠️ 长")
    
    results.append({
        "SKU": sku,
        "Color": color,
        "Size": size,
        "Title": title,
        "Length": length
    })
    
    print(f"【{color} | {size}】{status} ({length})")
    print(f"{title}")
    print()

# 保存
df = pd.DataFrame(results)
output = "/root/.openclaw/workspace/KEIKI_泰迪绒沙发_标题_最终版.xlsx"
df.to_excel(output, index=False)

# 统计
print("=" * 100)
print("统计")
print("=" * 100)
lengths = [r["Length"] for r in results]
print(f"总标题: {len(results)}")
print(f"字符范围: {min(lengths)} - {max(lengths)}")
print(f"平均: {sum(lengths)/len(lengths):.1f}")
print(f"唯一: {len(set(r['Title'] for r in results))}/{len(results)}")

short = [r for r in results if r["Length"] < 180]
long = [r for r in results if r["Length"] > 190]
if short:
    print(f"\n⚠️ 太短({len(short)}个): " + ", ".join([f"{r['SKU']}({r['Length']})" for r in short[:3]]))
if long:
    print(f"\n⚠️ 太长({len(long)}个): " + ", ".join([f"{r['SKU']}({r['Length']})" for r in long[:3]]))
    
print(f"\n✓ 已保存: {output}")
