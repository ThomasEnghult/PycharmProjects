source = open("input.txt")
source = source.read()
source = source.split(",", -1)


def Opcoder(inputlist):
    list = inputlist.copy()
    for i in range(0, len(list), 4):

        a = int(list[i])
        b = int(list[i + 1])
        c = int(list[i + 2])
        d = int(list[i + 3])

        if a == 1:
            list[d] = int(list[b]) + int(list[c])
        elif a == 2:
            list[d] = int(list[b]) * int(list[c])
        elif a == 99:
            return list
        else:
            raise Exception("Unknown Opcode at position " + str(i) + ". Encountered value: " + str(list[a]))
    return list


sourceCopy = source.copy()

for noun in range(100):
    for verb in range(100):
        sourceCopy[1] = noun
        sourceCopy[2] = verb
        output = Opcoder(sourceCopy)

        if int(output[0]) == 19690720:
            print(noun)
            print(verb)
        sourceCopy = source.copy()


# part 1 Val: 3224742
# part 2 Val: noun = 79, verb = 60
