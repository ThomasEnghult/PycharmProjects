import numpy

source = open("input.txt")
source = source.read()

wide_pixel = 25
tall_pixel = 6
total_pixels = wide_pixel * tall_pixel
leastZeros = total_pixels + 1
indx = 0

print(total_pixels)

for x in range(len(source) // total_pixels):
    numofZero = source[x * total_pixels:x * total_pixels + total_pixels].count('0')
    if numofZero < leastZeros:
        leastZeros = numofZero
        indx = x

theLayer = total_pixels * indx

answer = source[theLayer:theLayer + total_pixels].count('1') * source[theLayer:theLayer + total_pixels].count('2')

for i in range(tall_pixel):
    layer = []
    for k in range(wide_pixel):
        layer.append(source[k + theLayer])
    print(layer)

print(answer)

# Part 2
listlayer = []
for x in range(len(source) // total_pixels):
    listlayer.append(list(source[x * total_pixels:x * total_pixels + total_pixels]))

listlayer = numpy.array(listlayer)
listlayer = listlayer.transpose()

def pixelColor(l1):
    for x in l1:
        if x != '2':
            return x
    return '2'


finalImage = [*map(pixelColor, listlayer)]

for x in range(wide_pixel - 1, len(finalImage), wide_pixel):
    finalImage[x] = finalImage[x] + '\n'

print(''.join(finalImage).replace('0', ' ', -1))



