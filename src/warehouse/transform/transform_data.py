from src.warehouse.transform.process.remove_dot import remove_dot_process
from src.warehouse.transform.process.filter_balance import filter_balance_process
from src.warehouse.transform.process.casting_data import casting_data_process
import pandas as pd


def transform_process(data: pd.DataFrame) -> pd.DataFrame:
    try:
        print("===== Start Transform Data ===== \n")

        # removing dot
        data = remove_dot_process(data = data)
        
        # filter balance
        data = filter_balance_process(data = data)
        
        # casting data type
        data = casting_data_process(data = data)
        
        print("===== Finish Transform Data =====")
        
        return data

    except Exception as e:
        print("===== Failed Transform Data =====")
        raise Exception(e)
