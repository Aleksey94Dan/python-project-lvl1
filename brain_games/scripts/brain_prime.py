#!/usr/bin/env python3

from brain_games.engine import engine, SWITCH_PRIME
from brain_games.games.prime import DESCRIPTION_RULE


def main():
    engine(DESCRIPTION_RULE, SWITCH_PRIME)


if __name__ == '__main__':
    main()
