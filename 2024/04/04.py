import re

X = [l.strip() for l in open("input.txt")]

def match_pattern(matrix, pattern, width):
	matches = 0
	for i in range(len(matrix) - width + 1):
		for j in range(len(matrix[i]) - width + 1):
			line = "".join(matrix[i + d][j:j + width] for d in range(width))
			matches += bool(re.match(pattern, line))
	return matches

p1, p2 = 0, 0
for rotation in range(4):
	p1 += sum(line.count("XMAS") for line in X)
	p1 += match_pattern(X, r"X.{4}M.{4}A.{4}S", 4)
	p2 += match_pattern(X, r"M.M.A.S.S", 3)

	X = ["".join(line[::-1]) for line in zip(*X)]

print(p1)
print(p2)

