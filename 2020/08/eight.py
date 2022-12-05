def run(instructions):
    acc, i = 0, 0
    seen_inst = []
    while i < len(instructions):
        if i in seen_inst:
            return acc, True
        seen_inst.append(i)
        inst, const = instructions[i]
        const = int(const)
        if inst == 'acc':
            acc += const
        elif inst == 'jmp':
            i += const
            continue
        i += 1

    return acc, False


def fix(instructions):
    for i, inst in enumerate(instructions):
        if inst[0] == 'acc':
            continue
        d = instructions.copy()
        d[i] = ['nop', inst[1]] if inst[0] == 'jmp' else ['jmp', inst[1]]
        acc, loop = run(d)
        if not loop:
            return acc


with open('input.txt') as f:
    data = f.read().splitlines()
    data = [x.split(' ') for x in data]

    p1 = run(data)
    p2 = fix(data)

    print(f'Part one: {p1[0]}, Part two: {p2}')
