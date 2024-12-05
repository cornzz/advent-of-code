from collections import defaultdict
from functools import cmp_to_key

X = [l.strip() for l in open("input.txt")]

rules = defaultdict(list)
updates = []
for line in X:
	if "|" in line:
		a, b = [int(x) for x in line.split("|")]
		rules[b].append(a)
	elif "," in line:
		updates.append([int(x) for x in line.split(",")])

comes_before = lambda a, b: -1 if a in rules[b] else 1

p1, p2 = 0, 0
for update in updates:
	correct = sorted(update, key=cmp_to_key(comes_before))
	if update == correct:
		p1 += update[len(update) // 2]
	else:
		p2 += correct[len(correct) // 2]

print(p1)
print(p2)
		
