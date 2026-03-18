#!/usr/bin/env python3
"""Check which platforms have a movie/TV show available."""

import sys
import urllib.request
import urllib.parse
import re

def check_justwatch(query, region="cn"):
    """Check JustWatch for platform availability."""
    try:
        encoded = urllib.parse.quote(query)
        url = f"https://www.justwatch.com/{region}/search?q={encoded}"
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8")
            # Try to extract platform info from page
            platforms = re.findall(r'"name":"(Netflix|Disney\+|Prime Video|爱奇艺|优酷|腾讯视频|哔哩哔哩|Bilibili|芒果TV|Apple TV\+|HBO Max|Paramount\+)"', html)
            if platforms:
                unique = list(dict.fromkeys(platforms))
                return unique
    except Exception as e:
        print(f"[!] JustWatch check failed: {e}", file=sys.stderr)

    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 platforms.py \"movie name\"")
        sys.exit(1)

    query = sys.argv[1]

    print(f"🔍 查找「{query}」的观看平台...\n")

    platforms = check_justwatch(query)

    if platforms:
        print(f"📺 「{query}」可在以下平台观看：")
        for p in platforms:
            print(f"   ✅ {p}")
    else:
        print(f"未自动检测到平台信息，建议手动查看：")
        encoded = urllib.parse.quote(query)
        print(f"   🔗 JustWatch: https://www.justwatch.com/cn/search?q={encoded}")
        print(f"   🔗 豆瓣搜索: https://search.douban.com/movie/subject_search?search_text={encoded}")

if __name__ == "__main__":
    main()
