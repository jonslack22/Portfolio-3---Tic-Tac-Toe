# Project libraries
import random
import time
import os
import sys

board = [" " for x in range(9)]

PLAYER_LETTER = "X"
AI_LETTER = "O"
PLAYER_NUMBER = 1
CURRENT_PLAYER = 1


C = "{:^80}".format
C2 = "{:^82}".format
C3 = "{:^83}".format
BR = "\n"


def clear_console():
    """ Clears the console of previously generated information.
    """
    # This line is credited to
    # https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    os.system("cls" if os.name == "nt" else "clear")


def restart():
    """ Restarts game to clear the board
    """
    # This line is credited to
    # https://stackoverflow.com/questions/62248430/restart-function-in-python
    os.execl(sys.executable, sys.executable, *sys.argv)


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
    print(C("MENU:"))
    print(C("1. Play"))
    print(C("2. Instructions"))
    user_input = input(" " * 40).strip()
    if user_input == "1":
        clear_console()
        get_opponent()
    elif user_input == "2":
        clear_console()
        instructions()


def instructions():
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

    user_choice = input(" " * 20 + "Are you ready to play Tic Tac Toe? Y/N: ").strip()
    if user_choice.upper() == "Y":
        clear_console()
        get_opponent()
    elif user_choice.upper() == "N":
        clear_console()
        intro_message()


def get_opponent():
    """
    This function gets the player's desired opponent for the game.
    """

    clear_console()
    print(C("Who would you like to play against?"))
    print(C("1. Another player"))
    print(C("2. Basic AI"))
    print(C("3. Advanced AI"))
    print(BR)
    opponent = input(C("Enter the number of your opponent: "))

    while opponent not in ['1', '2', '3']:
        print("Invalid input, please enter 1, 2, or 3.")
        opponent = input("Enter the number of your opponent: ")

    opponent = int(opponent)
    if opponent == 1:
        print("You have chosen to play against a human opponent.")
    elif opponent == 2:
        print("You have chosen to play against a basic AI opponent.")
    else:
        print("You have chosen to play against an advanced AI opponent.")

    return opponent

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


def turn_order(opponent):
    """
    This function determines who goes first.
    """
    if random.randint(0, 1) == 0:
        return 'AI'
    return 'player'


def play_again(opponent):
    """
    This function allows the player to start a new game after the previous
    game has ended.
    """
    while True:
        clear_console()
        print(C("Do you want to play again?"))
        print(C("1. Yes"))
        print(C("2. No"))
        choice = input(C("Please enter a number (1-2): "))
        if choice == "1":
            global game_active
            board = [" " for x in range(9)]
            turn = turn_order(opponent)
            if turn == 'AI':
                if opponent == 2:
                    basic_ai()
                elif opponent == 3:
                    advanced_ai()
                input(C("The AI will go first. Press Enter to continue"))
            if turn == 'player':
                input(C("You will go first. Press Enter to continue."))
            else:
                print(C("Please decide between yourselves who goes first."))
                input(C("When you are ready, press Enter to continue"))
            game_active = True
        if choice == "2":
            restart()
            break  # Exit the play again loop and return to main menu


def player_move(PLAYER_NUMBER):
    if PLAYER_NUMBER == 1:
        print("Your turn, Player 1")
        icon = PLAYER_LETTER
    else:
        print("Your turn, Player 2")
        icon = AI_LETTER
    while True:
        move = int(input("Enter your move (1-9): "))
        if move in range(1, 10) and board[move-1] == " ":
            board[move-1] = icon
            PLAYER_NUMBER = 3 - PLAYER_NUMBER  # Switch the player
            if PLAYER_NUMBER == 1:
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


while True:
    intro_message()
    opponent = get_opponent()
    board = [" " for x in range(9)]  # This resets the board
    turn = turn_order(opponent)
    if turn == 'AI':
        if opponent == 2:
            basic_ai()
        elif opponent == 3:
            advanced_ai()
        input(C("The AI will go first. Press Enter to continue"))
    if turn == 'player':
        input(C("You will go first. Press Enter to continue."))
    else:
        print(C("Please decide between yourselves who goes first."))
        input(C("When you are ready, press Enter to continue"))
    game_active = True

    while game_active:
        clear_console()
        print_board()
        if turn == 'player':
            player_move(1)
            if is_victory(PLAYER_LETTER):
                clear_console()
                print_board()
                print("You win! Congratulations!")
                game_active = False
                break
            if is_draw():
                clear_console()
                print_board()
                print("It's a draw!")
                game_active = False
                break
            turn = 'computer'
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
                game_active = False
                break
            if is_draw():
                clear_console()
                print_board()
                print("It's a draw!")
                game_active = False
                break
            turn = 'player'

    play_again(opponent)
