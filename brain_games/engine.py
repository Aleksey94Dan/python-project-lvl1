from brain_games import cli


ATTEMPTS = 3


def run(game=None):
    print()
    print("Welcome to the Brain Games!")
    if not game:
        return
    game.get_denotation()
    username = cli.get_username()
    for attempt in range(ATTEMPTS):
        game_question, game_response = game.get_game()
        print(f'Question: {game_question}')
        user_response = cli.get_user_response()
        if user_response == game_response:
            print('Correct!')
        else:
            print(f"'{user_response}' is wrong answer ;(. "
                  f"Correct answer was '{game_response} "
                  f"Let's try again, {username}!")
            break
        if attempt == ATTEMPTS - 1:
            print(f'Congratulations, {username}!')
