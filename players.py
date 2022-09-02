from ships import AircraftCarrier, Battleship, Destroyer, Ship, Submarine



class Player():
    def __init__(self, name): #add name as argument when on board
        self.name = name
        self.fleet = [Destroyer, Submarine, Battleship, AircraftCarrier]
        
        self.target_grid = [
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]
    ] #GOING TO MAKE SHIPS DESIGNATED BY THE LETTER, this way I can search the list for letters, and if its lackin said letter, the ship is destroyed
    #enemy attacks will have to target ocean grid, but give feedback to the attacking player's target grid...
        self.ocean_grid = [
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]
    ] 


    def grid_printer(self, grid):
        print("       1    2    3    4    5    6    7    8    9    10")
        incrementor = 1
        while incrementor < len(grid):
            for row in grid:
                print(f"  {incrementor}: {row}")
                incrementor += 1



    def display_target_grid(self):
        print("                      TARGET GRID")
        self.grid_printer(self.target_grid)

    def display_ocean_grid(self):
        print("\n                     OCEAN GRID")
        self.grid_printer(self.ocean_grid)



    def select_coordinates(self):#maybe use opp grid as a parameter
        chosen_row = int(input("Select row(y): ")) - 1
        chosen_column = int(input("Select column(x): ")) - 1
        self.target_grid[chosen_row].pop(chosen_column)
        if self.target_grid[chosen_row][chosen_column] != "W": #change to enemy's ocean grid
            self.target_grid[chosen_row].insert(chosen_column, "X")
        else:
            self.target_grid[chosen_row].insert(chosen_column, "O")
             #if opp_board (coordinates) == "S" then it hits
#i could give players points anytime hey turn S to X
#player attacks should also be reflected on enemy board


#  def grid_printer(self, grid):
#         print("       1    2    3    4    5    6    7    8    9    10")
#         incrementor = 1
#         while incrementor < len(self.target_grid):
#             for row in self.target_grid:
#                 print(f"  {incrementor}: {row}")
#                 incrementor += 1