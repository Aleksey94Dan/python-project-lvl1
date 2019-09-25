import prompt


def run():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def main():
    run()


if __name__ == '__main__':
    main()
