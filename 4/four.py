import re


fields = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}
valid_one, valid_two = 0, 0

with open('input.txt') as f:
    lines = f.read().splitlines()
    fields_copy_one = fields.copy()
    fields_copy_two = fields.copy()
    for line in lines:
        if line == '':
            if all(fields_copy_one.values()):
                valid_one += 1
            if all(fields_copy_two.values()):
                valid_two += 1
            fields_copy_one = fields.copy()
            fields_copy_two = fields.copy()
            continue
        for field in line.split(' '):
            field = field.split(':')
            fields_copy_one[field[0]] = True
            if field[0] == 'byr' and 1920 <= int(field[1]) <= 2002\
                    or field[0] == 'iyr' and 2010 <= int(field[1]) <= 2020\
                    or field[0] == 'eyr' and 2020 <= int(field[1]) <= 2030\
                    or field[0] == 'hgt' and ((field[1][-2:] == 'cm' and 150 <= int(field[1][:-2]) <= 193) or
                                              (field[1][-2:] == 'in' and 59 <= int(field[1][:-2]) <= 76))\
                    or field[0] == 'hcl' and field[1][0] == '#' and re.search('^[0-9a-f]{6}$', field[1][1:])\
                    or field[0] == 'ecl' and ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].__contains__(field[1])\
                    or field[0] == 'pid' and re.search('^[0-9]{9}$', field[1]):
                fields_copy_two[field[0]] = True

print(f'Part one: {valid_one}, Part two: {valid_two}')
