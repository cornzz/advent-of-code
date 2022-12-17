import re
import math

X = [l.strip() for l in open('input.txt')]

def get_monkeys():
	# 0: items, 1: operation, 2-4: condition, targets, 5: inspections
	monkeys = []
	for i in range(0, len(X), 7):
		monkey = X[i+1:i+6]
		monkey[0] = list(map(int, monkey[0].split(': ')[1].split(', ')))
		monkey[1] = monkey[1].split('= ')[1]
		assert re.match(r'old [-+*\/] (old|\d+)', monkey[1])
		for j in [2, 3, 4]: monkey[j] = int(monkey[j].split()[-1])
		monkeys.append([*monkey, 0])
	return monkeys

def play(rounds, p2=False):
	monkeys = get_monkeys()
	mod = math.lcm(*[m[2] for m in monkeys])
	for _ in range(rounds):
		for m in monkeys:
			c, t, f = m[2:5]
			for old in m[0]:
				old = eval(m[1]) // (3 if not p2 else 1)
				monkeys[t if not old % c else f][0].append(old % mod)
				m[5] += 1
			m[0] = []
	a, b = sorted([m[-1] for m in monkeys])[-2:]
	return a * b

print(play(20))
print(play(10000, True))
