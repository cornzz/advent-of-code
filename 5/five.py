import numpy as np


def convert(string):
    string = string.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    row, col = int(string[:7], 2), int(string[-3:], 2)
    return row * 8 + col


data = np.loadtxt('input.txt', str)

data = list(map(convert, data))
data.sort()
lower, upper = data[0], data[-1]
my_seat_id = set(range(lower, upper + 1)).difference(data).pop()

print(f'Part one: {data[-1]}, Part two: {my_seat_id}')
