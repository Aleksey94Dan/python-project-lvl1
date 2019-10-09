DESCRIPTION_RULE = "Answer \"yes\" if number even otherwise answer \"no\"."


def gen_question(arg):
    arg = arg
    if arg % 2 == 0:
        return arg, 'yes'
    else:
        return arg, 'no'
