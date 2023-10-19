import random
import numpy as np
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import tools
from scipy import stats

def histo(data, bins, range, color='blue'):
    """Create a histogram."""
    plt.hist(data, range = range, color=color, bins = bins, alpha = 0.5, weights=np.ones_like(data) / np.size(data))

def hist_comparison(data1, data2, bins, range):
    """Create a histogram comparing two distributions."""
    #TODO: Implement range functionality
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

def t_test_repeated(data1, data2, number, size):
    """Test a method to obtain p-value distribution."""
    pvalues = []
    i = 0
    while i < number:
        sample1 = random.sample(data1, k = size)
        sample2 = random.sample(data2, k = size)
        stat, pvalue = stats.ttest_ind(sample1, sample2, equal_var=False)
        pvalues.append(pvalue)
        i += 1
    return pvalues

def double_dist(data1, data2, number, size):
    """Create a sampling distribution of the difference between 2 samples."""
    samp_dist = []
    i = 0
    while i < number:
        sample1 = random.sample(data1, k = size)
        sample2 = random.sample(data2, k = size)
        mean = np.mean(sample1) - np.mean(sample2)
        samp_dist.append(mean)
        i += 1
    return samp_dist

def bootstrap_sampdist(smol, larg, number, size):
    samp_dist = []
    i = 0 
    while i < number:
        sample1 = random.choices(smol, k = size)
        sample2 = random.choices(larg, k = size)
        mean = np.mean(sample2) - np.mean(sample1)
        samp_dist.append(mean)
        i += 1
    return samp_dist
