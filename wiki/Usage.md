# Usage Guide

## Basic Usage

Always use `FitGirlClient` as an async context manager to ensure the underlying HTTP session is closed properly.

```python
import asyncio
from fitgirl import FitGirlClient

async def main():
    async with FitGirlClient() as client:
        # Your code here...
        pass

if __name__ == "__main__":
    asyncio.run(main())
```

## Searching for Games

You can search using the **Public API** (Recommended) or HTML scraping.

### Using the API (Structured Data)

```python
results = await client.search_api("cyberpunk")

for post in results.items:
    print(f"{post.title} (Published: {post.date})")
    print(f"URL: {post.url}")
```

### Advanced Filtering

Filter by category, tag, or date range.

```python
from datetime import datetime

results = await client.advanced_search(
    query="elden ring",
    after=datetime(2023, 1, 1),
    categories=[2]  # ID 2 might be specific category
)
```

## Getting Repack Details

Fetch comprehensive details including magnet links, file sizes, and game version.

```python
slug = "cyberpunk-2077"
repack = await client.get_repack_api(slug)

print(f"Title: {repack.title}")
print(f"Size: {repack.repack_size}")

for source in repack.torrent_sources:
    if source.magnet:
        print(f"Magnet: {source.magnet.raw_uri}")
```

## Checking Torrent Health

Use the built-in tracker scraper to check seeders/leechers in real-time.

```python
magnet_link = repack.torrent_sources[0].magnet
health = await client.check_magnet_health(magnet_link)

if health:
    print(f"Seeds: {health.seeds}, Peers: {health.peers}")
```

## browsing Categories

```python
# Get Lossless Repacks
lossless = await client.get_category("lossless-repack")

# Get Upcoming Repacks
upcoming = await client.get_upcoming_repacks()
print(f"Coming soon: {upcoming}")
```

## Error Handling

The library uses a custom exception hierarchy.

```python
from fitgirl.exceptions import NotFoundError, NetworkError

try:
    repack = await client.get_repack_api("non-existent-game")
except NotFoundError:
    print("Game not found!")
except NetworkError as e:
    print(f"Connection failed: {e}")
```
