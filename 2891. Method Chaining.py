import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:

    new_df = animals[animals.weight > 100].sort_values(
        by="weight", ascending=False)[["name"]]

    return new_df
