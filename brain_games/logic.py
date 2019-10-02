from random import randint
import prompt


# Set range random numbers
START = 1
END = 100

# Attempts
ATTEMPTS = 3


def gen_examaple():
    arg1 = randint(START, END)
    arg2 = randint(START, END)
    arg3 = randint(START, END)
    arg4 = randint(START, END)
    arg5 = randint(START, END)
    arg6 = randint(START, END)
    return ((f'{arg1} + {arg2}', arg1 + arg2),
            (f'{arg3} + {arg4}', arg3 + arg4),
            (f'{arg5} + {arg6}', arg5 + arg6),)


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
    ans = prompt.string("Your answer: ")
    return ans


def is_even(data):
    arg = data
    if arg % 2 == 0:
        return True, 'Yes'
    return False, 'No'


def check(answer, name, data):
    even = is_even(data)
    if answer in even:
        return respond(answer, even[1], name, 1)
    else:
        return respond(answer, even[1], name)


def point(attempt, name):
    i = 0
    while True:
        data = gen_question()
        ask(data)
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
    point(ATTEMPTS, 'Bill')
    # data = gen_question()
    # ask(data)
    # answer = reply()
    # print(check(answer, 'Bill', data))


if __name__ == '__main__':
    main()
