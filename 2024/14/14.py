import re
import math
from collections import Counter

X = [l.strip() for l in open("input.txt")]
W, H = 101, 103

robots = []
for line in X:
    robot = [int(g) for g in re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)[0]]
    robots.append(robot)

for d_t in range(100000):
    positions = [((p_y + v_y * d_t) % H, (p_x + v_x * d_t) % W) for p_x, p_y, v_x, v_y in robots]
    counts = Counter(positions)
    if d_t == 100:
        quadrants = [0, 0, 0, 0]
        for (y, x), count in counts.items():
            if y == H // 2 or x == W // 2:
                continue
            q = (0 <= y < H // 2) + 2 * (0 <= x < W // 2)
            quadrants[q] += count
        p1 = math.prod(quadrants)
    if max(counts.values()) == 1:
        p2 = d_t
        for y in range(H):
            line = "".join(str(counts[(y, x)]) if (y, x) in counts else "." for x in range(W))
            print(line)
        break

print(p1)
print(p2)
