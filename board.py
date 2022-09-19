from players import Player

class Board():
    def __init__(self):
        self.user_1 = Player("Player 1")
        self.user_2 = Player("Player 2")

    def play_game(self):
        self.user_1.set_board()
        self.user_1.display_ocean_grid()

        input("\n" + "SWAP PLAYER - PRESS ENTER" + "\n")        

        self.user_2.set_board()
        self.user_2.display_ocean_grid()

        input("\n" + "SWAP PLAYER - PRESS ENTER" + "\n")

        game_on = True
        while game_on == True:

            print("\n" + f"{self.user_1.name}" + "\n")
            self.user_1.display_target_grid()
            self.user_1.display_ocean_grid()
            game_on = self.user_1.select_coordinates(self.user_2)
            if game_on == False:
                break
            
            input("\n" + "SWAP PLAYER - PRESS ENTER" + "\n")


            print("\n" + f"{self.user_2.name}" + "\n")
            self.user_2.display_target_grid()
            self.user_2.display_ocean_grid()
            game_on = self.user_2.select_coordinates(self.user_1)
            if game_on == False:
                break

            input("\n" + "SWAP PLAYER - PRESS ENTER" + "\n")

        self.game_over()
    
    
    
    
    def game_over(self):
        if len(self.user_1.fleet) == 0:
            print(f"{self.user_2.name} wins!")

        if len(self.user_2.fleet) == 0:
            print(f"{self.user_1.name} wins!")
            