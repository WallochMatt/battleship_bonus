from ships import AircraftCarrier, Battleship, Destroyer, Submarine



class Player():
    def __init__(self, name): #add name as argument when on board
        self.name = name
        self.fleet = [Destroyer(), Submarine(), Battleship(), AircraftCarrier()]
        #points? see check_for_ships
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


#seems to work for player 1
    def select_coordinates(self, player):#maybe use opp grid as a parameter
        chosen_row = int(input("Select row(y): ")) - 1
        chosen_column = int(input("Select column(x): ")) - 1
        self.target_grid[chosen_row].pop(chosen_column) #your grid
        if player.ocean_grid[chosen_row][chosen_column] != "W":
            self.target_grid[chosen_row].insert(chosen_column, "X") #your grid
            #+1 point if i change to that
            self.check_for_ships(player) #should be the enemy player

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
            #might add apoint value and add to a IV for points

#modulus?
    def place_ships(self):#This needs error handling, really bad
        #NEEDS TO HAVE COORDINATES ERROR HANDLING

        for ship in self.fleet: #if a space == w, and the following length spaces, place(turn w into ship id)
            #TRY?
            print(f"Place your {ship.name}")
            chosen_row = int(input("Select row(y): ")) - 1
            chosen_column = int(input("Select column(x): ")) - 1

            choice = int(input("1:UP    2:Down       3:Right     4:Left")) #do opposite for Horiz

            #ELSE
            if choice == 1:#UP
                for row in range(chosen_column , (chosen_column - ship.length), -1):
                    if self.ocean_grid[row][chosen_column] == "W":
                        self.ocean_grid[row][chosen_column] = ship.symbol
            
            elif choice == 2:#DOWN
                for row in range(chosen_column, (chosen_column + ship.length)):
                    if self.ocean_grid[row][chosen_column] == "W":
                        self.ocean_grid[row][chosen_column] = ship.symbol
            
            elif choice == 3:#RIGHT
                for column in range(chosen_row, (chosen_row + ship.length)):
                    if self.ocean_grid[chosen_row][column] == "W":
                        self.ocean_grid[chosen_row][column] = ship.symbol

            elif choice == 4:#LEFT
                for column in range(chosen_row, (chosen_row - ship.length), -1):
                    if self.ocean_grid[chosen_row][column] == "W":
                        self.ocean_grid[chosen_row][column] = ship.symbol
        
            # if choice < 0 or choice > 4:
            #     raise Exception("Must be between 1 and 4")











        # Your logic actually looks solid in terms of approach (using the nested for loop, setting the number of spots using range and the length of the ship). But focusing on a single axis will help build some confidence on your logic before expanding it.
        # for ship in self.fleet: #if a space == w, and the following length spaces, place(turn w into ship id)
        #     print(f"Place your {ship.name}")
        #     chosen_row = int(input("Select row(y): ")) - 1
        #     chosen_column = int(input("Select column(x): ")) - 1
        #     choice = input("Vert or Horiz")
        #     if choice == 'V':
        #         for row in range(self.fleet[0].length):
        #         #pass #check rows at column position
        #     if choice == 'H':
        #         for column in self.ocean_grid[chosen_row]:
        #             pass #check columns at row psotion


        #     #if self.ocean_grid[chosen_row][chosen_column] == "W":

            



