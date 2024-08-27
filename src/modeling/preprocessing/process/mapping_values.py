import pandas as pd


def mapping_values_process(data: pd.DataFrame) -> pd.DataFrame:
    try:
        COLS_TO_MAP = ["default", "housing", "loan", "deposit"]

        VALUES_TO_MAP = {"yes": 1, "no": 0}

        print("===== Start Mapping Values =====")

        for col in COLS_TO_MAP:
            data[col] = data[col].map(VALUES_TO_MAP)

        print("===== Finish Mapping Values =====")
        
        return data
        
    except Exception as e:
        print("===== Failed Mapping Values =====")
        raise Exception(e)
