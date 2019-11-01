from random import randint, choice
from operator import add, mul, sub

DENOTATION = "What is the result of the expression?"
START = 0
FINISH = 100


def get_denotation():
    print(DENOTATION)
    print()


def get_game():
    first_number = randint(START, FINISH)
    second_number = randint(START, FINISH)
    math_operation, answer = get_operation(first_number, second_number)
    return f'{first_number} {math_operation} {second_number}', str(answer)


def get_operation(a, b):
    operation = (('+', add(a, b)),
                 ('-', sub(a, b)),
                 ('*', mul(a, b)),
                )
    return choice(operation)
