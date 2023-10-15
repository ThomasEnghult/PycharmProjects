source = open("input.txt")
source = source.read()
source = source.replace(" bags", '')
source = source.replace(" bag", '')
source = source.split(".\n")


def addrule(rule: str, mydict: dict):
    key, val = rule.split(" contain ")
    val = val.split(', ')
    bag = []
    for bags in val:
        if bags == "no other":
            continue
        amount = int(bags[0])
        color = bags[2:]
        bag.append((amount, color))

    mydict[key] = bag


rulesforbags = {}

for rule in source:
    addrule(rule, rulesforbags)


def open_bags_in_bag(bag: str, amount: int, rulebook: dict, counter: int):
    open_bag = rulebook[bag]

    if not open_bag:
        return 0, counter

    for bags in open_bag:
        (local_amount, color) = bags
        local_amount = local_amount * amount
        # print(f'{bags[0] * amount} {bags[1]} contains {rulebook[bags[1]]}')

        if color == "shiny gold":
            # print(f'counter: {counter}')
            # print("Found Gold!")
            return local_amount, counter
        else:
            look = open_bags_in_bag(color, local_amount, rulebook, counter)
            # print(f'counter: {counter} look: {look}')
            counter = look[0] + look[1]

    return 0, counter


shinygold = 0
totalgold = 0

for rules in rulesforbags:
    shinygold = open_bags_in_bag(rules, 1, rulesforbags, 0)
    print(f'1 {rules} bag contain {shinygold[0] + shinygold[1]} bags of shiny gold bags')
    if shinygold[0] + shinygold[1] > 0:
        totalgold = totalgold + 1

print(f'\nPart 1: Unique bags with shiny gold inside: {totalgold}')


# Part 2

def open_bags_in_bag2(bag: str, amount: int, rulebook: dict, counter: int):
    open_bag = rulebook[bag]

    if not open_bag:
        return 0, counter

    for bags in open_bag:
        (local_amount, color) = bags
        local_amount = local_amount * amount
        look = open_bags_in_bag2(color, local_amount, rulebook, counter)
        counter = look[1] + local_amount

    return 0, counter


bags_in_shinygold = open_bags_in_bag2("shiny gold", 1, rulesforbags, 0)[1]
print(f'Part 2: There is {bags_in_shinygold} bags in the shiny gold bag.')
