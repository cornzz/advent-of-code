from functools import lru_cache

X = [int(x) for x in open("input.txt").read().split()]

@lru_cache(maxsize=None)
def blink(num, d):
	if d == 0:
		return 1
	numlen = len(str(num))
	if num == 0:
		return blink(1, d - 1)
	elif numlen % 2 == 0:
		left, right = int(str(num)[:numlen // 2]), int(str(num)[numlen // 2:])
		return blink(left, d - 1) + blink(right, d - 1)
	else:
		return blink(num * 2024, d - 1)

p1 = sum([blink(num, 25) for num in X])
p2 = sum([blink(num, 75) for num in X])
print(p1)
print(p2)


