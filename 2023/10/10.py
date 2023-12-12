import os
import sys

print_fill = len(sys.argv) > 1
X = [l.strip() for l in open('input.txt')]
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def get_start(net):
	for i, line in enumerate(net):
		if 'S' in line:
			return i, line.index('S')

def get_dir(net, sy, sx):
	H, W = len(net), len(net[0])
	start_pipes = [['|', 'L', 'J'], ['-', 'L', 'F'], ['|', '7', 'F'], ['-', '7', 'F']]
	for (dy, dx), allowed_pipes in zip(dirs, start_pipes):
		if 0 <= sy+dy < H and 0 <= sx+dx < W:
			pipe = X[sy+dy][sx+dx]
			if pipe != '.' and pipe in allowed_pipes:
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
	H, W = len(net), len(net[0])
	loop = [[False for _ in range(W)] for _ in range(H)]
	while True:
		cy, cx = cy+dir_y, cx+dir_x
		loop[cy][cx] = True
		match net[cy][cx]:
			case 'S':
				break
			case 'L':
				dir_y, dir_x = 0 if dir_y == 1 else -1, 1 if dir_y == 1 else 0
			case 'J':
				dir_y, dir_x = 0 if dir_y == 1 else -1, -1 if dir_y == 1 else 0
			case '7':
				dir_y, dir_x = 1 if dir_x == 1 else 0, 0 if dir_x == 1 else -1
			case 'F':
				dir_y, dir_x = 0 if dir_y == -1 else 1, 1 if dir_y == -1 else 0
			case '.':
				if p2: # Fill in missing pipes
					net[cy] = net[cy][:cx] + ('|' if dir_y else '-') + net[cy][cx+1:]
		steps += 1
	return steps // 2 if not p2 else (net, loop)

def flood_fill(net, visited):
	H, W = len(net), len(net[0])
	# Add non-loop edge fields to queue
	queue = [(y, x) for x in range(W) for y in range(H) if (y in (0, H-1) or x in (0, W-1)) and not visited[y][x]]
	while queue:
		y, x = queue.pop(0)
		net[y] = net[y][:x] + '#' + net[y][x+1:]
		visited[y][x] = True
		for dy, dx in dirs:
			cy, cx = y+dy, x+dx
			if 0 <= cy < H and 0 <= cx < W and not visited[cy][cx] and net[cy][cx] != '#' and (cy, cx) not in queue:
				queue.append((cy, cx))
				visited[cy][cx] = True
		if print_fill:
			os.system('clear')
			for line in net:
				print(line)
	return net

p1 = trace_net(X)

X, loop = trace_net(X, True)
X = flood_fill(X, loop)
# Traverse filled grid with stride 2 and count fields inside loop
p2 = len([(y, x) for y in range(0, len(X), 2) for x in range(0, len(X[0]), 2) if X[y][x] != '#' and not loop[y][x]])

print(p1)
print(p2)
