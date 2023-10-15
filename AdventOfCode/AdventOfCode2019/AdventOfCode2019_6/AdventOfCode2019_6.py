source = open("input.txt")
source = source.read()
source = source.splitlines()

linkeddict = {}
for x in source:
    ab = x.split(")")
    #linkeddict.update({ab[1]: ab[0]})
    linkeddict[ab[1]] = ab[0]

linkeddict_ = linkeddict.copy()
totaljumps = 0
for x, y in linkeddict_.items():
    i = 1
    while y != 'COM':
        y = linkeddict_[y]
        i += 1
    totaljumps += i

print(totaljumps)

you = linkeddict.get('YOU')
youdict = {}
while you != 'COM':
    nxt = linkeddict.get(you)
    youdict.update({you: nxt})
    you = nxt
print(youdict)

san = linkeddict.get('SAN')
sandict = {}
while san != 'COM':
    nxt = linkeddict.get(san)
    sandict.update({san: nxt})
    san = nxt
print(sandict)


def findCommon(dictA, dictB):
    i = 0
    for x, y in dictA.items():
        if x in dictB:
            return i
        else:
            i += 1


youtosanta = findCommon(youdict, sandict)
youtosanta += findCommon(sandict, youdict)
print(youtosanta)
