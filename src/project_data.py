import os

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from src.pre_process import (
    CATEGORICAL_COLUMNS,
    DROP_COLUMNS,
    pre_process,
    standardscaler,
)

DATA_DIR = "../etc/data/"


def get_all_files():
    files_dict = {}
    for file_name in os.listdir(DATA_DIR):
        files_dict[file_name] = f"{DATA_DIR}{file_name}"
    return files_dict


def replace(x):
    if "?" in x.values:
        x.replace({"?": np.nan})
    else:
        return x


def read_csv():
    data_files = get_all_files()
    _data_dict = {}
    for file_name, file_path in data_files.items():
        data = pd.read_csv(file_path, skipinitialspace=True)
        categorical_columns = CATEGORICAL_COLUMNS.get(file_name, None)
        columns_to_drop = DROP_COLUMNS.get(file_name, None)
        print("File name", file_name)
        try:
            data, updated_cols = pre_process(
                data=data,
                categorical_columns=categorical_columns,
                columns_to_drop=columns_to_drop,
            )
            data = standardscaler(
                data=data, columns=categorical_columns, updated_cols=updated_cols
            )
            # file_name_without_ext = os.path.splitext(file_name)[0]
            # file_path = DATA_DIR+f"{file_name_without_ext}_1.csv"
            # data.to_csv(file_path, index=False)
            _data_dict[file_name] = data
        except Exception as e:
            print(data[data.values == "?"])

            print(f"Error processing {file_name}: {e}")
    return _data_dict


def split_x_y(data):
    x, y = [], []
    for column_name in data.columns:
        if not column_name[-1].isalpha():
            y.append(column_name)
        else:
            x.append(column_name)
    _x_train, _x_test, _y_train, _y_test = train_test_split(
        data[x], data[y], test_size=0.33, random_state=42
    )
    return _x_train, _x_test, _y_train, _y_test


data_dict = read_csv()
for i in data_dict:
    # x_train, x_test, y_train, y_test = split_x_y(data_dict[i])
    # cluster(x_train, y_train, x_test, y_test)
    # decision_tree(x_train, y_train, x_test, y_test)
    # random_forest(x_train, y_train, x_test, y_test)
    # kmeans_sway(x_train,4,42)
    # recursive_kmeans_sway(data_dict[i], round(len(data_dict[i])**0.5), 10)
    print(i)
