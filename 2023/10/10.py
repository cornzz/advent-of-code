import os

X = [l.strip() for l in open('input.txt')]

pipes = { '|': (1, 0, 1, 0), '-': (0, 1, 0, 1), 'L': (1, 1, 0, 0), 'J': (1, 0, 0, 1), '7': (0, 0, 1, 1), 'F': (0, 1, 1, 0) }
start_dir_y, start_dir_x = 0, 0

def get_start(net):
	for i, line in enumerate(net):
		if 'S' in line:
			return i, line.index('S')

def get_dir(net, cy, cx):
	for i, (dy, dx) in enumerate([(1, 0), (0, -1), (-1, 0), (0, 1)]):
		if not 0 <= cy+dy < len(net) or not 0 <= cx+dx < len(net[0]):
			continue
		pipe = X[cy+dy][cx+dx]
		if pipe != '.' and pipes[pipe][i]:
			return dy, dx

def trace_net(net, p2=False):
	steps = 1
	cy, cx = get_start(net)
	dir_y, dir_x = get_dir(net, cy, cx)
	if p2:
		# Expand grid
		new = []
		for line in net:
			new.append(''.join([f'{x}.' for x in line]))
			new.append('..' * len(line))
		net = new
		cy, cx = cy*2, cx*2
	loop = []
	while True:	
		cy, cx = cy+dir_y, cx+dir_x
		loop.append((cy, cx))
		if net[cy][cx] == 'S':
			break
		match net[cy][cx]:
			case '|':
				assert dir_y and not dir_x
			case '-':
				assert dir_x and not dir_y
			case 'L':
				assert dir_y == 1 or dir_x == -1, f'{dir_y}, {dir_x}'
				dir_y, dir_x = 0 if dir_y == 1 else -1, 1 if dir_y == 1 else 0
			case 'J':
				assert dir_y == 1 or dir_x == 1, f'{dir_y}, {dir_x}'
				dir_y, dir_x = 0 if dir_y == 1 else -1, -1 if dir_y == 1 else 0
			case '7':
				assert dir_y == -1 or dir_x == 1, f'{dir_y}, {dir_x}'
				dir_y, dir_x = 1 if dir_x == 1 else 0, 0 if dir_x == 1 else -1
			case 'F':
				assert dir_y == -1 or dir_x == -1, f'{dir_y}, {dir_x}'
				dir_y, dir_x = 0 if dir_y == -1 else 1, 1 if dir_y == -1 else 0
			case '.':
				if p2:
					net[cy] = net[cy][:cx] + ('|' if dir_y else '-') + net[cy][cx+1:]
		steps += 1
	return steps // 2, net, loop

p1 = trace_net(X)[0]

def flood_fill(net, loop):
	H, W = len(net), len(net[0])
	stack = [(y, x) for x in range(W) for y in (0, H-1) if (y, x) not in loop]
	stack.extend([(y, x) for y in range(H) for x in (0, W-1) if (y, x) not in loop])
	while len(stack):
		y, x = stack.pop(0)
		net[y] = net[y][:x] + '#' + net[y][x+1:]
		for dy in (-1, 0, 1):
			for dx in (-1, 0, 1):
				cy, cx = min(max(0, y+dy), H-1), min(max(0, x+dx), W-1)	
				if net[cy][cx] != '#' and (cy, cx) not in [*stack, *loop]:
					stack.append((cy, cx))
		os.system('clear')
		for line in net:
			print(line)
	return net

steps, X, loop = trace_net(X, True)
X = flood_fill(X, loop)
p2 = len([(y, x) for y in range(0, len(X), 2) for x in range(0, len(X[0]), 2) if X[y][x] != '#' and (y, x) not in loop])

print(p1)
print(p2)
