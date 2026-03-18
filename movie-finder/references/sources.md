# Data Sources & API Details

## Primary Sources

### Douban (豆瓣)
- URL: https://movie.douban.com/
- Search: https://movie.douban.com/j/subject_suggest?q={query}
- API: https://movie.douban.com/j/subject/{id}
- Rate limit: ~40 req/min (unauthenticated)
- Fallback: web_fetch with search URL when API blocked
- Notes: Douban blocks automated requests; use web_fetch as primary, API as fallback

### IMDb
- URL: https://www.imdb.com/
- Search: https://www.imdb.com/find/?q={query}&s=tt
- API: OMDb API (free tier: 1000/day)
  - Key: obtain from https://www.omdbapi.com/apikey.aspx
  - URL: https://www.omdbapi.com/?t={title}&apikey={key}
- Fallback: web_fetch IMDb search page

### Rotten Tomatoes
- URL: https://www.rottentomatoes.com/
- Search: https://www.rottentomatoes.com/search?search={query}
- No free public API; use web_fetch
- Extract: Tomatometer (critic) + Audience Score

## Platform Availability

### JustWatch
- URL: https://www.justwatch.com/
- Search: https://www.justwatch.com/cn/search?q={query}
- Provides: streaming platform availability by region
- Use web_fetch to extract platform list

### Region-Specific
- China: iQIYI (爱奇艺), Youku (优酷), Bilibili (哔哩哔哩), Tencent Video (腾讯视频), Mango TV (芒果TV)
- International: Netflix, Disney+, Prime Video, Apple TV+, HBO Max

## Fallback Strategy

1. Try web_search with Brave API
2. Fall back to direct web_fetch on source URLs
3. If all automated methods fail, provide search links for user to check manually

## Rate Limiting Guidelines

- Space requests at least 2s apart
- Cache results in conversation context
- Don't hit the same source more than 5 times per session
