import numpy as np


with open('input.txt') as f:
    data = f.read().splitlines()
    data = [x.split(' ') for x in data]
    acc, i = 0, 0
    seen_inst = []
    while i not in seen_inst:
        seen_inst.append(i)
        inst, const = data[i]
        const = int(const)
        if inst == 'acc':
            acc += const
        elif inst == 'jmp':
            i += const
            continue
        i += 1

    print(acc)
