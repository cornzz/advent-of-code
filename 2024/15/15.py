import copy
import sys
import time
from collections import defaultdict

X = [list(l.strip()) for l in open("input.txt") if l.strip()]
D = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def print_grid(grid):
    for line in grid:
        print("".join(line))
    print("\n")

def get_gps(grid):
    s = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            s += 100 * y + x if grid[y][x] in ["O", "["] else 0
    return s

def move_boxes_p1(y, x, dy, dx):
    y_n, x_n = y + dy, x + dx
    n = G[y_n][x_n]
    if n == "." or n == "O" and move_boxes_p1(y_n, x_n, dy, dx):
        G[y][x] = "."
        G[y_n][x_n] = "O"
        return True
        
def move_boxes_p2(G2, y, x, dy, dx):
    if dx:
        a = G2[y][x]
        y_n, x_n = y + dy, x + dx
        y_n2, x_n2 = y + dy*2, x + dx*2
        n, n2 = G2[y_n][x_n], G2[y_n2][x_n2]
        if n2 == "." or n2 in ["[", "]"] and move_boxes_p2(G2, y_n2, x_n2, dy, dx):
            G2[y][x] = "."
            G2[y_n][x_n] = a
            G2[y_n2][x_n2] = n
            return True
    else:
        a = G2[y][x]
        y_b, x_b = y, x + (1 if a == "[" else -1)
        y_na, x_na = y + dy, x + dx
        y_nb, x_nb = y_b + dy, x_b + dx
        na = G2[y_na][x_na]
        if na == "." or na in ["[", "]"] and move_boxes_p2(G2, y_na, x_na, dy, dx):
            G2[y][x] = "."
            G2[y_na][x_na] = a
            nb = G2[y_nb][x_nb]
            if nb == "." or nb in ["[", "]"] and move_boxes_p2(G2, y_nb, x_nb, dy, dx):
                G2[y_b][x_b] = "."
                G2[y_nb][x_nb] = "[" if a == "]" else "]"
                return True

G, G2 = [], defaultdict(list)
for i, line in enumerate(X):
    if line and line[0] == "#":
        G.append(line)
        for c in line:
            G2[i].extend(["[", "]"] if c == "O" else ["@", "."] if c == "@" else [c] * 2)
        if "@" in line:
            y, x = i, line.index("@")
            y2, x2 = y, x * 2
        continue
    if isinstance(G2, dict):
        G2 = list(G2.values())

    for move in line:
        dy, dx = D[move]

        # part 1
        y_n, x_n = y + dy, x + dx
        n = G[y_n][x_n]
        if n == "." or n == "O" and move_boxes_p1(y_n, x_n, dy, dx):
            G[y][x] = "."
            G[y_n][x_n] = "@"
            y, x = y_n, x_n

        # part 2
        y2_n, x2_n = y2 + dy, x2 + dx
        n2 = G2[y2_n][x2_n]
        if n2 in ["[", "]"]:
            G2_ = copy.deepcopy(G2)
            if (moved := move_boxes_p2(G2_, y2_n, x2_n, dy, dx)):
                G2 = G2_
        if n2 == "." or n2 in ["[", "]"] and moved:
            G2[y2][x2] = "."
            G2[y2_n][x2_n] = "@"
            y2, x2 = y2_n, x2_n
        if '-p' in sys.argv:
            print(f"Move {move}:")
            print_grid(G2)
            time.sleep(0.1)

p1, p2 = get_gps(G), get_gps(G2)
print(p1)
print(p2)
