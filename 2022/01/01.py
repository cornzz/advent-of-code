with open('input.txt') as f:
	inv = [i.split('\n') for i in f.read().split('\n\n')]
	sums = [sum(i) for i in [map(int, j) for j in inv]]
	p1 = max(sums)
	print(p1)
	p2 = sum(sorted(sums)[-3:])
	print(p2)
