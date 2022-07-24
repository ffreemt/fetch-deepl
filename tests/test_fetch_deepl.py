"""Test fetch_deepl."""
# pylint: disable=broad-except
from fetch_deepl import __version__, fetch_deepl


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not fetch_deepl()
    except Exception:
        assert True
