import unittest
from unittest.mock import patch
from io import StringIO

import TicTacToe


def test_get_player_input():

    # test board one
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}

    test = TicTacToe.get_player_input(board, 'X')


test_get_player_input()
