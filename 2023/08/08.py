import math 

X = [l.strip() for l in open('input.txt')]

instructions = X[0]
net = {}
start_2 = []

for line in X[2:]:
	node, lr = line.split(' = ')
	net[node] = lr[1:-1].split(', ')
	if node.endswith('A'):
		start_2.append(node)

def walk(current, p2=False):
	steps = 0
	while not p2 and current != 'ZZZ' or not current.endswith('Z'):
		current = net[current][0 if instructions[steps % len(instructions)] == 'L' else 1]
		steps += 1
	return steps

p1 = walk('AAA')
print(p1)

p2 = []
for start in start_2:
	p2.append(walk(start, True))

print(math.lcm(*p2))
	
