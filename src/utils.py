import numpy as np
import pandas as pd
from sklearn import preprocessing


def encode_datetime(data: pd.DataFrame, col: str, max_val: int)-> pd.DataFrame:
    data[col + "_sin"] = np.sin(2 * np.pi * data[col] / max_val)
    data[col + "_cos"] = np.cos(2 * np.pi * data[col] / max_val)
    return data


def encode_label(data: pd.DataFrame, col: str) -> pd.DataFrame:
    le = preprocessing.LabelEncoder()
    le.fit(data[col])
    col_category = col + "_category"
    data[col_category] = le.transform(data[col]) + 1
    return data
