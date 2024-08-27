from src.staging.extract.extract_spreadsheet import extract_spreadsheet_process
from src.staging.load.load_data import load_to_staging
from src.warehouse.extract.extract_staging import extract_staging_process
from src.warehouse.transform.transform_data import transform_process
from src.warehouse.load.load_data import load_to_warehouse
from src.modeling.extract.extract_warehouse import extract_warehouse_process
from src.modeling.preprocessing.preprocessing_data import preprocessing_process
from src.modeling.preprocessing.splitting_data import splitting_process
from src.modeling.decision_tree import modeling_process
import os
from dotenv import load_dotenv

load_dotenv()

WORKSHEET_NAME = os.getenv("WORKSHEET_NAME")
STG_TABLE_NAME = os.getenv("STG_TABLE_NAME")
WH_TABLE_NAME = os.getenv("WH_TABLE_NAME")
TARGET_COL = os.getenv("TARGET_COL")

TEST_SIZE = 0.2


if __name__ == "__main__":
    print("===== Start Data Pipeline =====")
    print("")
    
    # 1. read from spreadsheet
    df_raw = extract_spreadsheet_process(worksheet_name = WORKSHEET_NAME)
    
    # 2. dump to staging
    load_to_staging(data = df_raw, table_name = STG_TABLE_NAME)
    
    # 3. extract staging
    df_stg = extract_staging_process(table_name = STG_TABLE_NAME)
    
    # 4. transform
    df_stg = transform_process(data = df_stg)
    
    # 5. dump to warehouse
    load_to_warehouse(data = df_stg, table_name = WH_TABLE_NAME)
    
    print("===== Finish Data Pipeline =====")
    print("")
    
    print("===== Start ML Pipeline =====")
    print("")
    # 6. extract warehouse
    df_wh = extract_warehouse_process(table_name = WH_TABLE_NAME)
    
    # 7. preprocessing data
    df_wh = preprocessing_process(data = df_wh)
    
    # 8. splitting data
    X_train, X_test, y_train, y_test = splitting_process(data = df_wh,
                                                         target_col = TARGET_COL,
                                                         test_size = TEST_SIZE)
    
    # 9. modeling
    modeling_process(X_train = X_train,
                     X_test = X_test,
                     y_train = y_train,
                     y_test = y_test)
    
    print("===== Finish ML Pipeline =====")
