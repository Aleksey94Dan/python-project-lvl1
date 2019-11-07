from random import randint, choice


DENOTATION = "What number is missing in the progression?"
START = 0
FINISH = 100
START_OF_DIFFERENCE = 1
FINISH_OF_DIFFERENCE = 10


def get_denotation():
    print(DENOTATION)
    print()


def get_game():
    a0 = randint(START, FINISH)
    d = randint(START_OF_DIFFERENCE, FINISH_OF_DIFFERENCE)
    progression = [str(a0) for a0 in range(a0, a0 + 10 * d, d)]
    element = choice(progression)
    progression[progression.index(element)] = '..'
    return ' '.join(progression), element
