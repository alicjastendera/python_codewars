class Connect4():

    def __init__(self):
        self.player_1 = Player(1) 
        self.player_2 = Player(2)
        self.turn = 1
        self.current_player = self.player_1
        self.end_game = False
        self.columns = 7
        self.rows = 6
        self.board = [[0]*self.columns for _ in range(self.rows)]


    def check_column_capacity(self, column):    
        if self.board[0][column] != 0:
            return True

    def play(self, col):

        if self.end_game:
            return "Game has finished!"

        if self.check_column_capacity(col):
            return "Column full!"

        self.add_to_column(col)

        if self.check_connect4(self.current_player.token):
            self.end_game = True
            return f"Player {self.current_player.token} wins!"

        self.turn += 1

        return_msg = f"Player {self.current_player.token} has a turn"

        if self.turn % 2 != 0:
            self.current_player = self.player_1
        else:
            self.current_player = self.player_2

        return return_msg
      

    def check_connect4(self, token):
        for r in range(self.rows):
            for c in range(self.columns - 3):
                if all(_ == token for _ in [self.board[r][c], self.board[r][c+1], self.board[r][c+2], self.board[r][c+3]]):
                    return True
        for r in range(self.rows - 3):
            for c in range(self.columns):
                if all(_ == token for _ in [self.board[r][c], self.board[r+1][c], self.board[r+2][c], self.board[r+3][c]]): 
                    return True
        for r in range(self.rows-3):
            for c in range(self.columns - 3):
                if all(_ == token for _ in [self.board[r][c], self.board[r+1][c+1], self.board[r+2][c+2],self.board[r+3][c+3]]):
                    return True
        for r in range(3, self.rows):
            for c in range(self.columns - 3):
                if all(_ == token for _ in [self.board[r][c], self.board[r-1][c+1], self.board[r-2][c+2], self.board[r-3][c+3]]):
                    return True

    def add_to_column(self, column):
        for _ in reversed(range(0, self.rows)):
            if self.board[_][column] == 0:
                self.board[_][column] = self.current_player.token
                break

class Player():

    def __init__(self, token):
        self.token = token
