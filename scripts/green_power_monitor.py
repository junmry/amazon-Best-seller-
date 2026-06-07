#!/usr/bin/env python3
"""
绿电 ETF + 个股监控脚本
生成格式化报告，保存到文件
"""
import warnings
warnings.filterwarnings('ignore')

import sys
import json
import akshare as ak
import pandas as pd
from datetime import datetime

# 绿电ETF列表
ETF_CODES = {
    '159625': '绿色电力ETF嘉实',
    '159669': '绿色电力ETF国泰',
    '562960': '绿色电力ETF易方达',
    '561170': '绿色电力ETF富国',
    '562550': '绿电ETF华夏',
}

# 绿电核心个股 (新浪格式: sh/sz + 代码)
STOCK_CODES = {
    'sh600900': '长江电力',
    'sh600011': '华能国际',
    'sh601985': '中国核电',
    'sh600905': '三峡能源',
    'sh600795': '国电电力',
    'sh600886': '国投电力',
    'sh600674': '川投能源',
    'sh600025': '华能水电',
    'sh601991': '大唐发电',
    'sz000591': '太阳能',
    'sh601778': '晶科科技',
    'sh601016': '节能风电',
    'sh601619': '嘉泽新能',
    'sh600021': '上海电力',
    'sz000875': '吉电股份',
}

def fmt_num(v):
    if v is None or (isinstance(v, float) and v != v):
        return '-'
    if isinstance(v, (int, float)):
        if abs(v) >= 1e8:
            return f'{v/1e8:.2f}亿'
        elif abs(v) >= 1e4:
            return f'{v/1e4:.2f}万'
        return f'{v:.2f}'
    return str(v)

def get_etf_data():
    try:
        df = ak.fund_etf_spot_em()
        df = df[df['代码'].isin(ETF_CODES.keys())].copy()
        df['名称'] = df['代码'].map(ETF_CODES)
        return df[['代码', '名称', '最新价', '涨跌额', '涨跌幅', '成交量', '成交额']]
    except Exception as e:
        print(f'ETF获取失败: {e}', file=sys.stderr)
        return None

def get_stock_data():
    """使用新浪接口获取个股实时行情"""
    try:
        import requests
        codes = ','.join(STOCK_CODES.keys())
        url = f'https://hq.sinajs.cn/list={codes}'
        headers = {'Referer': 'https://finance.sina.com.cn'}
        r = requests.get(url, headers=headers, timeout=20)
        r.raise_for_status()

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
            # 新浪格式: 名称,今开,昨收,最新,最高,最低,买入,卖出,成交量,成交额...
            name = parts[0]
            prev_close = float(parts[2]) if parts[2] else 0
            latest = float(parts[3]) if parts[3] else 0
            change = latest - prev_close
            pct = (change / prev_close * 100) if prev_close else 0
            volume = float(parts[8]) * 100 if parts[8] else 0  # 手 -> 股
            amount = float(parts[9]) if parts[9] else 0
            # 映射纯数字代码
            pure_code = code_key[2:]
            rows.append({
                '代码': pure_code,
                '名称': STOCK_CODES.get(code_key, name),
                '最新价': latest,
                '涨跌额': change,
                '涨跌幅': pct,
                '成交量': volume,
                '成交额': amount,
            })
        return pd.DataFrame(rows)
    except Exception as e:
        print(f'个股获取失败: {e}', file=sys.stderr)
        return None

def generate_report(etf_df, stock_df):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lines = [f'📊 绿电板块监控 | {now}', '=' * 40]
    
    if etf_df is not None and not etf_df.empty:
        lines.append('')
        lines.append('🔹 绿电ETF')
        lines.append('-' * 40)
        for _, row in etf_df.iterrows():
            emoji = '🔴' if row['涨跌幅'] > 0 else '🟢' if row['涨跌幅'] < 0 else '➖'
            lines.append(f"{emoji} {row['名称']}({row['代码']})")
            lines.append(f"   最新价: {fmt_num(row['最新价'])}  涨跌: {fmt_num(row['涨跌额'])}  幅度: {fmt_num(row['涨跌幅'])}%")
            lines.append(f"   成交额: {fmt_num(row['成交额'])}")
    else:
        lines.append('ETF数据获取失败')
    
    if stock_df is not None and not stock_df.empty:
        lines.append('')
        lines.append('🔹 绿电核心个股')
        lines.append('-' * 40)
        # 按涨跌幅排序
        stock_df = stock_df.sort_values('涨跌幅', ascending=False)
        for _, row in stock_df.iterrows():
            emoji = '🔴' if row['涨跌幅'] > 0 else '🟢' if row['涨跌幅'] < 0 else '➖'
            lines.append(f"{emoji} {row['名称']}({row['代码']})")
            lines.append(f"   最新价: {fmt_num(row['最新价'])}  涨跌: {fmt_num(row['涨跌额'])}  幅度: {fmt_num(row['涨跌幅'])}%")
            lines.append(f"   成交额: {fmt_num(row['成交额'])}")
    else:
        lines.append('个股数据获取失败')
    
    # 汇总统计
    if stock_df is not None and not stock_df.empty:
        up = (stock_df['涨跌幅'] > 0).sum()
        down = (stock_df['涨跌幅'] < 0).sum()
        flat = (stock_df['涨跌幅'] == 0).sum()
        avg = stock_df['涨跌幅'].mean()
        lines.append('')
        lines.append('📈 板块统计')
        lines.append('-' * 40)
        lines.append(f'上涨: {up} | 下跌: {down} | 平盘: {flat}')
        lines.append(f'平均涨跌幅: {avg:.2f}%')
    
    lines.append('')
    lines.append('数据来源: AKShare / 东方财富 / 新浪')
    return '\n'.join(lines)

def main():
    etf_df = get_etf_data()
    stock_df = get_stock_data()
    
    report = generate_report(etf_df, stock_df)
    
    # 保存到文件
    today = datetime.now().strftime('%Y-%m-%d')
    out_path = f'/root/.openclaw/workspace/memory/green-power/{today}.md'
    import os
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    # 同时输出到stdout，方便捕获
    print(report)
    print(f'\n[报告已保存: {out_path}]')

if __name__ == '__main__':
    main()
