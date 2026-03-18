#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timedelta
from pathlib import Path

HEADER = ['名称','数量','单位','购买日期','过期日期','存放位置','状态','来源图片','备注']


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--csv', required=True)
    ap.add_argument('--name', action='append', default=[])
    ap.add_argument('--qty', action='append', default=[])
    ap.add_argument('--unit', action='append', default=[])
    ap.add_argument('--purchase-date', required=True)
    ap.add_argument('--expiry-date', default='')
    ap.add_argument('--location', default='冰箱保鲜格')
    ap.add_argument('--status', default='在库')
    ap.add_argument('--source-image', default='')
    ap.add_argument('--note', default='图片识别录入')
    args = ap.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        csv_path.write_text(','.join(HEADER) + '\n', encoding='utf-8-sig')

    purchase = datetime.strptime(args.purchase_date, '%Y-%m-%d').date()
    expiry = args.expiry_date or str(purchase + timedelta(days=15))

    qtys = args.qty or ['若干'] * len(args.name)
    units = args.unit or ['个'] * len(args.name)
    while len(qtys) < len(args.name):
        qtys.append('若干')
    while len(units) < len(args.name):
        units.append('个')

    with csv_path.open('a', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        for i, name in enumerate(args.name):
            w.writerow([name, qtys[i], units[i], args.purchase_date, expiry, args.location, args.status, args.source_image, args.note])

    print(f'appended={len(args.name)}')
    print(f'expiry={expiry}')

if __name__ == '__main__':
    main()
