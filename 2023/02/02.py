import re
from math import prod

X = [l.strip() for l in open('input.txt')]

config = { 'red': 12, 'green': 13, 'blue': 14 }
p1 = p2 = 0

for line in X:
	game, rounds = line.split(': ')
	possible = True
	minimum = { 'red': 0, 'green': 0, 'blue': 0 }

	for r in re.split(', |; ', rounds):
		n, color = r.split(' ')
		if config[color] < int(n):
			possible = False
		if minimum[color] < int(n):
			minimum[color] = int(n)
	if possible:
		p1 += int(game[5:])
	p2 += prod(minimum.values())

print(p1)
print(p2)
