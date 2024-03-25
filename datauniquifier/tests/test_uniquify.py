"""Confirm that the functions in the uniquify module work correctly."""


from datauniquifier import uniquify


def test_unique_small_empty_set():
    """Ensure that creating a unique set works for a small list with a drop."""
    list = []
    output = uniquify.unique_set(list)
    assert len(output) == 0


def test_unique_small_set_drop():
    """Ensure that creating a unique set works for a small list with a drop."""
    list = ["1", "2", "1", "4", "5"]
    output = uniquify.unique_set(list)
    assert len(output) == 4


def test_unique_small_set_no_drop():
    """Ensure that creating a unique set works for a small list without a drop."""
    list = ["1", "2", "10", "4", "5"]
    output = uniquify.unique_set(list)
    assert len(output) == 5
