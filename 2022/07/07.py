X = [l.strip() for l in open('input.txt')]

class Node:
	def __init__(self, name, sup, size):
		self.name = name
		self.sup = sup
		self.sub = []
		self.size = int(size) if size is not None else size

# Build tree structure
wdir = root = Node('/', None, None)
for cmd in X:
	cmd = cmd.split()
	if cmd[0] == '$' and cmd[1] == 'cd':
		wdir = (
			root 		if cmd[2] == '/' else
			wdir.sup 	if cmd[2] == '..' else
			[d for d in wdir.sub if d.name == cmd[2]][0]
		)
	elif cmd[0] == 'dir':
		wdir.sub.append(Node(cmd[1], wdir, None))
	elif cmd[0] != '$':
		size, name = cmd
		wdir.sub.append(Node(name, wdir, size))

# Calculate dir sizes using recursive DFS
def get_size(d):
	if d.size is None:
		d.size = sum([get_size(subd) for subd in d.sub])
	return d.size
get_size(root)

# Solve problems using iterative DFS
p1 = 0
p2 = float('inf')
to_free = root.size - (70000000 - 30000000)
queue = [root]
while len(queue):
	curr = queue.pop()
	queue += [node for node in curr.sub if node.sub]
	if curr.size <= 100000:
		p1 += curr.size
	if curr.size >= to_free and curr.size < p2:
		p2 = curr.size
print(p1)
print(p2)

