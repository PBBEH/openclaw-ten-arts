#!/usr/bin/env python3
"""Recommend movies/TV shows based on preferences."""

import argparse
import json
import random
import sys
import urllib.request
import urllib.parse

RECOMMENDATIONS = {
    "action": [
        {"title": "疾速追杀4 (John Wick: Chapter 4)", "year": "2023", "douban": 8.2, "genre": "动作"},
        {"title": "碟中谍7：致命清算 (上)", "year": "2023", "douban": 7.9, "genre": "动作/冒险"},
        {"title": "壮志凌云2 (Top Gun: Maverick)", "year": "2022", "douban": 8.0, "genre": "动作/剧情"},
    ],
    "comedy": [
        {"title": "满江红", "year": "2023", "douban": 7.0, "genre": "喜剧/悬疑"},
        {"title": "保你平安", "year": "2023", "douban": 7.7, "genre": "喜剧"},
        {"title": "人生路不熟", "year": "2023", "douban": 6.8, "genre": "喜剧/公路"},
    ],
    "scifi": [
        {"title": "流浪地球2", "year": "2023", "douban": 8.3, "genre": "科幻/冒险"},
        {"title": "沙丘2 (Dune: Part Two)", "year": "2024", "douban": 8.2, "genre": "科幻/冒险"},
        {"title": "奥本海默 (Oppenheimer)", "year": "2023", "douban": 8.8, "genre": "传记/历史"},
    ],
    "drama": [
        {"title": "封神第一部", "year": "2023", "douban": 7.8, "genre": "奇幻/古装"},
        {"title": "消失的她", "year": "2023", "douban": 6.4, "genre": "悬疑/剧情"},
        {"title": "过往人生 (Past Lives)", "year": "2023", "douban": 7.7, "genre": "剧情/爱情"},
    ],
    "anime": [
        {"title": "你想活出怎样的人生", "year": "2023", "douban": 7.6, "genre": "动画/奇幻"},
        {"title": "蜘蛛侠：纵横宇宙", "year": "2023", "douban": 8.6, "genre": "动画/动作"},
        {"title": "铃芽之旅", "year": "2023", "douban": 7.9, "genre": "动画/奇幻"},
    ],
    "thriller": [
        {"title": "孤注一掷", "year": "2023", "douban": 6.9, "genre": "犯罪/剧情"},
        {"title": "坚如磐石", "year": "2023", "douban": 6.2, "genre": "犯罪/悬疑"},
        {"title": "看不见的客人 (Contratiempo)", "year": "2017", "douban": 8.8, "genre": "悬疑/惊悚"},
    ],
}

def get_recommendations(genre=None, min_rating=7.0, year=None):
    """Get movie recommendations based on filters."""
    results = []

    if genre and genre in RECOMMENDATIONS:
        pool = RECOMMENDATIONS[genre]
    else:
        # Mix from all genres
        pool = []
        for items in RECOMMENDATIONS.values():
            pool.extend(items)

    for item in pool:
        if item["douban"] < min_rating:
            continue
        if year:
            y_min, y_max = map(int, year.split("-"))
            item_year = int(item["year"])
            if item_year < y_min or item_year > y_max:
                continue
        results.append(item)

    # Shuffle and return top 5
    random.shuffle(results)
    return results[:5]

def main():
    parser = argparse.ArgumentParser(description="Get movie recommendations")
    parser.add_argument("--genre", default=None, help="Genre filter (action/comedy/scifi/drama/anime/thriller)")
    parser.add_argument("--min-rating", type=float, default=7.0, help="Minimum Douban rating")
    parser.add_argument("--year", default=None, help="Year range, e.g. 2020-2026")
    args = parser.parse_args()

    results = get_recommendations(
        genre=args.genre,
        min_rating=args.min_rating,
        year=args.year
    )

    if not results:
        print("没有找到符合条件的推荐，试试降低评分门槛或更换类型？")
        return

    print("🎬 为你推荐：\n")
    for i, r in enumerate(results, 1):
        emoji = "🔥" if r["douban"] >= 8.5 else "⭐" if r["douban"] >= 7.5 else "📺"
        print(f"{i}. {emoji} {r['title']} ({r['year']})")
        print(f"   豆瓣: {r['douban']} | 类型: {r['genre']}")
        print("")

if __name__ == "__main__":
    main()
