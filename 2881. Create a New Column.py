import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:

    # employees["bonus"] = employees["salary"]*2
    employees["bonus"] = employees.apply(lambda x: x["salary"]*2, axis=1)
    # employees.head(10)
    return employees
