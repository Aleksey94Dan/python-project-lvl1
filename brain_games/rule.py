
# Констаннты, задающие цвет тексту
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'


def rule():
    print("Answer" +
          RED + " \"yes\" " + END +
          "if number even otherwise answer" +
          RED + " \"no\"" + END + ".")


def main():
    rule()


if __name__ == '__main__':
    main()