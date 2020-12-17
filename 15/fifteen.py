import time
from collections import defaultdict


def play(d, n):
    last_spoken = defaultdict(list)
    for i, num in enumerate(d):
        last_spoken[num].append(i + 1)

    i = len(data) + 1
    last_num = data[-1]
    while i <= n:
        x_last = last_spoken[last_num]
        new_num = str(x_last[1] - x_last[0]) if len(x_last) > 1 else '0'

        x_new = last_spoken[new_num]
        last_spoken[new_num] = [x_new[-1], i] if len(x_new) > 0 else [i]

        last_num = new_num
        i += 1

    return last_num


data = '13,16,0,12,15,1'.split(',')
p1 = play(data, 2020)
time1 = time.time()
p2 = play(data, 30000000)
print(time.time() - time1)
print(f'Part one: {p1}, Part two {p2}')
