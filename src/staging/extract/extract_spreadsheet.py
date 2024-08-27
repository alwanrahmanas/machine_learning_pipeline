import pandas as pd
import os
from dotenv import load_dotenv
from src.utils.helper import auth_gspread, logging_process
import logging

load_dotenv()
logging_process()

GS_KEY = os.getenv("GS_KEY")


def extract_spreadsheet_process(worksheet_name: str) -> pd.DataFrame:
    try:
        logging.info("===== Start Extracting Spreadsheet data =====")
        # init gspread engine
        gc = auth_gspread()
        
        # init spreadsheet by key
        sheet_result = gc.open_by_key(GS_KEY)
        
        # read spreadsheet data
        worksheet_result = sheet_result.worksheet(worksheet_name)

        # convert it to dataframe
        df_result = pd.DataFrame(worksheet_result.get_all_values())
        
        # set first rows as headers columns
        df_result.columns = df_result.iloc[0]
        
        # get all the rest of the values
        df_result = df_result[1:].copy()
        
        return df_result
        
        logging.info("===== Finish Extracting Spreadsheet data =====")
        
    except Exception as e:
        logging.error("===== Failed to Extract Spreadsheet =====")
        raise Exception(e)
