import AdventOfCode2019_5
import itertools

source = open("input.txt")
source = source.read()
source = source.split(",", -1)

outputInt = 0

'''for a in range(5):
    for b in range(5):
        if b != a:
            for c in range(5):
                if c != a and c != b:
                    for d in range(5):
                        if d != a and d != b and d != c:
                            for e in range(5):
                                if e != a and e != b and e != c and e != d:
                                    inputInt = 0
                                    for i in range(5):
                                        phase = [a, b, c, d, e]
                                        print(phase)
                                        #print(inputInt)
                                        inputInt = int(AdventOfCode2019_5.Opcoder(source, inputInt, phase[i]))
                                    if inputInt > outputInt:
                                        outputInt = inputInt
                                    
print(outputInt)
'''
comb = [*itertools.permutations([0, 1, 2, 3, 4], 5)]

for x in comb:
    inputInt = 0
    for i in x:
        inputInt = int(AdventOfCode2019_5.Opcoder(source, 0, inputInt, i)[0])
        if inputInt > outputInt:
            outputInt = inputInt

print(outputInt)

# Part 2

biggestOutput = 0
comb = [*itertools.permutations([5, 6, 7, 8, 9], 5)]
for x in comb:
    outputInt = 0
    programs = [source.copy(), source.copy(), source.copy(), source.copy(), source.copy()]
    pointr = [0, 0, 0, 0, 0]
    run = True
    first = True
    while run:
        for i, y in enumerate(x):

            if not first:
                y = outputInt

            outputInt, programs[i], pointr[i] = AdventOfCode2019_5.Opcoder(programs[i], pointr[i], outputInt, y)

            if i == 4:
                outp = outputInt
            if pointr[i] == -1:
                run = False
                break
        if outp > biggestOutput:
            biggestOutput = outp
        first = False
print(biggestOutput)
