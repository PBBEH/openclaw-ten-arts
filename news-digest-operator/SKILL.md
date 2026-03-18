---
name: news-digest-operator
description: Collect, deduplicate, summarize, format, and deliver daily news digests from RSS feeds, search results, or public news pages. Use when the user asks for 早报, 新闻汇编, digest, RSS 摘要, 每日新闻推送, AI早报, 国际局势早报, or wants scheduled/newsletter-style summaries sent or prepared for publication.
---

# News Digest Operator

Produce concise, high-value daily digests from multiple news sources.

## Workflow

1. Identify topic and audience:
   - AI
   - international affairs
   - finance
   - mixed custom sources
2. Gather sources from RSS, search, or known pages.
3. Deduplicate overlapping headlines.
4. Rank by value, not by volume.
5. Format into a digest with:
   - headline
   - short summary or key line
   - timestamp when available
   - optional source link
6. Save the digest to a predictable file name when needed.
7. Deliver through the requested channel or prepare for later sending.

## Rules

- Prefer 5-10 strong items over long noisy lists.
- If sources are weak, say so implicitly by keeping fewer items rather than padding.
- Preserve publication time when available.
- Match the user format preference: concise, readable, no fluff.
- For scheduled digests, verify the delivery job is enabled and the content file exists.

## Common Modes

### 1. AI early digest
- 10 items
- product/model/company focus

### 2. International affairs digest
- 3-8 items
- emphasize main geopolitical line

### 3. Custom RSS digest
- user-defined sources
- grouped by source or topic

## References

- Read `references/source-strategy.md` for sourcing priority.
- Read `references/format-templates.md` for digest structures.
