import tempfile
from pathlib import Path

import pandas as pd
import pytest

from utw.fixtures import count_lines, filter_counts, uppercase_names


@pytest.fixture
def temp_text_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        file = Path(tmpdir) / "data.txt"
        file.write_text("hello\nworld\n123")
        yield file


@pytest.fixture
def df_test():
    return pd.DataFrame(
        {
            "name": ["s1", "s2", "s3", "s4", "s5"],
            "counts": [3000, 175, 45, 500, 1500],
        }
    )


def test_filter_counts(df_test):
    """Test the filter_counts function."""

    filtered = filter_counts(df_test, threshold=1000)
    assert len(filtered) == 2
    assert all(filtered["counts"] >= 1000)


def test_filter_counts_1(df_test):
    """Test the filter_counts function."""

    filtered_df = filter_counts(df_test, threshold=10)
    assert len(filtered_df) == 5
    assert all(filtered_df["counts"] >= 10)


def test_count_lines(temp_text_file):
    assert count_lines(temp_text_file) == 3


def test_upper_case_names(df_test):
    uppercase_df = uppercase_names(df_test)
    assert list(uppercase_df["name"]) == ["S1", "S2", "S3", "S4", "S5"]
