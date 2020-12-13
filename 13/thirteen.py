import math
from functools import reduce


def chinese_remainder(con):
    s = 0
    prod = reduce(lambda x, y: x*y, [n[1] for n in con])

    for a_i, n_i in con:
        p = prod // n_i
        s += a_i * pow(p, -1, n_i) * p
    return s % prod


with open('input.txt') as f:
    data = f.read().splitlines()

start = int(data[0])
buses = [int(x) for x in data[1].split(',') if x != 'x']

# Get next departure time for each bus, select one closest to start
departures = [math.ceil(start / x) * x for x in buses]
next_dep = min((time, index) for (index, time) in enumerate(departures))
p1 = (next_dep[0] - start) * buses[next_dep[1]]

# Solve task with CRA, for explanation see input.txt
congruences = [(-a, int(n)) for a, n in enumerate(data[1].split(',')) if n != 'x']
p2 = chinese_remainder(congruences)

print(f'Part one: {p1}, Part two: {p2}')
