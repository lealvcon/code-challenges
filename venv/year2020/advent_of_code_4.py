# advent of code day 4
# description at https://adventofcode.com/2020/day/4

test = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''
test = test.split('\n\n')
input = ""
with open('input_files/input_4') as file:
    input = file.read()

input = input.split('\n\n')

fields=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def check_passports(input):
    valid = 0
    for passport in input:
        passport = passport.split('\n')
        features = []
        for row in passport:
            features += row.split(' ')
        checks = 0
        present = {}
        for f in features:
            t = f.split(':')
            present[t[0]] = t[1]

        for field in fields:
            try:
                present[field]
                checks += 1
            except KeyError:
                break
        if checks == 7:
            valid += 1
    return valid

print("valid passports in test:", check_passports(test))
print("valid passports:", check_passports(input))

valids = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''

invalids = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''
valids = valids.split('\n\n')
invalids = invalids.split('\n\n')

import re


def validate_field(name, val):
    if name == 'byr':
        val = int(val)
        return val >= 1920 and val <= 2002

    elif name == 'iyr':
        val = int(val)
        return val >= 2010 and val <= 2020

    elif name == 'eyr':
        val = int(val)
        return val >= 2020 and val <= 2030

    elif name == 'hgt':
        units = val[-2:]
        if val[:-2] != '':
            h = int(val[:-2])
        else:
            return False
        if units == 'in':
            return h >= 59 and h <= 76
        elif units == 'cm':
            return h >= 150 and h <= 193
        else:
            return False

    elif name == 'hcl':
        return len(val[1:]) == 6 and not re.findall('[g-z]', val[1:])

    elif name == 'ecl':
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return val in colors

    elif name == 'pid':
        return len(val) == 9

def check_passwords_v2(input):
    valid = 0
    for passport in input:
        passport = passport.split('\n')
        features = []
        for row in passport:
            features += row.split(' ')
        checks = 0
        present = {}

        for f in features:
            t = f.split(':')
            present[t[0]] = t[1]

        for field in fields:
            try:
                if validate_field(field, present[field]):
                    checks += 1
            except KeyError:
                break
        if checks == 7:
            valid += 1
    return valid
print("new valid test passports:", check_passwords_v2(test))
print("new valid passports:", check_passwords_v2(input))
