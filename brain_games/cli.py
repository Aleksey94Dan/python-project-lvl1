import prompt


def get_username():
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print()
    return username


def get_user_response():
    return prompt.string('Your answer: ').lower()
