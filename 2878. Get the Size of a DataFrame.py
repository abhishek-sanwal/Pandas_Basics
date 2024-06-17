import pandas as pd
from typing import List


def getDataframeSize(players: pd.DataFrame) -> List[int]:

    # return [len(players),len(players.iloc[0])]

    return list(players.shape)
    return [players.shape[0], players.shape[1]]
