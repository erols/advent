class Instruction():

    def __init__(self, ins, val):
        self.instruction = ins
        self.value = int(val)
        self.visited = False

    def set_visited(self):
        self.visited = True


instructions = []
# accumulator = 0
# position = 0

with open('input8') as data:
    for line in data:
        line = line.strip()
        instruction = line.split(' ')
        instructions.append(Instruction(instruction[0], instruction[1]))


def copy_instructions():
    copy = []
    for i in instructions:
        copy.append(Instruction(i.instruction, i.value))
    return copy


def run(test_instructions):
    accumulator = 0
    position = 0
    for i in range(len(test_instructions)):
        if position == len(test_instructions):
            return ["terminated", accumulator]
        if 0 > position > len(test_instructions):
            return ["unterminated", accumulator]
        print("position is", position)
        if test_instructions[position].instruction == 'nop':
            test_instructions[position].set_visited()
            position = position + 1
        elif test_instructions[position].instruction == 'jmp':
            test_instructions[position].set_visited()
            position = position + test_instructions[position].value
        elif test_instructions[position].instruction == 'acc':
            accumulator = accumulator + test_instructions[position].value
            position = position + 1
            # if test_instructions[position].visited and position == len(test_instructions):
            #     return ["terminated", accumulator]
            # else:
            #     test_instructions[position].set_visited()
            #     accumulator = accumulator + test_instructions[position].value
            #     position = position + 1
    return ["unterminated", accumulator]


def main():
    global instructions
    for n in range(len(instructions)):
        test_instructions = copy_instructions()
        if test_instructions[n].instruction == "nop":
            print(n)
            test_instructions[n].instruction = "jmp"
        elif test_instructions[n].instruction == "jmp":
            print(n)
            test_instructions[n].instruction = "nop"
        else:
            print(n)
        result = run(test_instructions)
        if result[0] == "terminated":
            print("Terminated correctly, accumulator is ", result[1])
            break

main()


main()

