---
name: movie-finder
description: "Private movie and TV show discovery assistant. Search for movies/TV shows across platforms, check ratings from multiple sources (Douban, IMDb, Rotten Tomatoes), get recommendations, track personal watch history, and find where to watch. Use when the user says 宝典十, 搜片, 找电影, 推荐电影, 影评, 哪个平台有, 看什么, 豆瓣评分, IMDb评分, 追剧, 观影记录, movie recommendation, what to watch, or wants to discover/filter/rate movies or TV shows."
---

# Movie & TV Finder (影剧看门人)

Find, rate, recommend, and track movies and TV shows.

## Workflow

### 1. Search for a Movie/Show

Use the search script to query multiple rating sources:

```bash
python3 scripts/search.py "movie name" [--type movie|tv] [--lang zh|en]
```

Returns: title, year, Douban score, IMDb score, Rotten Tomatoes score, genre, plot summary, platform availability.

### 2. Get Recommendations

Ask the user for preferences (genre, mood, year range, platform), then use web search to find curated lists:

```bash
python3 scripts/recommend.py --genre "action" --min-rating 7.0 --year 2020-2026
```

### 3. Check Platform Availability

Search where a title is available to stream:

```bash
python3 scripts/platforms.py "movie name"
```

Checks: Netflix, Disney+, Prime Video, iQIYI, Youku, Bilibili, Tencent Video, and more.

### 4. Track Watch History

Maintain `references/watchlist.json`:

```bash
python3 scripts/tracker.py add "movie name" --rating 8 --date 2026-03-18
python3 scripts/tracker.py list [--filter watched|watching|wishlist]
python3 scripts/tracker.py stats
```

### 5. Generate Personal Stats

```bash
python3 scripts/tracker.py stats
```

Returns: total watched, average rating, genre distribution, monthly breakdown.

## Rating Reference

- 9.0+ = Must-watch masterpiece
- 8.0-8.9 = Highly recommended
- 7.0-7.9 = Worth watching
- 6.0-6.9 = Average, watch if bored
- Below 6.0 = Skip it

## Output Format

Present results in a clean card format:

```
🎬 Movie Title (Year)
⭐ Douban: 8.5 | IMDb: 7.8 | 🍅 85%
🎭 Genre | 📅 Year | ⏱️ Duration
📝 One-line summary
📺 Available on: Platform1, Platform2
```

Do NOT use markdown tables. Use bullet lists or card format instead.

## Data Sources

- **Douban (豆瓣)**: Primary for Chinese audience, rich Chinese reviews
- **IMDb**: International standard, comprehensive database
- **Rotten Tomatoes**: Critic + audience scores
- **JustWatch**: Platform availability across regions
- **TMDb**: Supplemental metadata and artwork

See `references/sources.md` for detailed API endpoints and fallback strategies.

## Watchlist Data

Personal watch history and wishlist stored in `references/watchlist.json`. Initialize on first use with an empty structure:

```json
{
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
```

## Interaction Patterns

- User sends a movie name → Search and return full info card
- User says "recommend something" → Ask preferences, then search
- User says "what's good lately" → Search recent highly-rated releases
- User says "track/rate X" → Add to watchlist with rating
- User says "my stats" → Generate personal stats summary
- User sends a screenshot of a movie poster → Identify with image tool, then search
