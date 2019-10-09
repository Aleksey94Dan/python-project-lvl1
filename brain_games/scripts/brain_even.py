#!/usr/bin/env python3

from brain_games.engine import engine, SWITCH_EVEN
from brain_games.games.even import DESCRIPTION_RULE


def main():
    engine(DESCRIPTION_RULE, SWITCH_EVEN)


if __name__ == '__main__':
    main()
