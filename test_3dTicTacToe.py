import unittest
from unittest.mock import patch
from io import StringIO

import TicTacToe


def test_get_player_input(board):

    test = TicTacToe.get_player_input(board, 'X')
    return test


def board_spot_full_test_get_player_input():
    # test board one
    board = {'0': ['X', 'O', 'X'], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}

    test_get_player_input(board)


def user_input_test_get_player_input():
    # test board one
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}

    for x in range(5):
        test_get_player_input(board)
        print("\n\n\nNext test\n\n\n")


def check_index_is_returned_correctly_get_player_input():

    # index calculated by position['x']*BOARD_SIZE + position['y']

    # test board one
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}

    print("Test 1")
    print("x = 1, y = 1")
    try:
        assert test_get_player_input(board) == '0'
        print("Test 1 passed")
    except AssertionError:
        print("Test 1 failed")

    print("\n\nTest 2")
    print("x = 2, y = 1")
    try:
        assert test_get_player_input(board) == '3'
        print("Test 2 passed")
    except AssertionError:
        print("Test 2 failed")

    print("\n\nTest 3")
    print("x = 3, y = 1")
    try:
        assert test_get_player_input(board) == '6'
        print("Test 3 passed")
    except AssertionError:
        print("Test 3 failed")

    print("\n\nTest 4")
    print("x = 1, y = 3")
    try:
        assert test_get_player_input(board) == '2'
        print("Test 4 passed")
    except AssertionError:
        print("Test 4 failed")

    print("\n\nTest 5")
    print("x = 3, y = 3")
    try:
        assert test_get_player_input(board) == '8'
        print("Test 5 passed")
    except AssertionError:
        print("Test 5 failed")
