# Amazon Best Seller 数据仓库

## 目录结构

```
.
├── raw_data/          # 原始数据
│   ├── chairs/        # 椅子类原始数据
│   └── sofas/         # 沙发类原始数据
├── processed/         # 处理后数据（KEIKI 优化结果）
├── docs/              # 文档和配置
└── README.md          # 本文件
```

## 文件夹说明

- **raw_data/**: 从 Amazon 抓取的原始 BSR/NEW 数据，按品类分子文件夹
- **processed/**: 经过标题优化、词频分析等处理后的结果文件
- **docs/**: 词汇表、生成规则、词频分析结果等文档

## 更新记录

- 2026-03-05: 初始化仓库，规整文件结构
