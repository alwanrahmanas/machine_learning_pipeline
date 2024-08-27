import pandas as pd


def filter_balance_process(data: pd.DataFrame) -> pd.DataFrame:
        
    data = data[data["balance"].astype(int) >= 0]
    
    return data
