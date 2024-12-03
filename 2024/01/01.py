from collections import Counter

X = [l.strip() for l in open('input.txt')]

nums = [map(int, line.split()) for line in X]
left, right = [sorted(l) for l in zip(*nums)]

p1 = sum(a - b if a > b else b - a for a, b in zip(left, right))
print(p1)

counts = Counter(right)
p2 = sum(num * counts[num] for num in left)
print(p2)
