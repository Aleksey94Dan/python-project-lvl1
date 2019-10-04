#!/usr/bin/env python3

from .brain_games import out_text
from brain_games.rule import question_calc
from brain_games.cli import run
from brain_games.logic import point, ATTEMPTS, SWITCH_CALC


def main():
    out_text()
    question_calc()
    print()

    name = run()
    point(ATTEMPTS, name, SWITCH_CALC)


if __name__ == '__main__':
    main()
