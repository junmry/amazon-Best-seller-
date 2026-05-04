#!/usr/bin/env python3
"""
Amazon Best Sellers & New Releases Monitor
监控亚马逊Sofa和Chair类目的Best Seller和New Release前100产品
"""

import json
import os
import re
import time
from datetime import datetime
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

# 配置
DATA_DIR = "/root/.openclaw/workspace/data/amazon_monitor"
CATEGORIES = {
    "sofa": {
        "best_sellers": "https://www.amazon.com/Best-Sellers-Sofas-Couches/zgbs/home-garden/3733651",
        "new_releases": "https://www.amazon.com/gp/new-releases/home-garden/3733651"
    },
    "chair": {
        "best_sellers": "https://www.amazon.com/Best-Sellers-Chairs/zgbs/home-garden/3733811",
        "new_releases": "https://www.amazon.com/gp/new-releases/home-garden/3733811"
    }
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
}


def ensure_dir(path):
    """确保目录存在"""
    os.makedirs(path, exist_ok=True)


def fetch_page(url, max_retries=3):
    """获取页面内容，带重试机制"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=30)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # 指数退避
            else:
                raise
    return None


def parse_products(html, category, list_type):
    """解析产品信息"""
    soup = BeautifulSoup(html, 'html.parser')
    products = []
    
    # 亚马逊Best Sellers页面的产品卡片选择器
    # 注意：亚马逊经常更新页面结构，这些选择器可能需要调整
    
    # 尝试多种可能的选择器
    selectors = [
        'div[data-asin]',
        'div[data-component-type="s-search-result"]',
        'div.zg-grid-general-faceout',
        'div._cDEzb_grid-cell_1LJt2'
    ]
    
    items = []
    for selector in selectors:
        items = soup.select(selector)
        if items:
            break
    
    for idx, item in enumerate(items[:100], 1):  # 只取前100
        try:
            product = {
                "rank": idx,
                "category": category,
                "list_type": list_type,
                "crawl_time": datetime.now().isoformat(),
                "asin": item.get('data-asin', ''),
            }
            
            # 提取标题 - 尝试多种选择器（亚马逊经常更新页面结构）
            title_selectors = [
                'a span[data-a-color="base"]',
                'a span[dir="auto"]',
                'h2 a span',
                '._cDEzb_p13n-sc-css-line-clamp-3_g3dyQ',
                '.p13n-sc-truncated',
                'a[href*="/dp/"]',  # 标题常在链接中
                'a',  # 兜底：任何链接
            ]
            for ts in title_selectors:
                title_elem = item.select_one(ts)
                if title_elem:
                    text = title_elem.get_text(strip=True)
                    if text and len(text) > 5:  # 过滤掉太短的文本
                        product["title"] = text
                        break
            
            # 如果从HTML提取不到标题，尝试从URL解析
            if not product.get("title"):
                link_elem = item.select_one('a[href*="/dp/"]') or item.select_one('a[href]')
                if link_elem:
                    href = link_elem.get('href', '')
                    match = re.search(r'/([^/]+)/dp/', href)
                    if match:
                        slug = match.group(1)
                        product["title"] = slug.replace('-', ' ').title()
            
            # 提取价格
            price_selectors = [
                'span.a-price .a-offscreen',
                'span.a-price-range .a-offscreen',
                '._cDEzb_p13n-sc-price_3mJ9Z'
            ]
            for ps in price_selectors:
                price_elem = item.select_one(ps)
                if price_elem:
                    product["price"] = price_elem.get_text(strip=True)
                    break
            
            # 提取评分
            rating_selectors = [
                'span.a-icon-alt',
                'i.a-icon-star-small span'
            ]
            for rs in rating_selectors:
                rating_elem = item.select_one(rs)
                if rating_elem:
                    rating_text = rating_elem.get_text(strip=True)
                    match = re.search(r'(\d+\.?\d*)\s*out\s*of', rating_text)
                    if match:
                        product["rating"] = match.group(1)
                    break
            
            # 提取评论数
            review_selectors = [
                'span.a-size-base',
                'a[href*="#customerReviews"] span'
            ]
            for rs in review_selectors:
                review_elem = item.select_one(rs)
                if review_elem:
                    text = review_elem.get_text(strip=True).replace(',', '')
                    if text.isdigit():
                        product["review_count"] = int(text)
                        break
            
            # 提取产品链接
            link_elem = item.select_one('a[href*="/dp/"]') or item.select_one('a[href]')
            if link_elem:
                href = link_elem.get('href', '')
                product["url"] = urljoin("https://www.amazon.com", href)
            
            # 提取图片
            img_elem = item.select_one('img')
            if img_elem:
                product["image_url"] = img_elem.get('src', '') or img_elem.get('data-src', '')
            
            # 只添加有ASIN的产品
            if product.get("asin"):
                products.append(product)
                
        except Exception as e:
            print(f"Error parsing product: {e}")
            continue
    
    return products


def save_data(products, category, list_type):
    """保存数据到JSON文件"""
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{category}_{list_type}_{today}.json"
    filepath = os.path.join(DATA_DIR, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    
    return filepath


def compare_with_previous(products, category, list_type):
    """与上一次的数据比较，检测排名变动"""
    # 查找最近的历史文件
    files = sorted([f for f in os.listdir(DATA_DIR) 
                   if f.startswith(f"{category}_{list_type}_") and f.endswith('.json')])
    
    if len(files) < 2:
        return None  # 没有历史数据可比较
    
    # 读取上一次的数据
    prev_file = files[-2]  # 倒数第二个文件
    prev_path = os.path.join(DATA_DIR, prev_file)
    
    try:
        with open(prev_path, 'r', encoding='utf-8') as f:
            prev_products = json.load(f)
        
        # 创建ASIN到排名的映射
        prev_ranks = {p['asin']: p['rank'] for p in prev_products if 'asin' in p}
        
        changes = []
        for p in products:
            asin = p.get('asin')
            if asin and asin in prev_ranks:
                old_rank = prev_ranks[asin]
                new_rank = p['rank']
                if old_rank != new_rank:
                    change = old_rank - new_rank  # 正值表示排名上升
                    changes.append({
                        "asin": asin,
                        "title": p.get('title', '')[:50] + '...' if p.get('title') and len(p.get('title')) > 50 else p.get('title', ''),
                        "old_rank": old_rank,
                        "new_rank": new_rank,
                        "change": change,
                        "direction": "up" if change > 0 else "down"
                    })
        
        return sorted(changes, key=lambda x: abs(x['change']), reverse=True)[:20]  # Top 20变化
    
    except Exception as e:
        print(f"Error comparing data: {e}")
        return None


def send_notification(changes, category, list_type):
    """发送变动通知（通过message工具或保存到文件）"""
    if not changes:
        return
    
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"changes_{category}_{list_type}_{today}.json"
    filepath = os.path.join(DATA_DIR, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(changes, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'='*60}")
    print(f"📊 {category.upper()} - {list_type.replace('_', ' ').upper()} 排名变动")
    print(f"{'='*60}")
    
    for c in changes[:10]:  # 显示前10个变化
        emoji = "🚀" if c['direction'] == 'up' else "📉"
        print(f"{emoji} #{c['new_rank']} (was #{c['old_rank']}, {c['change']:+d}) - {c['title']}")
    
    print(f"\n详细变动已保存: {filepath}")


def main():
    """主函数"""
    print(f"🕐 开始爬取: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    ensure_dir(DATA_DIR)
    
    all_results = {}
    
    for category, urls in CATEGORIES.items():
        print(f"\n📦 正在爬取 {category.upper()} 类目...")
        
        for list_type, url in urls.items():
            print(f"  └─ {list_type.replace('_', ' ').title()}...", end=" ")
            
            try:
                html = fetch_page(url)
                if html:
                    products = parse_products(html, category, list_type)
                    
                    if products:
                        filepath = save_data(products, category, list_type)
                        print(f"✓ 获取 {len(products)} 个产品 -> {os.path.basename(filepath)}")
                        
                        # 检测变动
                        changes = compare_with_previous(products, category, list_type)
                        if changes:
                            send_notification(changes, category, list_type)
                        else:
                            print(f"     ℹ️ 首次爬取，无历史数据可比较")
                    else:
                        print(f"⚠️ 未获取到产品数据（页面结构可能已变更）")
                else:
                    print(f"❌ 获取页面失败")
                    
            except Exception as e:
                print(f"❌ 错误: {e}")
            
            time.sleep(2)  # 请求间隔，避免被封
    
    print(f"\n{'='*60}")
    print(f"✅ 爬取完成: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📁 数据目录: {DATA_DIR}")


if __name__ == "__main__":
    main()
