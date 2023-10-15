from __future__ import division

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
    return output


def snaketotoupl(inputList):
    output = []
    list = inputList.copy()
    for x in range(0, len(list) - 1, 2):
        toupl = (list[x], list[x + 1])
        output.append(toupl)
        toupl = (list[x + 2], list[x + 1])
        output.append(toupl)
    return output


snake1 = snaketocoords(snake1)
snake2 = snaketocoords(snake2)

snakePath1 = snake1.copy()
snakePath2 = snake2.copy()

snake1 = snaketotoupl(snake1)
snake2 = snaketotoupl(snake2)


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


closest = 0

snake2.insert(0, (0, 0))  # Offset to get the x-axis and y-axis pairings correct

print(snake1)
print(snake2)

for i in range(0, len(snake1) - 1, 2):
    for k in range(0, len(snake2) - 1, 2):
        result = checkIntersection(snake1[i], snake1[i + 1], snake2[k], snake2[k + 1])
        if result != False and result is not None:
            if closest > manhattan(result) or closest == 0:
                # print(str(result) + "    " + str(snake1[i]) + str(snake1[i + 1]) + str(snake2[k]) + str(snake2[k + 1]))
                closest = manhattan(result)

for i in range(1, len(snake2) - 1, 2):
    for k in range(1, len(snake1) - 1, 2):
        result = checkIntersection(snake2[i], snake2[i + 1], snake1[k], snake1[k + 1])
        if result != False and result is not None:
            if closest > manhattan(result) or closest == 0:
                # print(str(result) + "    " + str(snake1[i]) + str(snake1[i + 1]) + str(snake2[k]) + str(snake2[k + 1]))
                closest = manhattan(result)

print(closest)


# part 1 Val: 651


def pather1(_snake1, _snake2):
    for i in range(0, len(_snake1) - 1, 2):
        for k in range(0, len(_snake2) - 1, 2):
            result = checkIntersection(_snake1[i], _snake1[i + 1], _snake2[k], _snake2[k + 1])
            if result is not False and result is not None:
                total1 = 0
                total2 = 0
                for n in range(i):
                    total1 += abs(snakePath1[i])

                for n in range(k):
                    total2 += abs(snakePath2[i])

                total1 += abs(snakePath1[i] - result[0])
                total2 += abs(snakePath2[k] - result[1])

                print(" ")
                print(total1)
                print(total2)



def pather2(_snake1, _snake2):
    for i in range(1, len(_snake1) - 1, 2):
        for k in range(1, len(_snake2) - 1, 2):
            result = checkIntersection(_snake1[i], _snake1[i + 1], _snake2[k], _snake2[k + 1])
            if result is not False and result is not None:
                total1 = 0
                total2 = 0
                for n in range(i):
                    total1 += abs(snakePath2[i])

                for n in range(k):
                    total2 += abs(snakePath1[i])

                total1 += abs(snakePath2[i] - result[0])
                total2 += abs(snakePath1[k] - result[1])

                print(" ")
                print(total1)
                print(total2)



#shortestPath1 = pather1(snake1, snake2)
shortestPath2 = pather2(snake2, snake1)

#print(shortestPath1)
#print(shortestPath2)
