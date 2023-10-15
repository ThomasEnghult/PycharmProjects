source = open("input.txt")
source = source.read()
source = source.split(",", -1)


def Opcoder(inputlist, inputInt):
    lst = inputlist.copy()
    opcodes = {'e': 0, 'd': 0, 'c': 0, 'b': 0, 'a': 0}
    i = para2 = para3 = 0
    while i < len(lst):
        locallist = lst.copy()
        op = locallist[i]
        # print("op: " + str(op))
        for k, v in opcodes.items():
            if len(op) != 0:
                op, opcodes[k] = op[:-1], int(op[-1])
            else:
                opcodes[k] = 0
        # print(opcodes)

        opde = (opcodes['d'] * 10) + opcodes['e']
        print("op: " + str(opde))
        # Parameters 1-3
        # Immediate mode or position mode
        if opde == 99:
            return outputInt

        para1 = int(locallist[i + 1])

        if opde == 5 or opde == 6:
            if opcodes['c'] == 0:
                para1 = int(locallist[para1])

            para2 = int(locallist[i + 2])
            if opcodes['b'] == 0:
                para2 = int(locallist[para2])

        if opde == 1 or opde == 2 or opde == 7 or opde == 8:
            if opcodes['c'] == 0:
                para1 = int(locallist[para1])

            para2 = int(locallist[i + 2])
            if opcodes['b'] == 0:
                para2 = int(locallist[para2])

            para3 = int(locallist[i + 3])

        print("parameters 1-3: " + str(para1) + " " + str(para2) + " " + str(para3))

        # Performing the correct operation
        if opde == 1:  # Addition
            lst[para3] = str(para1 + para2)
            i += 4
        elif opde == 2:  # Multiplication
            lst[para3] = str(para1 * para2)
            i += 4
        elif opde == 3:  # Save Input
            lst[para1] = str(inputInt)
            i += 2
        elif opde == 4:  # Save Output
            outputInt = str(lst[para1])
            i += 2
        elif opde == 5:  # Jump if true
            if para1 != 0:
                i = para2
            else:
                i += 3
        elif opde == 6:  # Jump if false
            if para1 == 0:
                i = para2
            else:
                i += 3
        elif opde == 7:  # Less than
            if para1 < para2:
                lst[para3] = 1
            else:
                lst[para3] = 0
            i += 4
        elif opde == 8:  # Equals
            if para1 == para2:
                lst[para3] = 1
            else:
                lst[para3] = 0
            i += 4
        else:
            raise Exception("Unknown Opcode at position " + str(i) + ". Encountered value: " + str(opde))

    return outputInt


inputInt_ = input("Insert ID of unit:\n")
out = Opcoder(source, inputInt_)
print("output: " + str(out))
