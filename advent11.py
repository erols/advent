with open('input11') as data:
    seats_list = [list(x.strip()) for x in data.readlines()]


def set_seat_state(c, sl, cs):
    occupied, unoccupied, floor = count_surrounding_seats_b(c, cs)
    if cs[c[0]][c[1]] == 'L' and occupied == 0:
        sl[c[0]][c[1]] = '#'
    if cs[c[0]][c[1]] == '#' and occupied >= 5:
        sl[c[0]][c[1]] = 'L'


def count_surrounding_seats(c, sl):
    occupied = 0
    unoccupied = 0
    floor = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == 0 and j == 0:
                continue
            if c[0] + i < 0:
                continue
            if c[0] + i == len(sl):
                continue
            if c[1] + j < 0:
                continue
            if c[1] + j == len(sl[0]):
                continue
            if sl[c[0]+i][c[1]+j] == '#':
                occupied = occupied + 1
            elif sl[c[0]+i][c[1]+j] == 'L':
                unoccupied = unoccupied + 1
            elif sl[c[0] + i][c[1] + j] == '.':
                floor = floor + 1
    return occupied, unoccupied, floor


def count_surrounding_seats_b(c, sl):
    cursor = [x for x in c]
    occupied = 0
    unoccupied = 0
    floor = 0
    for t in [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]:
        c = [x for x in cursor]
        print(cursor, c)
        c = [c[i] + t[i] for i in range(len(c))]
        if c[0] < 0 or c[0] >= len(sl) or c[1] < 0 or c[1] >= len(sl[0]):
            continue
        while True:
            if c[0] < 0 or c[0] >= len(sl) or c[1] < 0 or c[1] >= len(sl[0]):
                c = [c[i] + t[i] for i in range(len(c))]
                break
            if sl[c[0]][c[1]] == ".":
                c = [c[i] + t[i] for i in range(len(c))]
                floor = floor + 1
                continue
            if sl[c[0]][c[1]] == '#':
                occupied = occupied + 1
                break
            if sl[c[0]][c[1]] == 'L':
                unoccupied = unoccupied + 1
                break
    return occupied, unoccupied, floor


def count_seats(sl):
    occupied = 0
    unoccupied = 0
    floor = 0
    for i in sl:
        for j in i:
            if j == '#':
                occupied = occupied + 1
            if j == 'L':
                unoccupied = unoccupied + 1
            if j == '.':
                floor = floor + 1
    return occupied, unoccupied, floor


def copy_seats(sl):
    copy_of_seats = []
    for r in sl:
        copy = []
        for s in r:
            copy.append(s)
        copy_of_seats.append(copy)
    return copy_of_seats


def compare_seats(s1, s2):
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            if s1[i][j] != s2[i][j]:
                return False
    return True


def part_a(sl):
    while True:
        previous_seats = copy_seats(sl)
        check_seats = copy_seats(sl)
        for i in range(len(sl)):
            for j in range(len(sl[0])):
                set_seat_state([i, j], sl, check_seats)
        if compare_seats(sl, previous_seats):
            return count_seats(sl)


print(part_a(seats_list))
