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


def welcome_message():
    print(logo)
    print("Welcome to 3d Tic Tac Toe")
    print("Rules:")
    print("1. The game is played on a 3x3x3 grid.")
    print("2. Players take turns placing their marks (X or O) on an empty cell.")
    print("3. The goal is to get three marks in a row, column, or diagonal.")
    print("4. The game ends in a draw if all cells are filled without a winner.")


def main():
    welcome_message()


if __name__ == "__main__":
    main()
