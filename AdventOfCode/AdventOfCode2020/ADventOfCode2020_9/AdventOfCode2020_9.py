source = open("input.txt")
source = source.read()
source = source.split("\n")

preamble = []


def create_preamble(XMAS: list, preamble_length: int):
    global preamble
    preamble = [XMAS[:25]] * preamble_length
    print(preamble)
    # for current_number in range(preamble_length):


create_preamble(source, 25)
print(len(preamble))
print(preamble[0])