from math import gcd
from random import randint

DESCRIPTION = "Find the greatest common divisor of given numbers."


def gen():
    arg1 = randint(0, 100)
    arg2 = randint(0, 100)
    answer = gcd(arg1, arg2)
    return f'{arg1} {arg2}', f'{answer}'
