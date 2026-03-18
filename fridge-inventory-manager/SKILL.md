---
name: fridge-inventory-manager
description: Recognize food and grocery images, append structured rows into a fridge inventory CSV, and infer expiry dates for newly bought food. Use when the user tests 宝典七, sends grocery/food photos, asks to 识别食材, 记录库存, 建立冰箱表格, 更新食材 CSV, or wants expiry dates auto-filled from purchase date.
---

# Fridge Inventory Manager

Maintain a simple food inventory from user-sent images.

## Workflow

1. Treat uploaded grocery photos as today's purchases unless the user says otherwise.
2. Recognize visible food names and rough quantities from the image.
3. Append rows into the inventory CSV.
4. If exact expiry information is not visible, infer expiry as `购买日期 + 15天`.
5. Report what was added and what was inferred.

## Default behavior

- Default CSV path: `/Users/yaoyi/Desktop/食材库存管理.csv`
- Default purchase date: today for the current upload
- Default inferred expiry rule: purchase date + 15 days
- Default location: 冰箱保鲜格 unless the image or user says otherwise
- Default status: 在库

## Output rules

- Keep the user update brief.
- Separate recognition from inference.
- If quantity is unclear, use conservative labels like “若干”.
- If packaging labels are visible, prefer the visible date over the +15 day default.

## Resources

### scripts/
- `scripts/update_inventory.py`
  - Append recognized food rows into the CSV
  - Auto-fill expiry using purchase date + 15 days when missing

### references/
- `references/csv-rules.md`
  - Read when you need the CSV columns and default inference rules
