from random import randint, choice


DENOTATION = "What is the result of the expression?"
START = 0
FINISH = 100


def get_denotation():
    print(DENOTATION)
    print()


def get_operation_sign():
    signs_of_operation = ['+', '-', '*']
    return choice(signs_of_operation)


def calculate(arg1, arg2, sign):
    if sign == '+':
        return arg1 + arg2
    elif sign == '-':
        return arg1 - arg2
    elif sign == '*':
        return arg1 * arg2


def get_game():
    first_number = randint(START, FINISH)
    second_number = randint(START, FINISH)
    math_operation = get_operation_sign()
    result = calculate(first_number, second_number, math_operation)
    return f'{first_number} {math_operation} {second_number}', str(result)
