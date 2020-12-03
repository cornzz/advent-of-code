import numpy as np


def find(d):
    for i in np.arange(len(d)):
        for j in np.arange(i, len(d)):
            if d[i] + d[j] == 2020:
                return d[i] * d[j]


data = np.loadtxt('input.txt', int)
print(find(data))
