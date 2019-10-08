#!/usr/bin/env python3

from .brain_games import out_text
from brain_games.games.rule import rule
from brain_games.cli import run
from brain_games.games.logic import point, ATTEMPTS, SWITCH_EVEN


def main():
    out_text()
    rule()
    name = run()
    point(ATTEMPTS, name, SWITCH_EVEN)


if __name__ == '__main__':
    main()
