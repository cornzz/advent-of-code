import sys
from functools import cache

input_file = len(sys.argv) > 1 and sys.argv[1] or 'input.txt'
X = [l.strip() for l in open(input_file)]

# Idea to use DP from reddit
def get_arrangements(line, req_groups):
    @cache
    def f(char, index, current_group, current_group_length):
        if char == '#':
            current_group_length += 1
            if current_group_length > req_groups[current_group]:
                # Group too long
                return 0
            elif index == len(line) - 1:
                # Last char, return 1 if group complete
                return int(
                    current_group_length == req_groups[current_group] and
                    current_group == len(req_groups) - 1
                )
        elif char == '.' and current_group_length > 0:
            # End of current group
            if current_group_length == req_groups[current_group]:
                # Group complete
                current_group += 1
                current_group_length = 0
                if current_group == len(req_groups):
                    # All groups complete, return 1 if no more springs left
                    return int('#' not in line[index + 1:])
            else:
                # Group too short
                return 0
        if index == len(line) - 1:
            # Last char, groups incomplete
            return 0
        return (
            f('#', index + 1, current_group, current_group_length) +
            f('.', index + 1, current_group, current_group_length)
            if line[index + 1] == '?'
            else f(line[index + 1], index + 1, current_group, current_group_length)
        )

    return f('#', 0, 0, 0) + f('.', 0, 0, 0) if line[0] == '?' else f(line[0], 0, 0, 0)

lines = [[springs, list(map(int, req_groups.split(',')))] for springs, req_groups in [l.split() for l in X]]
p1 = sum([get_arrangements(springs, req_groups) for springs, req_groups in lines])

lines = [['?'.join([springs] * 5), req_groups * 5] for springs, req_groups in lines]
p2 = sum([get_arrangements(springs, req_groups) for springs, req_groups in lines])

print(p1)
print(p2)