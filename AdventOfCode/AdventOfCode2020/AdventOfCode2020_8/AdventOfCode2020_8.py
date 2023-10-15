source = open("input.txt")
source = source.read()
source = source.split("\n")

for i in range(len(source)):
    instr, val = source[i].split(" ")
    source[i] = instr, int(val)

accumulator = 0
pointer = 0


def acc(instr):
    global accumulator, pointer
    accumulator = accumulator + instr
    pointer = pointer + 1


def jmp(inst):
    global pointer
    pointer = pointer + inst


def nop(inst):
    global pointer
    pointer = pointer + 1


class InfiniteException(Exception):
    pass


def run(instructions):
    global pointer, accumulator
    usedinstructions = {}
    while len(instructions) > pointer:
        if str(pointer) not in usedinstructions:
            # print(f'Pointer: {pointer}, accumulator: {accumulator}')
            usedinstructions[str(pointer)] = 'None'
        else:
            # print(f'Pointer: {pointer}, accumulator: {accumulator}')
            raise InfiniteException("Loop detected, terminating program.")

        globals()[instructions[pointer][0]](instructions[pointer][1])
    print(f'Program finished with accumulator: {accumulator}')

print("part 1:")

try:
    run(source)
except InfiniteException as error:
    print(error)
    print(f'Accumulator: {accumulator}')

print("\npart 2:")

for i in range(len(source)):
    copy = source.copy()
    pointer = 0
    accumulator = 0

    if copy[i][0] == "nop":
        copy[i] = "jmp", copy[i][1]
        # print(copy)
    else:
        continue

    try:
        run(copy)
    except InfiniteException as error:
        pass
    else:
        print(f'Changed nop to jmp on row {i}')
        break

for i in range(len(source)):
    copy = source.copy()
    pointer = 0
    accumulator = 0

    if copy[i][0] == "jmp":
        copy[i] = "nop", copy[i][1]
        # print(copy)
    else:
        continue

    try:
        run(copy)
    except InfiniteException as error:
        pass
    else:
        print(f'Changed jmp to nop on row {i}')
        break
