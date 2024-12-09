X = [list(l.strip()) for l in open("input.txt")]

pos = next((i, j) for i in range(len(X)) for j in range(len(X[i])) if X[i][j] == "^")
d = 0
D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def run(X, pos, d, main=True):
	visited, visited_d, obstructions = set([pos]), set([(pos, d)]), set()
	while 0 < pos[0] < len(X) - 1 and 0 < pos[1] < len(X[0]) - 1:
		while True:
			y, x = tuple(x + d for x, d in zip(pos, D[d]))
			if not X[y][x] == "#":
				next_pos = (y, x)
				break
			d = (d + 1) % 4
		if not main and (next_pos, d) in visited_d:
			return True
		visited_d.add((next_pos, d))
		if main and next_pos not in visited | obstructions:
			X_ = [line[:] for line in X]
			X_[y][x] = "#"
			if run(X_, pos, d, False):
				obstructions.add(next_pos)
		visited.add(next_pos)
		pos = next_pos
	return (len(visited), len(obstructions)) if main else False

p1, p2 = run(X, pos, d)
print(p1)
print(p2)
