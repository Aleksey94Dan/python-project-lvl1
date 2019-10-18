from random import randint
DENOTATION = "Answer \"yes\" if given number is prime. " \
                   "Otherwise answer \"no\"."

START = 0
FINISH = 100


def get_game():
    prime_number = randint(START, FINISH)
    if is_prime(prime_number):
        return prime_number, 'yes'
    return prime_number, 'no'


def is_prime(arg1):
    pass
