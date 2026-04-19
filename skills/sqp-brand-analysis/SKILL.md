---
name: sqp-brand-analysis
description: 分析亚马逊 SQP (Search Query Performance) 品牌搜索词数据，生成周报报告、趋势图表、高转化词识别、周对周对比分析。用于优化亚马逊广告投放、Listing埋词策略、竞品关键词监控。当用户上传 SQP CSV 文件、要求分析品牌搜索词表现、进行周对周对比、识别高转化词、生成趋势图表时触发。
---

# SQP 品牌搜索词分析

分析亚马逊 Search Query Performance (SQP) Brand View 周报数据，生成完整分析报告。

## 使用场景

- 分析品牌搜索词表现趋势
- 识别高转化潜力词（购买率/曝光占比 ≥ 1）
- 周对周（WoW）对比：新入列词、跌出列词
- 品牌 vs 大盘对比分析
- 生成 Top 5 高价值词趋势图表

## 使用方法

```bash
python ~/.openclaw/workspace/skills/sqp-brand-analysis/scripts/sqp_report.py \
  --input "path/to/SQP/*.csv" \
  --output "./sqp_output/"
```

**--input** 支持：
- 通配符模式：`"SQP/*.csv"`
- 目录路径：`"./sqp_data/"`
- 多文件：`wk1.csv wk2.csv wk3.csv`

**--output** 默认为 `./sqp_output/`

## 输入文件要求

- 文件名格式：`..._Week_YYYY_MM_DD.csv`（亚马逊标准导出格式）
- 第一行为亚马逊元数据，脚本自动跳过
- 最少需要 **2 周** 数据才有 WoW 对比；1 周数据也能生成基础报告

## 输出文件

| 文件 | 说明 |
|------|------|
| `sqp_report.md` | 完整文字报告，包含所有数据表格 |
| `weekly_brand_portfolio.csv` | 每周每个搜索词的品牌数据占比 |
| `high_conv_terms.csv` | 高转化潜力词（购买率/品牌曝光占比 ≥ 1）|
| `wow_new_dropped.csv` | 周对周新入列/跌出列词 |
| `wow_self_drops.csv` | 品牌各指标下降最多的 Top 10 |
| `wow_market_deviation.csv` | 品牌与大盘偏离最大的 Top 10 |
| `top5_stable_terms.csv` | Top 5 高频高价值词逐周明细 |
| `sqp_top5_trend.png` | Top 5 词趋势图（大盘曝光+品牌占比）|

## 报告章节

1. **每周品牌数据快照** - 品牌总量 + Top 25 搜索词
2. **转化能力高于类目的词** - 高潜力词识别
3. **WoW 新入列 & 跌出列** - 词的出现/消失追踪
4. **和自己比** - 品牌各指标下降分析
5. **和大盘比** - 品牌 vs 市场偏离分析
6. **Top 5 稳定高价值词** - 全周期高频高占比词详情

## 核心指标说明

| 指标 | 公式 |
|------|------|
| `pct_brand_imp/clk/cart/pur` | 该词品牌数据 ÷ 当周品牌总计 × 100% |
| `conv_ratio` | 类目购买率% ÷ 品牌曝光占比% |
| `相对变化比` | 品牌 WoW 率 ÷ 大盘 WoW 率 |

## 趋势判断标签

| 标签 | 含义 |
|------|------|
| `↑↑ 比大盘涨得快` | 品牌增长 > 1.5× 大盘增长率 |
| `↑ 与大盘同步上涨` | 品牌与大盘同步增长 |
| `↑↓ 比大盘涨得慢` | 品牌增长但慢于大盘 |
| `↓↓ 比大盘跌得快` | 品牌下降 > 1.5× 大盘下降率 |
| `↓ 与大盘同步下跌` | 品牌与大盘同步下降 |
| `↓↑ 比大盘跌得慢` | 品牌下降但少于大盘 |
| `⚡ 逆势上涨` | 大盘跌，品牌涨 |
| `⚠ 逆势下跌` | 大盘涨，品牌跌 |

## 执行流程

1. 接收用户提供的 SQP CSV 文件路径
2. 执行脚本分析：`python scripts/sqp_report.py --input "*.csv" --output "./output"`
3. 读取生成的 `sqp_report.md` 作为主报告
4. 展示 `sqp_top5_trend.png` 趋势图
5. 说明 6 个 CSV 文件可供进一步分析
