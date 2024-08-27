from typing import Tuple
from sklearn.model_selection import train_test_split
import pandas as pd
from src.utils.helper import logging_process
import logging

logging_process()


def splitting_process(
    data: pd.DataFrame, target_col: str, test_size: float
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Function that will split the train and test into 80:20 proportion

    Parameters
    ----------
    data (pd.DataFrame): data telco that split into training and testing

    Returns
    -------
    X_train (pd.DataFrame): features data for training data
    X_test (pd.DataFrame): features data for test data
    y_train (pd.Series): target for training data
    y_test (pd.Series): target for test data
    """
    try:
        # determine the features and the target
        X = data.drop([target_col], axis=1)
        y = data[target_col]

        logging.info("===== Start Splitting Data =====")

        # before split the data, we check the data shape for features and target
        logging.info(f"Features Shape: {X.shape}")
        logging.info(f"Target Shape: {y.shape}")

        SEED = 42

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size = test_size, random_state = SEED
        )

        # validate the shape for train and test data

        logging.info(f"Train Features Shape: {X_train.shape}")
        logging.info(f"Test Features Shape: {X_test.shape}")
        logging.info(f"Train Target Shape: {y_train.shape}")
        logging.info(f"Test Target Shape: {y_test.shape}")

        logging.info("===== Finished splitting data =====")

        return X_train, X_test, y_train, y_test

    except Exception as e:
        logging.error("===== Failed to Splitting data =====")
        raise Exception(e)
