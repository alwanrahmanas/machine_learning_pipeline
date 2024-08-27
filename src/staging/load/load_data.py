import pandas as pd
from src.utils.helper import init_engine


def load_to_staging(data: pd.DataFrame, table_name: str) -> None:
    try:
        stg_engine = init_engine(engine_name = "staging")
        
        print("===== Start Load to Staging Database =====")
        
        data = data.copy()
        
        data.to_sql(name = table_name,
                    con = stg_engine,
                    if_exists = "replace",
                    index = False)
        
        print("===== Finish Load to Staging Database =====")
    
    except Exception as e:
        print("===== Failed Load to Staging Database =====")
        raise Exception(e)

    finally:
        stg_engine.dispose()
