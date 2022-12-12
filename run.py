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


def turn_order():
    """
    A function that randomly chooses who goes first. Effectively, this is a 
    coin flip.
    """
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def replay():
    """
    This function returns True if the player wants to play the game again, 
    otherwise it returns False.
    
    Any input that starts with the letter 'y', capitalised or not, will return 
    True.
    """
    print('Do you want to play again? (yes or no)')
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
        print('What is your next move? (1-9)')
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
    else:
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

    # Checks for an available space in the four corners. If none are free,
    # move to the next step.

    move = choose_random_possible_move(grid, [1, 3, 7, 9])
    if move != None:
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

    # Reset the grid
    the_grid = [' '] * 10
    player_letter, computer_letter = choose_letter()
    turn = turn_order()
    print('The ' + turn + ' will go first.')
    game_active = True

    while game_active:
        if turn == 'player':
            # The player’s turn.
            create_grid(the_grid)
            move = player_move(the_grid)
            make_a_move(the_grid, player_letter, move)
            if win_condition(the_grid, player_letter):
                create_grid(the_grid)
                print('Congratulations! You have won the game!')
                game_active = False
            else:
                if is_grid_full(the_grid):
                    create_grid(the_grid)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # The computer’s turn.
            move = computer_move(the_grid, computer_letter)
            make_a_move(the_grid, computer_letter, move)
            
            if win_condition(the_grid, computer_letter):
                create_grid(the_grid)
                print('The computer has beaten you! You lose.')
                game_active = False
            else:
                if is_grid_full(the_grid):
                    create_grid(the_grid)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not replay():
        break
