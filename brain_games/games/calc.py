from random import randint, choice
from operator import add, sub, mul


DENOTATION = "What is the result of the expression?"
START = 0
FINISH = 100


def get_denotation():
    print(DENOTATION)
    print()


def get_game():
    first_number = randint(START, FINISH)
    second_number = randint(START, FINISH)
    math_operation, answer = choice((('+', add), ('-', sub), ('*', mul)))
    return f'{first_number} {math_operation} {second_number}',\
        str(answer(first_number, second_number))
