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


def test_update_board():

    # test 1 board index is empty boundary case 1
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}

    test = TicTacToe.update_board(board, 'X', '0')

    try:
        assert test['0'] == ['X', ' ', ' ']
        print("Test 1 passed")
    except AssertionError:
        print("Test 1 failed")

    # test 2 board index is empty boundary case 2

    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}

    test = TicTacToe.update_board(board, 'X', '8')

    try:
        assert test['8'] == ['X', ' ', ' ']
        print("Test 2 passed")
    except AssertionError:
        print("Test 2 failed")

    # test 3 board index is partially full expected case

    board = {'0': ['X', 'O', ' '], '3': ['X', 'O', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': ['X', 'X', ' '], '2': [' ', ' ', ' '], '5': ['X', 'O', ' '], '8': [' ', ' ', ' ']}
    test = TicTacToe.update_board(board, 'X', '0')
    try:
        assert test['0'] == ['X', 'O', 'X']
        print("Test 3 passed")
    except AssertionError:
        print("Test 3 failed")

    # test 4 board index is partially full expected case

    board = {'0': ['X', 'O', ' '], '3': ['X', 'O', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': ['X', 'X', ' '], '2': [' ', ' ', ' '], '5': ['X', ' ', ' '], '8': [' ', ' ', ' ']}
    test = TicTacToe.update_board(board, 'X', '5')
    try:
        assert test['5'] == ['X', 'X', ' ']
        print("Test 4 passed")
    except AssertionError:
        print("Test 4 failed")


test_update_board()
