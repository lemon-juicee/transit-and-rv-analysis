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

transit_sd = analysis.gen_samp_dist(transit, 400, 50)
rv_sd = analysis.gen_samp_dist(rv, 400, 50)
trv_sd = analysis.gen_samp_dist(trv, 400, 50)
