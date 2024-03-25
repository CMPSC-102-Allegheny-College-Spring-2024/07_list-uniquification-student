"""Confirm that the functions in the analyze module work correctly."""


from datauniquifier import analyze


def test_half_reduction():
    """Confirm that a half reduction is calculated correctly."""
    list_start = ["a", "b", "c", "d"]
    list_end = ["a", "b"]
    reduction = analyze.calculate_reduction(list_start, list_end)
    assert reduction == 2


def test_half_reduction_percentage():
    """Confirm that a 50% reduction is calculated correctly."""
    list_start = ["a", "b", "c", "d"]
    list_end = ["a", "b"]
    reduction = analyze.calculate_percent_reduction(list_start, list_end)
    assert reduction == 50


def test_small_reduction():
    """Confirm that a half reduction is calculated correctly."""
    list_start = ["a", "b", "c", "d"]
    list_end = ["a", "b", "c"]
    reduction = analyze.calculate_reduction(list_start, list_end)
    assert reduction == 1


def test_small_reduction_percentage():
    """Confirm that a 25% reduction is calculated correctly."""
    list_start = ["a", "b", "c", "d"]
    list_end = ["a", "b", "c"]
    reduction = analyze.calculate_percent_reduction(list_start, list_end)
    assert reduction == 25


def test_no_reduction():
    """Confirm that a half reduction is calculated correctly."""
    list_start = ["a", "b", "c", "d"]
    list_end = ["a", "b", "c", "d"]
    reduction = analyze.calculate_reduction(list_start, list_end)
    assert reduction == 0


def test_no_reduction_percentage():
    """Confirm that a 0% reduction is calculated correctly."""
    list_start = ["a", "b", "c", "d"]
    list_end = ["a", "b", "c", "d"]
    reduction = analyze.calculate_percent_reduction(list_start, list_end)
    assert reduction == 0
