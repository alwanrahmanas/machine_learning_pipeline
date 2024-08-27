import pandas as pd


def mapping_month_process(data: pd.DataFrame) -> pd.DataFrame:
    try:
        print("===== Start Mapping Month ===== \n")
        DICT_MONTH = {
            "jan": 1,
            "feb": 2,
            "mar": 3,
            "apr": 4,
            "may": 5,
            "jun": 6,
            "jul": 7,
            "aug": 8,
            "sep": 9,
            "oct": 10,
            "nov": 11,
            "dec": 12
        }

        data["month"] = data["month"].map(DICT_MONTH)

        print("===== Finish Mapping Month =====")
        
        return data
        
    except Exception as e:
        print("===== Failed Mapping Month =====")
        raise Exception(e)
