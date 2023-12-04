import re
import math

X = [l.strip() for l in open('input.txt')]
p1 = p2 = 0
matches = [
	(
		[(m.group(), m.start(), m.end()) for m in re.finditer(r'\d+', line)],
		[m.start() for m in re.finditer(r'\*', line)]
	)
	for line in X
]
W, H = len(X[0]), len(X)

for i, (parts, gears) in enumerate(matches):
	for part in parts:
		n, start, end = part
		start, end = max(0, start - 1), min(W, end + 1) 
		check = X[i][start:end]
		if i > 0:
			check += X[i-1][start:end]
		if i < H - 1:
			check += X[i+1][start:end]
		if re.search(r'[^\.\d]', check):
			p1 += int(n)

	check = [*parts]
	if i > 0:
		check.extend(matches[i-1][0])
	if i < len(X) - 1:
		check.extend(matches[i+1][0])
	for gear in gears:
		adj = [int(n) for n, start, end in check if start - 1 <= gear and end >= gear]
		if len(adj) == 2:
			p2 += math.prod(adj)

print(p1)
print(p2)
