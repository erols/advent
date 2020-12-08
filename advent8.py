class Instruction:

    def __init__(self, ins, val):
        self.instruction = ins
        self.value = int(val)
        self.visited = False

    def set_visited(self):
        self.visited = True


instructions = []
accumulator = 0
position = 0

with open('input8') as data:
    for line in data:
        line = line.strip()
        instruction = line.split(' ')
        inst = Instruction(instruction[0], instruction[1])
        instructions.append(inst)


def main():
    global instructions, accumulator, position
    run = True
    while run:
        if instructions[position].instruction == 'nop':
            instructions[position].set_visited()
            position = position + 1
        elif instructions[position].instruction == 'jmp':
            instructions[position].set_visited()
            position = position + instructions[position].value
        else:
            if instructions[position].visited:
                print(accumulator)
                run = False
            else:
                accumulator = accumulator + instructions[position].value
                position = position + 1


main()

