---
name: bill-financial-advisor
description: Analyze bills, bank exports, payment CSVs, screenshots, and transaction lists to summarize spending, classify expenses, detect anomalies, and produce practical budgeting advice. Use when the user asks for 账单分析, 消费汇总, 财务军师, 支出分类, 异常消费识别, budget review, or sends a CSV/账单导出文件 and expects direct analysis without extra prompting.
---

# Bill Financial Advisor

Turn raw transaction data into useful financial insight.

## Workflow

1. Ingest source material:
   - CSV export
   - bill screenshot / OCR text
   - bank statement text
2. If the user directly sends a CSV attachment, start analysis immediately without asking for an extra confirmation.
3. Normalize fields:
   - date
   - amount
   - merchant
   - category
   - income vs expense
4. Produce the minimum useful outputs:
   - total income
   - total expense
   - net result
   - top categories
   - largest transactions
5. Flag suspicious patterns:
   - duplicate charges
   - unusually large spending
   - category overspend
   - impulse / discretionary concentration
6. End with practical advice, not abstract finance theory.
2. Normalize fields:
   - date
   - amount
   - merchant
   - category
   - income vs expense
3. Produce the minimum useful outputs:
   - total income
   - total expense
   - net result
   - top categories
   - largest transactions
4. Flag suspicious patterns:
   - duplicate charges
   - unusually large spending
   - category overspend
   - impulse / discretionary concentration
5. End with practical advice, not abstract finance theory.

## Rules

- Prefer plain-language conclusions.
- If category labels are missing, infer them conservatively from merchant names.
- Keep anomaly detection explainable.
- Separate facts from advice.
- Do not fabricate exact totals when source rows are unclear.

## Standard Output

【总览】
- 总收入
- 总支出
- 净支出 / 结余

【分类】
- 前几大消费类别

【异常】
- 大额消费
- 疑似重复扣款
- 可疑波动

【建议】
- 下一周 / 下个月怎么收缩

## References

- Read `references/category-rules.md` for common transaction classification ideas.
- Read `references/advice-patterns.md` for practical budgeting suggestions.
