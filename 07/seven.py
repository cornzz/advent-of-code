import re


def parse_inner(inner):
    inner = inner.split(' ', 1)
    return inner[1], int(inner[0])


def parse_rules(lines):
    lines = list(map(lambda x: re.sub(r' bag[s]?\.?', '', x), lines))
    lines = [line.split(' contain ') for line in lines]
    rul = {}
    for line in lines:
        outer, inner = line
        rul[outer] = {
            c: n
            for c, n in [
                parse_inner(i)
                for i in inner.split(', ')
                if 'no' not in i
            ]
        }
    return rul


def inside_out(rul, clr):
    out_bags = set()
    inn_bags = {clr}
    while len(inn_bags):
        for bag in list(inn_bags):
            inn_bags.remove(bag)
            for outer, inner in rul.items():
                if bag in inner.keys():
                    out_bags.add(outer)
                    inn_bags.add(outer)

    return out_bags


def outside_in(rul, clr):
    return sum([
        n + n * outside_in(rul, clr)
        for clr, n in rul[clr].items()
    ]) if rul[clr] else 0


with open('input.txt') as f:
    data = f.read().splitlines()
    rules = parse_rules(data)
    outside = len(inside_out(rules, 'shiny gold'))
    inside = outside_in(rules, 'shiny gold')
    print(f'Part one: {outside}, Part two: {inside}')
