import re

X = open("input.txt").read().strip().split(",")

p1, p2 = 0, 0

for r in X:
    a, b = r.split('-')
    for i in range(int(a), int(b) + 1):
        i = str(i)
        m = len(i) // 2
        if i[:m] == i[m:]:
            p1 += int(i)
        for j in range(1, m + 1):
            if re.match(rf"^(.{{{j}}})\1*$", i):
                p2 += int(i)
                break
   
print(p1)
print(p2)
