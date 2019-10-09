from math import gcd

DESCRIPTION_RULE = "Find the greatest common divisor of given numbers."


def gen_gcd(arg1, arg2):
    answer = gcd(arg1, arg2)
    return f'{arg1} {arg2}', f'{answer}'
