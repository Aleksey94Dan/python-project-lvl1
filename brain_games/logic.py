from random import randint
import prompt
from math import gcd

# Set range random numbers
START = 1
END = 10

# Attempts
ATTEMPTS = 3

# Key for games
SWITCH_EVEN = 0
SWITCH_CALC = 1
SWITCH_GCD = 2
SWITCH_PROGRESSION = 3
SWITCH_PRIME = 4

# The prime numbers (A000040)
PRIME_LIST = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
        61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
        131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
        193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
        263, 269, 271]


def gen_question():
    arg = randint(START, END)
    if arg % 2 == 0:
        return arg, 'yes'
    else:
        return arg, 'no'


def gen_example():
    arg1 = randint(START, END)
    arg2 = randint(START, END)
    arg3 = randint(START, END)
    arg4 = randint(START, END)
    arg5 = randint(START, END)
    arg6 = randint(START, END)
    return ((f'{arg1} + {arg2}', f'{arg1 + arg2}'),
            (f'{arg4} - {arg3}', f'{arg4 - arg3}'),
            (f'{arg5} * {arg6}', f'{arg5 * arg6}'),)


def gen_progression():
    a0 = randint(START, END)
    d = randint(START, END)
    progression = []
    for i in range(0, 10):
        a0 = a0 + d
        progression.append(str(a0))
    char = randint(0, len(progression) - 1)
    symbol = progression.pop(char)
    progression.insert(char, '...')
    return ' '.join(progression), symbol


def gen_gcd():
    arg1 = randint(START, END)
    arg2 = randint(START, END)
    answer = gcd(arg1, arg2)
    return f'{arg1} {arg2}', f'{answer}'


def gen_prime():
    number = randint(0, len(PRIME_LIST))
    if number in PRIME_LIST:
        return number, 'yes'
    else:
        return number, 'no'


def happy(name):
    return print(f'Congratulations, {name}!')


def ask(data):
    print(f'Question: {data}')


def respond(answer, ans, name, switch=0):
    if ans and switch == 1:
        return 'Correct!'
    return f"'{answer}' is wrong answer " \
        f";(. Correct answer was '{ans}'. Let's try again, {name}!"


def reply():
    ans = prompt.string("Your answer: ").lower()
    return ans


def check(answer, name, data):
    even = data
    if answer in even:
        return respond(answer, even[1], name, 1)
    else:
        return respond(answer, even[1], name)


def keys(switch, i=0):
    if switch == SWITCH_CALC:
        return gen_example()[i]
    elif switch == SWITCH_GCD:
        return gen_gcd()
    elif switch == SWITCH_PROGRESSION:
        return gen_progression()
    elif switch == SWITCH_PRIME:
        return gen_prime()
    else:
        return gen_question()


def point(attempt, name, switch):
    i = 0
    while True:
        data = keys(switch)
        ask(data[0])
        answer = reply()
        print(check(answer, name, data))
        if check(answer, name, data) == 'Correct!':
            i += 1
        else:
            i = 0
        if i == attempt:
            happy(name)
            break


def main():
    name = 'Bill'
    switch = SWITCH_EVEN
    point(ATTEMPTS, name, switch)
    switch = SWITCH_CALC
    point(ATTEMPTS, name, switch)
    switch = SWITCH_GCD
    point(ATTEMPTS, name, switch)
    switch = SWITCH_PROGRESSION
    point(ATTEMPTS, name, switch)
    switch = SWITCH_PRIME
    point(ATTEMPTS, name, switch)


if __name__ == '__main__':
    main()
