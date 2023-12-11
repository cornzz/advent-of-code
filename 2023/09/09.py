import re

X = [l.strip() for l in open('input.txt')]

def predict(curr, p2=False):
	succ = [curr[i+1] - curr[i] for i in range(len(curr) - 1)]
	pred = 0 if not any(succ) else predict(succ, p2)
	return curr[0 if p2 else -1] + pred * (-1 if p2 else 1)

p1 = p2 = 0
for line in X:
	nums = list(map(int, line.split()))
	p1 += predict(nums)
	p2 += predict(nums, True)

print(p1)
print(p2)
