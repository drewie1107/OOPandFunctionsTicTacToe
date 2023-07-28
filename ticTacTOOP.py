# Drew Pearlstein
# Engineering Programming: Python (EE-551)
# Kevin Ryan
# 4 May 2023

# Creates tic-tac-toe class.

class TicTacToe:
    def __init__(self):
        self.board = ["-" for _ in range(9)]
        self.current_player = "X"
        self.game_running = True
        self.winner = None

    def print_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("-" * 9)
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("-" * 9)
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def player_input(self):
        while True:
            try:
                inp = int(input(f"Enter a number 1-9 Player ({self.current_player}): "))
                if 1 <= inp <= 9 and self.board[inp - 1] == "-":
                    self.board[inp - 1] = self.current_player
                    break
                else:
                    print(f"That spot is already taken, doofus. Try again - Player ({self.current_player})!")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")

    def check_win(self):
        if self.check_diagonal() or self.check_horizontal() or self.check_row():
            self.winner = self.current_player
            print(f"The winner is {self.winner}!")
            self.game_running = False

    def check_horizontal(self):
        if (self.board[0] == self.board[1] == self.board[2] and self.board[0] != "-") or \
                (self.board[3] == self.board[4] == self.board[5] and self.board[3] != "-") or \
                (self.board[6] == self.board[7] == self.board[8] and self.board[6] != "-"):
            return True
        else:
            return False

    def check_row(self):
        if (self.board[0] == self.board[3] == self.board[6] and self.board[0] != "-") or \
                (self.board[1] == self.board[4] == self.board[7] and self.board[1] != "-") or \
                (self.board[2] == self.board[5] == self.board[8] and self.board[2] != "-"):
            return True
        else:
            return False

    def check_diagonal(self):
        if (self.board[0] == self.board[4] == self.board[8] and self.board[0] != "-") or \
                (self.board[2] == self.board[4] == self.board[6] and self.board[2] != "-"):
            return True
        else:
            return False

    def check_tie(self):
        if "-" not in self.board:
            print_board(self.board)
            print("It's a tie!")
            self.game_running = False

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def play(self):
        while self.game_running:
            self.print_board()
            self.player_input()
            self.check_win()
            self.check_tie()
            self.switch_player()


game = TicTacToe()
game.play()

# Thank you!
