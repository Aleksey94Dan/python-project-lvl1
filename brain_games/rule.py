
# Констаннты, задающие цвет тексту
# Цвета для rule
RED_RULE = '\033[91m'
RED_PRIME = '\033[91m'
BLUE_PRIME = '\033[34m'
END = '\033[0m'


def rule():
    print("Answer" +
          RED_RULE + " \"yes\" " + END +
          "if number even otherwise answer" +
          RED_RULE + " \"no\"" + END + ".")
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
          RED_PRIME + " \"yes\" " + END +
          ' if given ' + BLUE_PRIME + 'number' + END +
          ' is prime. Otherwise answer ' +
          RED_PRIME + " \"no\"" + END + '.')
    print()


def main():
    rule()
    question_calc()
    question_gcd()
    question_prime()
    question_progression()


if __name__ == '__main__':
    main()
