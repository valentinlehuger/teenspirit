import pandas as pd
import numpy as np
import json
from scipy.stats import entropy


path = '/home/romain/Documents/BitBucket/DataForGood/teenspirit/teenspirit/'
json_data=open(path+"dataset.json").read()
data = json.loads(json_data)

cont = True
i = 0
while cont:
    print(data[i])
    var = input('Continue ? y/n \n')
    if var.lower()=='y':
        cont = True
        i+=1
    else:
        cont = False

def movingaverage(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    ma = np.convolve(interval, window, 'full')
    ma = ma[:len(interval)]
    ma[0] = interval[0]
    return ma

def timeSerieFeatures(x,M):
    mn = np.mean(x)
    std = np.std(x)
    ent = entropy(x)
    mean_momentum = np.mean(x-movingaverage(x,M))
    return mn, std, ent, mean_momentum