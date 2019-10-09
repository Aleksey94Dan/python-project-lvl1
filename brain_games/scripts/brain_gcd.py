#!/usr/bin/env python3

from brain_games.engine import engine, SWITCH_GCD
from brain_games.games.gcd import DESCRIPTION_GCD


def main():
    engine(DESCRIPTION_GCD, SWITCH_GCD)


if __name__ == '__main__':
    main()
