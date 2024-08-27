import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from src.utils.helper import logging_process
import logging

logging_process()


def modeling_process(
    X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.Series, y_test: pd.Series
) -> None:
    """
    Function for modeling using Decision Tree Classifier

    Parameters
    ----------
    X_train (pd.DataFrame): features data for training data
    X_test (pd.DataFrame): features data for test data
    y_train (pd.Series): target for training data
    y_test (pd.Series): target for test data
    """
    try:
        logging.info("===== Start Modeling Data =====\n")
        # create decision tree object
        dt_clf = DecisionTreeClassifier()

        # train the data
        dt_clf = dt_clf.fit(X_train, y_train)

        y_pred_train = dt_clf.predict(X_train)
        y_pred_test = dt_clf.predict(X_test)

        acc_train = accuracy_score(y_train, y_pred_train)
        acc_test = accuracy_score(y_test, y_pred_test)

        logging.info(f"Decision Tree training accuracy {acc_train}")
        logging.info(f"Decision Tree test accuracy {acc_test}")
        
        logging.info("===== Finish Modeling Data =====")

    except Exception as e:
        logging.error("===== Failed Modeling Data =====")
        raise Exception(e)
