CMDS = [l.strip() for l in open('input.txt')]

X, C = 1, 0
check = [20, 60, 100, 140, 180, 220]
p1 = 0
p2 = ''

def inc_cycle():
	global C, p1, p2
	C += 1
	if C in check: p1 += C * X
	p2 += '#' if abs(X - (C - 1) % 40) <= 1 else '.'

for cmd in CMDS:
	inc_cycle()
	if cmd != 'noop':
		inc_cycle()
		X += int(cmd.split()[1])
print(p1)
print('\n'.join([p2[c-20:c+20] for c in check]))
