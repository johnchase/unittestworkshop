import pandas as pd
import pytest

from utw.fixtures import filter_counts


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
    df_test.drop(index=filtered.index, inplace=True)
    assert len(df_test) == 2
    assert all(df_test["counts"] >= 1000)


def test_filter_counts_1(df_test):
    """Test the filter_counts function."""

    filtered_df = filter_counts(df_test, threshold=10)
    assert len(filtered_df) == 5
    assert all(filtered_df["counts"] >= 10)
