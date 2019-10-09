import prompt


def run():
    print()
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    return name


def main():
    run()


if __name__ == '__main__':
    main()
