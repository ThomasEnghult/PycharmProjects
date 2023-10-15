import itertools
import timeit


def timewaster():
    for a in range(5):
        for b in range(5):
            if b != a:
                for c in range(5):
                    if c != a and c != b:
                        for d in range(5):
                            if d != a and d != b and d != c:
                                for e in range(5):
                                    if e != a and e != b and e != c and e != d:
                                        thing = [a, b, c, d, e]

tim = timeit.timeit('''
for a in range(5):
    for b in range(5):
        if b != a:
            for c in range(5):
                if c != a and c != b:
                    for d in range(5):
                        if d != a and d != b and d != c:
                            for e in range(5):
                                if e != a and e != b and e != c and e != d:
                                    thing = [a, b, c, d, e]''', number=10000)

print (tim)
#print(*itertools.permutations([0, 1, 2, 3, 4], 5), sep='\n')

tim2 = timeit.timeit('''[*itertools.permutations([0, 1, 2, 3, 4], 5)]''', number=10000)
print(tim2)

print(tim/tim2)