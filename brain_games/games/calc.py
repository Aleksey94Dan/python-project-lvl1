from random import randint

DESCRIPTION = "What is the result of the expression?"


def gen():
    arg1 = randint(0, 50)
    arg2 = randint(0, 50)
    return ((f'{arg1} + {arg2}', f'{arg1 + arg2}'),
            (f'{arg1} - {arg2}', f'{arg1 - arg2}'),
            (f'{arg1} * {arg2}', f'{arg1 * arg2}'), 'calc')
