import re

import pandas as pd
from sklearn.preprocessing import StandardScaler

CATEGORICAL_COLUMNS = {
    "auto93.csv": ["Clndrs", "origin"],
    "auto2.csv": [
        "maker",
        "type",
        "Air_Bags_standard",
        "Drive_train_type",
        "manual_transmission_available",
        "domestic",
    ],
    "china.csv": ["Resource", "DevType"],
    "healthCloseIsses12mths0001-hard.csv": ["criterion"],
    "healthCloseIsses12mths0011-easy.csv": ["criterion"],
    "nasa93dem.csv": [
        "prec",
        "flex",
        "resl",
        "team",
        "pmat",
        "rely",
        "data",
        "cplx",
        "ruse",
        "docu",
        "time",
        "stor",
        "pvol",
        "acap",
        "pcap",
        "pcon",
        "apex",
        "plex",
        "ltex",
        "tool",
        "site",
        "sced",
    ],
    "pom.csv": [
        "Criticality Modifier",
        "InterDependency",
        "Dynamism",
        "Size",
        "Plan",
        "Team Size",
    ],
    "SSM.csv": ["f"],
    "SSN.csv": ["Crf"],
}

DROP_COLUMNS = {
    "china.csv": ["IDX"],
    "nasa93dem.csv": ["idX"],
}


def pre_process(data, categorical_columns=None, columns_to_drop=None):
    updated_cols = {}
    if columns_to_drop:
        data = data.drop(columns_to_drop, axis=1)
    if categorical_columns:
        for col in categorical_columns:
            data[col] = data[col].astype("category")
            # if re.match(r'^\w+$', str(data.iloc[0][col])):
            if isinstance(data.iloc[0][col], str) and (
                data.iloc[0][col].isalpha()
                or re.match(r"^[A-Za-z0-9_]+$", data.iloc[0][col])
            ):
                updated_cols[col] = f"{col}_cat"
                data[f"{col}_cat"] = data[col].cat.codes
                data.drop(col, axis=1, inplace=True)
    data = data.replace("?", None)
    data = data.dropna()
    data = data.drop_duplicates()
    return data, updated_cols


def standardscaler(data, columns=None, updated_cols=None):
    scaler = StandardScaler()
    for cols in updated_cols:
        columns[columns.index(cols)] = updated_cols[cols]
    if not columns:
        scaler.fit(data)
        return pd.DataFrame(scaler.transform(data), columns=data.columns)
    else:
        categorical_df = data[columns]
        scalable_cols = [col for col in data.columns if col not in columns]
        scaler.fit(data[scalable_cols])
        scaled_df = pd.DataFrame(
            scaler.transform(data[scalable_cols]), columns=scalable_cols
        )
        return pd.concat([categorical_df, scaled_df], axis=1, join="inner")
