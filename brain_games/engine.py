from brain_games import cli


ATTEMPTS = 3


def run(game=None):
    greet()
    if not game:
        return
    game.get_denotation()
    username = cli.get_username()
    for attempt in range(ATTEMPTS):
        game_question, game_response = game.get_game()
        ask(game_question)
        user_response = cli.get_user_response()
        correct_answer_text, answer_is_value = check_response(
            username,
            user_response,
            game_response,
        )
        print(correct_answer_text)
        if not answer_is_value:
            break
        if attempt == ATTEMPTS:
            congratulate(username)


def greet():
    print("Welcome to the Brain Games!")


def ask(question):
    print(f'Question: {question}')


def check_response(name_player, actual_response, expected_response):
    if actual_response == expected_response:
        return 'Correct!', True
    return f"'{actual_response}' is wrong answer " \
        f";(. Correct answer was '{expected_response}'. " \
           f"Let's try again, {name_player}!", False


def congratulate(name_player):
    return print(f'Congratulations, {name_player}!')
