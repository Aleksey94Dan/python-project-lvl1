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
    pass


def happy(name):
    return print(f'Congratulations, {name}!')


def gen_question():
    return randint(START, END)


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


def is_even(data):
    arg = data
    if arg % 2 == 0:
        return True, 'yes'
    return False, 'no'


def check(answer, name, data, switch=0):
    if switch == 0:
        even = is_even(data)
    else:
        even = data
    if answer in even:
        return respond(answer, even[1], name, 1)
    else:
        return respond(answer, even[1], name)


def point(attempt, name,  switch,):
    i = 0
    while True:
        if switch == SWITCH_CALC:
            data = gen_example()[i]
            ask(data[0])
        elif switch == SWITCH_GCD:
            data = gen_gcd()
            ask(data[0])
        elif switch == SWITCH_PROGRESSION:
            data = gen_progression()
            ask(data[0])
        elif switch ==  SWITCH_PRIME:
            data = gen_prime()
            ask(data[0])
        else:
            data = gen_question()
            ask(data)

        answer = reply()
        print(check(answer, name, data, switch))
        if check(answer, name, data, switch) == 'Correct!':
            i += 1
        else:
            i = 0
        if i == attempt:
            happy(name)
            break


def main():
    point(ATTEMPTS, 'Bill',  SWITCH_EVEN)
    point(ATTEMPTS, 'Bill', SWITCH_CALC)
    point(ATTEMPTS, 'Bill', SWITCH_GCD)
    point(ATTEMPTS, 'Bill', SWITCH_PROGRESSION)


if __name__ == '__main__':
    main()
