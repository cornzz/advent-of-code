import numpy as np


data = np.loadtxt('input.txt', str)
seats = [['x' for col in range(8)] for row in range(128)]

highest = 0

for line in data:
    rows = range(128)
    cols = range(8)
    for char in line:
        half_rows = len(rows) // 2
        half_cols = len(cols) // 2
        if char == 'F':
            rows = rows[:half_rows]
        elif char == 'B':
            rows = rows[half_rows:]
        elif char == 'L':
            cols = cols[:half_cols]
        elif char == 'R':
            cols = cols[half_cols:]
    seats[rows[0]][cols[0]] = 'o'
    seat_id = rows[0] * 8 + cols[0]
    if seat_id > highest:
        highest = seat_id

skipped = False
my_seat_id = None
for row in range(len(seats)):
    if my_seat_id:
        break
    for col in range(8):
        if not skipped and seats[row][col] == 'o':
            skipped = True
        if skipped and seats[row][col] == 'x':
            my_seat_id = row * 8 + col

print(f'Part one: {highest}, Part two: {my_seat_id}')
