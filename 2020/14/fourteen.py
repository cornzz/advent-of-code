from fileinput import input
from itertools import product
import re


def run_p1(d):
    mask = []
    mem = {}
    for line in d:
        if line.startswith('mask'):
            mask = line.split('= ')[1]
            or_mask = int(mask.replace('X', '0'), 2)
            and_mask = int(mask.replace('X', '1'), 2)
            mask = [or_mask, and_mask]
        else:
            ad, val = [int(x) for x in re.findall(r'[\d]+', line)]
            mem[ad] = (val | mask[0]) & mask[1]

    return sum(mem.values())


def run_p2(d):
    mask = []
    mem = {}
    for line in d:
        if line.startswith('mask'):
            mask = line.split('= ')[1]
        else:
            ad, val = [int(x) for x in re.findall(r'[\d]+', line)]
            masked_ad = []
            ad = ad | int(mask.replace('X', '0'), 2)
            ad = list(f'{ad:036b}')
            for ind in [i for (i, c) in enumerate(mask) if c == 'X']:
                ad[ind] = 'X'
            ad = ''.join(ad)
            for c in product(['0', '1'], repeat=ad.count('X')):
                ad_copy = ad
                for d in c:
                    ad_copy = ad_copy.replace('X', d, 1)
                masked_ad.append(ad_copy)
            for m_ad in masked_ad:
                mem[m_ad] = val

    return sum(mem.values())


data = [line.strip() for line in input('input.txt')]

p1_val = run_p1(data)
p2_val = run_p2(data)

print(f'Part one: {p1_val}, Part two: {p2_val}')
