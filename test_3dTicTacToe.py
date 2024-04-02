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


def call_check_for_winner(board):
    return TicTacToe.check_for_win(board)


def test_check_for_winner():
    check_rows()
    check_columns()
    check_vertical()
    check_flat_diagonals()
    check_3d_diagonals_x_is_constant()
    check_3d_diagonals_y_is_constant()
    check_3d_diagonals_nothing_is_constant()


def check_rows():

    print("Testing check_rows")
    # Test case 1:
    board = {'0': ['X', ' ', ' '], '3': ['X', ' ', ' '], '6': ['X', ' ', ' '], '1': ['O', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 1 passed")
    except AssertionError:
        print("Test 1 failed")

    # Test case 2:
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': ['O', ' ', ' '], '4': [
        'O', ' ', ' '], '7': ['O', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 2 passed")
    except AssertionError:
        print("Test 2 failed")

    # Test case 3:
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == False
        print("Test 3 passed")
    except AssertionError:
        print("Test 3 failed")

    # Test case 4:
    board = {'0': ['X', ' ', ' '], '3': ['O', ' ', ' '], '6': ['X', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': ['O', ' ', ' '], '5': ['X', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == False
        print("Test 4 passed")
    except AssertionError:
        print("Test 4 failed")

    # Test case 5:
    board = {'0': ['X', 'O', 'X'], '3': ['X', 'O', ' '], '6': ['O', 'O', ' '], '1': ['O', '', ' '], '4': [
        ' ', ' ', ' '], '7': ['O', ' ', ' '], '2': ['X', 'O', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 5 passed")
    except AssertionError:
        print("Test 5 failed")

    print("\n\n")


def check_columns():
    print("Testing check_columns")
    # Test case 1
    board = {'0': ['X', ' ', ' '], '3': ['O', ' ', ' '], '6': ['X', ' ', ' '], '1': ['X', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': ['X', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 1 passed")
    except AssertionError:
        print("Test 1 failed")

    # Test case 2:
    board = {'0': ['O', 'O', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': ['O', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': ['O', ' ', ' '], '2': ['X', 'O', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 2 passed")
    except AssertionError:
        print("Test 2 failed")

    # Test case 3:
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == False
        print("Test 3 passed")
    except AssertionError:
        print("Test 3 failed")

    # Test case 4:
    board = {'0': ['X', 'O', 'X'], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == False
        print("Test 4 passed")
    except AssertionError:
        print("Test 4 failed")
    print("\n\n")


def check_vertical():
    print("Testing check_vertical")
    # Test case 1:
    board = {'0': ['X', 'X', 'X'], '3': [' ', ' ', ' '], '6': ['X', ' ', ' '], '1': ['O', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 1 passed")
    except AssertionError:
        print("Test 1 failed")

    # Test case 2:
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        'O', 'O', 'O'], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 2 passed")
    except AssertionError:
        print("Test 2 failed")

    # Test case 3:
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == False
        print("Test 3 passed")
    except AssertionError:
        print("Test 3 failed")

    # Test case 4:
    board = {'0': ['X', ' ', ' '], '3': ['O', ' ', ' '], '6': ['X', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': ['O', ' ', ' '], '5': ['X', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == False
        print("Test 4 passed")
    except AssertionError:
        print("Test 4 failed")

    print("\n\n")


def check_flat_diagonals():
    print("Testing check_diagonals")
    # Test case 1:
    board = {'0': ['X', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': ['O', ' ', ' '], '4': [
        'X', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': ['X', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 1 passed")
    except AssertionError:
        print("Test 1 failed")

    # Test case 2:
    board = {'0': [' ', 'X', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', 'X', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', 'X', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 2 passed")
    except AssertionError:
        print("Test 2 failed")

    # Test case 3:
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': ['X', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        'X', ' ', ' '], '7': [' ', ' ', ' '], '2': ['X', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 3 passed")
    except AssertionError:
        print("Test 3 failed")

    # Test case 4:
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', 'X', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', 'X', ' '], '7': [' ', ' ', ' '], '2': [' ', 'X', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}

    try:
        assert call_check_for_winner(board) == True
        print("Test 4 passed")
    except AssertionError:
        print("Test 4 failed")

    print("\n\n")


def check_3d_diagonals_x_is_constant():
    print("Testing check_3d_diagonals x is constant")
    # Test case 1:
    board = {'0': ['X', ' ', ' '], '3': [' ', 'X', ' '], '6': [' ', ' ', 'X'], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 1 passed")
    except AssertionError:
        print("Test 1 failed")

    # Test case 2:
    board = {'0': ['O', 'O', 'X'], '3': ['O', 'X', ' '], '6': ['X', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 2 passed")
    except AssertionError:
        print("Test 2 failed")

    # Test case 3:
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': ['X', ' ', ' '], '4': [
        ' ', 'X', ' '], '7': [' ', ' ', 'X'], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 3 passed")
    except AssertionError:
        print("Test 3 failed")

    # Test case 4:
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', 'X'], '4': [
        ' ', 'X', ' '], '7': ['X', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 4 passed")
    except AssertionError:
        print("Test 4 failed")

    # Test case 5:
    board = {'0': ['X', ' ', ' '], '3': [' ', 'O', ' '], '6': [' ', ' ', 'X'], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == False
        print("Test 5 passed")
    except AssertionError:
        print("Test 5 failed")

    print("\n\n")


def check_3d_diagonals_y_is_constant():
    print("Testing check_3d_diagonals y is constant")
    # Test case 1:
    board = {'0': ['X', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', 'X', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', 'X'], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 1 passed")
    except AssertionError:
        print("Test 1 failed")

    # Test case 2:
    board = {'0': [' ', ' ', 'X'], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': ['X', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': ['X', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 2 passed")
    except AssertionError:
        print("Test 2 failed")

    # Test case 3:
    board = {'0': [' ', ' ', ' '], '3': ['X', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', 'X', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', 'X'], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 3 passed")
    except AssertionError:
        print("Test 3 failed")

    # Test case 4:
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', 'X'], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', 'X', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': ['X', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 4 passed")
    except AssertionError:
        print("Test 4 failed")

    # Test case 5:
    board = {'0': ['X', ' ', ' '], '3': [' ', 'O', ' '], '6': [' ', ' ', 'X'], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == False
        print("Test 5 passed")
    except AssertionError:
        print("Test 5 failed")

    print("\n\n")


def check_3d_diagonals_nothing_is_constant():
    print("Testing check_3d_diagonals nothing is constant")
    # Test case 1:
    board = {'0': ['X', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', 'X', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', 'X']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 1 passed")
    except AssertionError:
        print("Test 1 failed")

    # Test case 2:
    board = {'0': ['O', 'O', 'X'], '3': [' ', ' ', ' '], '6': [' ', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        'O', 'X', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': ['X', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 2 passed")
    except AssertionError:
        print("Test 2 failed")

    # Test case 3:
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', ' '], '6': [' ', ' ', 'X'], '1': [' ', ' ', ' '], '4': [
        ' ', 'X', ' '], '7': [' ', ' ', ' '], '2': ['X', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 3 passed")
    except AssertionError:
        print("Test 3 failed")

    # Test case 4:
    board = {'0': [' ', ' ', ' '], '3': [' ', ' ', 'X'], '6': ['X', ' ', ' '], '1': [' ', ' ', ' '], '4': [
        ' ', 'X', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', 'X'], '5': ['X', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == True
        print("Test 4 passed")
    except AssertionError:
        print("Test 4 failed")

    # Test case 5:
    board = {'0': ['X', ' ', ' '], '3': [' ', 'O', ' '], '6': [' ', ' ', 'X'], '1': [' ', ' ', ' '], '4': [
        ' ', ' ', ' '], '7': [' ', ' ', ' '], '2': [' ', ' ', ' '], '5': [' ', ' ', ' '], '8': [' ', ' ', ' ']}
    try:
        assert call_check_for_winner(board) == False
        print("Test 5 passed")
    except AssertionError:
        print("Test 5 failed")

    print("\n\n")


test_check_for_winner()
