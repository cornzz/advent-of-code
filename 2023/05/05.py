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
for map_ in maps:
	for i, seed in enumerate(p1):
		for dst, src, rng in map_:
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
				# no overlap
				# -> no mapping, continue
				if end <= map_start or start >= map_end:
					temp.append((start, end))
				# start .. map_start .. end .. map_end
				# -> map map_start .. end, continue with start .. map_start
				elif start < map_start < end < map_end:
					mapped.append((map_start + diff, end + diff))
					temp.append((start, map_start))
				# map_start .. start .. map_end .. end
				# -> map start .. map_end, continue with map_end .. end
				elif map_start <= start < map_end < end:
					mapped.append((start + diff, map_end + diff))
					temp.append((map_end, end))
				# start .. map_start .. map_end .. end
				# -> map map_start .. map_end, continue with start .. map_start, map_end .. end
				elif start < map_start < map_end <= end:
					mapped.append((map_start + diff, map_end + diff))
					temp.extend([(start, map_start), (map_end, end)])
				# map_start .. start .. end .. map_end
				# -> map start .. end
				elif map_start <= start < end <= map_end:
					mapped.append((start + diff, end + diff))
			ranges_to_map = [*temp]
		ranges_to_map += mapped
	p2.extend(ranges_to_map)
print(min(p2)[0])

