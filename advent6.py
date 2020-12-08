

# with open('input6') as answers:
#     scores = [0] * 26
#     letters = list("abcdefghijklmnopqrstuvwxyz")
#     group_score = 0
#     total = 0
#     for passenger in answers:
#         passenger = passenger.strip()
#         if passenger == "":
#             total = total + sum(scores)
#             scores = [0] * 26
#             print("GROUP-----------------------------------------------")
#         for letter in passenger:
#             if scores[letters.index(letter)] == 0:
#                 scores[letters.index(letter)] = 1
#                 print(scores)
#     total = total + sum(scores)
#     print("Total is ", total)


"""
Get the group as a list of lists of passengers
Reverse sort by length
for each letter in the shortest passenger
for each passenger
for each letter
check if the letter exists in the shortest passenger list
if it does not, pop that letter from the shortest list
finally, answer is len(shortest list) * len(group)
"""


def get_group_score(p_group):
    p_group = sorted(p_group, key=len, reverse=False)
    letters = p_group[0].copy()
    pos = 0
    founds = 0
    for letter in letters:
        for g in p_group:
            if letter in g:
                founds = founds + 1
        if founds == len(p_group):
            pos = pos + 1
            founds = 0
        else:
            founds = 0
    return pos


with open('input6') as answers:
    group = []
    groups = []
    total = 0
    for passenger in answers:
        passenger = passenger.strip()
        if passenger == "":
            groups.append(group)
            group = []
        else:
            passenger = list(passenger)
            group.append(passenger)

    print(str(len(groups)))
    for g in groups:
        group_score = get_group_score(g)
        total = total + group_score

    print("total", total)
