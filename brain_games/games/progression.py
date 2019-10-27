from random import randint


DENOTATION = "What number is missing in the progression?"
START = 0
FINISH = 100
START_OF_DIFFERENCE = 1
FINISH_OF_DIFFERENCE = 10


def get_denotation():
    print(DENOTATION)
    print()


def get_progression(a0, d, element_index):
    progression = []
    three_dots = '...'
    element = ''

    for i in range(0, 10):
        if i != element_index:
            progression.append(str(a0))
            a0 = a0 + d
        else:
            element = str(a0)
            progression.append(three_dots)
            a0 = a0 + d
    return ' '.join(progression), element


def get_game():
    a0 = randint(START, FINISH)
    d = randint(START_OF_DIFFERENCE, FINISH_OF_DIFFERENCE)
    replacement_index = randint(0, 9)
    return get_progression(a0, d, replacement_index)
