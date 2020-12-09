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


with open('input.txt') as f:
    data = f.read().splitlines()
    data = [x.split(' ') for x in data]

    p1 = run(data)

    to_change = [i for i in range(len(data)) if data[i][0] == 'jmp' or data[i][0] == 'nop']
    for i in to_change:
        d = data.copy()
        d[i] = ['nop', d[i][1]] if d[i][0] == 'jmp' else ['jmp', d[i][1]]
        accu, loop = run(d)
        if not loop:
            break

    print(f'Part one: {p1[0]}, Part two: {accu}')
