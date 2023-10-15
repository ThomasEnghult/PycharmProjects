import math

def massToFuel(mass):
    fuel = mass/3
    fuel = math.trunc(fuel)
    fuel -= 2
    return fuel

#Part 1

indata = open("input.txt")
indata = indata.read()
indata = indata.splitlines()

totalFuel = 0

for x in indata:
    totalFuel += massToFuel(float(x))
print(totalFuel)

#Part 2

totalFuel = 0

for x in indata:
    fuelForFuel = 0
    addedFuel = massToFuel(float(x))
    totalPart = addedFuel
    while (addedFuel > 0):
        addedFuel = massToFuel(addedFuel)
        if (addedFuel > 0):
            fuelForFuel += addedFuel
    totalFuel += (totalPart+fuelForFuel)


print(totalFuel)

#Old Val: 5079985
#New Val: 5077155