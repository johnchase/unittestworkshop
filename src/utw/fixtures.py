from pathlib import Path

import pandas as pd


def filter_counts(df: pd.DataFrame, threshold: int = 1000) -> pd.DataFrame:
    """Return only rows where counts are greater than 1000."""
    return df[df["counts"] >= threshold].reset_index(drop=True)


def uppercase_names(df: pd.DataFrame) -> pd.DataFrame:
    """Return a new DataFrame with uppercase names."""
    df_copy["name"] = df["name"].str.upper()
    return df_copy


def count_lines(path: Path) -> int:
    """Count the number of lines in a file."""
    return len(path.read_text().splitlines())
