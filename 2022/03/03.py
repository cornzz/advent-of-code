X = [l.strip() for l in open('input.txt')]

score = lambda x: (ord(x) - 96) if x.islower() else (ord(x) - 38)
p1 = 0
for rs in X:
	left, right = rs[:len(rs) // 2], rs[len(rs) // 2:]
	common = list(set(left).intersection(right))[0]
	p1 += score(common)
print(p1)

p2 = 0
rs = iter(X)
for a, b, c in zip(rs, rs, rs):
	common = list(set(a).intersection(b).intersection(c))[0]
	p2 += score(common)
print(p2)
