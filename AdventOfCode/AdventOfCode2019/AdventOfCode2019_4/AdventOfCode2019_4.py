puzzleMin = 165432
puzzleMax = 707912


def validNumber(min, max, number):
    if min > number:
        return False
    if number > max:
        return False
    cNumber = str(number)
    prev = cNumber[0]
    doubleBit = False
    for n in range(1, len(cNumber)):
        if int(prev) > int(cNumber[n]):
            return False
        if prev == cNumber[n]:
            doubleBit = True
        prev = cNumber[n]

    return doubleBit

def validNumber2(min, max, number):
    if min > number:
        return False
    if number > max:
        return False
    cNumber = str(number)
    prev = cNumber[0]
    doubleBit = False
    for n in range(1, len(cNumber)):
        if int(prev) > int(cNumber[n]):
            return False
        prev = cNumber[n]

    for n in range(1, len(cNumber) - 2):
        if cNumber[n] != cNumber[n-1] and cNumber[n] == cNumber[n+1] and cNumber[n] != cNumber[n+2]:
            doubleBit = True

    if cNumber[0] == cNumber[1] and cNumber[0] != cNumber[2]:
        doubleBit = True

    if cNumber[len(cNumber) - 2] == cNumber[len(cNumber) - 1] and cNumber[len(cNumber) -3] != cNumber[len(cNumber) - 1]:
        doubleBit = True
    return doubleBit


# Part 1 solver
counter = 0
for i in range(puzzleMin, puzzleMax):
    if validNumber(puzzleMin, puzzleMax, i):
        counter += 1
print(counter)

# Part 2 solver
counter2 = 0
for i in range(puzzleMin, puzzleMax):
    if validNumber2(puzzleMin, puzzleMax, i):
        counter2 += 1
print(counter2)