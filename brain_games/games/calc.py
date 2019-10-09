DESCRIPTION_CALC = "What is the result of the expression?"


def gen_calc(arg1, arg2):
    return ((f'{arg1} + {arg2}', f'{arg1 + arg2}'),
            (f'{arg1} - {arg2}', f'{arg1 - arg2}'),
            (f'{arg1} * {arg2}', f'{arg1 * arg2}'),)
