import numpy as np
import pandas
from pathlib import Path

def data_from_csv(name):
    '''Import a csv file from the data folder'''
    folder = Path("./data/")
    file = folder / name
    data = np.array(pandas.read_csv(file))
    return data
