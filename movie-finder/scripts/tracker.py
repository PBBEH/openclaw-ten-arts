#!/usr/bin/env python3
"""Track personal watch history and generate stats."""

import argparse
import json
import os
import sys
from datetime import datetime, date
from collections import Counter

WATCHLIST_FILE = os.path.join(os.path.dirname(__file__), "..", "references", "watchlist.json")

def load_watchlist():
    try:
        with open(WATCHLIST_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "watched": [],
            "watching": [],
            "wishlist": [],
            "stats": {
                "totalWatched": 0,
                "averageRating": 0,
                "genreBreakdown": {},
                "monthlyCount": {}
            }
        }

def save_watchlist(data):
    with open(WATCHLIST_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_item(name, status="watched", rating=None, genre=None, entry_date=None):
    """Add a movie/show to the watchlist."""
    data = load_watchlist()

    item = {
        "name": name,
        "date": entry_date or date.today().isoformat(),
    }
    if rating:
        item["rating"] = rating
    if genre:
        item["genre"] = genre

    # Check if already exists
    for lst in [data["watched"], data["watching"], data["wishlist"]]:
        for entry in lst:
            if entry["name"] == name:
                print(f"⚠️ 「{name}」已存在于观影记录中")
                return

    if status in data:
        data[status].append(item)
    else:
        print(f"⚠️ 无效状态: {status}，可选: watched/watching/wishlist")
        return

    # Update stats
    if status == "watched" and rating:
        data["stats"]["totalWatched"] = len(data["watched"])
        ratings = [e.get("rating", 0) for e in data["watched"] if e.get("rating")]
        if ratings:
            data["stats"]["averageRating"] = round(sum(ratings) / len(ratings), 1)

        if genre:
            genres = data["stats"]["genreBreakdown"]
            genres[genre] = genres.get(genre, 0) + 1

        month = (entry_date or date.today().isoformat())[:7]
        monthly = data["stats"]["monthlyCount"]
        monthly[month] = monthly.get(month, 0) + 1

    save_watchlist(data)
    status_text = {"watched": "已看完", "watching": "在看", "wishlist": "想看"}
    print(f"✅ 「{name}」已添加到{status_text.get(status, status)}列表")
    if rating:
        print(f"   评分: {'⭐' * int(rating)} ({rating})")

def list_items(status_filter=None):
    """List items in the watchlist."""
    data = load_watchlist()

    if status_filter:
        items = data.get(status_filter, [])
    else:
        # List all with headers
        for status, label in [("watching", "👀 在看"), ("watched", "✅ 已看"), ("wishlist", "📋 想看")]:
            items = data.get(status, [])
            if items:
                print(f"\n{label} ({len(items)}):")
                for item in items:
                    rating_str = f" ⭐{item['rating']}" if item.get("rating") else ""
                    print(f"  • {item['name']} ({item['date']}){rating_str}")
        return

    label = {"watching": "在看", "watched": "已看", "wishlist": "想看"}.get(status_filter, status_filter)
    if not items:
        print(f"「{label}」列表为空")
        return

    print(f"\n{label} ({len(items)}):")
    for item in items:
        rating_str = f" ⭐{item['rating']}" if item.get("rating") else ""
        print(f"  • {item['name']} ({item['date']}){rating_str}")

def show_stats():
    """Show viewing statistics."""
    data = load_watchlist()
    stats = data["stats"]

    print("📊 观影统计\n")
    print(f"  总观看数: {stats['totalWatched']}")
    print(f"  平均评分: {stats['averageRating']}")

    if stats.get("genreBreakdown"):
        print(f"\n  类型分布:")
        for genre, count in sorted(stats["genreBreakdown"].items(), key=lambda x: -x[1]):
            bar = "█" * count
            print(f"    {genre}: {bar} ({count})")

    if stats.get("monthlyCount"):
        print(f"\n  月度统计:")
        for month, count in sorted(stats["monthlyCount"].items()):
            print(f"    {month}: {'█' * count} ({count})")

def main():
    parser = argparse.ArgumentParser(description="Track watch history")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a movie/show")
    add_parser.add_argument("name", help="Movie/show name")
    add_parser.add_argument("--rating", type=float, help="Rating (1-10)")
    add_parser.add_argument("--genre", help="Genre")
    add_parser.add_argument("--date", help="Date (YYYY-MM-DD)")
    add_parser.add_argument("--status", choices=["watched", "watching", "wishlist"], default="watched")

    # List command
    list_parser = subparsers.add_parser("list", help="List watchlist")
    list_parser.add_argument("--filter", choices=["watched", "watching", "wishlist"], dest="status_filter")

    # Stats command
    subparsers.add_parser("stats", help="Show statistics")

    args = parser.parse_args()

    if args.command == "add":
        add_item(args.name, status=args.status, rating=args.rating, genre=args.genre, entry_date=args.date)
    elif args.command == "list":
        list_items(args.status_filter)
    elif args.command == "stats":
        show_stats()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
