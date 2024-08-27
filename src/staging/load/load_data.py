import pandas as pd
from src.utils.helper import init_engine, logging_process
import logging

logging_process()


def load_to_staging(data: pd.DataFrame, table_name: str) -> None:
    try:
        stg_engine = init_engine(engine_name = "staging")
        
        logging.info("===== Start Load to Staging Database =====")
        
        data = data.copy()
        
        data.to_sql(name = table_name,
                    con = stg_engine,
                    if_exists = "replace",
                    index = False)
        
        logging.info("===== Finish Load to Staging Database =====")
    
    except Exception as e:
        logging.error("===== Failed Load to Staging Database =====")
        raise Exception(e)

    finally:
        stg_engine.dispose()
