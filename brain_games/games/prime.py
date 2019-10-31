from random import randint
from math import sqrt


DENOTATION = "Answer \"yes\" if given number is prime. " \
                   "Otherwise answer \"no\"."
START = 0
FINISH = 100
FIRST_PRIME_NUMBER = 2


def get_denotation():
    print(DENOTATION)
    print()


def get_game():
    number = randint(START, FINISH)
    if is_prime(number):
        return number, 'yes'
    return number, 'no'


def is_prime(number):
    if number < FIRST_PRIME_NUMBER or not number % 2:
        return number == FIRST_PRIME_NUMBER
    divider = 3
    while divider <= sqrt(number):
        if not number % divider:
            return False
        divider = divider + 2
    return True
