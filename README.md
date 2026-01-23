<!--
 Copyright (c) 2026 Xsyncio
 Released under the MIT License
-->

<div align="center">

<img src="assets/banner.svg" alt="FitGirl Scraper Banner" width="100%" />

<br/>

[![PyPI version](https://img.shields.io/pypi/v/fitgirl?style=for-the-badge&color=ff00cc)](https://pypi.org/project/fitgirl/)
[![Python Version](https://img.shields.io/pypi/pyversions/fitgirl?style=for-the-badge&color=3333ff)](https://pypi.org/project/fitgirl/)
[![License](https://img.shields.io/github/license/xsyncio/fitgirl?style=for-the-badge&color=00ffbd)](LICENSE)
[![Tests](https://img.shields.io/github/actions/workflow/status/xsyncio/fitgirl/test.yml?branch=main&label=Tests&style=for-the-badge)](https://github.com/xsyncio/fitgirl/actions)

<h3>High-Performance, Async-First Scraper for the FitGirl Repacks Universe</h3>

[**Documentation**](wiki/Home.md) •
[**Installation**](wiki/Installation.md) •
[**Usage**](wiki/Usage.md) •
[**API Reference**](wiki/API-Reference.md)

</div>

---

## ⚡ Overview

**FitGirl Scraper** is a production-grade Python library designed to programmatically interact with *fitgirl-repacks.site*. Unlike simple HTML parsers, it leverages the hidden **WordPress REST API** for robust data retrieval, falling back to high-speed **HTML parsing** (via `selectolax`) only when necessary.

It is built for **speed**, **stealth**, and **type safety**.

## ✨ Key Features

<table>
  <tr>
    <td width="33%"><div align="center"><h3>🚀 Async & Fast</h3></div>I/O bound operations are fully asynchronous. Built on <b>curl_cffi</b> to impersonate real browsers (Chrome 131) and <b>selectolax</b> for ultra-fast C-based parsing.</td>
    <td width="33%"><div align="center"><h3>🛡️ Type Safe</h3></div>100% type-hinted and runtime validated using <b>msgspec</b>. Every API response is a structured, frozen, and immutable object. No more `Dict[str, Any]`.</td>
    <td width="33%"><div align="center"><h3>🕵️ Hybrid Engine</h3></div>Intelligently switches between the <b>LinkeDom-like</b> HTML scraping and the hidden <b>JSON API</b> to get the most reliable data available.</td>
  </tr>
</table>

*   **Torrent Health**: Real-time UDP tracker scraping to check seeds/peers.
*   **Smart Search**: Advanced filtering by category (Lossless, Repack), tags, and dates.
*   **Resilient**: Built-in exponential backoff, retry logic, and error handling.
*   **Zero-Config**: Works out of the box with sensible defaults.

## 📦 Installation

Requires **Python 3.13+**. Use [uv](https://github.com/astral-sh/uv) for the best experience.

```bash
uv add fitgirl
```

Or standard pip:

```bash
pip install fitgirl
```

## 🚀 Quick Start

```python
import asyncio
from fitgirl import FitGirlClient

async def main():
    # Context manager handles session cleanup automatically
    async with FitGirlClient() as client:
        
        # 1. Search for a game (Uses API for speed)
        print("🔍 Searching for 'Cyberpunk'...")
        results = await client.search_api("cyberpunk")
        
        for post in results.items:
            print(f"found: {post.title}")

        # 2. Get Deep Details
        slug = "cyberpunk-2077"
        print(f"\n📥 Fetching details for {slug}...")
        repack = await client.get_repack_api(slug)
        
        print(f"📦 Size: {repack.repack_size}")
        print(f"🧲 Magnet: {repack.torrent_sources[0].magnet.raw_uri[:60]}...")
        
        # 3. Check Real-time Health
        health = await client.check_magnet_health(repack.torrent_sources[0].magnet)
        if health:
            print(f"🟢 Seeds: {health.seeds} | 🔴 Peers: {health.peers}")

if __name__ == "__main__":
    asyncio.run(main())
```

> **Detailed Usage**: Check the [Wiki Usage Guide](wiki/Usage.md) for advanced examples.

## 📚 Documentation

The documentation is hosted in the **GitHub Wiki**:

*   **[Home](wiki/Home.md)**: Architecture & Design.
*   **[Installation](wiki/Installation.md)**: Setup & Requirements.
*   **[Usage Guide](wiki/Usage.md)**: Common patterns & recipes.
*   **[API Reference](wiki/API-Reference.md)**: Complete method documentation.
*   **[Contributing](wiki/Contributing.md)**: How to build & test.

## ⚖️ Legal & Disclaimer

This software is for **educational purposes only**. The authors are not affiliated with FitGirl Repacks. Downloading copyrighted material without permission may be illegal in your jurisdiction. Use this tool responsibly.

---

<div align="center">
    <sub>Built with ❤️ by <a href="https://github.com/xsyncio">xsyncio</a></sub>
</div>
