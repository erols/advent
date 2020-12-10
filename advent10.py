with open('input10') as data:
    adapters = sorted([int(x.strip()) for x in data.readlines()])

adapters.append(max(adapters)+3)
adapters.insert(0, 0)


def part_a():
    jolts = [0, 0, 0]
    for i, v in enumerate(adapters):
        if i == len(adapters) - 1:
            break
        diff = adapters[i+1] - adapters[i]
        if diff > 3:
            print("error: too big")
        if diff <= 0:
            print("error: too small")
        else:
            jolts[diff-1] = jolts[diff-1] + 1

    return jolts[0]*jolts[2]


def part_b():
    pass


print(part_a())