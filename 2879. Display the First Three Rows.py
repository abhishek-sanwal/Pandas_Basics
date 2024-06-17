import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:

    return employees.loc[0:2]

    return employees.iloc[:3]

    return employees.head(3)

    return employees[:3]
