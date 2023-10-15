import math
import numpy

source = open("input.txt")
source = source.read()
rows = source.split("\n", -1)
wide = len(rows[0])

treesHit = 0
x = 0

for y in range(1, len(rows)):
    x += 3
    xx = x % wide
    if rows[y][xx] == '#':
        treesHit += 1
print(treesHit)

'''Part 2'''


def treehitsimulator(right: int, down: int):
    treesHit = 0
    x = 0
    for y in range(down, len(rows), down):
        x += right
        xx = x % wide
        if rows[y][xx] == '#':
            treesHit += 1
    return treesHit



paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

results = [treehitsimulator(*i) for i in paths]
print(results)
print(math.prod(results))
print(numpy.prod(results))
