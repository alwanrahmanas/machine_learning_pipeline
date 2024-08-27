from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

from oauth2client.service_account import ServiceAccountCredentials
import gspread
import logging


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_WH_BANK = os.getenv("DB_WH_BANK")
DB_STG_BANK = os.getenv("DB_STG_BANK")

CRED_PATH = os.getenv("CRED_PATH")


def init_engine(engine_name: str):
    try:
        if engine_name.lower() == "staging":
            conn_stg = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5436/{DB_STG_BANK}")
            
            return conn_stg
        
        elif engine_name.lower() == "warehouse":
            conn_wh = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5437/{DB_WH_BANK}")
            
            return conn_wh
        
        else:
            raise Exception("Unknown engine name!")
        
    except Exception as e:
        raise Exception(e)


def auth_gspread():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CRED_PATH, scope)

    gc = gspread.authorize(credentials)

    return gc


def logging_process():
    # Configure logging
    logging.basicConfig(filename = "log/info_process.log",
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
