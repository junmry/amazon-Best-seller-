import zipfile
import re
import json
import os

os.makedirs('/root/.openclaw/workspace/mattress_van', exist_ok=True)

def col_to_idx(col_str):
    result = 0
    for c in col_str:
        result = result * 26 + (ord(c) - ord('A') + 1)
    return result - 1

def parse_cell(cell_block, inner, strings):
    """解析单元格，返回值"""
    val = ''
    has_t_s = 't="s"' in cell_block[:200] or "t='s'" in cell_block[:200]
    has_inline = 't="inlineStr"' in cell_block[:200] or "t='inlineStr'" in cell_block[:200]
    
    if inner:
        if has_t_s:
            v_match = re.search(r'<v>([^<]*)</v>', inner)
            if v_match:
                try:
                    s_idx = int(v_match.group(1))
                    val = strings[s_idx] if s_idx < len(strings) else ''
                except:
                    val = v_match.group(1)
        elif has_inline:
            t_matches = re.findall(r'<t[^>]*>([^<]*)</t>', inner)
            val = ''.join(t_matches)
        else:
            v_match = re.search(r'<v>([^<]*)</v>', inner)
            if v_match:
                val = v_match.group(1)
        
        # Check for <is> wrapper
        if not val:
            is_match = re.search(r'<is>(.*?)</is>', inner, re.DOTALL)
            if is_match:
                t_matches = re.findall(r'<t[^>]*>([^<]*)</t>', is_match.group(1))
                val = ''.join(t_matches)
    
    return val

def parse_sheet(z, sheet_path, strings):
    """解析Excel sheet，返回所有行数据"""
    sheet_raw = z.read(sheet_path).decode('utf-8')
    rows_xml = re.findall(r'<row[^>]*>(.*?)</row>', sheet_raw, re.DOTALL)
    
    all_rows = []
    for row_xml in rows_xml:
        row_dict = {}
        pos = 0
        while True:
            c_start = row_xml.find('<c r="', pos)
            if c_start == -1:
                break
            tag_end = row_xml.find('>', c_start)
            if tag_end == -1:
                break
            
            # Check self-closing
            if row_xml[tag_end-1] == '/':
                cell_block = row_xml[c_start:tag_end+1]
                inner = ''
                pos = tag_end + 1
            else:
                c_end = row_xml.find('</c>', c_start)
                if c_end == -1:
                    break
                cell_block = row_xml[c_start:c_end+4]
                inner = cell_block[cell_block.find('>')+1:-4]
                pos = c_end + 4
            
            ref_match = re.search(r'r="([A-Z]+)(\d+)"', cell_block[:100])
            if ref_match:
                col_idx = col_to_idx(ref_match.group(1))
                val = parse_cell(cell_block, inner, strings)
                row_dict[col_idx] = val
        
        max_col = max(row_dict.keys()) if row_dict else 0
        row_list = [row_dict.get(i, '') for i in range(max_col + 1)]
        all_rows.append(row_list)
    
    return all_rows

# ========== 文件1: 竞品拓词 ==========
print('=== Processing File 1: Variant Extend Keywords ===')
z1 = zipfile.ZipFile('19dd28b8-9dc2-8fd9-8000-000095a48168_variantExtendKeyword_fenjpjmivqh1777353806955_1777353818338.xlsx')

# 共享字符串（可能为空）
ss1 = z1.read('xl/sharedStrings.xml').decode('utf-8')
si_blocks1 = re.findall(r'<si[^>]*>(.*?)</si>', ss1, re.DOTALL)
strings1 = []
for si in si_blocks1:
    t_texts = re.findall(r'<t[^>]*>([^<]*)</t>', si)
    strings1.append(''.join(t_texts))
print(f'Shared strings: {len(strings1)}')

rows1 = parse_sheet(z1, 'xl/worksheets/sheet1.xml', strings1)
print(f'Total rows in sheet: {len(rows1)}')

# 找到header行和数据行
# Row 1通常是复合标题，Row 2是header
print('\nFirst 3 rows (first 5 cols):')
for i, r in enumerate(rows1[:3]):
    print(f'  Row {i+1}: {r[:5]}')

# 确定header和数据起始
# 通常Row 2（index 1）是header：#, 关键词, 翻译, ...
header_row = None
data_start = 0
for i, r in enumerate(rows1):
    if len(r) > 1 and r[1] == '关键词':
        header_row = r
        data_start = i + 1
        break

if header_row:
    print(f'\nHeader found at row {data_start}, columns:')
    for i, h in enumerate(header_row):
        if h:
            print(f'  Col {i}: {h}')
else:
    # Fallback: assume row 2 is header
    header_row = rows1[1] if len(rows1) > 1 else []
    data_start = 2

keyword_data = []
for r in rows1[data_start:]:
    if len(r) > 1 and r[1] and r[1] != '关键词':
        keyword_data.append({
            'rank': r[0],
            'keyword': r[1],
            'translation': r[2] if len(r) > 2 else '',
            'relevance_pct': r[3] if len(r) > 3 else '',
            'relevance': r[4] if len(r) > 4 else '',
            'top4_occupancy': r[5] if len(r) > 5 else '',
            'top8_occupancy': r[6] if len(r) > 6 else '',
            'top16_occupancy': r[7] if len(r) > 7 else '',
            'top32_occupancy': r[8] if len(r) > 8 else '',
            'top48_occupancy': r[9] if len(r) > 9 else '',
            'weekly_search': r[10] if len(r) > 10 else '',
            'bsr_rank': r[11] if len(r) > 11 else '',
            'relevance_manual': r[12] if len(r) > 12 else ''
        })

print(f'\nKeywords extracted: {len(keyword_data)}')
print('First 5:')
for k in keyword_data[:5]:
    print(f"  {k['rank']}. {k['keyword']} | 搜索量:{k['weekly_search']} | 相关:{k['relevance']} | 排名:{k['bsr_rank']}")

with open('/root/.openclaw/workspace/mattress_van/keyword_data.json', 'w', encoding='utf-8') as f:
    json.dump(keyword_data, f, ensure_ascii=False, indent=2)

# ========== 文件2: BSR ==========
print('\n=== Processing File 2: BSR Data ===')
z2 = zipfile.ZipFile('19dd28b9-01c2-82de-8000-0000c85b5d7f_BSR_Mattresses_Current_-3-US-20260428.xlsx')

ss2 = z2.read('xl/sharedStrings.xml').decode('utf-8')
si_blocks2 = re.findall(r'<si[^>]*>(.*?)</si>', ss2, re.DOTALL)
strings2 = []
for si in si_blocks2:
    t_texts = re.findall(r'<t[^>]*>([^<]*)</t>', si)
    strings2.append(''.join(t_texts))
print(f'Shared strings: {len(strings2)}')

rows2 = parse_sheet(z2, 'xl/worksheets/sheet1.xml', strings2)
print(f'Total rows: {len(rows2)}')

# BSR文件：Row 1是header，Row 2+是数据
bsr_data = []
for r in rows2[1:]:
    if len(r) > 2 and r[2]:  # ASIN exists
        bsr_data.append({
            'asin': r[2],
            'sku': r[3] if len(r) > 3 else '',
            'brand': r[5] if len(r) > 5 else '',
            'title': r[7] if len(r) > 7 else '',
            'bullet_points': r[8] if len(r) > 8 else '',
            'category_path': r[12] if len(r) > 12 else '',
            'main_bsr': r[14] if len(r) > 14 else '',
            'sub_bsr': r[18] if len(r) > 18 else '',
            'monthly_sales': r[19] if len(r) > 19 else '',
            'monthly_revenue': r[21] if len(r) > 21 else '',
            'price': r[25] if len(r) > 25 else '',
            'review_count': r[29] if len(r) > 29 else '',
            'rating': r[31] if len(r) > 31 else '',
            'launch_date': r[36] if len(r) > 36 else '',
            'ac_keyword': r[58] if len(r) > 58 else ''
        })

print(f'BSR products: {len(bsr_data)}')
for p in bsr_data:
    print(f"  {p['brand']} | BSR:{p['main_bsr']} | 销量:{p['monthly_sales']} | ${p['price']} | 评分:{p['rating']}")

with open('/root/.openclaw/workspace/mattress_van/bsr_data.json', 'w', encoding='utf-8') as f:
    json.dump(bsr_data, f, ensure_ascii=False, indent=2)

print('\nDone! Files saved to /root/.openclaw/workspace/mattress_van/')
