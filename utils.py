import string, random
import pandas as pd
import numpy as np
import time, os



def save_df(file, df):
    if file.endswith('.csv'):
        return df.to_csv(file, index=False)
    else:
        return df.to_excel(file, index=False)


def read_df(file):
    if file.endswith('.csv'):
        try:
            return pd.read_csv(file, index_col=None)
        except pd.errors.EmptyDataError:
            return pd.DataFrame()
    else:
        return pd.read_excel(file, index_col=None)