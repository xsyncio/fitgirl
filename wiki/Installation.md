# Installation

## Requirements

*   **Python 3.13+**

## Install via uv (Recommended)

This project uses `uv` for package management.

```bash
uv add fitgirl
```

## Install via pip

```bash
pip install fitgirl
```

## Dependencies

The library installs the following key dependencies:

*   `curl_cffi`: For high-performance, browser-impersonating HTTP requests (prevents bot detection).
*   `selectolax`: For ultra-fast HTML parsing.
*   `msgspec`: For fast JSON/Struct validation and serialization.

## Verifying Installation

Create a simple script `check.py` to test the connection:

```python
import asyncio
from fitgirl import FitGirlClient

async def main():
    async with FitGirlClient() as client:
        if await client.check_site_availability():
            print("Successfully connected to FitGirl Repacks!")
        else:
            print("Could not connect to site.")

if __name__ == "__main__":
    asyncio.run(main())
```
