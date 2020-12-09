with open('input9') as data:
    numbers = [int(x.strip()) for x in data.readlines()]


def part1():
    for i, n in enumerate(numbers[25:]):
        matches = []
        list1 = numbers[i:i+25].copy()
        list2 = numbers[i:i+25].copy()
        for v in list1:
            list2.pop(0)
            for w in list2:
                if v != w:
                    matches.append(v+w != n)
        if all(matches):
            return n


def part2():
    for i, n in enumerate(numbers):
        running_total = 0
        values = [n]
        while running_total < 26796446:
            running_total = sum(values)
            if running_total == 26796446:
                return min(values) + max(values)
            values.append(numbers[i+len(values)])


print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
