#!/usr/bin/env python3

from .brain_games import out_text
from brain_games.games.rule import question_gcd
from brain_games.cli import run
from brain_games.games.logic import point, ATTEMPTS, SWITCH_GCD


def main():
    out_text()
    question_gcd()
    name = run()
    point(ATTEMPTS, name, SWITCH_GCD)


if __name__ == '__main__':
    main()
