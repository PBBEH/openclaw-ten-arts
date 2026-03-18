#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path

EXT_MAP = {
    '.doc': '文档', '.docx': '文档', '.pdf': '文档', '.txt': '文档', '.md': '文档', '.rtf': '文档',
    '.xls': '表格', '.xlsx': '表格', '.csv': '表格', '.numbers': '表格',
    '.ppt': '演示', '.pptx': '演示', '.key': '演示',
    '.jpg': '图片', '.jpeg': '图片', '.png': '图片', '.gif': '图片', '.webp': '图片', '.svg': '图片', '.bmp': '图片', '.heic': '图片',
    '.mp3': '音频', '.wav': '音频', '.m4a': '音频', '.flac': '音频', '.aac': '音频', '.ogg': '音频', '.wma': '音频',
    '.mp4': '视频', '.mov': '视频', '.mkv': '视频', '.avi': '视频', '.webm': '视频',
    '.zip': '压缩包', '.rar': '压缩包', '.7z': '压缩包', '.tar': '压缩包', '.gz': '压缩包', '.bz2': '压缩包', '.xz': '压缩包', '.tgz': '压缩包',
    '.dmg': '安装包', '.pkg': '安装包', '.app': '安装包', '.apk': '安装包', '.exe': '安装包', '.msi': '安装包',
    '.html': '网页文件', '.htm': '网页文件', '.ttf': '字体', '.otf': '字体', '.woff': '字体', '.woff2': '字体',
}
IGNORE = {'.DS_Store', '.localized'}


def category_for(path: Path) -> str:
    if path.name.lower().endswith('.tar.gz'):
        return '压缩包'
    return EXT_MAP.get(path.suffix.lower(), '其他文件')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--skip', action='append', default=[])
    args = ap.parse_args()

    root = Path(args.root).expanduser().resolve()
    skip = set(args.skip)
    files = []
    for p in root.rglob('*'):
        if not p.is_file():
            continue
        rel = p.relative_to(root)
        if any(part.startswith('.') for part in rel.parts):
            continue
        if p.name in IGNORE:
            continue
        if rel.parts and rel.parts[0] in skip:
            continue
        files.append(p)

    moved = 0
    for src in files:
        dt = datetime.fromtimestamp(src.stat().st_mtime)
        target_dir = root / category_for(src) / f'{dt:%Y}年' / f'{dt:%m}月'
        target_dir.mkdir(parents=True, exist_ok=True)
        target = target_dir / src.name
        if target.exists() and target.resolve() != src.resolve():
            stem, suf = src.stem, src.suffix
            i = 1
            while True:
                cand = target_dir / f'{stem} ({i}){suf}'
                if not cand.exists():
                    target = cand
                    break
                i += 1
        if src.resolve() != target.resolve():
            shutil.move(str(src), str(target))
            moved += 1

    removed = 0
    for d in sorted([p for p in root.rglob('*') if p.is_dir()], key=lambda x: len(x.parts), reverse=True):
        if d == root:
            continue
        rel = d.relative_to(root)
        if any(part.startswith('.') for part in rel.parts):
            continue
        if rel.parts and rel.parts[0] in skip:
            continue
        try:
            if not any(d.iterdir()):
                d.rmdir()
                removed += 1
        except Exception:
            pass

    print(f'moved={moved}')
    print(f'removed_empty_dirs={removed}')

if __name__ == '__main__':
    main()
