import random
import math

hit = 0.5
headshot = 0.2
numofshots = int(input("hur många skott skjuter du? \n"))
killshot = [0] * numofshots
tries = int(input("hur många försök har du? \n"))
total = tries
survives = 0

while (tries != 0):
    tries -= 1
    health = 3
    shots = 0
    for (i, x) in enumerate(killshot):
        shots += 1
        if (hit > random.random()):
            if (headshot > random.random()):
                health = 0
            else:
                health -= 1
        if (health == 0):
            killshot[i] += 1
            break
        if (shots == numofshots):
            survives += 1

for i, x in enumerate(killshot):
    print("he died on shot " + str(i + 1) + ": " + str(math.trunc((x / total) * 10000) / 100) + "% of times")
print("\nhe died " + str(math.trunc((1 - (survives / total)) * 10000) / 100) + "% of times")
print("he survived " + str(math.trunc((survives / total) * 10000) / 100) + "% of times")
