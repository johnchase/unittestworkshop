import pandas as pd

from utw.fixtures import filter_counts

DF_TEST = pd.DataFrame(
    {
        "name": ["s1", "s2", "s3", "s4", "s5"],
        "counts": [3000, 175, 45, 500, 1500],
    }
)


def test_filter_counts():
    """Test the filter_counts function."""

    filtered = filter_counts(DF_TEST, threshold=1000)
    DF_TEST.drop(index=filtered.index, inplace=True)
    assert len(filtered) == 2
    assert all(filtered["counts"] >= 1000)


def test_filter_counts_1():
    """Test the filter_counts function."""

    filtered_df = filter_counts(DF_TEST, threshold=10)
    assert len(filtered_df) == 5
    assert all(filtered_df["counts"] >= 10)
