from typing import Tuple
from sklearn.model_selection import train_test_split
import pandas as pd


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

        print("===== Start Splitting Data =====")
        print("")

        # before split the data, we check the data shape for features and target
        print(f"Features Shape: {X.shape}")
        print(f"Target Shape: {y.shape}")

        SEED = 42

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size = test_size, random_state = SEED
        )

        # validate the shape for train and test data

        print(f"Train Features Shape: {X_train.shape}")
        print(f"Test Features Shape: {X_test.shape}")
        print(f"Train Target Shape: {y_train.shape}")
        print(f"Test Target Shape: {y_test.shape}")

        print("")
        print("===== Finished splitting data =====")

        return X_train, X_test, y_train, y_test

    except Exception as e:
        print("===== Failed to Splitting data =====")
        raise Exception(e)
