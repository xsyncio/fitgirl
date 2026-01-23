import pytest
from fitgirl.client import FitGirlClient
from fitgirl.models.repack import Repack


@pytest.mark.asyncio
async def test_site_availability(client: FitGirlClient):
    """Test that the site is reachable."""
    assert await client.check_site_availability() is True


@pytest.mark.asyncio
async def test_search_basic(client: FitGirlClient):
    """Test basic search functionality."""
    results = await client.search("cyberpunk")
    assert results is not None
    assert len(results.items) > 0
    # ensure at least one results has cyberpunk in title (case insensitive)
    assert any("cyberpunk" in item.title.lower() for item in results.items)


@pytest.mark.asyncio
async def test_get_repack_details(client: FitGirlClient):
    """Test retrieving details for a specific repack."""
    # First search to get a valid slug
    search_results = await client.search("elden ring")
    assert search_results.items

    first_item = search_results.items[0]
    slug = first_item.slug
    assert slug

    # Now get details
    repack = await client.get_repack(slug)
    assert repack is not None
    assert isinstance(repack, Repack)
    assert repack.title == first_item.title
    assert repack.date is not None
    # Check if we have at least one download source (magnet or mirror)
    assert repack.torrent_sources or repack.download_mirrors


@pytest.mark.asyncio
async def test_list_repacks(client: FitGirlClient):
    """Test listing repacks (homepage/pagination)."""
    # get_latest lists the homepage repacks
    results = await client.get_latest(page=1)
    assert results is not None
    assert len(results.items) > 0
    assert results.total_pages > 0


@pytest.mark.asyncio
async def test_search_no_results(client: FitGirlClient):
    """Test search with a query that should yield no results."""
    results = await client.search(
        "supercalifragilisticexpialidocious_nonexistent_game_12345"
    )
    assert results is not None
    assert len(results.items) == 0


@pytest.mark.asyncio
async def test_check_magnet_health(client: FitGirlClient):
    """Test checking magnet health."""
    # Search for something popular to ensure seeds
    results = await client.search("GTA V")
    if not results.items:
        pytest.skip("Could not find GTA V to test magnet health")

    first_item = results.items[0]
    repack = await client.get_repack(first_item.slug)

    # Repack might have multiple sources, try to find a magnet
    magnet_source = next((s for s in repack.torrent_sources if s.magnet), None)

    if not magnet_source or not magnet_source.magnet:
        pytest.skip("No magnet link found in repack")

    # Use a short timeout for test speed
    health = await client.check_magnet_health(magnet_source.magnet, timeout=2.0)

    # We don't assert seeds > 0 strictly because trackers might timeout or fail,
    # but the method should return None or a TorrentHealth object.
    if health:
        assert isinstance(health.seeds, int)
        assert isinstance(health.peers, int)
