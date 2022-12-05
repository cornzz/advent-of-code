from functools import lru_cache


@lru_cache(maxsize=None)  # Cache previous calls
def get_paths(i):
    if i == len(adapters) - 1:
        return 1
    num_paths = 0
    for j in range(i+1, min(i+4, len(adapters))):
        if adapters[j] - adapters[i] <= 3:
            num_paths += get_paths(j)

    return num_paths


with open('input.txt') as f:
    adapters = [int(x) for x in f.read().splitlines()]
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()

    diff = [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]
    p1 = diff.count(1) * diff.count(3)

    p2 = get_paths(0)

    print(f'Part one {p1}, Part two: {p2}')
