import random
import numpy as np
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import tools

def hist_comparison(data1, data2, bins, range):
    plt.hist(data1, range = range, color = 'red', bins = bins, alpha = 0.5, weights=np.ones_like(data1) / np.size(data1))
    plt.hist(data2, range = range, color = 'blue', bins = bins, alpha = 0.5, weights=np.ones_like(data2) / np.size(data2))

def gen_samp_dist(data, number, size):
    """Generate a sampling distribution of the parameter."""
    samp_dist = []
    i = 0
    while i < number:
        sample = random.sample(data, k = size)
        mean = np.mean(sample)
        samp_dist.append(mean)
        i += 1
    return samp_dist
