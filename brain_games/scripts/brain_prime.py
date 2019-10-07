#!/usr/bin/env python3

from .brain_games import out_text
from brain_games.rule import question_prime
from brain_games.cli import run
from brain_games.logic import point, ATTEMPTS, SWITCH_PRIME


def main():
    out_text()
    question_prime()
    name = run()
    point(ATTEMPTS, name, SWITCH_PRIME)


if __name__ == '__main__':
    main()
