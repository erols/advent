with open('input12') as data:
    directions = []
    for line in data.readlines():
        direction = []
        line = line.strip()
        direction.append(line[:1])
        direction.append(int(line[1:]))
        directions.append(direction)


# position = [0, 0, 'E']


def move(d):
    instruction = d[0]
    distance = d[1]
    if instruction == 'N':
        position[0] = position[0] + distance
    if instruction == 'S':
        position[0] = position[0] - distance
    if instruction == 'E':
        position[1] = position[1] + distance
    if instruction == 'W':
        position[1] = position[1] - distance
    if instruction == 'L':
        current_point = "NESW".index(position[2])
        turns = [90, 180, 270].index(distance) + 1
        position[2] = "NESW"[(current_point-turns) % 4]
    if instruction == 'R':
        current_point = "NESW".index(position[2])
        turns = [90, 180, 270].index(distance) + 1
        position[2] = "NESW"[(current_point+turns) % 4]
    if instruction == 'F':
        d[0] = position[2]
        move(d)
    print(position)


def move_direction(m, p, w):
    pass


def turn(m, p, w):
    pass


def move_forward(m, p, w):
    pass


def part_b(d):
    position = [0, 0]
    waypoint = [1, 10]
    for di in d:
        if di[0] in 'NSEW':
            e = [1, 1, -1, -1]['NSEW'.index(di[0])]
            if di[0] in 'NS':
                waypoint[0] = waypoint[0] + (di[1] * e)
            elif di[0] in 'EW':
                waypoint[1] = waypoint[1] + (di[1] * e)
            else:
                print("Error, direction is", di[0])


    print(abs(position[0]) + abs(position[1]))

