#!/usr/bin/env python3
"""
A股板块监控 v2（纯 Python，无 akshare/pandas 依赖）
ETF + 个股统一走新浪接口，requests + 纯 Python 解析
"""
import sys, json, os, requests, sqlite3
from datetime import datetime, timedelta
from pathlib import Path

# ────────────────────────── 配置 ──────────────────────────

ETF_CODES = {
    'sh512160': '绿色电力ETF',
    'sh159625': '绿色电力ETF嘉实',
    'sh159669': '绿色电力ETF国泰',
    'sh562960': '绿色电力ETF易方达',
    'sh561170': '绿色电力ETF富国',
    'sh562550': '绿电ETF华夏',
}

STOCK_CODES = {
    'sh600900': '长江电力', 'sh600011': '华能国际', 'sh601985': '中国核电',
    'sh600905': '三峡能源', 'sh600795': '国电电力', 'sh600886': '国投电力',
    'sh600674': '川投能源', 'sh600025': '华能水电', 'sh601991': '大唐发电',
    'sz000591': '太阳能', 'sh601778': '晶科科技', 'sh601016': '节能风电',
    'sh601619': '嘉泽新能', 'sh600021': '上海电力', 'sz000875': '吉电股份',
}

ALL_CODES = {**ETF_CODES, **STOCK_CODES}

DB_PATH = Path('/root/.openclaw/workspace/data/a_stock_monitor.db')
REPORT_DIR = Path('/root/.openclaw/workspace/memory/green-power')

# ────────────────────────── 数据库 ──────────────────────────

def ensure_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS daily_snapshot (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        snapshot_date TEXT,
        code TEXT,
        name TEXT,
        type TEXT,
        price REAL,
        change_pct REAL,
        volume REAL,
        amount REAL,
        sector_avg_pct REAL,
        deviation REAL,
        signal_level TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def save_snapshot(code, name, type_, price, change_pct, volume, amount, sector_avg, deviation, level):
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute('''
    INSERT INTO daily_snapshot (snapshot_date, code, name, type, price, change_pct, volume, amount, sector_avg_pct, deviation, signal_level)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (datetime.now().strftime('%Y-%m-%d'), code, name, type_, price, change_pct, volume, amount, sector_avg, deviation, level))
    conn.commit()
    conn.close()

# ────────────────────────── 数据获取（新浪接口） ──────────────────────────

def fetch_sina(codes_dict):
    """通过新浪接口获取实时行情"""
    codes = ','.join(codes_dict.keys())
    url = f'https://hq.sinajs.cn/list={codes}'
    headers = {'Referer': 'https://finance.sina.com.cn'}
    try:
        r = requests.get(url, headers=headers, timeout=20)
        r.raise_for_status()
    except Exception as e:
        print(f'请求失败: {e}', file=sys.stderr)
        return []
    
    rows = []
    for line in r.text.strip().split('\n'):
        line = line.strip()
        if not line or '=' not in line:
            continue
        code_key = line.split('=')[0].replace('var hq_str_', '')
        data = line.split('=')[1].strip('";')
        parts = data.split(',')
        if len(parts) < 4:
            continue
        
        name = parts[0]
        # 新浪格式: 名称,今开,昨收,最新,最高,最低,买入,卖出,成交量,成交额...
        prev_close = float(parts[2]) if parts[2] else 0
        latest = float(parts[3]) if parts[3] else 0
        change = latest - prev_close
        pct = (change / prev_close * 100) if prev_close else 0
        volume = float(parts[8]) * 100 if len(parts) > 8 and parts[8] else 0
        amount = float(parts[9]) if len(parts) > 9 and parts[9] else 0
        high = float(parts[4]) if len(parts) > 4 and parts[4] else 0
        low = float(parts[5]) if len(parts) > 5 and parts[5] else 0
        
        pure_code = code_key[2:]
        rows.append({
            'code': pure_code,
            'full_code': code_key,
            'name': ALL_CODES.get(code_key, name),
            'type': 'etf' if code_key in ETF_CODES else 'stock',
            'price': latest,
            'prev_close': prev_close,
            'change': change,
            'change_pct': pct,
            'volume': volume,
            'amount': amount,
            'high': high,
            'low': low,
        })
    return rows

# ────────────────────────── 分析层 ──────────────────────────

def analyze_sector(stock_rows):
    """板块分析：统计 + 异动标记"""
    stocks = [r for r in stock_rows if r['type'] == 'stock']
    if not stocks:
        return None
    
    # 板块均值
    pcts = [r['change_pct'] for r in stocks]
    sector_avg = sum(pcts) / len(pcts)
    
    # 标准差
    mean = sector_avg
    variance = sum((x - mean) ** 2 for x in pcts) / len(pcts)
    sector_std = variance ** 0.5
    
    # 偏离度 + 信号级别
    for r in stocks:
        r['deviation'] = r['change_pct'] - sector_avg
        z = abs(r['deviation'] / sector_std) if sector_std > 0 else 0
        if z > 2.5:
            r['level'] = 'L3'
        elif z > 1.5:
            r['level'] = 'L2'
        else:
            r['level'] = 'L1'
    
    # 排序
    stocks.sort(key=lambda x: x['change_pct'], reverse=True)
    
    up = sum(1 for r in stocks if r['change_pct'] > 0)
    down = sum(1 for r in stocks if r['change_pct'] < 0)
    l3 = sum(1 for r in stocks if r['level'] == 'L3')
    l2 = sum(1 for r in stocks if r['level'] == 'L2')
    
    anomalies = [r for r in stocks if r['level'] in ('L2', 'L3')]
    anomalies.sort(key=lambda x: abs(x['deviation']), reverse=True)
    
    return {
        'sector_avg': sector_avg,
        'sector_std': sector_std,
        'up': up, 'down': down,
        'l3_count': l3, 'l2_count': l2,
        'leader': stocks[0] if stocks else None,
        'laggard': stocks[-1] if stocks else None,
        'anomalies': anomalies,
    }

# ────────────────────────── 格式化 ──────────────────────────

def fmt_num(v):
    if v is None or v != v:
        return '-'
    if abs(v) >= 1e8:
        return f'{v/1e8:.2f}亿'
    elif abs(v) >= 1e4:
        return f'{v/1e4:.2f}万'
    return f'{v:.2f}'

def generate_report(etf_rows, stock_rows, analysis):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lines = [f'📊 绿电板块监控 v2 | {now}', '=' * 40]
    
    # ETF
    if etf_rows:
        lines.append('')
        lines.append('🔹 绿电ETF')
        lines.append('-' * 40)
        for r in etf_rows:
            emoji = '🔴' if r['change_pct'] > 0 else '🟢' if r['change_pct'] < 0 else '➖'
            lines.append(f"{emoji} {r['name']}({r['code']})  {r['change_pct']:+.2f}%")
    
    # 板块统计
    if analysis:
        lines.append('')
        lines.append('📈 板块统计')
        lines.append('-' * 40)
        lines.append(f"平均: {analysis['sector_avg']:+.2f}%  标准差: {analysis['sector_std']:.2f}%")
        lines.append(f"上涨: {analysis['up']} | 下跌: {analysis['down']}")
        
        if analysis['leader']:
            l = analysis['leader']
            lines.append(f"🏆 龙头: {l['name']} +{l['change_pct']:.2f}%")
        if analysis['laggard']:
            l = analysis['laggard']
            lines.append(f"💧 吊车尾: {l['name']} {l['change_pct']:+.2f}%")
    
    # 个股列表
    if stock_rows:
        lines.append('')
        lines.append('🔹 核心个股')
        lines.append('-' * 40)
        # 按涨幅排序
        sorted_stocks = sorted(stock_rows, key=lambda x: x['change_pct'], reverse=True)
        for r in sorted_stocks:
            emoji = '🔴' if r['change_pct'] > 0 else '🟢' if r['change_pct'] < 0 else '➖'
            sig = ''
            if r.get('level') == 'L3':
                sig = ' 🔥🔥'
            elif r.get('level') == 'L2':
                sig = ' 🔥'
            lines.append(f"{emoji} {r['name']} {r['change_pct']:+.2f}% {sig}")
    
    # 异动
    if analysis and analysis['anomalies']:
        lines.append('')
        lines.append('⚡ 异动个股')
        lines.append('-' * 40)
        for r in analysis['anomalies'][:5]:
            emoji = '🔴' if r['level'] == 'L3' else '🟠'
            lines.append(f"{emoji} [{r['level']}] {r['name']} 偏离板块 {r['deviation']:+.2f}% (自身 {r['change_pct']:+.2f}%)")
    
    lines.append('')
    lines.append('数据来源: 新浪实时行情')
    return '\n'.join(lines)

def generate_l3_report(etf_rows, stock_rows, analysis):
    base = generate_report(etf_rows, stock_rows, analysis)
    lines = [base]
    lines.append('')
    lines.append('🔍 深度分析')
    lines.append('-' * 40)
    lines.append('板块出现极端分化，建议关注：')
    lines.append('1. 是否有政策/行业消息驱动')
    lines.append('2. 龙头是否带量突破')
    lines.append('3. 吊车尾是否破位')
    return '\n'.join(lines)

# ────────────────────────── 主入口 ──────────────────────────

def main():
    ensure_db()
    
    # 获取数据
    all_rows = fetch_sina(ALL_CODES)
    
    if not all_rows:
        print('数据获取失败', file=sys.stderr)
        sys.exit(1)
    
    etf_rows = [r for r in all_rows if r['type'] == 'etf']
    stock_rows = [r for r in all_rows if r['type'] == 'stock']
    
    # 分析
    analysis = analyze_sector(stock_rows)
    
    # 确定输出级别
    level = 'L1'
    if analysis:
        if analysis['l3_count'] >= 2:
            level = 'L3'
        elif analysis['l2_count'] >= 3 or analysis['l3_count'] >= 1:
            level = 'L2'
    
    # 生成报告
    if level == 'L3':
        report = generate_l3_report(etf_rows, stock_rows, analysis)
    else:
        report = generate_report(etf_rows, stock_rows, analysis)
    
    # 保存到数据库
    if analysis:
        sector_avg = analysis['sector_avg']
        for r in stock_rows:
            save_snapshot(r['code'], r['name'], 'stock', r['price'], r['change_pct'], 
                         r['volume'], r['amount'], sector_avg, r.get('deviation', 0), r.get('level', 'L1'))
    
    # 保存报告
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    out_path = REPORT_DIR / f'{today}.md'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(report)
    print(f'\n[报告已保存: {out_path}] 级别: {level}')

if __name__ == '__main__':
    main()
