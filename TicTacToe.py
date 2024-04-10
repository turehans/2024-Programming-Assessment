import random

# My 3d tic tac toe
# Define the logo for the game
logo = """
   ____   ______    __________________ _______   _________ _______  _______   _________ _______  _______
/ ___  \ (  __  \   \__   __/\__   __/(  ____ \  \__   __/(  ___  )(  ____ \  \__   __/(  ___  )(  ____ \\
\/   \  \| (  \  )     ) (      ) (   | (    \/     ) (   | (   ) || (    \/     ) (   | (   ) || (    \/
   ___) /| |   ) |     | |      | |   | |           | |   | (___) || |           | |   | |   | || (__
  (___ ( | |   | |     | |      | |   | |           | |   |  ___  || |           | |   | |   | ||  __)
      ) \| |   ) |     | |      | |   | |           | |   | (   ) || |           | |   | |   | || (
/\___/  /| (__/  )     | |   ___) (___| (____/\     | |   | )   ( || (____/\     | |   | (___) || (____/\\
\______/ (______/      )_(   \_______/(_______/     )_(   |/     \|(_______/     )_(   (_______)(_______/
"""

# Define the size of the board

board_size = 3
MIN_BOARD_SIZE = 3
MAX_BOARD_SIZE = 10


# Function to display the welcome message
def welcome_message():
    print(logo)  # Print the game logo
    print("Welcome to 3d Tic Tac Toe")
    print("Rules:")
    print("1. The game is played on a 3d grid.")
    print("2. Players take turns placing their marks (X or O) on an empty cell.")
    print("3. The goal is to get three marks in a row, column, or diagonal.")
    print("4. The game ends in a draw if all cells are filled without a winner.\n", end='\n')


def test_board():
    global board_size
    print('')
    # Print the horizontal lines
    for i in range(1 + (2*board_size)):
        print(' _', end='')
    print("\n")
    for y_cord in range(board_size):
        print('|', end='')
        for x_cord in range(board_size):
            index = str(x_cord*board_size + y_cord)
            # Print the cell value
            print(f" {index} ", end='|')
        print('\n', end='')
        # Print the horizontal lines
        for i in range(1 + (2*board_size)):
            print(' _', end='')
        print("\n")


def check_for_win(board):
    """
    Checks if there is a winner in the game.

    Args:
        board (dict): The game board represented as a dictionary.

    Returns:
        bool: True if there is a winner, False otherwise.
    """
    global board_size

    # Check rows
    for z_cord in range(board_size):
        for x_cord in range(board_size):
            row = []
            for y_cord in range(board_size):
                index = str(x_cord * board_size + y_cord)
                row.append(board[index][z_cord])
            # If all elements in the row are the same and not empty, there is a winner
            if len(set(row)) == 1 and row[0] != ' ':
                return True

    # Check columns
    for z_cord in range(board_size):
        for y_cord in range(board_size):
            column = []
            for x_cord in range(board_size):
                index = str(x_cord * board_size + y_cord)
                column.append(board[index][z_cord])
            # If all elements in the column are the same and not empty, there is a winner
            if len(set(column)) == 1 and column[0] != ' ':
                return True

    # check vertical
    for x_cord in range(board_size):
        for y_cord in range(board_size):
            vertical = []
            index = str(x_cord * board_size + y_cord)
            for z_cord in range(board_size):
                vertical.append(board[index][z_cord])
            # if all elements in the column are the same and not empty, there is a winner
            if len(set(vertical)) == 1 and vertical[0] != ' ':
                return True

    # Check diagonals
    for z_cord in range(board_size):
        diagonal1 = []
        diagonal2 = []
        for i in range(board_size):
            index1 = str(i * board_size + i)
            index2 = str(i * board_size + (board_size - 1 - i))
            diagonal1.append(board[index1][z_cord])
            diagonal2.append(board[index2][z_cord])
        # If all elements in the diagonal1 are the same and not empty, there is a winner
        if len(set(diagonal1)) == 1 and diagonal1[0] != ' ':
            return True
        # If all elements in the diagonal2 are the same and not empty, there is a winner
        if len(set(diagonal2)) == 1 and diagonal2[0] != ' ':
            return True

    # Check diagonals y stays constant
    print()
    for y_cord in range(board_size):
        diagonal1 = []
        diagonal2 = []
        for i in range(board_size):
            index1 = str(i * board_size + y_cord)
            index2 = str((board_size - i - 1) * board_size + y_cord)
            diagonal1.append(board[index1][i])
            diagonal2.append(board[index2][i])
        # If all elements in the diagonal1 are the same and not empty, there is a winner
        if len(set(diagonal1)) == 1 and diagonal1[0] != ' ':
            return True
        # If all elements in the diagonal2 are the same and not empty, there is a winner
        if len(set(diagonal2)) == 1 and diagonal2[0] != ' ':
            return True

    # Check diagonals x stays constant
    for x_cord in range(board_size):
        diagonal1 = []
        diagonal2 = []
        for i in range(board_size):
            index1 = str(x_cord * board_size + i)
            index2 = str(x_cord * board_size + (board_size - 1 - i))
            diagonal1.append(board[index1][i])
            diagonal2.append(board[index2][i])
        # If all elements in the diagonal1 are the same and not empty, there is a winner
        if len(set(diagonal1)) == 1 and diagonal1[0] != ' ':
            return True
        # If all elements in the diagonal2 are the same and not empty, there is a winner
        if len(set(diagonal2)) == 1 and diagonal2[0] != ' ':
            return True

    # Check diagonals where x and y and z are changing
    diagonal1 = []
    diagonal2 = []
    diagonal3 = []
    diagonal4 = []
    for i in range(board_size):
        # bottom left
        index1 = str(i * board_size + i)
        # top right
        index2 = str(i * board_size + (board_size - 1 - i))
        # bottom right
        index3 = str((board_size - 1 - i) *
                     board_size + (board_size - 1 - i))
        # top left
        index4 = str((board_size - 1 - i) * board_size + i)

        diagonal1.append(board[index1][i])
        diagonal2.append(board[index2][i])
        diagonal3.append(board[index3][i])
        diagonal4.append(board[index4][i])

    # If all elements in the diagonal1 are the same and not empty, there is a winner
    if len(set(diagonal1)) == 1 and diagonal1[0] != ' ':
        return True
    # If all elements in the diagonal2 are the same and not empty, there is a winner
    if len(set(diagonal2)) == 1 and diagonal2[0] != ' ':
        return True
    # If all elements in the diagonal3 are the same and not empty, there is a winner
    if len(set(diagonal3)) == 1 and diagonal3[0] != ' ':
        return True
    # If all elements in the diagonal4 are the same and not empty, there is a winner
    if len(set(diagonal4)) == 1 and diagonal4[0] != ' ':
        return True

    # If no winner is found, return False
    return False


# Function to generate the starting board

def generate_starting_board():
    """
    Generates the starting board for a 3D Tic Tac Toe game.

    Returns:
        dict: The starting board represented as a dictionary.
    """
    global board_size
    board = {}
    for x_cord in range(board_size):
        for y_cord in range(board_size):
            # Initialize each cell with an empty space
            board.update({f"{x_cord*board_size+y_cord}": [' '] * board_size})

    return board


def print_board(board):
    """
    Prints the 3D Tic Tac Toe board.

    Args:
        board (dict): The game board represented as a dictionary.

    Returns:
        None
    """

    global board_size
    for z_cord in range(board_size):
        print('')
        # Print the horizontal lines
        for i in range(1 + (2*board_size)):
            print(' _', end='')
        print("\n")
        for y_cord in range(board_size):
            print('|', end='')
            for x_cord in range(board_size):
                index = str(x_cord*board_size + y_cord)
                # Print the cell value
                print(f" {board[index][z_cord]} ", end='|')
            print('\n', end='')
            # Print the horizontal lines
            for i in range(1 + (2*board_size)):
                print(' _', end='')
            print("\n")


def get_player_input(board, current_player):
    """
    Prompts the player to enter the x and y positions on the board and returns the index of the position.

    Args:
        board (list): The game board.

    Returns:
        str: The index of the position on the board.

    Raises:
        ValueError: If the player enters an invalid number.

    """

    print(f"Player {current_player} it is your turn\n")

    # Define the size of the board
    global board_size
    position = {}  # Create an empty dictionary to store the player's position
    cords = ["x", "y"]  # Define the coordinates as 'x' and 'y'

    cord_is_available = False  # Initialize a flag to check if the position is available
    while cord_is_available is False:  # Continue looping until a valid position is entered
        for cord in cords:  # Iterate through the coordinates
            # Initialize a flag to check if the player's input is valid
            gotten_player_input = False
            while gotten_player_input is False:  # Continue looping until a valid input is entered
                try:
                    # Prompt the player to enter the position and convert it to an integer
                    user_input = input(
                        f"\nPlease enter the {cord} position between 1 and {board_size}: ").strip()

                    if user_input == "" or user_input is None:
                        raise ValueError("Empty input")

                    position.update({cord: (-1 + int(user_input))})
                except ValueError:
                    print("\nPlease enter a valid number")
                    continue

                # Check if the entered position is within the desired range
                if 0 <= position[cord] < board_size:
                    gotten_player_input = True  # Set the flag to True if the input is valid
                else:
                    print("\nPlease enter a number in the desired range")

        # Calculate the index based on the entered positions
        index = str(position['x']*board_size + position['y'])
        # Check if the position is clear
        if check_that_position_is_clear(board, index) is True:
            cord_is_available = True  # Set the flag to True if the position is available
        else:
            print("Your position has already been taken, please try again\n")
    return index  # Return the index of the chosen position


def check_that_position_is_clear(board, index):
    """
    Check if a position on the board is clear.

    Args:
        board (list): The game board.
        index (int): The index of the position to check.

    Returns:
        bool: True if the position is clear, False otherwise.
    """
    global board_size
    if board[index][board_size-1] == ' ':  # Check if the first position in the row is empty
        return True
    else:
        return False


# Function to update the game board with the player's piece at the specified index
def update_board(board, piece, index):
    """
    Updates the game board with the player's piece at the specified index.

    Args:
        board (list): The game board.
        piece (str): The player's piece ('X' or 'O').
        index (int): The index of the row to update.

    Returns:
        list: The updated game board.
    """
    global board_size
    for i in range(board_size):
        if board[index][i] == ' ':  # Check if the position is empty
            board[index][i] = piece  # Place the player's piece at the position
            return board
    return board


def player_turn(board, piece):
    """
    Takes the current game board and the current player as input.
    Prompts the player for their desired position on the board.
    Updates the game board with the player's piece at the specified position.
    Returns the updated game board.
    """
    index = get_player_input(
        board, piece)  # Get the player's input for the desired position

    # Update the game board with the player's piece at the specified index
    board = update_board(board, piece, index)
    return board


def choose_board_size():
    global board_size
    gotten_input = False

    while gotten_input is False:

        try:
            user_input = input("Please enter the size of the board: ").strip()
            if user_input == "" or user_input is None:
                raise ValueError("Empty input", end='\n\n')
            elif int(user_input) < MIN_BOARD_SIZE:
                print("Board size should be greater than 2", end='\n\n')
            elif int(user_input) > MAX_BOARD_SIZE:
                print("Board size should be less than 11", end='\n\n')
            else:
                board_size = int(user_input)
                gotten_input = True

        except ValueError:
            print("Please enter a valid number")
            continue


def game_loop(board, piece):
    """
    This function represents the main game loop.
    It takes the current game board and the current player as input.
    It alternates between players, prompts for player input, and updates the board.
    If a player wins, it prints a congratulatory message and returns.
    """
    print_board(board)  # Print the current game board

    if check_for_win(board) is False:  # Check if there is no winner yet
        # Prompt the current player for their turn
        board = player_turn(board, piece)
    else:

        if piece == 'X':  # Switch to the next player
            piece = 'O'
        else:
            piece = 'X'

        # Print a congratulatory message
        print(f"Congrates Player {piece}, you won.")
        return  # Exit the game loop if a player wins

    if piece == 'X':  # Switch to the next player
        piece = 'O'
    else:
        piece = 'X'

    # Recursively call the game loop with the updated board and player
    game_loop(board, piece)


def check_if_player_wants_to_play_again():
    """
    Prompts the player to play again or quit the game.

    Returns:
        bool: True if the player wants to play again, False otherwise.
    """
    print("\n")
    try:
        play_again = input("Do you want to play again? (yes/no): ")
    except ValueError:
        print("Please enter a valid input")

    play_again.lower()

    if play_again == 'yes':
        return True
    elif play_again == 'no':
        return False
    else:
        print("Please enter yes or no")
        check_if_player_wants_to_play_again()


def main():
    """
    This function represents the main entry point of the program.
    """
    welcome_message()

    game_active = True  # Initialize the game flag to True

    while game_active is True:  # Continue looping while the game is active
        board = {}

        # ask for board size
        choose_board_size()

        board = generate_starting_board()
        piece = 'X'

        game_loop(board, piece)

        # Prompt the player to play again
        if check_if_player_wants_to_play_again() is True:
            game_active = True
        else:
            game_active = False
            print("\nThank you for playing 3D Tic Tac Toe")


if __name__ == "__main__":
    main()
