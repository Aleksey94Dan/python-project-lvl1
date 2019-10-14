from random import randint
DESCRIPTION = "What number is missing in the progression?"


def gen():
    a0 = randint(0, 100)
    d = randint(0, 20)
    progression = []
    for i in range(0, 10):
        a0 = a0 + d
        progression.append(str(a0))
    char = randint(0, len(progression) - 1)
    symbol = progression.pop(char)
    progression.insert(char, '...')
    return ' '.join(progression), symbol
