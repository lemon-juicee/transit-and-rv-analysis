import numpy as np
import pandas
from pathlib import Path
from scipy import stats

def data_from_csv(name):
    '''Import a csv file from the data folder'''
    folder = Path("./data/")
    file = folder / name
    data = np.array(pandas.read_csv(file))
    return data

def outlier_test(data):
    outliers = []
    median = np.median(data)
    iqr = stats.iqr(data)
    lower = np.percentile(data, 25) - (iqr * 1.5)
    upper = np.percentile(data, 75) + (iqr * 1.5)
    for value in data:
        if value < lower or value > upper:
            outliers.append(value)
    return outliers
