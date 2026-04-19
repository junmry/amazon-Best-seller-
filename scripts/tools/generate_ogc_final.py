#!/usr/bin/env python3
import pandas as pd

# 精确生成185-190字符标题 - 终极版

def build_title_v2(color, size, adj, ext):
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
    
    dim, size_type = size_configs[size]
    ottoman = ottoman_desc[size]
    
    title = f'KEIKI {dim} {adj} {size_type}{ottoman} {ext}, {color}'
    return title


# 扩展词库 - 按长度精确分类
extensions_db = {
    # 用于基础款(无ottoman) - 长扩展词
    "base": [
        "Teddy Fleece, Soft Plush Cushion Comfort Perfect for Your Modern Living Room Furniture Space with Ergonomic Curved Design and Contemporary Home Studio Style",  # ~190 for Loveseat
        "Teddy Fleece, Cushion Comfort Perfect for Your Modern Living Room Furniture Space with Ergonomic Curved Design and Contemporary Home Studio Style",  # ~185
        "Teddy Fleece Fabric, Soft Plush Cushion Comfort Perfect for Your Living Room Space with Ergonomic Curved Design and Modern Home Studio Furniture Style",  # ~190
        "Teddy Fleece Fabric, Cushion Comfort Perfect for Your Living Room Space with Ergonomic Curved Design and Modern Home Studio Furniture Style",  # ~185
        "Teddy Fleece, Soft Plush Comfort Perfect for Your Modern Living Room Furniture Space with Ergonomic Curved Design and Contemporary Home Studio Style",  # ~188
        "Teddy Fleece, Plush Cushion Comfort Perfect for Your Modern Living Room Space with Ergonomic Curved Design and Contemporary Home Studio Furniture Style",  # ~190
        "Teddy Fleece Fabric, Soft Cushion Comfort Perfect for Your Living Room Space with Ergonomic Curved Design and Modern Home Studio Furniture Style",  # ~186
        "Teddy Fleece, Soft Cushion Comfort Perfect for Your Living Room Furniture Space with Ergonomic Curved Design and Modern Home Studio Style",  # ~184
        "Teddy Fleece Fabric, Plush Cushion Comfort Perfect for Your Living Room Furniture Space with Ergonomic Curved Design and Home Studio Style",  # ~185
    ],
    # 用于+1O款 - 中等扩展词
    "plus1": [
        "Teddy Fleece, Cushion Comfort Perfect for Living Room with Ergonomic Curved Design and Modern Home Studio Style",
        "Teddy Fleece Fabric, Cushion Comfort for Living Room with Ergonomic Curved Design and Home Studio Style",
        "Teddy Fleece, Comfort Perfect for Living Room Furniture with Ergonomic Curved Design and Modern Home Style",
        "Teddy Fleece, Cushion Comfort for Living Room Space with Ergonomic Curved Design and Modern Home Studio Style",
        "Teddy Fleece Fabric, Comfort Perfect for Living Room with Ergonomic Curved Design and Home Studio Style",
        "Teddy Fleece, Comfort for Living Room Furniture with Ergonomic Curved Design and Modern Home Studio Style",
        "Teddy Fleece Fabric, Cushion Comfort Perfect for Living Room with Ergonomic Design and Home Studio Style",
        "Teddy Fleece, Cushion Comfort Perfect for Your Living Room with Ergonomic Curved Design and Home Style",
        "Teddy Fleece, Comfort Perfect for Living Room Space with Ergonomic Curved Design and Modern Home Studio Style",
    ],
    # 用于+2O款 - 短扩展词
    "plus2": [
        "Teddy Fleece, Comfort for Living Room with Ergonomic Curved Design and Modern Home Style",
        "Teddy Fleece Fabric, Comfort for Living Room with Ergonomic Design and Home Studio Style",
        "Teddy Fleece, Comfort Perfect for Living Room with Ergonomic Design and Home Style",
        "Teddy Fleece, Comfort for Living Room Space with Ergonomic Curved Design and Home Style",
        "Teddy Fleece Fabric, Comfort for Living Room Furniture with Ergonomic Design and Style",
        "Teddy Fleece, Comfort Perfect for Living Room Furniture with Ergonomic Design and Home Style",
        "Teddy Fleece, Comfort for Living Room with Ergonomic Curved Design and Home Studio Style",
        "Teddy Fleece Fabric, Comfort Perfect for Living Room with Ergonomic Design and Style",
        "Teddy Fleece, Comfort for Your Living Room with Ergonomic Curved Design and Home Style",
    ]
}

# 形容词 - 按长度分类
color_adjs = {
    "Orange": {
        "short": ["Bold", "Warm", "Retro"],
        "medium": ["Vibrant", "Citrus", "Energetic"],
        "long": ["Bold Vibrant", "Retro Warm", "Energetic Stylish"]
    },
    "Green": {
        "short": ["Fresh", "Calm", "Natural"],
        "medium": ["Serene", "Forest", "Organic"],
        "long": ["Fresh Natural", "Calming Serene", "Botanical Organic"]
    },
    "Camel": {
        "short": ["Classic", "Elegant"],
        "medium": ["Heritage", "Timeless", "Refined"],
        "long": ["Classic Heritage", "Timeless Elegant", "Sophisticated Refined"]
    }
}

# 为每个尺寸找到最佳组合
def find_best_title(color, size, color_idx):
    # 选择扩展词组
    if "2O" in size:
        ext_list = extensions_db["plus2"]
        adj_types = ["long", "medium", "short"]
    elif "1O" in size:
        ext_list = extensions_db["plus1"]
        adj_types = ["medium", "long", "short"]
    else:
        ext_list = extensions_db["base"]
        adj_types = ["short", "medium", "long"]
    
    # 尝试所有组合
    for adj_type in adj_types:
        adjs = color_adjs[color][adj_type]
        for adj in adjs:
            for ext in ext_list:
                title = build_title_v2(color, size, adj, ext)
                if 185 <= len(title) <= 190:
                    return title, len(title), True
    
    # 如果没找到，返回最接近的
    best_title = None
    best_len = 0
    for adj_type in adj_types:
        for adj in color_adjs[color][adj_type]:
            for ext in ext_list:
                title = build_title_v2(color, size, adj, ext)
                if best_title is None or abs(187 - len(title)) < abs(187 - best_len):
                    best_title = title
                    best_len = len(title)
    return best_title, best_len, False


# 生成所有标题
sizes = ["2S", "2S+1O", "2S+2O", "3S", "3S+1O", "3S+2O", "4S", "4S+1O", "4S+2O"]
sku_starts = {"Orange": 91, "Green": 76, "Camel": 96}

results = []

for color in ["Orange", "Green", "Camel"]:
    for i, size in enumerate(sizes):
        sku = f"XS-W5656S00{sku_starts[color] + i:03d}"
        title, length, perfect = find_best_title(color, size, i)
        
        results.append({
            "SKU": sku,
            "Color": color,
            "Size": size,
            "Title": title,
            "Length": length,
            "Perfect": perfect
        })

# 输出
print("=" * 90)
print("Orange/Green/Camel 标题优化结果 (185-190字符)")
print("=" * 90)

lengths = [r["Length"] for r in results]
perfect_count = sum(1 for r in results if r["Perfect"])
print(f"\n总标题: {len(results)}")
print(f"字符范围: {min(lengths)} - {max(lengths)}")
print(f"平均: {sum(lengths)/len(lengths):.1f}")
print(f"完全符合185-190: {perfect_count}/{len(results)}")

# 各颜色统计
for color in ["Orange", "Green", "Camel"]:
    color_results = [r for r in results if r["Color"] == color]
    color_lengths = [r["Length"] for r in color_results]
    color_perfect = sum(1 for r in color_results if r["Perfect"])
    print(f"\n{color}: 范围 {min(color_lengths)}-{max(color_lengths)}, 平均 {sum(color_lengths)/len(color_lengths):.1f}, 达标 {color_perfect}/9")

# 显示所有标题
print("\n" + "=" * 90)
print("完整标题列表")
print("=" * 90)

for color in ["Orange", "Green", "Camel"]:
    print(f"\n【{color}】")
    color_results = [r for r in results if r["Color"] == color]
    for r in color_results:
        status = "✓" if r["Perfect"] else f"✗({r['Length']})"
        print(f"  {r['Size']} {status}: {r['Title']}")

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
    print(f"⚠️ 发现{len(issues)}个问题:")
    for r, words in issues[:5]:
        print(f"  {r['Color']} {r['Size']}: {words}")
else:
    print("✓ 无禁用词")

# 保存
df = pd.DataFrame([{k: v for k, v in r.items() if k != "Perfect"} for r in results])
output = "/root/.openclaw/workspace/KEIKI_OGC_标题_最终版.xlsx"
df.to_excel(output, index=False)
print(f"\n✓ 已保存: {output}")
