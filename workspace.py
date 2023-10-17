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

transit_sd = analysis.gen_samp_dist(transit, 1000, 30)
rv_sd = analysis.gen_samp_dist(rv, 1000, 30)
trv_sd = analysis.gen_samp_dist(trv, 1000, 30)

'''fix, ax = plt.subplots()'''

"""
transit_hist = analysis.histo(transit, 100, (0, 100), color = 'blue')
ax.set_title("Transit M-R Mass Estimates")

rv_hist_1 = analysis.histo(rv, 100, (0, 9000), color = 'blue')
rv_hist_2 = analysis.histo(rv, 50, (0, 200), color = 'blue')
ax.set_title("RV m*sin(i) Minimum Masses")

trv_hist_1 = analysis.histo(trv, 100, (0, 9000), color = 'blue')
trv_hist_2 = analysis.histo(trv, 100, (0, 500), color = 'blue')
ax.set_title("Transit -> RV Mass Calculations")
"""

'''ax.set_ylabel("Frequency")
ax.set_xlabel("Mass (Earth Masses)")'''

transit_outliers = tools.outlier_test(transit)
rv_outliers = tools.outlier_test(rv)
trv_outliers = tools.outlier_test(trv)

res_transit = [i for i in transit if i not in transit_outliers]
res_rv = [i for i in rv if i not in rv_outliers]
res_trv = [i for i in trv if i not in trv_outliers]

fix, ax = plt.subplots()
ax.set_ylabel("Frequency")
ax.set_xlabel("Mass (Earth Masses)")

ax.set_title("Transit -> RV (Red) vs. Transit -> RV w/o Outliers (Blue)")
transit_comparison = analysis.hist_comparison(trv, res_trv, 50, (0, 500))
plt.show()