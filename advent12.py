with open('input12') as data:
    directions = []
    for line in data.readlines():
        direction = []
        line = line.strip()
        direction.append(line[:1])
        direction.append(int(line[1:]))
        directions.append(direction)


position = [0, 0, 'E']


def move(d):
    global position
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


for direction in directions:
    move(direction)
print(abs(position[0]) + abs(position[1]))

