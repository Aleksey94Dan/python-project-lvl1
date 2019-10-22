import prompt


def get_username():
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!\n')
    return username


def get_user_response():
    user_response = prompt.string('Your actual_response: ').lower()
    return user_response
