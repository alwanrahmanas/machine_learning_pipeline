import pandas as pd
from src.utils.helper import init_engine, logging_process
import logging

logging_process()


def extract_warehouse_process(table_name: str) -> pd.DataFrame:
    try:
        wh_engine = init_engine(engine_name = "warehouse")
        
        logging.info("===== Start Extracting data from Warehouse =====")
        
        # extract data
        df_data = pd.read_sql(sql = f"select * from {table_name}",
                              con = wh_engine)
                
        logging.info("===== Finish Extracting data from Warehouse =====")

        return df_data
    
    except Exception as e:
        logging.error("===== Failed Extracting data from Warehouse =====")
        
        raise Exception(e)
    
    finally:
        wh_engine.dispose()
