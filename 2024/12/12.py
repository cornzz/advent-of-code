X = [l.strip() for l in open("input.txt")]

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_region(i, j, region):
    region.add((i, j))
    adjacent = [(i + di, j + dj) for di, dj in D if 0 <= i + di < len(X) and 0 <= j + dj < len(X[0])]
    for ai, aj in adjacent:
        if X[i][j] == X[ai][aj] and (ai, aj) not in region:
            get_region(ai, aj, region)
    return region

regions = []
for i in range(len(X)):
    for j in range(len(X[0])):
        if not any(((i, j) in region) for region in regions):
            regions.append(get_region(i, j, set()))

p1, p2 = 0, 0
for region in regions:
    fences = []
    for i, j in region:
        adjacent = [(i + di, j + dj) for di, dj in D]
        fences += [a for a in adjacent if a not in region]
    p1 += len(fences) * len(region)

    sides = 0
    seen = set()
    for fi, fj in sorted(set(fences)):
        seen.add((fi, fj))
        for i in range(4):
            (di1, dj1), (di2, dj2), _, (di3, dj3) = D[i:] + D[:i]
            if (
                (fi + di1, fj + dj1) in region
                and ((fi + di2, fj + dj2) not in seen or (fi + di1 + di2, fj + dj1 + dj2) not in region)
                and ((fi + di3, fj + dj3) not in seen or (fi + di1 + di3, fj + dj1 + dj3) not in region)
            ):
                sides += 1
    p2 += sides * len(region)

print(p1)
print(p2)
