from players import Player
#NOTICE: PLAYE.OCEAN GRID SEEMS TO NOT WORK AS ENEMY OCEAN GRID, ON PLAYER METHOD SELECT COORDINATES
class Board():
    def __init__(self):
        self.user_1 = Player("Player 1")
        self.user_2 = Player("Player 2")

    def play_game(self):
        #self.user_1.place_ships()
        #self.user_1.display_ocean_grid()
        #self.user_1.select_coordinates(self.user_2)#trying to have player 1 attack p2 with the player method and parameters
        self.user_1.place_ships()
        self.user_1.display_ocean_grid()
        # 
