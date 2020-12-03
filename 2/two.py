import numpy as np


data = np.loadtxt('input.txt', str)

num, num_new = 0, 0
for line in data:
    lower, upper = map(int, line[0].split('-'))
    letter, password = line[1][0], line[2]
    if lower <= password.count(letter) <= upper:
        num += 1
    if (password[lower-1] == letter) != (password[upper-1] == letter):
        num_new += 1

print(f'{num}, new policy: {num_new}')
