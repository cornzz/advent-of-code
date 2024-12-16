import re

X = [l.strip() for l in open("input.txt")]
D = 10000000000000

def solve(a_x, a_y, b_x, b_y, x, y):
    a = (b_y*x - b_x*y) // (b_y*a_x - b_x*a_y)
    b = (x - a_x*a) // b_x
    return a*3 + b if x == a*a_x + b*b_x and y == a*a_y + b*b_y else 0

p1, p2 = 0, 0
for line in X:
    if not line:
        continue
    nums = map(int, re.findall(r"X.(\d+), Y.(\d+)", line)[0])
    if "A" in line:
        a_x, a_y = nums
    elif "B" in line:
        b_x, b_y = nums
    else:
        x, y = nums
        p1 += solve(a_x, a_y, b_x, b_y, x, y)
        p2 += solve(a_x, a_y, b_x, b_y, x+D, y+D)

print(p1)
print(p2)
