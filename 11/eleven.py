from copy import deepcopy
from itertools import product


def occ_adj_seats(r, c, d, p2=False):
    occ = 0
    direction = [[x, y] for x, y in product(range(-1, 2), range(-1, 2)) if not (x == 0 and y == 0)]
    for di in direction:
        m = 1
        while True:
            try:
                if r + di[0]*m < 0 or c + di[1]*m < 0:
                    raise IndexError
                cell = d[r + di[0]*m][c + di[1]*m]
                if cell != '.':
                    if cell == '#':
                        occ += 1
                    break
                m += 1
            except IndexError:
                break
            if not p2:
                break

    return occ


def iterate(grid, p2=False):
    grid_tmp = []
    while grid != grid_tmp:
        grid_tmp = deepcopy(grid)
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                occ_adj = occ_adj_seats(row, col, grid_tmp, p2)
                if grid[row][col] == 'L' and occ_adj == 0:
                    grid[row][col] = '#'
                elif grid[row][col] == '#' and (not p2 and occ_adj >= 4 or occ_adj >= 5):
                    grid[row][col] = 'L'

    return sum(row.count('#') for row in grid)


with open('input.txt') as f:
    data = f.read().splitlines()
    data = list(map(list, data))

    res_p1 = iterate(deepcopy(data))
    res_p2 = iterate(deepcopy(data), p2=True)
    print(f'Part one: {res_p1}, Part two: {res_p2}')
