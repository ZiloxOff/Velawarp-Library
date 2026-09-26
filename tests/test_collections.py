import pytest

from velawarp import chunked, flatten


def test_chunked_splits_an_iterable_into_bounded_lists():
    assert list(chunked(range(5), 2)) == [[0, 1], [2, 3], [4]]


def test_chunked_rejects_non_positive_size():
    with pytest.raises(ValueError):
        list(chunked([1, 2], 0))


def test_flatten_flattens_one_level_lazily():
    assert list(flatten([[1, 2], [], [3]])) == [1, 2, 3]