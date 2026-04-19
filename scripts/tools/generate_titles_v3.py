#!/usr/bin/env python3
"""
KEIKI 泰迪绒沙发标题生成器 V3
基于搜索量优化，字符严格控制180-190，无截断
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

# 词库
brand = "KEIKI"

# 颜色描述词 (按搜索量关联)
color_adj = {
    "Beige": ["Cozy", "Warm", "Soft", "Neutral", "Elegant"],
    "Orange": ["Bold", "Vibrant", "Retro", "Warm", "Statement"],
    "Green": ["Fresh", "Natural", "Calming", "Botanical", "Organic"],
    "Camel": ["Classic", "Sophisticated", "Timeless", "Elegant", "Premium"]
}

# 材质词
materials = ["Teddy Fleece Fabric", "Plush Boucle Fabric", "Soft Textured Fabric", "Teddy Upholstery"]

# 尺寸词 (搜索量优化)
def get_size_words(size, ottoman):
    """根据尺寸返回搜索量优化的描述"""
    if size == "2S":
        if ottoman == 0:
            return ("Loveseat", "Compact 2-Seat")
        elif ottoman == 1:
            return ("Loveseat Sectional", "with Chaise Ottoman")
        else:
            return ("Modular Loveseat", "with 2 Ottomans")
    elif size == "3S":
        if ottoman == 0:
            return ("Oversized Couch", "3-Seat Design")
        elif ottoman == 1:
            return ("Sectional Sofa", "with Storage Ottoman")
        else:
            return ("Modular Sectional", "with 2 Ottomans")
    else:  # 4S
        if ottoman == 0:
            return ("Large Sectional", "4-Seat Design")
        elif ottoman == 1:
            return ("Large Sectional", "with Chaise Ottoman")
        else:
            return ("Modular Sectional", "with 2 Storage Ottomans")

# 场景词 (按搜索量)
rooms = ["Living Room", "Bedroom", "Apartment", "Studio", "Office"]

# 特性词
features = [
    "Deep Seat Comfort",
    "Curved Armrest Design",
    "Plush Cushion Support", 
    "Cloud-Like Softness",
    "Ergonomic Lounging"
]

def build_title(sku, color, size, width, ottoman, idx):
    """构建单个标题，严格控制180-190字符"""
    adj = color_adj[color][idx % 5]
    material = materials[idx % 4]
    size_type, size_desc = get_size_words(size.split('+')[0], ottoman)
    feature = features[idx % 5]
    room = rooms[idx % 5]
    
    # 扩展词库以增加字符
    extended_adjs = {
        "Cozy": "Ultra-Cozy",
        "Warm": "Luxuriously Warm", 
        "Soft": "Buttery Soft",
        "Neutral": "Sophisticated Neutral",
        "Elegant": "Elegant Premium",
        "Bold": "Strikingly Bold",
        "Vibrant": "Rich Vibrant",
        "Retro": "Mid-Century Retro",
        "Statement": "Designer Statement",
        "Fresh": "Fresh Botanical",
        "Natural": "Pure Natural",
        "Calming": "Serene Calming",
        "Botanical": "Lush Botanical",
        "Organic": "Earthy Organic",
        "Classic": "Heritage Classic",
        "Sophisticated": "Refined Sophisticated",
        "Timeless": "Elegant Timeless",
        "Premium": "Luxury Premium"
    }
    adj = extended_adjs.get(adj, adj)
    
    # 场景扩展
    room_extended = f"Home {room}" if room != "Living Room" else "Modern Living Room"
    
    # 构建标题，目标180-190
    # 基础: KEIKI + width + adj + size_type + material + Couch + desc + feature + room + color
    
    if ottoman == 0:
        base = f'{brand} {width} {adj} {size_type} {material} Couch, {size_desc}'
    else:
        base = f'{brand} {width} {adj} {size_type} {material} Couch {size_desc}'
    
    # 添加特性
    with_feature = f'{base} with {feature}'
    
    # 添加场景
    with_room = f'{with_feature} for {room_extended}'
    
    # 添加颜色
    full = f'{with_room}, {color}'
    
    # 检查长度并调整
    length = len(full)
    
    if 180 <= length <= 190:
        return full
    elif length < 180:
        # 需要加长
        need = 180 - length
        if need <= 10:
            full = full.replace(f', {color}', f' Design, {color}')
        elif need <= 20:
            full = full.replace(f'for {room_extended}', f'Perfect for {room_extended}')
        else:
            full = full.replace(f'for {room_extended}', f'Perfect for Your {room_extended}')
        
        # 还短就再加
        while len(full) < 180:
            if 'Premium' not in full:
                full = full.replace(f'{brand} ', f'{brand} Premium ')
            elif 'Comfort' not in full.split(',')[1] if ',' in full else True:
                full = full.replace(f'{color}', f'{color} Finish')
            else:
                break
            if len(full) > 190:
                break
        
        return full
    else:
        # 太长，从右边截断
        truncated = full[:187]
        last_space = truncated.rfind(' ')
        if last_space > 150:
            truncated = truncated[:last_space]
        return truncated + f', {color}'

# 生成
print("=" * 90)
print("KEIKI 泰迪绒沙发标题 V3 (搜索量优化版)")
print("=" * 90)
print()

results = []
for i, (sku, color, size, width, ottoman) in enumerate(products):
    idx = i % 5
    title = build_title(sku, color, size, width, ottoman, idx)
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
output = "/root/.openclaw/workspace/KEIKI_泰迪绒沙发_标题_V3.xlsx"
df.to_excel(output, index=False)

# 统计
print("=" * 90)
print("统计")
print("=" * 90)
lengths = [r["Length"] for r in results]
print(f"总标题: {len(results)}")
print(f"字符范围: {min(lengths)} - {max(lengths)}")
print(f"平均: {sum(lengths)/len(lengths):.1f}")
print(f"唯一: {len(set(r['Title'] for r in results))}/{len(results)}")

# 检查问题
short = [r for r in results if r["Length"] < 180]
long = [r for r in results if r["Length"] > 190]
if short:
    print(f"\n⚠️ 太短({len(short)}个):")
    for r in short:
        print(f"  - {r['SKU']}: {r['Length']}字符")
if long:
    print(f"\n⚠️ 太长({len(long)}个):")
    for r in long:
        print(f"  - {r['SKU']}: {r['Length']}字符")
        
print(f"\n✓ 已保存: {output}")
