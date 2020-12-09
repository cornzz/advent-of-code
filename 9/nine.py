from itertools import combinations

with open('input.txt') as f:
    data = f.read().splitlines()
    data = list(map(int, data))

    pre = 25
    p1 = None
    for i in range(pre, len(data)):
        poss = [x + y for x, y in combinations(data[i - pre:i], 2)]
        if data[i] not in poss:
            p1 = data[i]
            break

    p2 = None
    for j in range(i):
        for k in range(j+2, i):
            set_ = data[j:k]
            if sum(set_) == p1:
                p2 = min(set_) + max(set_)
                break

    print(f'Part one: {p1}, Part two: {p2}')
