from random import randint
import prompt


# Set range random numbers
START = 1
END = 100

# Attempts
ATTEMPTS = 3


def gen_question():
    return randint(START, END)


def ask(data):
    print(f'Question: {data}')


def respond(answer, ans, name):
    if ans:
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
    if answer in data:
        return respond(answer, even[1], name)
    else:
        return respond(answer, even[1], name)


def point(attempt, name):
    i = 0
    while True:
        data = gen_question()
        ask(data)
        r = check(reply(), name, data)
        if r == R_RIGHT:
            print(r)
            i += 1
        else:
            i = 0
            print(r)
        if i == attempt:
            print(f'Congratulations, {name}!')
            break


def main():
    point(ATTEMPTS, 'Bill')


if __name__ == '__main__':
    main()
