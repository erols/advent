with open('input11') as data:
    seats_list = [list(x.strip()) for x in data.readlines()]


def set_seat_state(c, sl):
    occupied = 0
    unoccupied = 0
    if sl[c[0]][c[1]] == '.':
        return
    for i in range(-1, 1):
        for j in range(-1, 1):
            if i == 1 and j == 1:
                continue
            if c[0] + i < 0:
                continue
            if c[0] + i == len(sl[0]):
                continue
            if c[1] + j < 0:
                continue
            if c[1] + j == len(sl):
                continue
            if sl[c[0]+i][c[1]+j] == '#':
                occupied = occupied + 1
            # elif sl[c[0]+i][c[1]+j] == 'L' or sl[c[0]+i][c[1]+j] == '.':
            elif sl[c[0] + i][c[1] + j] == 'L':
                unoccupied = unoccupied + 1
        if sl[c[0]][c[1]] == 'L' and occupied == 0:
            sl[c[0]][c[1]] = '#'
        if sl[c[0]][c[1]] == '#' and occupied >= 4:
            sl[c[0]][c[1]] = 'L'


def count_seats(sl):
    occupied = 0
    unoccupied = 0
    blank = 0
    for i in sl:
        for j in i:
            if j == '#':
                occupied = occupied + 1
            if j == 'L':
                unoccupied = unoccupied + 1
            if j == '.':
                blank = blank + 1
    return occupied, unoccupied, blank


def copy_seats(sl):
    copy_of_seats = []
    for r in sl:
        copy = [x for x in r]
        copy_of_seats.append(copy)
    return copy_of_seats


def part_a(sl):
    previous_seats = copy_seats(sl)
    while True:
        for i in range(len(sl)):
            for j in range(len(sl[0])):
                set_seat_state([i, j], sl)
        if sl == previous_seats:
            for r in sl:
                print(r)
            return count_seats(sl)
        else:
            previous_seats = sl.copy()


print(part_a(seats_list))
