#!/usr/bin/env python3

from .brain_games import out_text
from brain_games.rule import question_gcd
from brain_games.cli import run


def main():
    out_text()
    question_gcd()
    name = run()


if __name__ == '__main__':
    main()