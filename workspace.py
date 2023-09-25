import random
import numpy as np
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import tools
import analysis

transit = tools.data_from_csv('m=transit;d=transit;mass=m-r.csv')
rv = tools.data_from_csv('m=rv;d=rv;mass=msini.csv')
trv = tools.data_from_csv('m=transit;d=rv,transit;mass=mass.csv')
