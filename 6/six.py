num_any, num_every = 0, 0

with open('input.txt') as f:
    blocks = f.read().strip().split('\n\n')

    for blk in blocks:
        blk = blk.split('\n')
        d = [{c for c in line} for line in blk]
        num_any += len(set.union(*d))
        num_every += len(set.intersection(*d))

print(f'Part one: {num_any}, Part two: {num_every}')
