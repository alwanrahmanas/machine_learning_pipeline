import pandas as pd
from src.utils.helper import init_engine, logging_process
import logging

logging_process()


def load_to_warehouse(data: pd.DataFrame, table_name: str) -> None:
    try:
        wh_engine = init_engine(engine_name = "warehouse")
        
        logging.info("===== Start Load to Warehouse Database =====")
        
        data = data.copy()
        
        data.to_sql(name = table_name,
                    con = wh_engine,
                    if_exists = "replace",
                    index = False)
        
        logging.info("===== Finish Load to Warehouse Database =====")
    
    except Exception as e:
        logging.error("===== Failed Load to Warehouse Database =====")
        raise Exception(e)

    finally:
        wh_engine.dispose()
