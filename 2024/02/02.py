X = [l.strip() for l in open('input.txt')]

def is_safe(levels):
	diffs = [a - b for a, b in zip(levels[:-1], levels[1:])]
	return all(-3 <= d < 0 for d in diffs) or all(0 < d <= 3 for d in diffs)

p1, p2 = 0, 0
for line in X:
	levels = [int(n) for n in line.split()]
	p1 += is_safe(levels)
	levels_tol = [levels[:i] + (levels[i + 1:] if i + 1 < len(levels) else []) for i in range(len(levels))]
	p2 += any(is_safe(l) for l in [levels] + levels_tol)

print(p1)
print(p2)


