source = open("input.txt")
source = source.read()
source = source.split("\n\n", -1)


# Part 1

def countYes(answers: str):
    result = {}
    for answer in answers:
        result[answer] = 'Yes'

    if '\n' in result:
        del result['\n']

    return len(result)


sum_of_yes = 0
for answer in source:
    sum_of_yes += countYes(answer)
print(f'Part 1: {sum_of_yes}')


# Part 2


def count_element_in_all(lst_of_ind: [str]):
    counter = 0
    if len(lst_of_ind) == 1:
        return len(lst_of_ind[0])

    for answer in lst_of_ind[0]:
        flag = 1
        for answers in lst_of_ind[1:]:
            if answer not in answers:
                flag = 0
                break
        counter = counter + flag
    return counter


total = 0

for group_answers in source:
    lst_of_ind = group_answers.split('\n')
    total = total + count_element_in_all(lst_of_ind)
print(f'Part 2: {total}')
