from fileinput import input
import re


def get_regex(i, p2=False):
    rule = rules[i]
    if re.fullmatch(r'"."', rule):
        return rule.strip('"')

    if i == '8' and p2:
        return f'(?:{get_regex("42", p2)})+'
    if i == '11' and p2:
        r42 = get_regex("42")
        r31 = get_regex("31")
        return '(?:' + '|'.join(f'{r42}{{{i}}}{r31}{{{i}}}' for i in range(1, 15)) + ')'

    res = [''.join([get_regex(r, p2) for r in alt.split()]) for alt in rule.split('|')]
    return f'(?:{"|".join(res)})'


d = [line.strip() for line in input('input.txt')]
rules = dict([rule.split(': ') for rule in d[:d.index('')]])
messages = d[d.index('') + 1:]

rgx = get_regex('0')
p1_res = sum([bool(re.fullmatch(rgx, x)) for x in messages])

rgx = get_regex('0', True)
p2_res = sum([bool(re.fullmatch(rgx, x)) for x in messages])

print(f'Part one: {p1_res}, Part two: {p2_res}')
