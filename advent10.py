with open('input10') as data:
    adapters = sorted([int(x.strip()) for x in data.readlines()])

adapters.append(max(adapters)+3)
adapters.insert(0, 0)


def part_a():
    jolts = [0, 0, 0]
    for i in range(len(adapters)):
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


with open('input10') as f:
    numbers = [0] + sorted([int(x) for x in f.readlines()])

placeholders = [1] + [0 for x in range(len(numbers)-1)]
for x in range(len(numbers)):
    for y in range(1, 4):
        if numbers[x] + y in numbers:
            placeholders[numbers.index(numbers[x] + y)] += placeholders[x]
            print(placeholders)

print(placeholders[-1])


# print(part_a())
