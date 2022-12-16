X = [l.strip() for l in open('input.txt')]

DIR = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

for length in [2, 10]:
	visited = set()
	R = [[0, 0] for _ in range(length)]
	for move in X:
		D, steps = move.split()
		for _ in range(int(steps)):
			R[0] = [R[0][0] + DIR[D][0], R[0][1] + DIR[D][1]]
			for i in range(0, length - 1):
				dy, dx = R[i][0] - R[i+1][0], R[i][1] - R[i+1][1]
				if abs(dy) == 2 or abs(dx) == 2:
					R[i+1][0] += int(dy / 2) if abs(dy) > 1 else dy
					R[i+1][1] += int(dx / 2) if abs(dx) > 1 else dx
			visited.add(str(R[-1]))
	print(len(visited))
