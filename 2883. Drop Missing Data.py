import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:

    return students[students["name"].notna()]
    return students.dropna(subset=["name"])
