source = open("input.txt")
source = source.read()

source = source.replace("F","0")
source = source.replace("B","1")

source = source.replace("L","0")
source = source.replace("R","1")

source = source.split("\n", -1)

def seatFinder(passport:str):
    row = passport[:7]
    column = passport[7:]
    #print(f'row:{ int(row,2)} col:{int(column,2) }')
    return int(row,2), int(column,2)

def get_seatID(seat):
    row, col = seat
    return row*8 + col

highest = 0

for passport in source:
    seat = seatFinder(passport)
    seatID = get_seatID(seat)
    if seatID > highest:
        highest = seatID

print("Part 1: " + str(highest))

# Part 2

lst_of_ID = [0]*(highest + 1)

for passport in source:
    seat = seatFinder(passport)
    seatID = get_seatID(seat)
    lst_of_ID[seatID] = seatID

lst_of_ID.sort()

for i in range(1, len(lst_of_ID)):
    seatID = lst_of_ID[i]
    if seatID - 2 == lst_of_ID[i-1]:
        print(f'Part 2: {seatID - 1}')