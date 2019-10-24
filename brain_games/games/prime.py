from random import randint

DENOTATION = "Answer \"yes\" if given number is prime. " \
                   "Otherwise answer \"no\"."
START = 0
FINISH = 100
FIRST_PRIME_NUMBER = 2


def get_denotation():
    print(DENOTATION)
    print()


def is_zero_or_one(number):
    if number == 0 or number == 1:
        return True


def is_prime(number):
    if is_zero_or_one(number):
        return False
    i = FIRST_PRIME_NUMBER
    while i * i <= number:
        if number % i == 0:
            return False
        i = i + 1
    return True


def get_game():
    prime_number = randint(START, FINISH)
    if is_prime(prime_number):
        return prime_number, 'yes'
    return prime_number, 'no'
