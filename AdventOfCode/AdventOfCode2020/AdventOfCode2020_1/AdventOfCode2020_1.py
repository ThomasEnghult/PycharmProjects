source = open("input.txt")
source = source.read()
source = source.split("\n", -1)
source = list(map(int, source))

for x in source:
    for i in range(len(source)):
        y = source[i]

        if (x + y) == 2020:
            print(x * y)

'''Part 2'''

for i in range(len(source)):
    for j in range(i+1, len(source)):
        for k in range(j+1, len(source)):
            if source[i] + source[j] + source[k] == 2020:
                print(source[i] * source[j] * source[k])
