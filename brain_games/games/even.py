from random import randint
DESCRIPTION = "Answer \"yes\" if number even otherwise answer \"no\"."


def gen():
    arg = randint(0, 100)
    if arg % 2 == 0:
        return arg, 'yes'
    else:
        return arg, 'no'
