# My 3d tic tac toe
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

BOARD_SIZE = 3
MIN_POSITION_SIZE = 0


def welcome_message():
    print(logo)
    print("Welcome to 3d Tic Tac Toe")
    print("Rules:")
    print("1. The game is played on a 3d grid.")
    print("2. Players take turns placing their marks (X or O) on an empty cell.")
    print("3. The goal is to get three marks in a row, column, or diagonal.")
    print("4. The game ends in a draw if all cells are filled without a winner.")


def generate_starting_board():
    global BOARD_SIZE
    board = {}
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):  # Added parentheses to close the dictionary update statement
            board.update({f"{i*BOARD_SIZE+j}": [' '] * BOARD_SIZE})

    return board


def get_player_input(board):
    global BOARD_SIZE
    position = {}
    cords = ["x", "y"]

    cord_is_available = False
    while cord_is_available == False:
        for cord in cords:
            gotten_player_input = False
            while gotten_player_input == False:
                try:
                    position.update(
                        {cord: (
                            -1 + int(input(f"Please enter the {cord} position between 1 and {BOARD_SIZE}: \n")))}
                    )
                except ValueError:
                    print("Please enter a valid number")
                if 0 <= position[cord] < BOARD_SIZE:
                    gotten_player_input = True
                else:
                    print("Please enter a number in the desired range")

        if check_that_position_is_clear(board, position) == True:
            cord_is_available = True
        else:
            print("Your position has already been taken, please try again\n")

    return position


def check_that_position_is_clear(board, position):
    global BOARD_SIZE
    if board[f"{position["x"]*BOARD_SIZE + position["y"]}"][BOARD_SIZE-1] == ' ':
        return True
    else:
        return False


def update_board(board, piece, position):
    global BOARD_SIZE
    for i in range(BOARD_SIZE):
        if position[f"{position["x"]*BOARD_SIZE + position["y"]}"][i] == ' ':
            position[f"{position["x"]*BOARD_SIZE + position["y"]}"][i] == ' ':

    board[f"{position['x']*BOARD_SIZE + position['y']}"][position['z']] = piece


def player_turn(board, current_player):
    position = get_player_input(board)
    piece = 'x'
    board = update_board(board, piece, position)


def main():

    board = {}
    welcome_message()
    board = generate_starting_board()
    print(board)
    player_turn(board, 1)


if __name__ == "__main__":
    main()
