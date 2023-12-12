import sys

input_file = len(sys.argv) > 1 and sys.argv[1] or 'input.txt'
X = [l.strip() for l in open(input_file)]

def get_empty(grid, rows=True):
    # zip(*grid) to get transposed grid
    return [i for i, line in enumerate(grid if rows else zip(*grid)) if len(set(line)) == 1]

def calc_distances(grid, rows, cols, multiplier):
    galaxies = [(i, j) for i, line in enumerate(grid) for j, c in enumerate(line) if c == '#']
    pairs = [(galaxies[i], galaxies[j]) for i in range(len(galaxies)) for j in range(i+1, len(galaxies))]
    distances = []
    for (y0, x0), (y1, x1) in pairs:
        empty = sum([1 for e in rows if y0 < e < y1 or y1 < e < y0] + [1 for e in cols if x0 < e < x1 or x1 < e < x0])
        # Manhattan distance + num. of empty rows between points * expansion multiplier
        distances.append(abs(x1 - x0) + abs(y1 - y0) + empty * (multiplier - 1))
    return sum(distances)

empty_rows = get_empty(X)
empty_cols = get_empty(X, False)
p1 = calc_distances(X, empty_rows, empty_cols, 2)
p2 = calc_distances(X, empty_rows, empty_cols, 1000000)
print(p1)
print(p2)