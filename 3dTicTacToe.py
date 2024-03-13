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
MIN_POSITION_SIZE = 0


# Function to display the welcome message
def welcome_message():
    print(logo)  # Print the game logo
    print("Welcome to 3d Tic Tac Toe")
    print("Rules:")
    print("1. The game is played on a 3d grid.")
    print("2. Players take turns placing their marks (X or O) on an empty cell.")
    print("3. The goal is to get three marks in a row, column, or diagonal.")
    print("4. The game ends in a draw if all cells are filled without a winner.\n", end='\n')


# Function to generate the starting board
def generate_starting_board():
    """
    Generates the starting board for a 3D Tic Tac Toe game.

    Returns:
        dict: The starting board represented as a dictionary.
    """
    # Function to generate the starting board
    def generate_starting_board():
        """
        Generates the starting board for a 3D Tic Tac Toe game.

        Returns:
            dict: The starting board represented as a dictionary.
        """
        global BOARD_SIZE
        board = {}
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                # Initialize each cell with an empty space
                board.update({f"{i*BOARD_SIZE+j}": [' '] * BOARD_SIZE})

        return board


def print_board(board):
    """
    Prints the 3D Tic Tac Toe board.

    Args:
        board (dict): The game board represented as a dictionary.

    Returns:
        None
    """

    # Function to print the 3D Tic Tac Toe board
    def print_board(board):
        global BOARD_SIZE
        for z_cord in range(BOARD_SIZE):
            print('')
            # Print the horizontal lines
            for i in range(1 + (2*BOARD_SIZE)):
                print(' _', end='')
            print("\n")
            for x_cord in range(BOARD_SIZE):
                print('|', end='')
                for y_cord in range(BOARD_SIZE):
                    index = str(x_cord*BOARD_SIZE + y_cord)
                    # Print the cell value
                    print(f" {board[index][z_cord]} ", end='|')
                print('\n', end='')
                # Print the horizontal lines
                for i in range(1 + (2*BOARD_SIZE)):
                    print(' _', end='')
                print("\n")


def get_player_input(board):
    """
    Prompts the player to enter the x and y positions on the board and returns the index of the position.

    Args:
        board (list): The game board.

    Returns:
        str: The index of the position on the board.

    Raises:
        ValueError: If the player enters an invalid number.

    """

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
                        {cord: (-1 + int(input(f"Please enter the {cord} position between 1 and {BOARD_SIZE}: \n")))}
                    )
                except ValueError:
                    print("Please enter a valid number")
                # Check if the entered position is within the desired range
                if 0 <= position[cord] < BOARD_SIZE:
                    gotten_player_input = True  # Set the flag to True if the input is valid
                else:
                    print("Please enter a number in the desired range")

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


def player_turn(board, current_player):
    """
    Takes the current game board and the current player as input.
    Prompts the player for their desired position on the board.
    Updates the game board with the player's piece at the specified position.
    Returns the updated game board.
    """
    index = get_player_input(
        board)  # Get the player's input for the desired position
    piece = 'x'  # Set the player's piece to 'x'
    # Update the game board with the player's piece at the specified index
    board = update_board(board, piece, index)
    return board


def main():
    """
    This function represents the main entry point of the program.
    It initializes the game board, displays the welcome message,
    and allows players to take turns until the game is over.
    """
    board = {}
    welcome_message()
    board = generate_starting_board()
    print_board(board)

    board = player_turn(board, 1)
    print_board(board)


if __name__ == "__main__":
    main()
