
# Констаннты, задающие цвет тексту
RED = '\033[91m'
BLUE = '\033[34m'
BOLD = '\033[1m'
END = '\033[0m'


def rule():
    print("Answer" +
          RED + " \"yes\" " + END +
          "if number even otherwise answer" +
          RED + " \"no\"" + END + ".")
    print()


def question_calc():
    print('What is the result of the expression?')
    print()


def question_gcd():
    print('Find the greatest common divisor of given numbers.')
    print()


def question_progression():
    print('What number is missing in the progression?')
    print()


def question_prime():
    print('Answer ' +
          RED + " \"yes\" " + END +
          ' if given ' + BLUE + 'number' + END +
          ' is prime. Otherwise answer ' +
          RED + " \"no\"" + END + '.')
    print()


def main():
    rule()
    question_calc()
    question_gcd()
    question_prime()
    question_progression()


if __name__ == '__main__':
    main()
