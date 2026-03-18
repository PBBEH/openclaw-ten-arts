---
name: downloads-folder-organizer
description: Organize messy folders such as Downloads into a clean hierarchy by file type, year, and month, while respecting user-specified skip folders. Use when the user says 整理下载文件夹, 整理下载目录, 下载目录太乱了, 按文件类型和时间整理, or wants a local folder reorganized into 文件类型/年份/月 structure.
---

# Downloads Folder Organizer

Reorganize a local folder into a stable, readable structure.

## Workflow

1. Identify the target folder.
2. Ask or infer skip folders that must not be touched.
3. Apply the default structure: `文件类型 / 年 / 月`.
4. Use `scripts/organize_downloads.py` for deterministic execution.
5. Avoid hidden files and system metadata.
6. Remove empty directories after reorganization when safe.

## Default behavior

- Default target is the user's Downloads folder if they say “整理下载文件夹”.
- Default skip example: `MG音效大合集` if the user has marked it as do-not-touch.
- Use file modified time for year/month buckets.
- Do not overwrite same-name files; append numeric suffixes instead.

## Output rules

- Report the final structure briefly.
- Mention any skip folders.
- Mention if the operation flattened nested content.
- If a protected folder was previously touched by mistake, explicitly avoid touching it in later runs.

## Resources

### scripts/
- `scripts/organize_downloads.py`
  - Reorganize a folder into type/year/month

Example:

```bash
python3 scripts/organize_downloads.py --root ~/Downloads --skip MG音效大合集
```

### references/
- `references/rules.md`
  - Read when you need the default folder rules and category behavior
