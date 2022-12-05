X = [l.strip() for l in open('input.txt')]

p1 = 0
shapes = {'X': 1, 'Y': 2, 'Z': 3}
win = ['C X', 'B Z', 'A Y']
lose = ['A Z', 'C Y', 'B X']
for round in X:
	p1 += shapes[round[-1]] + (0 if round in lose else 6 if round in win else 3)
print(p1)

p2 = 0
outcome = {'X': 0, 'Y': 3, 'Z': 6}
for round in X:
	target = win if round[-1] == 'Z' else lose if round[-1] == 'X' else ['A X', 'B Y', 'C Z']
	move = next(x for x in target if x.startswith(round[0]))
	p2 += outcome[round[-1]] + shapes[move[-1]]
print(p2)
