X = [l.strip() for l in open('input.txt')]

def get_stacks():
	stacks = [[]] * len(X[0][1::4])
	for row in X:
		if not row.startswith('['): break
		row = [crate.strip() for crate in row[1::4]]
		stacks = [[r, *s] for r, s in zip(row, stacks)]
	return [[c for c in stack if c] for stack in stacks]

stacks1, stacks2 = get_stacks(), get_stacks()
for move in X:
	if not move.startswith('m'): continue
	m, f, t = map(int, move.split()[1::2])

	stacks1[t - 1] += stacks1[f - 1][-m:][::-1]
	stacks1[f - 1] = stacks1[f - 1][:-m]
	stacks2[t - 1] += stacks2[f - 1][-m:]
	stacks2[f - 1] = stacks2[f - 1][:-m]

print(''.join([stack[-1] for stack in stacks1]))
print(''.join([stack[-1] for stack in stacks2]))

