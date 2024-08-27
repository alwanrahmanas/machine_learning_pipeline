import pandas as pd


def casting_data_process(data: pd.DataFrame) -> pd.DataFrame:

    COLS_TO_CAST = {
        "age": "int",
        "balance": "float",
        "day": "int",
        "campaign": "int",
        "pdays": "int",
        "previous": "int",
        "duration": "int"
    }

    data = data.astype(COLS_TO_CAST)
    
    return data
