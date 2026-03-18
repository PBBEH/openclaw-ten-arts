---
name: financial-experiment-writer
description: Write course experiment reports and lab-style academic reports from a provided .docx template, then output a ready-to-send .docx file. Use when the user says 宝典五, sends a report template, asks to “按这个模板写实验报告/课程报告/实验论文”, or wants a finished report generated from an existing Word template.
---

# Financial Experiment Writer

Use the provided Word template to generate a finished experiment report.

## Workflow

1. Identify the template.
   - If the user provides a `.docx` template, use it.
   - If the user says “默认模板”, use `assets/default-template.docx`.
2. Confirm the report topic from the user request.
   - If the topic is missing, write a safe generic finance experiment report.
3. Generate a `.docx` output instead of plain text whenever possible.
4. Prefer using `scripts/generate_report.py` for the default template workflow.
5. Send the finished `.docx` file back directly.

## Default behavior

- Default template: `assets/default-template.docx`
- Default domain: finance / financial experiment reports
- Default sections:
  - 一、实验题目
  - 二、实验目的和要求
  - 三、实验内容
  - 四、实验总结
- Default tone: normal undergraduate course report, directly usable, not overly academic

## Output rules

- Prioritize a usable `.docx` deliverable.
- Preserve template layout whenever possible.
- Do not invent precise experimental data the user never supplied.
- If the user gives no dataset, write a generic but coherent report suitable for template testing.
- If the template is the default one, use `scripts/generate_report.py`.

## Resources

### scripts/
- `scripts/generate_report.py`
  - Generate a finished `.docx` from the default template
  - Supports custom title, course, teacher, date range, purpose, content, and summary

Example:

```bash
python3 scripts/generate_report.py \
  --output /tmp/金融实验报告.docx \
  --title "基于股票收益率与波动率特征的金融数据分析实验"
```

### references/
- `references/defaults.md`
  - Read when you need the current default template rule and default writing behavior

### assets/
- `assets/default-template.docx`
  - Current default template for 宝典五
