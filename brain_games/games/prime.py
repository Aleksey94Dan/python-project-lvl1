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
    prime_number = randint(START, FINISH)
    if is_prime(prime_number):
        return prime_number, 'yes'
    return prime_number, 'no'


def is_prime(number):
    if number == FIRST_PRIME_NUMBER:
        return True
    if is_even(number) or is_zero_or_one(number):
        return False
    for i in range(FIRST_PRIME_NUMBER + 1, int(sqrt(number))+1, 2):
        if number % i == 0:
            return False
    return True


def is_even(number):
    if not number % 2:
        return True


def is_zero_or_one(number):
    if number == 0 or number == 1:
        return True
