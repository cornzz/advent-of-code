import re

X = [l.strip() for l in open('input.txt')]
p1 = p2 = 0

nums = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }
nums_re = '|'.join(nums.keys())

for line in X:
	matches = re.findall(r"\d", line)
	first, last = matches[0], matches[-1]
	p1 += int(first + last)

	matches = re.findall(fr"(?=(\d|{nums_re}))", line)
	first, last = matches[0], matches[-1] 
	first = nums[first] if first in nums else first
	last = nums[last] if last in nums else last
	p2 += int(first + last) 

print(p1)
print(p2)
