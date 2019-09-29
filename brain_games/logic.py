from random import randint
import prompt


# Set range random numbers
START = 1
END = 100


# Possible responses to user response
R_RIGHT = 'Correct!'

# Attempts
ATTEMPTS = 3


def gen_question():
    return randint(START, END)


def ask(data):
    arg = data
    print(f'Question: {arg}')


def reply():
    ans = prompt.string("Your answer: ")
    return ans


def is_even(data):
    arg = data
    if arg % 2 == 0:
        return True
    return False


def check(answer, name, data):
    even = is_even(data)
    if even and answer == 'yes':
        return R_RIGHT
    elif not even and answer == 'no':
        return R_RIGHT
    elif even and answer == 'no':
        return f"'{answer}' is wrong answer " \
               f";(. Correct answer was 'yes'. Let's try again, {name}!"
    elif not even and answer == 'yes':
        return f"'{answer}' is wrong answer " \
               f";(. Correct answer was 'no'. Let's try again, {name}!"
    elif even and (answer != 'no' or answer != 'yes'):
        return f"'{answer}' is wrong answer ;" \
               f"(. Correct answer was 'yes'. Let's try again, {name}!"
    elif not even and (answer != 'no' or answer != 'yes'):
        return f"'{answer}' is wrong answer ;" \
               f"(. Correct answer was 'no'. Let's try again, {name}!"


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
