# Drew Pearlstein
# Engineering Programming: Python (EE-551)
# Kevin Ryan
# 4 May 2023

# Initializes the board as a list of dashes. This makes it easy to check for wins or ties as it can reference the list.

INITIAL_BOARD = ['-', '-', '-',
                 '-', '-', '-',
                 '-', '-', '-']


# Prints board.

# Separates the board with dividers.

def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])


# Returns a new board with the specified move made.

def make_move(board, player, move):
    if board[move] == '-':
        return board[:move] + [player] + board[move+1:]
    else:
        return None


# Determines if the given player has won on the specified board horizontally, then vertically, then diagonally.

def check_win(board, player):
    # Check horizontal rows.
    for i in range(0, 9, 3):
        if board[i:i+3] == [player] * 3:
            return True

    # Check vertical columns.
    for i in range(3):
        if board[i] == player and board[i+3] == player and board[i+6] == player:
            return True

    # Check diagonals.
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True

    return False


# Determines if the game has ended in a tie.
def check_tie(board):
    return '-' not in board


# Switches the current player between X and O.
def switch_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'


# Takes player input and returns a new board with the move made.
def get_input(board, player):
    while True:
        move = input(f"Enter a number 1-9 \033[1;34m Player ({player}) \033[0;0m : ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            new_board = make_move(board, player, move)
            if new_board is not None:
                return new_board
        print(f"That spot is already taken, doofus. Try again, \033[1;34m Player ({player}) \033[0;0m !")
        print_board(board)


# Plays a single turn of the game.
def play_turn(board, player):
    print_board(board)
    new_board = get_input(board, player)
    return new_board, check_win(new_board, player), check_tie(new_board)


# Plays the game until either someone wins or there is a tie.
def play_game():
    board = INITIAL_BOARD
    player = 'X'
    while True:
        board, is_winner, is_tie = play_turn(board, player)
        if is_winner:
            print_board(board)
            print(f"The winner is {player}!")
            break
        elif is_tie:
            print_board(board)
            print("It's a tie!")
            break
        else:
            player = switch_player(player)


play_game()