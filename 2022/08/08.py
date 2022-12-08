X = [l.strip() for l in open('input.txt')]

x, y = len(X[0]), len(X)
p1 = p2 = 0
for i, row in enumerate(X):
	for j, tree in enumerate(row):
		vn = vs = vw = ve = True
		sn = ss = sw = se = 0
		for k in reversed(range(0, i)):
			sn += 1
			if tree <= X[k][j]:
				vn = False
				break
		for k in range(i + 1, y):
			ss += 1
			if tree <= X[k][j]:
				vs = False
				break
		for k in reversed(range(0, j)):
			sw += 1
			if tree <= X[i][k]:
				vw = False
				break
		for k in range(j + 1, x):
			se += 1
			if tree <= X[i][k]:
				ve = False
				break
		if vn or vs or ve or vw: p1 += 1
		score = sn * ss * sw * se
		p2 = max(p2, score)
print(p1)
print(p2)
