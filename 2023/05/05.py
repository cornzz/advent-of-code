import re

X = [l.strip() for l in open('input.txt')]

seeds = None
maps = []
for line in X:
	nums = list(map(int, re.findall(r'\d+', line)))
	if line.startswith('seeds:'):
		seeds = nums
	elif nums:
		maps[-1].append(nums)
	elif not line:
		maps.append([])

p1 = [*seeds]
for submaps in maps:
	for i, seed in enumerate(p1):
		for dst, src, rng in submaps:
			if src <= seed < src + rng:
				p1[i] = seed + dst - src
				break
print(min(p1))

p2 = []
for seed, range_ in zip(seeds[::2], seeds[1::2]):
	ranges_to_map = [(seed, seed + range_)]
	for submaps in maps:
		mapped = []
		for dst, src, rng in submaps:
			diff = dst - src
			map_start, map_end = src, src + rng
			temp = [] # not yet mapped ranges
			for start, end in ranges_to_map:
				temp_start = max(start, map_start)
				temp_end = min(end, map_end)
				if temp_start < temp_end:
					# ranges overlap
					mapped.append((temp_start + diff, temp_end + diff))
					if start < map_start:
						# left side leftover
						temp.append((start, map_start))
					if map_end < end:
						# right side leftover
						temp.append((map_end, end))
				else:
					# no overlap
					temp.append((start, end))
			ranges_to_map = [*temp]
		ranges_to_map += mapped
	p2.extend(ranges_to_map)
print(min(p2)[0])

