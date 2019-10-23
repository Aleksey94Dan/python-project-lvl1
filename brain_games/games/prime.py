from random import randint

DENOTATION = "Answer \"yes\" if given number is prime. " \
                   "Otherwise actual_response \"no\"."
START = 0
FINISH = 100


def get_denotation():
    print(DENOTATION)
    print()


def is_prime(arg1):
    if arg1 == 1 or arg1 == 0:
        return False
    i = 1
    while i * i > arg1:
        if arg1 % i == 0:
            return False
        i = i + 1
    return True


def get_game():
    prime_number = randint(START, FINISH)
    if is_prime(prime_number):
        return prime_number, 'yes'
    return prime_number, 'no'
