import prompt
from brain_games.cli import run
# welcoming
from brain_games.games.game import greeting

# Attempts
ATTEMPTS = 3


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


# Engine
def start(naming):
    rule = naming.DESCRIPTION
    greeting()
    description(rule)
    name = run()
    i = 0
    while i < ATTEMPTS:
        # if 'calc' in naming.gen():
        data = naming.gen()[i] if 'calc' in naming.gen() else naming.gen()
        ask(data[0])
        ans_user = reply()
        ans_check = check(ans_user, name, data)
        print(ans_check)
        i += 1
        if ans_check != 'Correct!':
            i = 0
    happy(name)
