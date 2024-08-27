import pandas as pd


def ohe_process(data: pd.DataFrame) -> pd.DataFrame:
    try:
        print("===== Start One Hot Encoding Process \n")
        CHECK_COLS = ["job", "marital", "education", "contact", "poutcome"]

        data = pd.get_dummies(data, columns = CHECK_COLS)
        
        print("===== Finished One Hot Encoding Process =====")
        
        return data
    
    except Exception as e:
        print("===== Failed One Hot Encoding Process =====")
        raise Exception(e)
