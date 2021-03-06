from random import randint


DENOTATION = "Find the greatest common divisor of given numbers."
START = 0
FINISH = 100


def get_denotation():
    print(DENOTATION)
    print()


def get_game():
    first_number = randint(START, FINISH)
    second_number = randint(START, FINISH)
    answer = gcd(first_number, second_number)
    return f'{first_number} {second_number}', str(answer)


def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)
