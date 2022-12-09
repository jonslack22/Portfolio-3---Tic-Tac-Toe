import random


def create_grid(grid):
    """
    This function prints out the grid that it was passed. A
    list of 10 strings represents the grid. Index 0 is ignored.
    """
    print('   |   |')
    print(' ' + grid[7] + ' | ' + grid[8] + ' | ' + grid[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + grid[4] + ' | ' + grid[5] + ' | ' + grid[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + grid[1] + ' | ' + grid[2] + ' | ' + grid[3])
    print('   |   |')


def choose_letter():
    """
    This function lets the player choose which letter they want to be, 
    returning a list with the player’s letter as the first item, and the 
    computer's letter as the second.
    
    The first element in the list is the player’s letter, the second is the 
    computer's letter.
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


print(
    """
    \u001b[32m
   _____ _        _____            _____          
  |_   _(_)      |_   _|          |_   _|         
    | |  _  ___    | | __ _  ___    | | ___   ___ 
    | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ |
    | | | | (__    | | (_| | (__    | | (_) |  __/
    \_/ |_|\___|   \_/\__,_|\___|   \_/\___/ \___|
\u001b[0m
""")


print("Welcome to Jonathan Slack's Tic Tac Toe!\n")
print("RULES: Using a format of a human versus computer, take turns "
      "marking a space in a 3*3 grid. The player who succeeds in placing "
      "three marks, represented by X and 0, in a horizontal, "
      "vertical, or diagonal row, wins.\n")
input("Press enter to continue.\n")

while True:
    """
    This 'while' loop resets the grid on starting the game and executes
    the game's functions so long as the loop returns True.
    """
    while game_active:
        if turn == 'player':
            # The player’s turn.
            create_grid(the_grid)
