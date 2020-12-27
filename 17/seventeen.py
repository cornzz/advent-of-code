from fileinput import input
from itertools import product


def boot(p2, d):
    active = set()
    sz = len(d)

    for x, row in enumerate(d):
        for y, col in enumerate(row):
            if col == '#':
                active.add((x, y, 0, 0))

    for it in range(6):
        new_active = set()
        w_range = range(-1-it, 2+it) if p2 else [0]
        for x in range(-1-it, sz+1+it):
            for y in range(-1-it, sz+1+it):
                for z in range(-1-it, 2+it):
                    for w in w_range:
                        num = 0
                        for dx, dy, dz, dw in product([-1, 0, 1], repeat=4):
                            if any([dx, dy, dz, dw]) and (x+dx, y+dy, z+dz, w+dw) in active:
                                num += 1
                        if ((x, y, z, w) in active and num in [2, 3]) or ((x, y, z, w) not in active and num == 3):
                            new_active.add((x, y, z, w))
        active = new_active

    return len(active)


data = [line.strip() for line in input('input.txt')]

print(f'Part one: {boot(False, data)}, Part two: {boot(True, data)}')
