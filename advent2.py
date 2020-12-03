passwords = []

with open('input2') as data:
    for line in data:
        l = []
        l.append(line.split(':')[1].strip('\n '))
        l.append(line.split(':')[0].split(' ')[0].split('-'))
        l.append(line.split(':')[0].split(' ')[1])
        passwords.append(l)

good_pwd_count = 0
# for p in passwords:
#     n = p[0].count(p[2])
#     lower = int(p[1][0])
#     upper = int(p[1][1])
#     if lower <= n <= upper:
#         bad_pwd_count = bad_pwd_count + 1
#     else:
#         continue

for p in passwords:
    n = p[0].count(p[2])
    a = int(p[1][0]) - 1
    b = int(p[1][1]) - 1
    if p[0][a] == p[2] and p[0][b] != p[2]:
        good_pwd_count = good_pwd_count + 1
    elif p[0][a] != p[2] and p[0][b] == p[2]:
        good_pwd_count = good_pwd_count + 1
    else:
        continue

print("number of bad passwords is ", good_pwd_count)
