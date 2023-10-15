source = open("input.txt")
source = source.read()
source = source.splitlines()
snake1 = source[0]
snake2 = source[1]

snake1 = snake1.split(",", -1)
snake2 = snake2.split(",", -1)


def snaketocoords(inputList):
    list = inputList.copy()
    output = [0, 0]

    for i, x in enumerate(list):
        if x[0] == "R" or x[0] == "U":
            output.append(output[i] + int(x[1:]))
        elif x[0] == "L" or x[0] == "D":
            output.append(output[i] - int(x[1:]))
    output.pop(0)
    return output

#Takes the directions of the input.txt and calculates distance to given index
def snakelength(number, inputList):
    list = inputList.copy()
    output = 0
    for i in range(0, number):
        output += int(list[i][1:])
    return output


def snaketotoupl(inputList):
    output = []
    list = inputList.copy()
    toupl = (0, 0)
    output.append(toupl)

    for x in range(0, len(list) - 2, 2):
        toupl = (list[x + 1], list[x])
        output.append(toupl)
        toupl = (list[x + 1], list[x + 2])
        output.append(toupl)
    return output


def checkIntersection(p1, p2, p3, p4):
    # p1 -> p2 is x-axis and p3 -> p4 is y-axis

    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    if p1[0] > p2[0]:
        x1 = p2[0]
        x2 = p1[0]

    y3 = p3[1]
    y4 = p4[1]
    x3 = p3[0]
    if p3[1] > p4[1]:
        y3 = p4[1]
        y4 = p3[1]

    if x3 > x1 and x3 < x2:
        if y1 > y3 and y1 < y4:
            return (x3, y1)
    else:
        return False


def manhattan(a):
    return abs(a[0]) + abs(a[1])


coordsnake1 = (snaketocoords(snake1))
touplesnake1 = snaketotoupl(coordsnake1)
coordsnake1.pop(0)

coordsnake2 = (snaketocoords(snake2))
touplesnake2 = snaketotoupl(coordsnake2)
coordsnake2.pop(0)

closest = 0
shortest = 0

for i in range(len(touplesnake1) - 1):
    p1 = touplesnake1[i]
    p2 = touplesnake1[i + 1]
    for k in range(len(touplesnake2) - 1):
        p3 = touplesnake2[k]
        p4 = touplesnake2[k + 1]

        # check for all the times snake1 has a Right or Left that crosses a Down or Up on snake2
        result1 = checkIntersection(p1, p2, p3, p4)
        if result1 is not False and result1 is not None:

            # part 1 solver
            if closest > manhattan(result1) or closest == 0:
                closest = manhattan(result1)

            # part 2 solver
            xdist = abs(touplesnake1[i][0] - result1[0])
            ydist = abs(touplesnake2[k][1] - result1[1])
            total1 = snakelength(i, snake1) + xdist
            total2 = snakelength(k, snake2) + ydist
            total = total1 + total2
            if shortest > total or shortest == 0:
                shortest = total

        # check for all the times snake2 has a Right or Left that crosses a Down or Up on snake1
        result2 = checkIntersection(p3, p4, p1, p2)
        if result2 is not False and result2 is not None:

            # part 1 solver
            if closest > manhattan(result2) or closest == 0:
                closest = manhattan(result2)

            # part 2 solver
            xdist = abs(touplesnake2[k][0] - result2[0])
            ydist = abs(touplesnake1[i][1] - result2[1])
            total1 = snakelength(k, snake2) + xdist
            total2 = snakelength(i, snake1) + ydist
            total = total1 + total2
            if shortest > total or shortest == 0:
                shortest = total

print()
print(closest)
print(shortest)
