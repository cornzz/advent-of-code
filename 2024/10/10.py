X = [list(map(int, l.strip())) for l in open("input.txt")]

trailheads = [(i, j) for i in range(len(X)) for j in range(len(X[0])) if X[i][j] == 0]
D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def follow(pos, ends):
	i, j = pos
	cur = X[i][j]
	if cur == 9:
		ends.append(pos)
	for di, dj in D:
		i_n, j_n = (i + di, j + dj)
		if 0 <= i_n < len(X) and 0 <= j_n < len(X[0]) and X[i_n][j_n] == cur + 1:
			follow((i_n, j_n), ends)
	return ends

trailends = [follow((i, j), []) for i, j in trailheads]
p1 = sum([len(set(ends)) for ends in trailends])
p2 = sum([len(ends) for ends in trailends])
print(p1)
print(p2)

