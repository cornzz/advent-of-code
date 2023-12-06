import math

X = [l.strip() for l in open('input.txt')]

times = X[0].split(':')[1].split()
distances = X[1].split(':')[1].split()

# Brute force part one:
p1 = 1
for time, distance in zip(times, distances):
	time, distance = int(time), int(distance)
	wins = 0
	for x in range(distance):
		if x*(time-x) > distance:
			wins += 1
	p1 *= wins
print(p1)

# Solve reduced quadratic eq: x**2 - time*x + distance = 0
# -> p = -time, q = distance

p, q = -int(''.join(times)), int(''.join(distances))
a = -p / 2
b = math.sqrt(a**2 - q)
min_, max_ = a - b, a + b
p2 = math.floor(max_) + 1 - math.ceil(min_)
print(p2)
