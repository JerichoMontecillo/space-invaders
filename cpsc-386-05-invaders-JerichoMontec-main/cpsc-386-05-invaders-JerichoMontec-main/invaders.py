#!/usr/bin/env python3

"""
Imports the the game demo and executes the main function.
"""

import sys
from videogame import game

if __name__ == "__main__":
    my_game = game.MyVideoGame(0, 3, 1)
    RETURN_VALUE = my_game.run()
    sys.exit(0)
