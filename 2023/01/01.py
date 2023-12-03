import re

X = [l.strip() for l in open('input.txt')]
p1 = p2 = 0

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
nums_re = '|'.join(nums)

for line in X:
	matches = re.findall(r"\d", line)
	first, last = matches[0], matches[-1]
	p1 += int(first + last)

	matches = re.findall(fr"(?=(\d|{nums_re}))", line)
	first, last = matches[0], matches[-1] 
	first = str(nums.index(first) + 1) if first in nums else first
	last = str(nums.index(last) + 1) if last in nums else last
	p2 += int(first + last) 

print(p1)
print(p2)
