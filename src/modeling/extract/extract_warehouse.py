import pandas as pd
from src.utils.helper import init_engine


def extract_warehouse_process(table_name: str) -> pd.DataFrame:
    try:
        wh_engine = init_engine(engine_name = "warehouse")
        
        print("===== Start Extracting data from Warehouse =====")
        
        # extract data
        df_data = pd.read_sql(sql = f"select * from {table_name}",
                              con = wh_engine)
                
        print("===== Finish Extracting data from Warehouse =====")

        return df_data
    
    except Exception as e:
        print("===== Failed Extracting data from Warehouse =====")
        
        raise Exception(e)
    
    finally:
        wh_engine.dispose()
