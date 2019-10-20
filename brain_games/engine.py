from brain_games import cli


ATTEMPTS = 3
GREETING = "Welcome to the Brain Games!"


def greet():
    print()
    print(GREETING)


def ask(data):
    print(f'Question: {data}')


def congratulate(name):
    return print(f'Congratulations, {name}!')


def check_response(answer, name, data):
    if answer == data:
        return 'Correct!'
    return f"'{answer}' is wrong answer " \
        f";(. Correct answer was '{data}'. Let's try again, {name}!"


def run(game=None):
    greet()
    game.get_denotation()
    username = cli.get_username()
    i = 0
    while i < ATTEMPTS:
        game_issue, game_response = game.get_game()
        ask(game_issue)
        user_response = cli.get_user_response()
        a = check_response(user_response, username, game_response)
        print(a)
        i = i + 1
        if a != 'Correct!':
            i = 0
    congratulate(username)
