from random import randint
import prompt


# Set range random numbers
START = 1
END = 10

# Attempts
ATTEMPTS = 3

# Key for games
SWITCH_EVEN = 0
SWITCH_CALC = 1


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


if __name__ == '__main__':
    main()
