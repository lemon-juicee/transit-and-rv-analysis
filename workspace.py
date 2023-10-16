import random
import numpy as np
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import tools
import analysis

transit = []
for planet in tools.data_from_csv('m=transit;d=transit;mass=m-r.csv'):
    transit.append(planet[1])
rv = []
for planet in tools.data_from_csv('m=rv;d=rv;mass=msini.csv'):
    rv.append(planet[1])
trv = [] 
for planet in tools.data_from_csv('m=transit;d=rv,transit;mass=mass.csv'):
    trv.append(planet[1])

p_dist = analysis.t_test_repeated(rv, trv, 50000, 80)
print(np.median(p_dist))
print(stats.ttest_ind(rv, trv, equal_var=False))
analysis.histo(p_dist, 100, (0, 1), 'blue')
plt.show()