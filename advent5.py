


def get_position(num, data):
    positions = list(range(num))
    for i in data:
        if i == 'L' or i == 'F':
            positions = positions[:int(round(len(positions) / 2))]
        elif i == 'R' or i == 'B':
            positions = positions[int(round(len(positions) / 2)):]
    return positions[0]


def get_seat_id(code):
    seat = list(code.strip())
    row_id = seat[:7]
    col_id = seat[7:]
    row = get_position(128, row_id)
    col = get_position(8, col_id)
    return row * 8 + col


def get_my_seat(sids):
    sids = sorted(sids)
    my_seat = []
    for i in range(len(sids) - 1):
        if (sids[i] + 1) != sids[i + 1]:
            my_seat.append(sids[i] + 1)
    return my_seat


with open('input5') as seats:
    seat_ids = []
    for s in seats:
        seat_id = get_seat_id(s)
        seat_ids.append(seat_id)
    print(max(seat_ids))
    print(len(seat_ids))
    print(len(set(seat_ids)))
    print(get_my_seat(seat_ids))


print(get_seat_id('FFFFFFFLLR'))
get_position(128, 'FFFBBBF')
get_position(128, 'BBFFBBF')