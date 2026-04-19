#!/usr/bin/env python3
"""
生成金融从业资格考试Excel规划表
"""

import csv
from datetime import datetime

output_dir = "/root/.openclaw/workspace"

# ==================== 文件1: 考试时间表 ====================
with open(f"{output_dir}/1-考试时间表.csv", 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(["考试名称", "考试类型", "考试时间", "报名时间", "报名网站", "科目", "费用", "成绩有效期"])
    writer.writerow(["期货从业", "统考", "5月16日", "4月中下旬", "www.cfachina.org", "基础知识+法律法规", "65元/科", "长期"])
    writer.writerow(["期货从业", "专场", "9月19日", "待定", "www.cfachina.org", "三科可选", "65元/科", "长期"])
    writer.writerow(["期货从业", "专场", "11月21日", "待定", "www.cfachina.org", "三科可选", "65元/科", "长期"])
    writer.writerow(["基金从业", "统考", "5月23日", "4月中下旬", "www.amac.org.cn", "科1必考+科2/3选考", "61元/科", "4年"])
    writer.writerow(["基金从业", "统考", "11月28日", "10月中下旬", "www.amac.org.cn", "科1必考+科2/3选考", "61元/科", "4年"])
    writer.writerow(["证券从业", "统考", "6月27日", "5月中下旬", "www.sac.net.cn", "金融市场基础+法律法规", "61元/科", "36个月"])
    writer.writerow(["证券从业", "统考", "9月19日", "8月中下旬", "www.sac.net.cn", "金融市场基础+法律法规", "61元/科", "36个月"])
    writer.writerow(["证券从业", "专场", "4月18日", "3月中下旬", "www.sac.net.cn", "两科", "61元/科", "36个月"])
    writer.writerow(["证券从业", "专场", "11月", "10月中下旬", "www.sac.net.cn", "两科", "61元/科", "36个月"])

# ==================== 文件2: 备考时间线 ====================
with open(f"{output_dir}/2-备考时间线.csv", 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(["阶段", "时间", "目标考试", "备考内容", "建议时长", "备注"])
    writer.writerow(["准备期", "3月", "了解考情", "查看大纲，准备资料", "1周", "确定报考科目"])
    writer.writerow(["第一阶段", "4月", "期货从业", "基础知识+法规", "4-5周", "重点：套期保值、套利"])
    writer.writerow(["第二阶段", "5-6月", "证券从业", "金融基础+法规", "5-6周", "重点：股票、债券、衍生品"])
    writer.writerow(["第三阶段", "9-10月", "基金从业", "科1+科2", "6-8周", "重点：投资组合、估值"])
    writer.writerow(["冲刺", "考前2周", "全科", "刷真题+错题", "2周", "机位紧张，早报早安心"])

# ==================== 文件3: 证券从业重点 ====================
with open(f"{output_dir}/3-证券从业重点.csv", 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(["章节", "内容", "分值", "难度", "重点内容"])
    writer.writerow(["第四章", "股票", "20分", "★★★", "股票估值、发行交易"])
    writer.writerow(["第七章", "金融衍生工具", "15分", "★★★", "期货、期权、互换"])
    writer.writerow(["第二章", "中国金融体系", "15分", "★★", "多层次资本市场"])
    writer.writerow(["第五章", "债券", "15分", "★★", "债券估值、风险"])
    writer.writerow(["第一章", "金融市场体系", "10分", "★", "基本概念"])
    writer.writerow(["第三章", "证券市场主体", "10分", "★", "中介机构"])
    writer.writerow(["第六章", "证券投资基金", "10分", "★", "基金类型"])
    writer.writerow(["第八章", "金融风险管理", "5分", "★", "风险类型"])

# ==================== 文件4: 基金从业重点 ====================
with open(f"{output_dir}/4-基金从业重点.csv", 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(["章节", "内容", "分值", "难度", "重点内容"])
    writer.writerow(["第三章", "固定收益投资", "15分", "★★★", "久期、凸性、YTM"])
    writer.writerow(["第七章", "投资组合管理", "15分", "★★★", "CAPM、有效市场"])
    writer.writerow(["第二章", "权益投资", "15分", "★★", "股票估值方法"])
    writer.writerow(["第四章", "衍生工具", "10分", "★★", "远期、期货、期权"])
    writer.writerow(["第十章", "基金业绩评价", "10分", "★★", "夏普比率、阿尔法"])
    writer.writerow(["第一章", "投资管理基础", "10分", "★", "财务报表分析"])
    writer.writerow(["第九章", "投资风险管理", "10分", "★", "VaR、风险类型"])

# ==================== 文件5: 期货从业重点 ====================
with open(f"{output_dir}/5-期货从业重点.csv", 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(["章节", "内容", "分值", "难度", "重点内容"])
    writer.writerow(["第三章", "套期保值", "20分", "★★★", "基差、套保效果计算"])
    writer.writerow(["第四章", "投机与套利", "20分", "★★★", "价差套利盈亏计算"])
    writer.writerow(["第二章", "期货合约与制度", "15分", "★★", "保证金、逐日盯市"])
    writer.writerow(["第六章", "金融期货", "15分", "★★", "国债期货、股指期货"])
    writer.writerow(["第五章", "期货期权", "10分", "★★", "希腊字母、盈亏平衡点"])
    writer.writerow(["第一章", "期货市场概述", "10分", "★", "发展历程"])
    writer.writerow(["第七章", "监管与风控", "10分", "★", "风险控制体系"])

# ==================== 文件6: 报名检查清单 ====================
with open(f"{output_dir}/6-报名检查清单.csv", 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(["类别", "检查项", "状态"])
    writer.writerow(["基本条件", "年满18周岁", "☐"])
    writer.writerow(["基本条件", "具有完全民事行为能力", "☐"])
    writer.writerow(["基本条件", "高中/大专及以上学历", "☐"])
    writer.writerow(["准备材料", "身份证原件（有效期内）", "☐"])
    writer.writerow(["准备材料", "学历证明（毕业证编号）", "☐"])
    writer.writerow(["准备材料", "近期白底证件照（JPG，30-100KB）", "☐"])
    writer.writerow(["准备材料", "电子邮箱", "☐"])
    writer.writerow(["准备材料", "手机号码", "☐"])
    writer.writerow(["报名流程", "1. 登录官网注册账号", "☐"])
    writer.writerow(["报名流程", "2. 填写个人信息（核对无误）", "☐"])
    writer.writerow(["报名流程", "3. 选择考试科目", "☐"])
    writer.writerow(["报名流程", "4. 选择考区城市", "☐"])
    writer.writerow(["报名流程", "5. 在线支付报名费", "☐"])
    writer.writerow(["报名流程", "6. 确认报名成功", "☐"])
    writer.writerow(["考前准备", "考前一周打印准考证", "☐"])
    writer.writerow(["考前准备", "确认考试地点和时间", "☐"])
    writer.writerow(["考前准备", "准备身份证原件+准考证", "☐"])
    writer.writerow(["考前准备", "熟悉考场路线", "☐"])
    writer.writerow(["注意事项", "⚠️ 机位有限，先报先得！", ""])
    writer.writerow(["注意事项", "⚠️ 缴费成功才算报名完成", ""])
    writer.writerow(["注意事项", "⚠️ 姓名和身份证号注册后不可修改", ""])
    writer.writerow(["注意事项", "⚠️ 连续两次缺考将被限制报考一次", ""])

# ==================== 文件7: 重要公式汇总 ====================
with open(f"{output_dir}/7-重要公式汇总.csv", 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(["考试", "公式名称", "公式", "应用场景"])
    writer.writerow(["证券", "股票估值-DDM", "V = D/(r-g)", "股利贴现模型"])
    writer.writerow(["证券", "债券到期收益率", "YTM ≈ (C+(F-P)/n)/((F+P)/2)", "近似计算"])
    writer.writerow(["基金", "夏普比率", "Sharpe = (Rp-Rf)/σp", "风险调整后收益"])
    writer.writerow(["基金", "CAPM", "E(Ri) = Rf + β(E(Rm)-Rf)", "预期收益率"])
    writer.writerow(["基金", "詹森阿尔法", "α = Rp-[Rf+β(Rm-Rf)]", "超额收益"])
    writer.writerow(["基金", "久期", "D = Σ(t×PVt)/P", "利率风险衡量"])
    writer.writerow(["期货", "基差", "基差 = 现货价 - 期货价", "套期保值效果"])
    writer.writerow(["期货", "套期保值盈亏", "盈亏 = 基差变动", "盈亏计算"])
    writer.writerow(["期货", "保证金", "初始保证金 = 合约价值×比例", "保证金计算"])
    writer.writerow(["期货", "期权盈亏平衡", "买权：X+C / 卖权：X-P", "期权策略"])

print("✅ CSV文件已生成，共7个文件：")
print("   1-考试时间表.csv")
print("   2-备考时间线.csv")  
print("   3-证券从业重点.csv")
print("   4-基金从业重点.csv")
print("   5-期货从业重点.csv")
print("   6-报名检查清单.csv")
print("   7-重要公式汇总.csv")
print("")
print("提示：CSV文件可用Excel直接打开")
