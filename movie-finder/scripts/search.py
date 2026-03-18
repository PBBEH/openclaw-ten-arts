#!/usr/bin/env python3
"""Search for a movie or TV show across multiple rating sources."""

import argparse
import json
import re
import subprocess
import sys
import urllib.request
import urllib.parse
import urllib.error

def web_search(query):
    """Use web search to find movie info."""
    try:
        # Use Brave Search via Bocha fallback or direct fetch
        encoded = urllib.parse.quote(query)
        url = f"https://search.brave.com/search?q={encoded}+豆瓣+IMDb+评分"
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8")[:5000]
    except Exception:
        return ""

def search_douban(query):
    """Search Douban for movie info."""
    try:
        encoded = urllib.parse.quote(query)
        url = f"https://movie.douban.com/j/subject_suggest?q={encoded}"
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = []
            for item in data[:3]:
                results.append({
                    "title": item.get("title", ""),
                    "year": item.get("year", ""),
                    "id": item.get("id", ""),
                    "type": item.get("type", ""),
                    "sub_title": item.get("sub_title", ""),
                })
            return results
    except Exception as e:
        print(f"[!] Douban search failed: {e}", file=sys.stderr)
        return []

def search_omdb(query, api_key=None):
    """Search OMDb for movie info."""
    if not api_key:
        return None
    try:
        encoded = urllib.parse.quote(query)
        url = f"https://www.omdbapi.com/?t={encoded}&apikey={api_key}"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data.get("Response") == "True":
                return {
                    "title": data.get("Title", ""),
                    "year": data.get("Year", ""),
                    "imdb_rating": data.get("imdbRating", "N/A"),
                    "genre": data.get("Genre", ""),
                    "plot": data.get("Plot", ""),
                    "runtime": data.get("Runtime", ""),
                    "director": data.get("Director", ""),
                    "actors": data.get("Actors", ""),
                    "type": data.get("Type", ""),
                }
    except Exception as e:
        print(f"[!] OMDb search failed: {e}", file=sys.stderr)
    return None

def format_output(douban_results, omdb_data):
    """Format combined results."""
    output = []
    for i, item in enumerate(douban_results):
        title = item.get("title", "Unknown")
        year = item.get("year", "")
        sub = item.get("sub_title", "")
        mid = item.get("id", "")
        item_type = item.get("type", "")

        lines = [f"🎬 {title} ({year})"]
        if sub:
            lines.append(f"   原名: {sub}")
        lines.append(f"   类型: {item_type}")
        if mid:
            lines.append(f"   豆瓣: https://movie.douban.com/subject/{mid}/")

        # Try to match with OMDb data
        if omdb_data and omdb_data.get("title", "").lower() in title.lower():
            imdb = omdb_data.get("imdb_rating", "N/A")
            genre = omdb_data.get("genre", "")
            plot = omdb_data.get("plot", "")
            runtime = omdb_data.get("runtime", "")
            director = omdb_data.get("director", "")
            actors = omdb_data.get("actors", "")
            if imdb != "N/A":
                lines.append(f"   IMDb: ⭐ {imdb}")
            if genre:
                lines.append(f"   类型: {genre}")
            if runtime:
                lines.append(f"   时长: {runtime}")
            if director:
                lines.append(f"   导演: {director}")
            if plot:
                lines.append(f"   简介: {plot[:200]}")

        lines.append("")
        output.append("\n".join(lines))

    if not output:
        output.append(f"[!] 未找到关于「{douban_results}」的结果，请尝试其他关键词")

    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="Search movies/TV shows")
    parser.add_argument("query", help="Movie or TV show name to search")
    parser.add_argument("--type", choices=["movie", "tv"], default=None, help="Filter by type")
    parser.add_argument("--lang", choices=["zh", "en"], default="zh", help="Search language")
    parser.add_argument("--omdb-key", default=None, help="OMDb API key")
    args = parser.parse_args()

    print(f"🔍 搜索: {args.query}", file=sys.stderr)

    # Search Douban
    douban_results = search_douban(args.query)

    # Search OMDb if key provided
    omdb_data = None
    if args.omdb_key:
        omdb_data = search_omdb(args.query, args.omdb_key)

    # Output
    if douban_results:
        print(format_output(douban_results, omdb_data))
    else:
        print(f"未找到「{args.query}」的相关结果。")
        print(f"建议手动查看: https://search.douban.com/movie/subject_search?search_text={urllib.parse.quote(args.query)}")

if __name__ == "__main__":
    main()
