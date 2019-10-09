DESCRIPTION_RULE = "What is the result of the expression?"


def gen_calc(arg1, arg2, arg3, arg4, arg5, arg6):
    return ((f'{arg1} + {arg2}', f'{arg1 + arg2}'),
            (f'{arg4} - {arg3}', f'{arg4 - arg3}'),
            (f'{arg5} * {arg6}', f'{arg5 * arg6}'),)
