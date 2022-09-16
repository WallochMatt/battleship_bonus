from players import Player
#NOTICE: PLAYE.OCEAN GRID SEEMS TO NOT WORK AS ENEMY OCEAN GRID, ON PLAYER METHOD SELECT COORDINATES
class Board():
    def __init__(self):
        self.user_1 = Player("Player 1")
        self.user_2 = Player("Player 2")

    def play_game(self):
        #self.user_2.
        #self.user_1.set_board()
        #self.user_1.display_ocean_grid()
        while len(self.user_1.fleet) > 0 and len(self.user_2.fleet) > 0:
            self.user_1.display_target_grid()
            self.user_1.select_coordinates(self.user_2)