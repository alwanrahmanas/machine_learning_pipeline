import pandas as pd


def remove_dot_process(data: pd.DataFrame) -> pd.DataFrame:
    data["job"] = data["job"].str.replace(".", "", regex = False)
    
    return data
