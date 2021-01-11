class SnakesLadders():

    snakesandladders = {16:6, 46:25, 49:11, 62:19, 64:60, 74:53, 89:68, 92:88, 95:75, 99:80, 
                        2:38, 7:14, 8:31, 15:26, 21:42, 28:84, 36:44, 51:67, 71:91, 78:98, 87:94}

    def __init__(self):
        self.player_1 = Player(1) 
        self.player_2 = Player(2)
        self.turn = 1
        self.current_player = self.player_1
        self.end_game = False


    def check_position(self):
        if self.current_player.position == 100:
            self.end_game = True
            return f"Player {self.current_player.number} Wins!"

        if self.current_player.position > 100:
            self.current_player.position = 100 - (self.current_player.position - 100)

    def execute_snails_and_ladders(self):
        if self.current_player.position in SnakesLadders.snakesandladders:
            self.current_player.position = SnakesLadders.snakesandladders[self.current_player.position]

    def play(self, die1, die2):
        if self.end_game:
            return "Game over!"

        self.current_player.position += (die1 + die2)
        r = self.check_position()
        if self.end_game:
            return r
        self.execute_snails_and_ladders()
        

        if die1 == die2:
            return f"Player {self.current_player.number} is on square {self.current_player.position}"

        self.turn = self.turn + 1

        return_string = f"Player {self.current_player.number} is on square {self.current_player.position}"

        if self.turn % 2 != 0:
            self.current_player = self.player_1
        else:
            self.current_player = self.player_2

        return return_string
        
class Player():
    def __init__(self, number):
        self.position = 0
        self.number = number
