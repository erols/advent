import json

# with open('input4') as passport_data:
#     passports = []
#     valid_passports = 0
#     passport = {}
#     for line in passport_data:
#         line = line.strip()
#         # print(len(line))
#         if line == "":
#             # print(json.dumps(passport, indent=4))
#             if len(passport) >= 8:
#                 valid_passports = valid_passports + 1
#             if len(passport) == 7 and 'cid' in passport:
#                 valid_passports = valid_passports + 1
#                 # print("cid found in passport")
#             passport = {}
#             continue
#         line = line.split(' ')
#         print(line)
#         for entry in line:
#             entry = entry.split(':')
#             # print("> ", entry)
#             passport[entry[0]] = entry[1]
#     if len(passport) >= 8:
#         valid_passports = valid_passports + 1
#     if len(passport) == 7 and 'cid' in passport:
#         valid_passports = valid_passports + 1
#     # print(json.dumps(passport, indent=4))
#     print("Number of valid passports: ", valid_passports)


# passports = []
# valid_passports = 0
#
# with open('input4') as passport_data:
#     passport = ""
#     for line in passport_data:
#         line = line.strip('\n')
#         if line == "":
#             passports.append(passport)
#             passport = ""
#             continue
#         passport = passport + " " + line
#
# for p in passports:
#     print(p)
#     if len(p.split(' ')) >= 8:
#         valid_passports = valid_passports + 1
#     if 'cid:' in p and len(p.split(' ')) == 7:
#         valid_passports = valid_passports + 1
# print(str(valid_passports))

import re

with open('input4') as f:
    data = [line.strip() for line in f]

def parse_passports(data):
    passports = []
    current = {}

    for line in data:
        if line == '':
            passports.append(current)
            current = {}
        else:
            fields = line.split(' ')
            for field in fields: current[field[:3]] = field[4:]

    passports.append(current)
    return passports

def has_fields(passport):
    return all(field in passport for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def validate_birth(birth_year):
    return 1920 <= birth_year  <= 2002

def validate_issue(issue_year):
    return 2010 <= issue_year <= 2020

def validate_expire(expire_year):
    return 2020 <= expire_year  <= 2030

def validate_hair(hair_color):
    return re.match('^#[0-9a-f]{6}$', hair_color)

def validate_eye(eye_color):
    return eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate_pid(pid):
    return re.match('^[0-9]{9}$', pid)

def validate_height(height):
    if height[-2:] == 'cm' and 150 <= int(height[:-2]) <= 193:
        return True
    elif height[-2:] == 'in' and  59 <= int(height[:-2]) <= 76:
        return True
    else:
        return False

def full_validation(passport):
    if not has_fields(passport): return False
    return all([validate_birth(int(passport['byr'])),
                validate_issue(int(passport['iyr'])),
                validate_expire(int(passport['eyr'])),
                validate_height(passport['hgt']),
                validate_hair(passport['hcl']),
                validate_eye(passport['ecl']),
                validate_pid(passport['pid'])])

def solve_a(passports):
    return len([passport for passport in passports if has_fields(passport)])

def solve_b(passports):
    return len([passport for passport in passports if full_validation(passport)])

passports = parse_passports(data)

print(solve_a(passports))
print(solve_b(passports))