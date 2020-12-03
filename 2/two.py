import numpy as np


data = np.loadtxt('input.txt', str)

num = 0
for line in data:
    bounds = line[0].split('-')
    if int(bounds[0]) <= line[2].count(line[1][0]) <= int(bounds[1]):
        num += 1

print(num)
