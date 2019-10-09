import prompt
from random import randint
from brain_games.cli import run
from brain_games.games.game import greeting
from brain_games.games.even import gen_question
from brain_games.games.gcd import gen_gcd
from brain_games.games.progression import gen_progression
from brain_games.games.prime import gen_prime
from brain_games.games.calc import gen_calc
# Set range random numbers
START = 1
END = 10
END_RANGE_PROGRESSION = 10 - 1

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


# questions
def ask(data):
    print(f'Question: {data}')


# description
def description(rule):
    print(rule)


# congratulations
def happy(name):
    return print(f'Congratulations, {name}!')


# answer of user
def reply():
    ans = prompt.string("Your answer: ").lower()
    return ans
# right answers


def respond(answer, ans, name, switch=0):
    if ans and switch == 1:
        return 'Correct!'
    return f"'{answer}' is wrong answer " \
        f";(. Correct answer was '{ans}'. Let's try again, {name}!"


def check(answer, name, data):
    if answer in data:
        return respond(answer, data[1], name, 1)
    else:
        return respond(answer, data[1], name)


def fcn_question(switch):
    if switch == SWITCH_EVEN:
        arg1 = randint(START, END)
        return gen_question(arg1)
    elif switch == SWITCH_GCD:
        arg1 = randint(START, END)
        arg2 = randint(START, END)
        return gen_gcd(arg1, arg2)
    elif switch == SWITCH_PROGRESSION:
        arg1 = randint(START, END)
        arg2 = randint(START, END)
        arg3 = randint(START, END_RANGE_PROGRESSION)
        return gen_progression(arg1, arg2, arg3)
    elif switch == SWITCH_PRIME:
        arg1 = randint(START, len(PRIME_LIST) - 1)
        return gen_prime(arg1, PRIME_LIST)
    elif switch == SWITCH_CALC:
        arg1 = randint(START, END)
        arg2 = randint(START, END)
        arg3 = randint(START, END)
        arg4 = randint(START, END)
        arg5 = randint(START, END)
        arg6 = randint(START, END)
        return gen_calc(arg1, arg2, arg3, arg4, arg5, arg6)

# Rules


# Engine
def engine(rule, switch):
    # Часть игры, которая привествует игрока
    greeting()
    description(rule)
    name = run()
    i = 0
    while True:
        if switch == SWITCH_CALC:
            data = fcn_question(switch)[i]
        else:
            data = fcn_question(switch)
        ask(data[0])
        ans_user = reply()
        ans_check = check(ans_user, name, data)
        print(ans_check)
        if ans_check == 'Correct!':
            i += 1
        else:
            i = 0
        if i == ATTEMPTS:
            happy(name)
            break


def main():
    engine(None, SWITCH_PROGRESSION)


if __name__ == '__main__':
    main()
