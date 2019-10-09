#!/usr/bin/env python3

from brain_games.engine import engine, SWITCH_PROGRESSION
from brain_games.games.progression import DESCRIPTION_PROGRESSION


def main():
    engine(DESCRIPTION_PROGRESSION, SWITCH_PROGRESSION)


if __name__ == '__main__':
    main()
