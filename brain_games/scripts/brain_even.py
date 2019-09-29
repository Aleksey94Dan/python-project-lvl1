#!/usr/bin/env python3

from .brain_games import out_text
from brain_games.rule import rule
from brain_games.cli import run
from brain_games.logic import point, ATTEMPTS


def main():
    out_text()
    rule()
    print()
    name = run()
    point(ATTEMPTS, name)


if __name__ == '__main__':
    main()
