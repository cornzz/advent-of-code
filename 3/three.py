import numpy as np


def count_trees(slope):
    loc = [0, 0]  # [row, pos]
    trees = 0
    while loc[0] < len(data):
        if data[loc[0]][loc[1]] == '#':
            trees += 1
        loc = [loc[0] + slope[1], (loc[1] + slope[0]) % 31]
    return trees


data = np.loadtxt('input.txt', str, comments=None)

print('Part one:', count_trees([3, 1]))

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
print('Part two:', np.prod([count_trees(s) for s in slopes], dtype=np.uint))
