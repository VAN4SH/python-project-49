#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from brain_games.games.engine import play
from brain_games.games import brain_calc


def main():
    """Run game."""
    play(brain_calc)


if __name__ == "__main__":
    main()
