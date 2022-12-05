from fileinput import input
from itertools import product


def boot(p2, d):
    active = set()

    for x, row in enumerate(d):
        for y, col in enumerate(row):
            if col == '#':
                active.add((x, y, 0, 0))

    offsets = [x for x in product([-1, 0, 1], repeat=4) if x != (0, 0, 0, 0)]
    for it in range(6):
        new_active, check = set(), set()
        for x, y, z, w in active:
            for dx, dy, dz, dw in offsets:
                if p2 or w+dw == 0:
                    check.add((x+dx, y+dy, z+dz, w+dw))

        for x, y, z, w in check:
            num = 0
            for dx, dy, dz, dw in offsets:
                if (x+dx, y+dy, z+dz, w+dw) in active:
                    num += 1
            if ((x, y, z, w) in active and num in [2, 3]) or ((x, y, z, w) not in active and num == 3):
                new_active.add((x, y, z, w))
        active = new_active

    return len(active)


data = [line.strip() for line in input('input.txt')]

print(f'Part one: {boot(False, data)}, Part two: {boot(True, data)}')
