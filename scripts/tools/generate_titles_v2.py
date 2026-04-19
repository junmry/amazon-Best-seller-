#!/usr/bin/env python3
"""
KEIKI 泰迪绒沙发标题生成器 V2
基于搜索量数据针对性优化，不添加无中生有的功能
"""

# 产品基础信息
products = [
    # Beige 系列
    {"sku": "XS-W5656S00073", "color": "Beige", "size": "2S", "width": "68.5\"", "ottoman": 0},
    {"sku": "XS-W5656S00075", "color": "Beige", "size": "2S+1O", "width": "68.5\"", "ottoman": 1},
    {"sku": "XS-W5656S00078", "color": "Beige", "size": "2S+2O", "width": "68.5\"", "ottoman": 2},
    {"sku": "XS-W5656S00080", "color": "Beige", "size": "3S", "width": "98.2\"", "ottoman": 0},
    {"sku": "XS-W5656S00082", "color": "Beige", "size": "3S+1O", "width": "98.2\"", "ottoman": 1},
    {"sku": "XS-W5656S00084", "color": "Beige", "size": "3S+2O", "width": "98.2\"", "ottoman": 2},
    {"sku": "XS-W5656S00085", "color": "Beige", "size": "4S", "width": "129.1\"", "ottoman": 0},
    {"sku": "XS-W5656S00087", "color": "Beige", "size": "4S+1O", "width": "129.1\"", "ottoman": 1},
    {"sku": "XS-W5656S00089", "color": "Beige", "size": "4S+2O", "width": "129.1\"", "ottoman": 2},
    # Orange 系列
    {"sku": "XS-W5656S00091", "color": "Orange", "size": "2S", "width": "68.5\"", "ottoman": 0},
    {"sku": "XS-W5656S00093", "color": "Orange", "size": "2S+1O", "width": "68.5\"", "ottoman": 1},
    {"sku": "XS-W5656S00094", "color": "Orange", "size": "2S+2O", "width": "68.5\"", "ottoman": 2},
    {"sku": "XS-W5656S00095", "color": "Orange", "size": "3S", "width": "98.2\"", "ottoman": 0},
    {"sku": "XS-W5656S00097", "color": "Orange", "size": "3S+1O", "width": "98.2\"", "ottoman": 1},
    {"sku": "XS-W5656S00099", "color": "Orange", "size": "3S+2O", "width": "98.2\"", "ottoman": 2},
    {"sku": "XS-W5656S00101", "color": "Orange", "size": "4S", "width": "129.1\"", "ottoman": 0},
    {"sku": "XS-W5656S00103", "color": "Orange", "size": "4S+1O", "width": "129.1\"", "ottoman": 1},
    {"sku": "XS-W5656S00105", "color": "Orange", "size": "4S+2O", "width": "129.1\"", "ottoman": 2},
    # Green 系列
    {"sku": "XS-W5656S00076", "color": "Green", "size": "2S", "width": "68.5\"", "ottoman": 0},
    {"sku": "XS-W5656S00077", "color": "Green", "size": "2S+1O", "width": "68.5\"", "ottoman": 1},
    {"sku": "XS-W5656S00079", "color": "Green", "size": "2S+2O", "width": "68.5\"", "ottoman": 2},
    {"sku": "XS-W5656S00081", "color": "Green", "size": "3S", "width": "98.2\"", "ottoman": 0},
    {"sku": "XS-W5656S00083", "color": "Green", "size": "3S+1O", "width": "98.2\"", "ottoman": 1},
    {"sku": "XS-W5656S00086", "color": "Green", "size": "3S+2O", "width": "98.2\"", "ottoman": 2},
    {"sku": "XS-W5656S00088", "color": "Green", "size": "4S", "width": "129.1\"", "ottoman": 0},
    {"sku": "XS-W5656S00090", "color": "Green", "size": "4S+1O", "width": "129.1\"", "ottoman": 1},
    {"sku": "XS-W5656S00092", "color": "Green", "size": "4S+2O", "width": "129.1\"", "ottoman": 2},
    # Camel 系列
    {"sku": "XS-W5656S00096", "color": "Camel", "size": "2S", "width": "68.5\"", "ottoman": 0},
    {"sku": "XS-W5656S00098", "color": "Camel", "size": "2S+1O", "width": "68.5\"", "ottoman": 1},
    {"sku": "XS-W5656S00100", "color": "Camel", "size": "2S+2O", "width": "68.5\"", "ottoman": 2},
    {"sku": "XS-W5656S00102", "color": "Camel", "size": "3S", "width": "98.2\"", "ottoman": 0},
    {"sku": "XS-W5656S00104", "color": "Camel", "size": "3S+1O", "width": "98.2\"", "ottoman": 1},
    {"sku": "XS-W5656S00106", "color": "Camel", "size": "3S+2O", "width": "98.2\"", "ottoman": 2},
    {"sku": "XS-W5656S00107", "color": "Camel", "size": "4S", "width": "129.1\"", "ottoman": 0},
    {"sku": "XS-W5656S00108", "color": "Camel", "size": "4S+1O", "width": "129.1\"", "ottoman": 1},
    {"sku": "XS-W5656S00109", "color": "Camel", "size": "4S+2O", "width": "129.1\"", "ottoman": 2},
]

# ============ 基于搜索量的词库配置 ============

# 颜色维度（搜索量从高到低）
color_keywords = {
    # Beige - 中性温暖
    "Beige": {
        "adj": ["Neutral", "Warm", "Cozy", "Soft", "Elegant"],  # cozy权重高(cloud相关)
        "rooms": ["Living Room", "Apartment", "Bedroom", "Studio"],
        "vibe": ["inviting", "comfortable", "relaxing"]
    },
    # Orange - 活力复古
    "Orange": {
        "adj": ["Bold", "Vibrant", "Retro", "Statement", "Warm"],
        "rooms": ["Living Room", "Studio", "Dorm", "Apartment"],
        "vibe": ["energetic", "stylish", "modern"]
    },
    # Green - 自然清新
    "Green": {
        "adj": ["Fresh", "Natural", "Calming", "Botanical", "Organic"],
        "rooms": ["Living Room", "Bedroom", "Apartment", "Office"],
        "vibe": ["peaceful", "serene", "refreshing"]
    },
    # Camel - 经典高端
    "Camel": {
        "adj": ["Classic", "Timeless", "Sophisticated", "Elegant", "Premium"],
        "rooms": ["Living Room", "Office", "Studio", "Apartment"],
        "vibe": ["refined", "luxurious", "professional"]
    }
}

# 尺寸维度 - 基于搜索量优化
def get_size_config(size_code):
    """
    基于搜索量返回最优尺寸描述
    2S → Loveseat (32,999) 而非 2-Seater
    3S → Oversized 3-Seat (oversized 20,101)
    4S → Oversized Sectional / Large Sectional (sectional 122,224)
    """
    base = size_code.split('+')[0]
    ottoman = 1 if '+1O' in size_code else (2 if '+2O' in size_code else 0)
    
    if base == "2S":
        # Loveseat 32,999 搜索量最高
        if ottoman == 0:
            return {
                "type": "Loveseat",
                "desc": "Compact Loveseat",
                "width_show": True,  # Loveseat需要显示宽度
                "ottoman_phrase": ""
            }
        elif ottoman == 1:
            return {
                "type": "Loveseat Sectional",
                "desc": "Loveseat with Chaise",
                "width_show": True,
                "ottoman_phrase": "and Ottoman"
            }
        else:  # +2O
            return {
                "type": "Modular Loveseat",
                "desc": "Loveseat with Storage Ottomans",
                "width_show": True,
                "ottoman_phrase": "and 2 Ottomans"
            }
    
    elif base == "3S":
        # Oversized 20,101 + 3-Seat
        if ottoman == 0:
            return {
                "type": "Oversized Couch",
                "desc": "Oversized 3-Seat Sofa",
                "width_show": True,
                "ottoman_phrase": ""
            }
        elif ottoman == 1:
            return {
                "type": "Sectional Sofa",
                "desc": "Oversized 3-Seat Sectional",
                "width_show": True,
                "ottoman_phrase": "with Ottoman"
            }
        else:
            return {
                "type": "Modular Sectional",
                "desc": "3-Seat with Storage Ottomans",
                "width_show": True,
                "ottoman_phrase": "with 2 Ottomans"
            }
    
    else:  # 4S
        # Sectional 122,224 搜索量极高
        if ottoman == 0:
            return {
                "type": "Large Sectional",
                "desc": "Oversized 4-Seat Couch",
                "width_show": True,
                "ottoman_phrase": ""
            }
        elif ottoman == 1:
            return {
                "type": "Large Sectional",
                "desc": "4-Seat with Chaise Ottoman",
                "width_show": True,
                "ottoman_phrase": "with Storage Ottoman"
            }
        else:
            return {
                "type": "Modular Sectional",
                "desc": "4-Seat with Storage Ottomans",
                "width_show": True,
                "ottoman_phrase": "with 2 Storage Ottomans"
            }

# 材质词（搜索量高且准确）
material_phrases = [
    "Teddy Fleece Fabric",  # 准确材质
    "Plush Teddy Upholstery",
    "Soft Boucle Fabric",
    "Textured Teddy Fabric"
]

# 场景词（按搜索量排序）
room_keywords = {
    "Living Room": 179399,      # 最高
    "Bedroom": 26080,
    "Apartment": 4813,
    "Studio": 2803,
    "Dorm": 8676,
    "Office": 8666
}

# 功能/特性词（产品实际有的）
feature_words = [
    "Deep Seat Comfort",
    "Curved Armrest Design", 
    "Plush Cushion Support",
    "Cloud-Like Softness",
    "Ergonomic Lounging"
]

# 人群词（搜索量相关）
audience_words = {
    "Adults": 156039,       # 搜索量高
    "Family": "high_conv",  # 转化好
    "Small Space": 223685,  # small搜索量高
    "Couples": "relevant"   # loveseat相关
}

def generate_title_v2(product, variant_idx=0):
    """生成基于搜索量优化的标题"""
    color = product["color"]
    size_code = product["size"]
    width = product["width"]
    ottoman = product["ottoman"]
    
    # 获取尺寸配置
    size_config = get_size_config(size_code)
    
    # 获取颜色策略
    strategy = color_keywords.get(color, {})
    adjectives = strategy.get("adj", ["Modern"])
    rooms = strategy.get("rooms", ["Living Room"])
    
    # 根据variant_idx轮替元素确保唯一性
    adj = adjectives[variant_idx % len(adjectives)]
    room = rooms[variant_idx % len(rooms)]
    
    # 材质
    material = material_phrases[variant_idx % len(material_phrases)]
    
    # 特性
    feature = feature_words[variant_idx % len(feature_words)]
    
    brand = "KEIKI"
    
    # 构建标题 - 按权重排序：
    # 1. Brand (必须)
    # 2. Width (具体数字)
    # 3. Color Adj (颜色描述)
    # 4. Size Type (尺寸类型 - 搜索量优化)
    # 5. Material (材质)
    # 6. Core Product (couch优先于sofa)
    # 7. Ottoman/Config (配置)
    # 8. Feature (特性)
    # 9. Room (场景)
    # 10. Color (颜色)
    
    # 多种组合尝试，确保180-190字符
    titles = []
    
    # 组合1: 完整版
    t1 = f"{brand} {width} {adj} {size_config['type']} {material} Couch, {size_config['desc']}, {feature} for {room}, {color}"
    titles.append(t1)
    
    # 组合2: 强调配置
    if ottoman > 0:
        t2 = f"{brand} {width} {size_config['type']} {material} Couch {size_config['ottoman_phrase']}, {adj} {size_config['desc']}, {feature} for {room}, {color}"
    else:
        t2 = f"{brand} {width} {adj} {size_config['type']} {material} Couch, {feature} {size_config['desc']}, Perfect for {room}, {color}"
    titles.append(t2)
    
    # 组合3: 强调体验
    t3 = f"{brand} {width} {size_config['type']} {material} Couch for {room}, {adj} {size_config['desc']} {size_config['ottoman_phrase']}, {feature}, {color}"
    titles.append(t3)
    
    # 组合4: 更长版
    t4 = f"{brand} {width} {adj} {size_config['type']} {material} Couch, {size_config['desc']} {size_config['ottoman_phrase']}, {feature} Design for {room}, {color}"
    titles.append(t4)
    
    # 清理并检查长度
    for t in titles:
        t_clean = t.replace("  ", " ").replace(" ,", ",").replace(", ,", ",").strip()
        if 180 <= len(t_clean) <= 190:
            return t_clean
    
    # 找最接近190的
    best = None
    for t in sorted(titles, key=len, reverse=True):
        t_clean = t.replace("  ", " ").replace(" ,", ",").strip()
        if len(t_clean) <= 190:
            best = t_clean
            break
    
    if best:
        # 如果太短，补充到180+
        extensions = [
            (" for ", " Perfect for "),
            (" Design for ", " Design Ideal for "),
            (", Couch,", ", Couch with Deep Seat Comfort,"),
        ]
        for old, new in extensions:
            if len(best) < 180:
                best = best.replace(old, new, 1)
        # 如果还短，直接加长描述
        if len(best) < 180:
            best = best.replace(" for ", " Perfect for Home Relaxation in ")
        if len(best) > 190:
            best = best[:187].rsplit(' ', 1)[0] + "..."
        return best
    
    return titles[0][:187] + "..."

# 生成所有标题
print("=" * 90)
print("KEIKI 泰迪绒沙发标题 V2 (搜索量优化版)")
print("=" * 90)
print()

results = []
for i, p in enumerate(products):
    # 计算variant_idx确保唯一性
    colors = ["Beige", "Orange", "Green", "Camel"]
    sizes = ["2S", "2S+1O", "2S+2O", "3S", "3S+1O", "3S+2O", "4S", "4S+1O", "4S+2O"]
    color_idx = colors.index(p["color"])
    size_idx = sizes.index(p["size"])
    variant_idx = (color_idx * 9 + size_idx) % 5
    
    title = generate_title_v2(p, variant_idx)
    char_count = len(title)
    
    # 检查是否有...
    has_ellipsis = "..." in title
    
    results.append({
        "SKU": p["sku"],
        "Color": p["color"],
        "Size": p["size"],
        "Title": title,
        "Char Count": char_count,
        "Has Ellipsis": has_ellipsis
    })
    
    status = "⚠️ 被截断" if has_ellipsis else "✓"
    print(f"【{p['color']} | {p['size']}】{status}")
    print(f"SKU: {p['sku']}")
    print(f"字符: {char_count}")
    print(f"标题: {title}")
    print()

# 保存
import pandas as pd
df = pd.DataFrame(results)
output_path = "/root/.openclaw/workspace/KEIKI_泰迪绒沙发_标题_V2.xlsx"
df.to_excel(output_path, index=False)
print(f"✓ 已保存: {output_path}")
print()

# 统计
print("=" * 90)
print("统计")
print("=" * 90)
print(f"总标题数: {len(results)}")
print(f"字符范围: {min(r['Char Count'] for r in results)} - {max(r['Char Count'] for r in results)}")
print(f"平均字符: {sum(r['Char Count'] for r in results) / len(results):.1f}")

# 检查唯一性和截断
titles_list = [r["Title"] for r in results]
unique_titles = set(titles_list)
print(f"唯一标题: {len(unique_titles)} / {len(titles_list)}")

ellipsis_count = sum(1 for r in results if r["Has Ellipsis"])
print(f"被截断标题: {ellipsis_count}")

if ellipsis_count > 0:
    print("\n⚠️ 以下标题被截断，需要手动调整：")
    for r in results:
        if r["Has Ellipsis"]:
            print(f"  - {r['SKU']} ({r['Color']} {r['Size']})")
