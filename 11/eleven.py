from fileinput import input
from copy import deepcopy
from itertools import product


def occ_adj_seats(r, c, d, p2=False):
    occ = 0
    direction = [[x, y] for x, y in product([-1, 0, 1], [-1, 0, 1]) if not (x == 0 and y == 0)]
    for dr, dc in direction:
        rr = r + dr
        cc = c + dc
        if p2:
            while 0 <= rr < R and 0 <= cc < C and d[rr][cc] == '.':
                rr = rr + dr
                cc = cc + dc
        if 0 <= rr < R and 0 <= cc < C and d[rr][cc] == '#':
            occ += 1

    return occ


def iterate(grid, p2=False):
    grid_tmp = []
    while grid != grid_tmp:
        grid_tmp = deepcopy(grid)
        for row in range(R):
            for col in range(C):
                occ = occ_adj_seats(row, col, grid_tmp, p2)
                if grid[row][col] == 'L' and occ == 0:
                    grid[row][col] = '#'
                elif grid[row][col] == '#' and occ >= (4 if not p2 else 5):
                    grid[row][col] = 'L'

    return sum(row.count('#') for row in grid)


data = [list(line.strip()) for line in input('input.txt')]
R = len(data)
C = len(data[0])

res_p1 = iterate(deepcopy(data))
res_p2 = iterate(deepcopy(data), p2=True)
print(f'Part one: {res_p1}, Part two: {res_p2}')
