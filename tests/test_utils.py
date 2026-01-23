import pytest
from fitgirl.utils.magnets import resolve_magnet_link


def test_resolve_magnet_link_clean():
    clean_magnet = "magnet:?xt=urn:btih:1234567890abcdef&dn=Test"
    assert resolve_magnet_link(clean_magnet) == clean_magnet


def test_resolve_magnet_link_embedded():
    embedded = "https://example.com/redirect?url=magnet:?xt=urn:btih:embedded"
    assert "magnet:?xt=urn:btih:embedded" in resolve_magnet_link(embedded)


def test_resolve_magnet_link_invalid():
    with pytest.raises(ValueError):
        resolve_magnet_link("https://google.com/nothing-here")
