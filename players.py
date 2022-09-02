from ships import AircraftCarrier, Battleship, Destroyer, Ship, Submarine



class Player():
    def __init__(self, name): #add name as argument when on board
        self.name = name
        self.fleet = [Destroyer(), Submarine(), Battleship(), AircraftCarrier()]
        
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



    def select_coordinates(self, player):#maybe use opp grid as a parameter
        chosen_row = int(input("Select row(y): ")) - 1
        chosen_column = int(input("Select column(x): ")) - 1
        self.target_grid[chosen_row].pop(chosen_column) #your grid
        if player.ocean_grid[chosen_row][chosen_column] != "W" or "O": #change to ENEMY'S ocean grid
            self.target_grid[chosen_row].insert(chosen_column, "X") #your grid
            #+1 point if i change to that
        else:
            self.target_grid[chosen_row].insert(chosen_column, "O")

#i could give players points anytime hey turn S to X
#player attacks should also be reflected on enemy board

    def check_for_ships(self, player): #opposite player as parameter
        for ship in player.fleet:
            ship_id = self.fleet.symbol #trying to specify any ship symbols
            ship_track = 0
            for row in player.ocean_grid: #enemny ocean grid
                ship_track += row.count(ship_id)
            if ship_track == 0:
                player.fleet.remove(ship) #enemy ship removed when destroyed, it wont check for it in further instances
                print("ship destroyed")

    def place_ships(self):

        for ship in self.fleet: #if a space == w, and the following length spaces, place(turn w into ship id)
            print(f"Place your {ship.name}")
            chosen_row = int(input("Select row(y): ")) - 1
            chosen_column = int(input("Select column(x): ")) - 1
            choice = input("Vert or Horiz")
            if choice == 'V':
                for row in self.ocean_grid[chosen_column]:
                    for row in range(self.fleet[0].length):
                        self.target_grid[chosen_row].insert(chosen_column, self.fleet[0].name)
                #pass #check rows at column position
            if choice == 'H':
                pass #check columns at row psotion


            #if self.ocean_grid[chosen_row][chosen_column] == "W":

            



