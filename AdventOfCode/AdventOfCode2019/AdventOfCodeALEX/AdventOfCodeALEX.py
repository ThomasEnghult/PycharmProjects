# Input Ex: 0,0,0,0,0,1,1,1,1,1,2,2,2,2,2

source = open("input.txt")
source = source.read()
sourceList = source.split(",", -1)
seq = [int(sourceList[0])]
counter = 0

for x in sourceList:
    currentNum = int(x)
    if (currentNum != seq[counter]):
        seq.append(currentNum)
        counter += 1

a = len(sourceList)
b = len(seq)

output = seq*int(a / b)

print(output)