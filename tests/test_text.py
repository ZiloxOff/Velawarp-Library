import pytest

from velawarp import normalize_whitespace, slugify, truncate


def test_slugify_normalizes_accents_and_punctuation():
    assert slugify("  Vélawarp, ça déchire ! ") == "velawarp-ca-dechire"
    assert slugify("Cafe creme", separator="_") == "cafe_creme"


def test_normalize_whitespace_collapses_spaces_and_newlines():
    assert normalize_whitespace("  une\tphrase\n sur   deux  ") == "une phrase sur deux"


def test_truncate_counts_suffix_in_maximum_length():
    assert truncate("Velawarp est pratique", 12) == "Velawarp..."
    assert truncate("court", 12) == "court"
    assert truncate("long", 2) == ".."


def test_truncate_rejects_negative_length():
    with pytest.raises(ValueError):
        truncate("texte", -1)