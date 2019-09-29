from random import randint
import prompt


# Set range random numbers
START = 1
END = 100


# Possible responses to user response
R_RIGHT = 'Correct!'


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
        return print(R_RIGHT)
    elif not even and answer == 'no':
        return print(R_RIGHT)
    elif even and answer == 'no':
        return print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {name}!")
    elif not even and answer == 'yes':
        return print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}!")
    elif even and (answer != 'no' or answer != 'yes'):
        return print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {name}!")
    elif not even and (answer != 'no' or answer != 'yes'):
        return print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}!")


def main():
    i = 0
    while True:
        data = gen_question()
        ask(data)
        check(reply(), 'Bill', data)
        i += 1
        if i == 10:
            break


if __name__ == '__main__':
    main()
