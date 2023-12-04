X = [l.strip() for l in open('input.txt')]

parse_nums = lambda nums: set(map(int, nums.split()))
p1 = 0
p2 = [1] * len(X) 

for i, line in enumerate(X):
	card, nums = line.split(':')
	winning, have = map(parse_nums, nums.split('|'))
	common = len(have.intersection(winning))
	if common:
		p1 += 2 ** (common - 1)
	for j in range(common):
		p2[i+1+j] += p2[i]

print(p1)
print(sum(p2))
