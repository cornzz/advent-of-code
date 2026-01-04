X = [l.strip() for l in open("input.txt")]

p1, p2 = 0, 0
n = 50

for l in X:
    d, s = l[0], int(l[1:])
    for _ in range(s):
        n = (n + (-1 if d == "L" else 1)) % 100
        if n == 0:
            p2 += 1
    if n == 0:
        p1 += 1

print(p1)
print(p2)
