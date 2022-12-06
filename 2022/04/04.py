X = [l.strip() for l in open('input.txt')]

p1 = p2 = 0
for pair in X:
	s1, e1, s2, e2 = [int(x) for y in pair.split(',') for x in y.split('-')]
	one, two = set(range(s1, e1 + 1)), set(range(s2, e2 + 1))
	if one.issubset(two) or two.issubset(one): p1 += 1
	if one.intersection(two): p2 += 1
print(p1)
print(p2)
