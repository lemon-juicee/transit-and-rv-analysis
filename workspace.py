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

pvalues = analysis.bootstrap_differences(transit, trv, 100000, 30, 15)
print(pvalues)
print(np.mean(pvalues), np.std(pvalues))
