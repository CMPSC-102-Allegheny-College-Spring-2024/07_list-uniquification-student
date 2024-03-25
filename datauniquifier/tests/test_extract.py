"""Ensure that the extract function works correctly."""

from datauniquifier import extract


def test_extract_column_zero_and_one_correct_length():
    """Check that the extraction of column one and two works correctly for length."""
    data = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    result = extract.extract_data_given_column(data, 0)
    assert len(result) == 4
    result = extract.extract_data_given_column(data, 1)
    assert len(result) == 4


def test_extract_column_zero_and_one_correct_content():
    """Check that the extraction of column one works correctly for content."""
    data = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    result = extract.extract_data_given_column(data, 0)
    assert "shawkins@watson.com" in result
    result = extract.extract_data_given_column(data, 1)
    assert "Records manager" in result
