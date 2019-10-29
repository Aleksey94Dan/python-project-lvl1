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
    if number < FIRST_PRIME_NUMBER or not number % 2:
        return number == FIRST_PRIME_NUMBER
    i = 3
    while i <= int(sqrt(number)):
        if not number % i:
            return False
        i = i + 2
    return True
