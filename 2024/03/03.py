import re

X = "".join([l.strip() for l in open('input.txt')])

def calc(memory):
	matches = re.findall(r"mul\((\d+),(\d+)\)", memory)
	return sum(int(a) * int(b) for a, b in matches)

p1 = calc(X)
print(p1)

X = "".join(re.findall(r"(?:do\(\)|^).*?(?:don't\(\)|$)", X))
p2 = calc(X)
print(p2)
