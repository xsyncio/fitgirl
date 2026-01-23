# API Reference

**Class**: `fitgirl.FitGirlClient`

The client combines multiple mixins to provide a unified API.

---

## 1. API Methods (`_api.py`)

Methods that leverage the WordPress REST API.

### `get_latest_api(page=1, per_page=10)`
Get the latest repacks with structured pagination.
*   **Returns**: `ListingPage`

### `search_api(query, page=1, per_page=10)`
Search for repacks.
*   **Returns**: `ListingPage`

### `get_repack_api(slug)`
Get full details for a repack by its URL slug.
*   **Returns**: `Repack`
*   **Raises**: `NotFoundError`

### `advanced_search(...)`
Search with filters (categories, tags, date range).
*   **Params**: `query`, `categories` (list[int]), `tags` (list[int]), `after` (datetime), `before` (datetime).

---

## 2. Browse Methods (`_browse.py`)

Methods that scrape HTML pages. Use these when API data is insufficient.

### `get_latest(page=1)`
Get latest repacks from home page.

### `search(query, page=1)`
Search via website search form.

### `get_repack(slug)`
Get details via HTML scraping.

### `get_category(category_slug, page=1)`
### `get_tag(tag_slug, page=1)`
### `get_daily_repacks(date, page=1)`

---

## 3. Special Methods (`_special.py`)

### `get_popular_monthly()`
Returns top 50 popular repacks this month.

### `get_popular_yearly()`
Returns top 150 popular repacks this year.

### `get_upcoming_repacks()`
Returns list of game names coming soon.

### `get_updates_list()`
Returns list of recently updated repacks.

### `get_switch_repacks()`
### `get_ps3_repacks()`

---

## 4. Helper Methods

### `check_site_availability()`
Returns `True` if the site is reachable.

### `check_magnet_health(magnet, timeout=3.0)`
Scrapes UDP trackers to get Seeds/Peers count.

### `download_torrent_file(url, path)`
Downloads a `.torrent` file to the local filesystem.
