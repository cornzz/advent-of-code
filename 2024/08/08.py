from collections import defaultdict
from itertools import combinations

X = [list(l.strip()) for l in open("input.txt")]

H, W = len(X), len(X[0])
antennas = defaultdict(list)
for y, line in enumerate(X):
	for x, c in enumerate(line):
		if c != ".":
			antennas[c].append((y, x))

p1, p2 = set(), set()
for antenna, locations in antennas.items():
	for (y1, x1), (y2, x2) in combinations(locations, 2):
		dy, dx = (y2 - y1, x2 - x1)
		i = 0
		while 0 <= y1 - dy * i < H and 0 <= x1 - dx * i < W:
			if i == 1:
				p1.add((y1 - dy, x1 - dx))
			p2.add((y1 - dy * i, x1 - dx * i))
			i += 1
		i = 0
		while 0 <= y2 + dy * i < H and 0 <= x2 + dx * i < W:
			if i == 1:
				p1.add((y2 + dy, x2 + dx))
			p2.add((y2 + dy * i, x2 + dx * i))
			i += 1

print(len(p1))
print(len(p2))
