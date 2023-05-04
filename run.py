# Project libraries
import keyboard
import random
import time
import os

board = [" " for x in range(9)]

PLAYER_LETTER = "X"
AI_LETTER = "O"
player_number = 1


# Variables to keep track of game mode and last opponent
game_mode = None
last_opponent = None


C = "{:^80}".format
C2 = "{:^82}".format
C3 = "{:^83}".format
BR = "\n"


def clear_console():
    """ Clears the console of previously generated information.
    """
    os.system("cls" if os.name == "nt" else "clear")
        

def print_board():
    row1 = "|".join(board[6:9])
    row2 = "|".join(board[3:6])
    row3 = "|".join(board[:3])
    print()
    print(row1)
    print("-+-+-")
    print(row2)
    print("-+-+-")
    print(row3)
    print()


def player_move(player_number):
    if player_number == 1:
        print("Your turn, Player 1")
        icon = PLAYER_LETTER
    else:
        print("Your turn, Player 2")
        icon = AI_LETTER
    while True:
        move = int(input("Enter your move (1-9): "))
        if move in range(1, 10) and board[move-1] == " ":
            board[move-1] = icon
            player_number = 3 - player_number  # Switch the player
            if player_number == 1:
                icon = PLAYER_LETTER
            else:
                icon = AI_LETTER
            break
        print("Invalid move. Please try again.")


def is_victory(icon):
    """
    There are eight winning combinations in tic-tac-toe; all are listed below.
    Each is checked for inside a nested 'while' loop further on.
    """
    return (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[6] == icon and board[3] == icon and board[0] == icon) or \
        (board[7] == icon and board[4] == icon and board[1] == icon) or \
        (board[8] == icon and board[5] == icon and board[2] == icon) or \
        (board[6] == icon and board[4] == icon and board[2] == icon) or \
        (board[8] == icon and board[4] == icon and board[0] == icon)


def is_draw():
    if " " not in board:
        return True

    return False


def basic_ai():
    """
    This computer opponent will assign its letter to the board in a random spot.
    """
    available = [i for i, x in enumerate(board) if x == " "]
    move = random.choice(available)
    board[move] = "O"


def advanced_ai():
    """
    This computer opponent is smarter than the other, in that it will block the
    player from winning on their next turn, and will choose a winning move if
    the player doesn't block it themselves.
    """
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    count_o = 0
    count_x = 0
    # The AI checks for winning combinations and returns it
    for combination in winning_combinations:
        for i in combination:
            if board[i] == "O":
                count_o += 1
            elif board[i] == "X":
                count_x += 1
            else:
                open_spot = i
        if count_o == 2 and count_x == 0:
            board[open_spot] = "O"
            return
        count_o = 0
        count_x = 0

    # Check for winning combinations for player and block them
    for combination in winning_combinations:
        for i in combination:
            if board[i] == "X":
                count_x += 1
            elif board[i] == "O":
                count_o += 1
            else:
                open_spot = i
        if count_x == 2 and count_o == 0:
            board[open_spot] = "O"
            return
        count_x = 0
        count_o = 0

    # Otherwise, select random empty spot
    available = [i for i, x in enumerate(board) if x == " "]
    move = random.choice(available)
    board[move] = "O"


def turn_order():
    return random.randint(0, 1)


def get_move(player_number):
    """
    This function gets the player's move or the computer's move, depending on
    whose turn it is.
    """
    if player_number == 1 or player_number == 2:
        player_move(player_number)
    elif player_number == 3:
        basic_ai()
    elif player_number == 4:
        advanced_ai()


def get_opponent():
    """
    This function allows the player to select an opponent. The 'player_number'
    variable is used to track who's turn it is (and therefore, which function
    to call in the 'get_move' function.
    """
    global player_number
    clear_console()
    print(C("Who would you like to play against?"))
    print(C("1. Another player"))
    print(C("2. Basic AI"))
    print(C("3. Advanced AI"))
    opponent = input("Please enter a number (1-3): ")
    if opponent == "1":
        player_number = 1
    elif opponent == "2":
        player_number = 3
    elif opponent == "3":
        player_number = 4


def intro_message():
    """ This function displays a welcome message in every new game instance
    """
    clear_console()
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
    
    print(C("If you would like to view the rules of the game, please "
                    "type 'R'.\n")) 
    rules = input(C("Otherwise, press Enter to continue."))

    if rules.lower() == 'r':
        clear_console()
        print(C("Here are the rules of the game:\n"))
        print(C("Players take turns marking spaces in a 3*3 grid against an "
                "opponent.\n"))
        print(C("The 3*3 grid is laid out like a calculator:\n"))
        print(C("The top row represents numbers    7, 8 and 9;"))
        print(C("The middle row represents numbers 4, 5 and 6;"))
        print(C("The bottom row represents numbers 1, 2 and 3.\n"))
        print(C("The player who succeeds in placing three marks, represented "
                "by X and 0, in a "))
        print(C("horizontal, vertical, or diagonal row, wins.\n"))
        print(C("If one of the players is the AI, their turn will "
                "happen immediately after the player")) 
        print(C("makes their move."))
        while True:
            print("Press Esc to exit.")
            if keyboard.is_pressed('esc'):
                intro_message()
    clear_console()
    get_opponent()


intro_message()
current_player = 1

def game_loop(opponent, board):
    """ This function handles the game logic for Tic Tac Toe
    """
    while True:
        board = [" " for x in range(9)]  # This resets the board
        GAME_ACTIVE = True
        
        # Decide who goes first
        if opponent != 1:
            turn_order()
            if turn_order() == 0:
                print("The AI will go first. Press Enter to continue")
                input()
                if opponent == 2:
                    basic_ai()
                elif opponent == 3:
                    advanced_ai()
            else:
                print("You will go first. Press Enter to continue")
                input()
        
        # Game loop for player vs player
        if opponent == 1:
            print('Please decide between yourselves who goes first.')
            input('When you are ready, press Enter to continue.\n')
            current_player = 1
            while GAME_ACTIVE:
                clear_console()
                print_board()
                player_move(current_player)
                if is_victory(PLAYER_LETTER):
                    clear_console()
                    print_board()
                    print(f"Player {current_player} wins!")
                    GAME_ACTIVE = False
                    break
                if is_draw():
                    clear_console()
                    print_board()
                    print("It's a draw!")
                    GAME_ACTIVE = False
                    break
                current_player = 3 - current_player
        
        # Game loop for player vs AI
        else:
            player_number = 1
            while GAME_ACTIVE:
                clear_console()
                print_board()
                if player_number == 1:
                    player_move(player_number)
                    if is_victory(PLAYER_LETTER):
                        clear_console()
                        print_board()
                        print("You win! Congratulations!")
                        GAME_ACTIVE = False
                        break
                    if is_draw():
                        clear_console()
                        print_board()
                        print("It's a draw!")
                        GAME_ACTIVE = False
                        break
                    player_number = 2
                else:
                    if opponent == 2:
                        basic_ai()
                    elif opponent == 3:
                        advanced_ai()
                    print_board()
                    if is_victory(AI_LETTER):
                        clear_console()
                        print_board()
                        print("AI wins! Better luck next time.")
                        GAME_ACTIVE = False
                        break
                    if is_draw():
                        clear_console()
                        print_board()
                        print("It's a draw!")
                        GAME_ACTIVE = False
                        break
                    player_number = 1


def play_again(opponent, player_number):
    """
    This function allows the player to start a new game after the previous
    game has ended.
    """
    global board
    clear_console()
    print(C("Do you want to play again?"))
    print(C("1. Yes"))
    print(C("2. No"))
    play_again = input("Please enter a number (1-2): ")
    if play_again == "1":
        clear_console()
        board = [" " for x in range(9)]
        game_loop(opponent, board)
    elif play_again == "2":
        clear_console()
        player_number = 0
        intro_message()
