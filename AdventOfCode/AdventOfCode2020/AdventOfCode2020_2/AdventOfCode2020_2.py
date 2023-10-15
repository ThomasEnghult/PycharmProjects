source = open("input.txt")
source = source.read()
source = source.split("\n", -1)

valid = 0

for rawData in source:
    data = rawData.split(" ")
    _minmax = data[0].split("-")
    _min = int(_minmax[0])
    _max = int(_minmax[1])
    _char = data[1][0]
    password = data[2]

    x = password.count(_char)
    if _min <= x <= _max:
        valid += 1
print(valid)

'''Part 2'''

valid = 0

for rawData in source:
    data = rawData.split(" ")
    _minmax = data[0].split("-")
    indx1 = int(_minmax[0])
    indx2 = int(_minmax[1])
    _char = data[1][0]
    password = data[2]

    if (password[indx1 - 1] == _char) ^ (password[indx2 - 1] == _char):
        valid += 1
print(valid)
