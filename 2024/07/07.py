from itertools import product

X = [l.strip() for l in open("input.txt")]

def check(res, nums, operations):
	for ops in product(operations, repeat=len(nums) - 1):
		cur = nums[0]
		for op, num in zip(ops, nums[1:]):
			cur = int(f"{cur}{num}") if op == "||" else eval(f"{cur}{op}{num}")
		if cur == res:
			return res
	return 0

p1, p2 = 0, 0
for line in X:
	res, *nums = [int(x) for x in line.replace(":", "").split()]
	p1 += check(res, nums, ["+", "*"])
	p2 += check(res, nums, ["+", "*", "||"])

print(p1)
print(p2)
