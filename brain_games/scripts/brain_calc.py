#!/usr/bin/env python3

from brain_games.engine import engine, SWITCH_CALC
from brain_games.games.calc import DESCRIPTION_RULE


def main():
    engine(DESCRIPTION_RULE, SWITCH_CALC)


if __name__ == '__main__':
    main()
