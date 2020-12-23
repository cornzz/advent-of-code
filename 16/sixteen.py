import re
from fileinput import input
from functools import lru_cache


@lru_cache(maxsize=None)
def possible_names(n):
    return [r[0] <= n <= r[1] or r[2] <= n <= r[3] for r in rules]


data = [line.strip() for line in input('input.txt')]

# Parse rules
first_block = data.index('')
names, rules = [], []
for row in data[:first_block]:
    names.append(row.split(':')[0])
    rules.append([int(x) for x in re.findall(r'\d+', row)])

# Parse my ticket and nearby tickets
second_block = data.index('', first_block + 1)
my_ticket = [int(x) for x in data[second_block - 1].split(',')]
nearby_tickets = [[int(y) for y in x.split(',')] for x in data[second_block + 2:]]

# Sum up invalid fields for part 1
# Mark impossible field names if ticket is valid; rows are fields, cols are possible field names
p1 = 0
n_fields = len(rules)
poss_names = [[True for _ in range(n_fields)] for _ in range(n_fields)]
for ticket in nearby_tickets:
    valid = True
    for field in ticket:
        if not any(possible_names(field)):
            p1 += field
            valid = False
            break
    if valid:
        for i, field in enumerate(ticket):
            poss_names[i] = [x & y for x, y in zip(poss_names[i], possible_names(field))]

# Assign field name to every field with only one possible name, mark as used
# Iterate until all field names assigned
found = 0
actual_names = ['' for _ in range(n_fields)]
used = [False for _ in range(n_fields)]
while found < n_fields:
    for i in range(n_fields):
        poss_not_used = [j for j in range(n_fields) if poss_names[i][j] and not used[j]]
        if len(poss_not_used) == 1:
            actual_names[i] = names[poss_not_used[0]]
            used[poss_not_used[0]] = True
            found += 1

# Multiply values of fields that start with 'departure'
p2 = 1
for i in range(n_fields):
    if actual_names[i].startswith('departure'):
        p2 *= my_ticket[i]

print(f'Part one: {p1}, Part two: {p2}')
