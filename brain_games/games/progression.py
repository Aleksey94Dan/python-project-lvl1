DESCRIPTION_RULE = "What number is missing in the progression?"


def gen_progression(arg1, arg2, arg3):
    a0 = arg1
    d = arg2
    progression = []
    for i in range(0, 10):
        a0 = a0 + d
        progression.append(str(a0))
    char = arg3
    symbol = progression.pop(char)
    progression.insert(char, '...')
    return ' '.join(progression), symbol
