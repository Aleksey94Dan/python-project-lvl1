DESCRIPTION_PRIME = "Answer \"yes\" if given number is prime. " \
                   "Otherwise answer \"no\"."


def gen_prime(arg1, prime_list):
    number = arg1
    if number in prime_list:
        return number, 'yes'
    else:
        return number, 'no'
