num = 0

with open('input.txt') as f:
    data = f.read().strip().split('\n\n')

    for block in data:
        block = block.split('\n')
        d = []
        for i in range(len(block)):
            d.append(set())
            for c in block[i]:
                d[i].add(c)
        inter = set.intersection(*d)
        num += len(inter)

print(num)
