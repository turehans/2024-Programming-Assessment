import random

# My 3d tic tac toe
# Define the logo for the game
logo = """
 ______   ______    __________________ _______   _________ _______  _______   _________ _______  _______ 
/ ___  \ (  __  \   \__   __/\__   __/(  ____ \  \__   __/(  ___  )(  ____ \  \__   __/(  ___  )(  ____ \\
\/   \  \| (  \  )     ) (      ) (   | (    \/     ) (   | (   ) || (    \/     ) (   | (   ) || (    \/
   ___) /| |   ) |     | |      | |   | |           | |   | (___) || |           | |   | |   | || (__    
  (___ ( | |   | |     | |      | |   | |           | |   |  ___  || |           | |   | |   | ||  __)   
      ) \| |   ) |     | |      | |   | |           | |   | (   ) || |           | |   | |   | || (      
/\___/  /| (__/  )     | |   ___) (___| (____/\     | |   | )   ( || (____/\     | |   | (___) || (____/\\
\______/ (______/      )_(   \_______/(_______/     )_(   |/     \|(_______/     )_(   (_______)(_______/
                                                                                                         
"""

# Define the size of the board

BOARD_SIZE = 3


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
    global BOARD_SIZE
    print('')
    # Print the horizontal lines
    for i in range(1 + (2*BOARD_SIZE)):
        print(' _', end='')
    print("\n")
    for y_cord in range(BOARD_SIZE):
        print('|', end='')
        for x_cord in range(BOARD_SIZE):
            index = str(x_cord*BOARD_SIZE + y_cord)
            # Print the cell value
            print(f" {index} ", end='|')
        print('\n', end='')
        # Print the horizontal lines
        for i in range(1 + (2*BOARD_SIZE)):
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
    global BOARD_SIZE

    # Check rows
    for z_cord in range(BOARD_SIZE):
        for x_cord in range(BOARD_SIZE):
            row = []
            for y_cord in range(BOARD_SIZE):
                index = str(x_cord * BOARD_SIZE + y_cord)
                row.append(board[index][z_cord])
            # If all elements in the row are the same and not empty, there is a winner
            if len(set(row)) == 1 and row[0] != ' ':
                return True

    # Check columns
    for z_cord in range(BOARD_SIZE):
        for y_cord in range(BOARD_SIZE):
            column = []
            for x_cord in range(BOARD_SIZE):
                index = str(x_cord * BOARD_SIZE + y_cord)
                column.append(board[index][z_cord])
            # If all elements in the column are the same and not empty, there is a winner
            if len(set(column)) == 1 and column[0] != ' ':
                return True

    # check vertical
    for x_cord in range(BOARD_SIZE):
        for y_cord in range(BOARD_SIZE):
            vertical = []
            index = str(x_cord * BOARD_SIZE + y_cord)
            for z_cord in range(BOARD_SIZE):
                vertical.append(board[index][z_cord])
            # if all elements in the column are the same and not empty, there is a winner
            if len(set(vertical)) == 1 and vertical[0] != ' ':
                return True

    # Check diagonals
    for z_cord in range(BOARD_SIZE):
        diagonal1 = []
        diagonal2 = []
        for i in range(BOARD_SIZE):
            index1 = str(i * BOARD_SIZE + i)
            index2 = str(i * BOARD_SIZE + (BOARD_SIZE - 1 - i))
            diagonal1.append(board[index1][z_cord])
            diagonal2.append(board[index2][z_cord])
        # If all elements in the diagonal1 are the same and not empty, there is a winner
        if len(set(diagonal1)) == 1 and diagonal1[0] != ' ':
            return True
        # If all elements in the diagonal2 are the same and not empty, there is a winner
        if len(set(diagonal2)) == 1 and diagonal2[0] != ' ':
            return True

    # Check diagonals x stays constant
    print("Testing now")
    for x_cord in range(BOARD_SIZE):
        diagonal1 = []
        diagonal2 = []
        for i in range(BOARD_SIZE):
            index1 = str(x_cord*BOARD_SIZE + i)
            index2 = str(x_cord * BOARD_SIZE + (BOARD_SIZE - 1 - i))
            diagonal1.append(board[index1][i])
            diagonal2.append(board[index2][i])
        # If all elements in the diagonal1 are the same and not empty, there is a winner
        if len(set(diagonal1)) == 1 and diagonal1[0] != ' ':
            return True
        # If all elements in the diagonal2 are the same and not empty, there is a winner
        if len(set(diagonal2)) == 1 and diagonal2[0] != ' ':
            return True

    # Check diagonals y stays constant
    for y_cord in range(BOARD_SIZE):
        diagonal1 = []
        diagonal2 = []
        for i in range(BOARD_SIZE):
            index1 = str(i * BOARD_SIZE + y_cord)
            index2 = str(i * BOARD_SIZE + (BOARD_SIZE - 1 - y_cord))
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
    for i in range(BOARD_SIZE):
        # bottom left
        index1 = str(i * BOARD_SIZE + i)
        # top right
        index2 = str(i * BOARD_SIZE + (BOARD_SIZE - 1 - i))
        # bottom right
        index3 = str((BOARD_SIZE - 1 - i) *
                     BOARD_SIZE + (BOARD_SIZE - 1 - i))
        # top left
        index4 = str((BOARD_SIZE - 1 - i) * BOARD_SIZE + i)

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
    global BOARD_SIZE
    board = {}
    for x_cord in range(BOARD_SIZE):
        for y_cord in range(BOARD_SIZE):
            # Initialize each cell with an empty space
            board.update({f"{x_cord*BOARD_SIZE+y_cord}": [' '] * BOARD_SIZE})

    return board


def print_board(board):
    """
    Prints the 3D Tic Tac Toe board.

    Args:
        board (dict): The game board represented as a dictionary.

    Returns:
        None
    """

    global BOARD_SIZE
    for z_cord in range(BOARD_SIZE):
        print('')
        # Print the horizontal lines
        for i in range(1 + (2*BOARD_SIZE)):
            print(' _', end='')
        print("\n")
        for y_cord in range(BOARD_SIZE):
            print('|', end='')
            for x_cord in range(BOARD_SIZE):
                index = str(x_cord*BOARD_SIZE + y_cord)
                # Print the cell value
                print(f" {board[index][z_cord]} ", end='|')
            print('\n', end='')
            # Print the horizontal lines
            for i in range(1 + (2*BOARD_SIZE)):
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
    global BOARD_SIZE
    position = {}  # Create an empty dictionary to store the player's position
    cords = ["x", "y"]  # Define the coordinates as 'x' and 'y'

    cord_is_available = False  # Initialize a flag to check if the position is available
    while cord_is_available == False:  # Continue looping until a valid position is entered
        for cord in cords:  # Iterate through the coordinates
            # Initialize a flag to check if the player's input is valid
            gotten_player_input = False
            while gotten_player_input == False:  # Continue looping until a valid input is entered
                try:
                    # Prompt the player to enter the position and convert it to an integer
                    position.update(
                        {cord: (-1 + int(input(f"\nPlease enter the {cord} position between 1 and {BOARD_SIZE}: \n")))}
                    )
                except ValueError:
                    print("\nPlease enter a valid number")
                # Check if the entered position is within the desired range
                if 0 <= position[cord] < BOARD_SIZE:
                    gotten_player_input = True  # Set the flag to True if the input is valid
                else:
                    print("\nPlease enter a number in the desired range")

        # Calculate the index based on the entered positions
        index = str(position['x']*BOARD_SIZE + position['y'])
        # Check if the position is clear
        if check_that_position_is_clear(board, index) == True:
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
    global BOARD_SIZE
    if board[index][BOARD_SIZE-1] == ' ':  # Check if the first position in the row is empty
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
    global BOARD_SIZE
    for i in range(BOARD_SIZE):
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


def game_loop(board, piece):
    """
    This function represents the main game loop.
    It takes the current game board and the current player as input.
    It alternates between players, prompts for player input, and updates the board.
    If a player wins, it prints a congratulatory message and returns.
    """
    print_board(board)  # Print the current game board

    if check_for_win(board) == False:  # Check if there is no winner yet
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


def main():
    """
    This function represents the main entry point of the program.
    """
    board = {}
    welcome_message()
    board = generate_starting_board()
    test_board()
    # print(board)

    piece = 'X'
    game_loop(board, piece)


if __name__ == "__main__":
    main()
