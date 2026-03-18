---
name: travel-packing-officer
description: Build travel packing checklists, trip briefs, and departure reminders from destination, date, transport, weather, and trip purpose. Use when the user says 宝典九, 出差/旅行带什么, 行李清单, 帮我查航班和酒店, 帮我整理出行方案, or wants a travel brief exported as a local document.
---

# Travel Packing Officer

Plan a trip like an organized human assistant.

## Workflow

1. Extract destination, date, departure window, trip purpose, and transport mode.
2. Check weather, transport options, and hotel price range when the user asks for them.
3. Convert the trip into a practical packing checklist.
4. Separate must-carry items from optional items.
5. If requested, export a trip brief as a `.docx`.
6. If details are missing, make reasonable travel assumptions and mark them clearly.

## Default behavior

- For business trips, prioritize: 身份证件、电脑、充电器、正式衣物、洗护、雨具。
- For flights, remind about提前到机场、证件、充电宝限制、托运行李风险。
- Weather should affect clothing and rain gear.
- Hotel research can be summarized as a price range plus 2–3 suggested areas.

## Output rules

- Keep the user-facing checklist concrete.
- Use short categories, not essays.
- Mark uncertain flight and hotel info as “以实际预订页为准”.
- Prefer a brief + checklist document when the user wants something to save or send.

## Resources

### scripts/
- `scripts/write_trip_brief.py`
  - Generate a `.docx` travel brief and packing checklist

### references/
- `references/checklist-rules.md`
  - Read when building the checklist structure and business-trip defaults
