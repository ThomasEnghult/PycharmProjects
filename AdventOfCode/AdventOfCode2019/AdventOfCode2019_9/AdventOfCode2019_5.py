source = open("input2.txt")
source = source.read()
source = source.split(",", -1)


def listExtender(inputlist, totalsize):
    listofZeros = ['0'] * (totalsize + 1 - len(inputlist))
    inputlist.extend(listofZeros)
    print("Extended list: " + str(len(inputlist)))


def writeToAdress(inputlist, adress, value):
    if adress > len(inputlist):
        listExtender(inputlist, adress)
    inputlist[adress] = value
    print("adress: " + str(adress) + " Value: " + str(value))


#  writeToAdress(lst, i + 3, val)

def Opcoder(inputlist, inputInt):
    lst = inputlist.copy()

    opcodes = {'e': 0, 'd': 0, 'c': 0, 'b': 0, 'a': 0}
    i = relativeBase = 0
    numOfParameters = [3, 3, 1, 1, 2, 2, 3, 3, 1]  # OPcodes from 1-9
    prohibitImmediate = [1, 1, 1, 0, 0, 0, 1, 1, 0]
    print(lst)
    while i < len(lst):
        op = lst[i]
        # print("op: " + str(op))
        for k, v in opcodes.items():
            if len(op) != 0:
                op, opcodes[k] = op[:-1], int(op[-1])
            else:
                opcodes[k] = 0
        # print(opcodes)

        opde = (opcodes['d'] * 10) + opcodes['e']
        print("\nop: " + str(opde) + " i: " + str(i))
        # Parameters 1-3
        # 0 - Position mode: Address pointer to the Value
        # 1 - Immediate mode: The Value that is stored at the location
        # 2 - Relative mode: The Value that is stored at the offset of relativeBase
        if opde == 99:
            return outputInt

        parameters = [-1, -1, -1]
        opCBA = [opcodes['c'], opcodes['b'], opcodes['a']]
        print(opCBA)

        for x in range(0, numOfParameters[opde - 1]):
            mode = opCBA[x]

            if prohibitImmediate[opde - 1] and x > (numOfParameters[opde - 1] - 1):
                if mode == 0:
                    mode = 1
                if mode == 2:
                    mode = 1.5

            if mode == 0:
                try:
                    parameters[x] = lst[int(lst[i + (x + 1)])]  # Position mode

                except IndexError:
                    listExtender(lst, int(lst[i + (x + 1)]))
                    parameters[x] = lst[int(lst[i + (x + 1)])]

            if mode == 1 or mode == 1.5:
                parameters[x] = lst[i + (x + 1)]  # Immediate mode
                if mode == 1.5:
                    parameters[x] = parameters[x] + relativeBase

            if mode == 2:
                try:
                    parameters[x] = lst[int(lst[i + (x + 1)]) + relativeBase]  # Relative mode
                except IndexError:
                    listExtender(lst, int(lst[i + (x + 1)]) + relativeBase)
                    parameters[x] = lst[int(lst[i + (x + 1)]) + relativeBase]

        print("parameters" + str(parameters))
        # Performing the correct operation
        if opde == 1:  # Addition
            writeToAdress(lst, int(parameters[2]), str(int(parameters[0]) + int(parameters[1])))
            i += 4
        elif opde == 2:  # Multiplication
            writeToAdress(lst, int(parameters[2]), str(int(parameters[0]) * int(parameters[1])))
            i += 4
        elif opde == 3:  # Save Input
            writeToAdress(lst, int(parameters[0]), str(inputInt))
            i += 2
        elif opde == 4:  # Save Output
            outputInt = int(parameters[0])
            i += 2
        elif opde == 5:  # Jump if true
            if int(parameters[0]) != 0:
                i = int(parameters[1])
            else:
                i += 3
        elif opde == 6:  # Jump if false
            if int(parameters[0]) == 0:
                i = int(parameters[1])
            else:
                i += 3
        elif opde == 7:  # Less than
            if int(parameters[0]) < int(parameters[1]):
                writeToAdress(lst, int(parameters[2]), 1)
            else:
                writeToAdress(lst, int(parameters[2]), 0)
            i += 4
        elif opde == 8:  # Equals
            if int(parameters[0]) == int(parameters[1]):
                writeToAdress(lst, int(parameters[2]), 1)
            else:
                writeToAdress(lst, int(parameters[2]), 0)
            i += 4
        elif opde == 9:  # Adjust Relative Base
            relativeBase += int(parameters[0])
            i += 2
        else:
            raise Exception("Unknown Opcode at position " + str(i) + ". Encountered value: " + str(opde))
        print(lst)
    return outputInt


inputInt_ = input("Insert ID of unit:\n")
out = Opcoder(source, inputInt_)
print("output: " + str(out))
