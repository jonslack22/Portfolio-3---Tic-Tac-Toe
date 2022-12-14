# Project libraries
import random
import os
import sys


C = "{:^80}".format
C2 = "{:^82}".format
C3 = "{:^83}".format
BR = "\n"


def clear_console():
    """
    Clears the console.
    """
    # This line is credited to
    # https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    os.system("cls" if os.name == "nt" else "clear")


def restart():
    """
    Restarts game to clear the board
    """
    # This line is credited to
    # https://stackoverflow.com/questions/62248430/restart-function-in-python
    os.execl(sys.executable, sys.executable, *sys.argv)


def intro_message():
    clear_console()
    # This function displays a welcome message in every new game instance
    print(
        """\
    \u001b[32m
               _____ _        _____            _____          
              |_   _(_)      |_   _|          |_   _|
                | |  _  ___    | | __ _  ___    | | ___   ___ 
                | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ |
                | | | | (__    | | (_| | (__    | | (_) |  __/
                \_/ |_|\___|   \_/\__,_|\___|   \_/\___/ \___|
\u001b[0m
""")

    print(C("Welcome to Jonathan Slack's Tic Tac Toe!\n"))
    print(C("RULES: Take turns marking spaces in a 3*3 grid against a computer "
            "opponent.\n"))
    print(C("The player who succeeds in placing three marks, represented by X "
            "and 0, in a horizontal, "))
    print(C("vertical, or diagonal row, wins.\n"))
    input(C("Press Enter to continue.\n"))
    clear_console()


def create_grid(grid):
    """
    This function prints out the grid that it was passed. A
    list of 10 strings represents the grid. Index 0 is ignored.
    """
    print(C('   |   |'))
    print(C2(' ' + grid[7] + ' | ' + grid[8] + ' | ' + grid[9]))
    print(C('   |   |'))
    print(C3('-----------'))
    print(C('   |   |'))
    print(C2(' ' + grid[4] + ' | ' + grid[5] + ' | ' + grid[6]))
    print(C('   |   |'))
    print(C3('-----------'))
    print(C('   |   |'))
    print(C2(' ' + grid[1] + ' | ' + grid[2] + ' | ' + grid[3]))
    print(C('   |   |'))


def choose_letter():
    """
    This function lets the player choose which letter they want to be,
    returning a list with the player’s letter as the first item, and the
    computer's letter as the second.

    The first element in the list is the player’s letter, the second is the
    computer's letter.
    """
    letter = set(("X", "O"))
    print(C('Do you want to be X or O?'))
    letter = input().upper()

    if letter == 'X':
        return ['X', 'O']

    return ['O', 'X']


def turn_order():
    """
    A function that randomly chooses who goes first. Effectively, this is a
    coin flip.
    """
    if random.randint(0, 1) == 0:
        return 'computer'

    return 'player'


def replay():
    """
    This function returns True if the player wants to play the game again,
    otherwise it returns False.

    Any input that starts with the letter 'y', capitalised or not, will return
    True.
    """
    print(C('Do you want to play again? (yes or no)'))
    return input().lower().startswith('y')


def make_a_move(grid, letter, move):
    """
    This function assigns a letter, X or O, to one of the positions on
    the grid (defined as an integer) for the player or computer move.
    """
    grid[move] = letter


def win_condition(gr, le):
    """
    Given a grid and the player’s letter, this function returns True if the
    player has won. Grid and letter are abbreviated to 'gr' and 'le',
    respectively.

    There are eight winning combinations in tic-tac-toe; all are listed below.
    Each is checked for inside a nested 'while' loop further on.
    """
    return ((gr[7] == le and gr[8] == le and gr[9] == le) or  # across top
            (gr[4] == le and gr[5] == le and gr[6] == le) or  # across middle
            (gr[1] == le and gr[2] == le and gr[3] == le) or  # across bottom
            (gr[7] == le and gr[4] == le and gr[1] == le) or  # down left side
            (gr[8] == le and gr[5] == le and gr[2] == le) or  # down middle
            (gr[9] == le and gr[6] == le and gr[3] == le) or  # down right side
            (gr[7] == le and gr[5] == le and gr[3] == le) or  # diagonal 1
            (gr[9] == le and gr[5] == le and gr[1] == le))  # diagonal 2


def get_grid_copy(grid):
    """
    This function makes a duplicate of the grid list and returns it.
    The duplicate is used by the computer to make non-permanent changes
    to a temporary copy of the grid without changing the original.
    """
    copy_grid = []
    for i in grid:
        copy_grid.append(i)
    return copy_grid


def check_free_space(grid, move):
    """
    This function returns true if the passed move is free on the current grid.
    """
    return grid[move] == ' '


def player_move(grid):
    """
    This function lets the player type in their move.

    The loop ensures the execution doesn't occur until the player has typed
    an integer between 1-9 that represents a free space on the current grid.
    """
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not check_free_space(grid, int(move)):
        print(BR)
        print(C('Please enter your next move (1-9)'))
        move = input()
    return int(move)


def choose_random_possible_move(grid, move_list):
    """
    This function is for the benefit of the computer. It returns a valid move 
    from the passed list on the passed grid. It returns None if there is no 
    valid move.
    """
    possible_moves = []
    for i in move_list:
        if check_free_space(grid, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)

    return None


def computer_move(grid, computer_letter):
    """
    This function contains the computer's algorithm, defined by five seperate
    checks of the current game state. Each check completes in listed order.

    The variables 'computer_letter' and 'player_letter' allows the same code
    to be used whatever letter the computer is assigned.
    """
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Checks if a winning move exists. If not, move to the next step.

    for i in range(1, 10):
        copy = get_grid_copy(grid)

        if check_free_space(copy, i):
            make_a_move(copy, computer_letter, i)
        if win_condition(copy, computer_letter):
            return i

    # If a winning move exists for the player, the computer will stop it. If
    # not, move to the next step.

    for i in range(1, 10):
        copy = get_grid_copy(grid)
        if check_free_space(copy, i):
            make_a_move(copy, player_letter, i)
        if win_condition(copy, player_letter):
            return i
    
    # Checks for an available space in the four corners. If none are free,
    # move to the next step.

    move = choose_random_possible_move(grid, [1, 3, 7, 9])
    if move is not None:
        return move

    # Checks if the center space is available. If not, move to the next step.

    if check_free_space(grid, 5):
        return 5

    # Take a space on the sides.

    return choose_random_possible_move(grid, [2, 4, 6, 8])


def is_grid_full(grid):
    """
    If every space on the grid is filled, this returns True.
    """
    for i in range(1, 10):
        if check_free_space(grid, i):
            return False
    return True


while True:
    # This 'while' loop resets the grid on starting the game and executes
    # the game's functions so long as the loop returns True.

    # Reset the grid
    intro_message()
    the_grid = [' '] * 10
    player_letter, computer_letter = choose_letter()
    TURN = turn_order()
    input(C('The ' + TURN + ' will go first. Press Enter to continue.\n'))
    GAME_ACTIVE = True

    while GAME_ACTIVE:
        if TURN == 'player':
            # The player’s turn.
            clear_console()
            create_grid(the_grid)
            MOVE = player_move(the_grid)
            make_a_move(the_grid, player_letter, MOVE)
            
            if win_condition(the_grid, player_letter):
                clear_console()
                create_grid(the_grid)
                print(C('Congratulations! You have won the game!'))
                GAME_ACTIVE = False
            elif is_grid_full(the_grid):
                clear_console()
                create_grid(the_grid)
                print(C('The game is a tie!'))
                break
            else:
                TURN = 'computer'
        else:
            # The computer’s turn.
            clear_console()
            move = computer_move(the_grid, computer_letter)
            make_a_move(the_grid, computer_letter, move)

            if win_condition(the_grid, computer_letter):
                clear_console()
                create_grid(the_grid)
                print(C('The computer has beaten you! You lose.'))
                GAME_ACTIVE = False
            elif is_grid_full(the_grid):
                clear_console()
                create_grid(the_grid)
                print(C('The game is a tie!'))
                break
            else:
                TURN = 'player'
    if not replay():
        break
