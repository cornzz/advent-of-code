def play(d, n):
    last_spoken = dict()
    for i in range(len(d) - 1):
        last_spoken[d[i]] = i + 1

    i = len(data) + 1
    last_num = data[-1]
    while i <= n:
        x_last = last_spoken.get(last_num, -1)
        new_num = i - 1 - x_last if x_last > 0 else 0

        last_spoken[last_num] = i - 1
        last_num = new_num
        i += 1

    return last_num


data = [int(x) for x in '13,16,0,12,15,1'.split(',')]
p1 = play(data, 2020)
p2 = play(data, 30000000)

print(f'Part one: {p1}, Part two {p2}')
