#!/usr/bin/env python3
"""
KEIKI 泰迪绒沙发标题生成器
根据拆词数据和埋词规则生成符合规范的标题
"""

# 产品信息
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

# 颜色差异化策略
color_strategy = {
    "Beige": {"keywords": ["cozy", "neutral", "modern", "elegant"], "rooms": ["Living Room", "Apartment"]},
    "Orange": {"keywords": ["vibrant", "bold", "retro", "statement"], "rooms": ["Living Room", "Studio"]},
    "Green": {"keywords": ["fresh", "nature", "calming", "organic"], "rooms": ["Living Room", "Bedroom"]},
    "Camel": {"keywords": ["warm", "classic", "timeless", "sophisticated"], "rooms": ["Living Room", "Office"]},
}

# 尺寸映射
size_map = {
    "2S": "2-Seater",
    "3S": "3-Seater", 
    "4S": "4-Seater"
}

def get_size_descriptor(size_code):
    """获取尺寸描述"""
    if size_code.startswith("2S"):
        return "Compact 2-Seater"
    elif size_code.startswith("3S"):
        return "Mid-Size 3-Seater"
    elif size_code.startswith("4S"):
        return "Large 4-Seater"
    return ""

def get_ottoman_phrase(ottoman_count):
    """获取ottoman描述"""
    if ottoman_count == 0:
        return ""
    elif ottoman_count == 1:
        return "with Ottoman"
    elif ottoman_count == 2:
        return "with 2 Ottomans"
    return ""

def generate_title(product, variant_idx=0):
    """
    生成符合规范的标题
    格式: KEIKI [Size]" [Shape/Type] [Size Descriptor] [Material/Texture] [Core Product], [Configuration], [Convertible Function] with [Key Feature], [Pain Point Solution], for [Room], [Color]
    字符控制: 180-190
    """
    color = product["color"]
    size_code = product["size"]
    width = product["width"]
    ottoman = product["ottoman"]
    
    # 获取颜色策略
    strategy = color_strategy.get(color, {})
    keywords = strategy.get("keywords", ["modern"])
    rooms = strategy.get("rooms", ["Living Room"])
    
    # 基础元素
    brand = "KEIKI"
    shape_type = "Modular Sectional" if "+" in size_code else "Sectional"
    size_descriptor = get_size_descriptor(size_code)
    material = "Premium Teddy Fleece Fabric"
    core_product = "Sofa Couch"
    
    # Ottoman配置描述
    if ottoman == 0:
        config = "Standalone Configuration"
    elif ottoman == 1:
        config = "with Storage Ottoman Chaise"
    else:
        config = "with 2 Storage Ottomans"
    
    # 差异化元素 - 扩展词库以增加字符
    extra_adjectives = [
        "Ultra-Soft", "Luxuriously", "Premium Quality", "Designer", 
        "Handcrafted Style", "Modern Elegant", "Contemporary Chic"
    ]
    adj = extra_adjectives[variant_idx % len(extra_adjectives)]
    
    keyword = keywords[variant_idx % len(keywords)]
    room = rooms[variant_idx % len(rooms)]
    
    # 功能特点 - 扩展
    features = [
        "Plush Cloud-Like Cushions",
        "Soft Teddy Boucle Fabric Texture", 
        "Ergonomic Curved Armrests Design",
        "Deep Comfortable Seating Experience",
        "Tool-Free Easy Assembly Setup"
    ]
    feature = features[variant_idx % len(features)]
    
    # 痛点解决 - 扩展
    pain_points = [
        "Ultimate Lounging Comfort",
        "Cozy All-Day Relaxation Experience",
        "Stylish Modern Living Upgrade",
        "Perfect Family Gathering Spot",
        "Easy Maintenance Daily Care"
    ]
    pain_point = pain_points[variant_idx % len(pain_points)]
    
    # 组装标题 (多版本策略，确保180-190字符)
    titles = []
    
    # 版本1: 完整结构
    title1 = f"{brand} {width} {adj} {shape_type} {size_descriptor} {material} {core_product}, {config}, {keyword} Design with {feature} for {pain_point} in {room}, {color}"
    titles.append(title1)
    
    # 版本2: 强调风格+功能
    title2 = f"{brand} {width} {size_descriptor} {material} {core_product}, {adj} {shape_type} {config}, {keyword} Style with {feature} for {pain_point}, Perfect for {room}, {color}"
    titles.append(title2)
    
    # 版本3: 强调体验
    title3 = f"{brand} {width} {adj} {material} {core_product}, {size_descriptor} {shape_type} {config}, {keyword} Aesthetic with {feature}, Ideal for {pain_point} in {room}, {color}"
    titles.append(title3)
    
    # 版本4: 更长版本
    title4 = f"{brand} {width} {adj} {shape_type} {material} {core_product}, {size_descriptor} {config}, {keyword} Inspired Design with {feature} for {pain_point}, Best Choice for {room}, {color}"
    titles.append(title4)
    
    # 清理并检查
    for t in titles:
        t_clean = t.replace("  ", " ").strip()
        if 180 <= len(t_clean) <= 190:
            return t_clean
    
    # 如果没有符合的，找最接近190的并微调
    best = None
    for t in sorted(titles, key=len, reverse=True):
        t_clean = t.replace("  ", " ").strip()
        if len(t_clean) <= 190:
            best = t_clean
            break
    
    if best:
        # 如果太短，补充描述
        while len(best) < 180:
            best = best.replace(", Perfect for", ", Perfectly Crafted for").replace(", Ideal for", ", Ideal Choice for").replace(", Best Choice for", ", The Best Choice for")
            if len(best) >= 180:
                break
            # 随机插入扩展词
            extensions = [
                "Your Living Space",
                "Home Comfort", 
                "Everyday Relaxation",
                "Quality Time"
            ]
            for ext in extensions:
                test = best.replace(", " + color, f" and {ext}, {color}")
                if 180 <= len(test) <= 190:
                    return test
            break
        return best
    
    # 最终回退
    return titles[0][:187].strip() + "..."

# 生成所有标题
print("=" * 80)
print("KEIKI 泰迪绒沙发标题生成结果")
print("=" * 80)
print()

results = []
for i, p in enumerate(products):
    # 根据颜色和尺寸组合生成不同的variant_idx确保唯一性
    color_idx = ["Beige", "Orange", "Green", "Camel"].index(p["color"])
    size_idx = ["2S", "2S+1O", "2S+2O", "3S", "3S+1O", "3S+2O", "4S", "4S+1O", "4S+2O"].index(p["size"])
    variant_idx = (color_idx * 9 + size_idx) % 5
    
    title = generate_title(p, variant_idx)
    char_count = len(title)
    
    results.append({
        "SKU": p["sku"],
        "Color": p["color"],
        "Size": p["size"],
        "Title": title,
        "Char Count": char_count
    })
    
    print(f"【{p['color']} | {p['size']}】")
    print(f"SKU: {p['sku']}")
    print(f"字符: {char_count}")
    print(f"标题: {title}")
    print()

# 保存到Excel
import pandas as pd
df = pd.DataFrame(results)
output_path = "/root/.openclaw/workspace/KEIKI_泰迪绒沙发_标题.xlsx"
df.to_excel(output_path, index=False)
print(f"✓ 已保存到: {output_path}")
print()

# 统计
print("=" * 80)
print("标题统计")
print("=" * 80)
print(f"总标题数: {len(results)}")
print(f"字符范围: {min(r['Char Count'] for r in results)} - {max(r['Char Count'] for r in results)}")
print(f"平均字符: {sum(r['Char Count'] for r in results) / len(results):.1f}")

# 检查唯一性
titles = [r["Title"] for r in results]
unique_titles = set(titles)
print(f"唯一标题: {len(unique_titles)} / {len(titles)}")
if len(unique_titles) != len(titles):
    print("⚠ 警告: 发现重复标题!")
else:
    print("✓ 所有标题唯一")
