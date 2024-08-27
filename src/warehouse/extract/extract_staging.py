import pandas as pd
from src.utils.helper import init_engine


def extract_staging_process(table_name: str) -> pd.DataFrame:
    try:
        stg_engine = init_engine(engine_name = "staging")
        
        print("===== Start Extracting data from Staging =====")
        
        # extract data
        df_data = pd.read_sql(sql = f"select * from {table_name}",
                              con = stg_engine)
                
        print("===== Finish Extracting data from Staging =====")

        return df_data
    
    except Exception as e:
        print("===== Failed Extracting data from Staging =====")
        
        raise Exception(e)

    finally:
        stg_engine.dispose()
