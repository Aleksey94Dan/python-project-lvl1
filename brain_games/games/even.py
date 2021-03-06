from random import randint


DENOTATION = "Answer \"yes\" if number even otherwise answer \"no\"."
START = 0
FINISH = 100


def get_denotation():
    print(DENOTATION)
    print()


def get_game():
    number = randint(START, FINISH)
    if not number % 2:
        return number, 'yes'
    return number, 'no'
