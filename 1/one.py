import numpy as np
from itertools import product


# Mapping int() results in faster run times than using the result of loadtxt(file, dtype=int)
data = list(map(int, np.loadtxt('input.txt')))
for x, y in product(data, data):
    if x + y == 2020:
        print('Part one:', x*y)
        break
for x, y, z in product(data, data, data):
    if x + y + z == 2020:
        print('Part two:', x*y*z)
        break
