with open('input11') as data:
    seats_list = [list(x.strip()) for x in data.readlines()]


def set_seat_state(c, sl):
    occupied = 0
    unoccupied = 0
    if sl[c[0]][c[1]] == '.':
        return
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            if c[0] - i < 0:
                continue
            if c[0] + i == len(sl[0]):
                continue
            if c[1] - j < 0:
                continue
            if c[1] + j == len(sl):
                continue
            if sl[i][j] == '#':
                occupied = occupied + 1
            elif sl[i][j] == 'L':
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


def part_a(sl):
    previous_seats = sl.copy()
    while True:
        for i in range(len(sl)):
            for j in range(len(sl[0])):
                set_seat_state([i, j], sl)
        if sl == previous_seats:
            return count_seats(sl)
        else:
            previous_seats = sl.copy()


print(part_a(seats_list))
