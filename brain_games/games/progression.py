from random import randint, choice


DENOTATION = "What number is missing in the progression?"
START = 0
FINISH = 100
START_OF_DIFFERENCE = 1
FINISH_OF_DIFFERENCE = 10
FIRST_MEMBER_PROGRESSION = 0
LAST_MEMBER_PROGRESSION = 10


def get_denotation():
    print(DENOTATION)
    print()


def get_progression(a0, d):
    progression = []
    for i in range(FIRST_MEMBER_PROGRESSION, LAST_MEMBER_PROGRESSION):
        a0 = a0 + d
        progression.append(str(a0))
    return progression


def replace_with_ellipsis(lst):
    element_index = lst.index(choice(lst))
    element = lst.pop(element_index)
    lst.insert(element_index, '...')
    return ' '.join(lst), element


def get_game():
    a0 = randint(START, FINISH)
    d = randint(START_OF_DIFFERENCE, FINISH_OF_DIFFERENCE)
    progression = get_progression(a0, d)
    return replace_with_ellipsis(progression)
