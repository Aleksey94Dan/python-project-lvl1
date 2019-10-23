from brain_games import cli


ATTEMPTS = 3
GREETING = "Welcome to the Brain Games!"


def greet():
    print(GREETING)


def ask(question):
    print(f'Question: {question}')


def congratulate(name_player):
    return print(f'Congratulations, {name_player}!')


def check_response(name_player, actual_response, expected_response):
    if actual_response == expected_response:
        return 'Correct!'
    return f"'{actual_response}' is wrong answer " \
        f";(. Correct answer was '{expected_response}'. " \
           f"Let's try again, {name_player}!"


def run_gameplay(game):
    game.get_denotation()
    username = cli.get_username()
    i = 0
    while i < ATTEMPTS:
        game_question, game_response = game.get_game()
        ask(game_question)
        user_response = cli.get_user_response()
        correct_answer = check_response(
            username,
            user_response,
            game_response
        )
        print(correct_answer)
        i = i + 1
        if correct_answer != 'Correct!':
            i = 0
    congratulate(username)


def run(game=None):
    greet()
    if game:
        run_gameplay(game)
