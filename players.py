from ships import AircraftCarrier, Battleship, Destroyer, Submarine

class Player():
    def __init__(self, name):
        self.name = name
        self.fleet = [Destroyer(), Submarine(), Battleship(), AircraftCarrier()]
        self.target_grid =  [
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
        
        #HEY!: A testing version of ocean grid is located below, paste it and comment out set_board() in the board.py module!
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

#I CAN AUTOMATE THIS GRID WITH A FUNCTION,WHICH COULD ALLOW THE PLAYER TO CHOOSE THE SIZE OF THE BOARD
#AND CONSIDER CREATING A BOARD CLASS
    def grid_printer(self, grid):
        """
        Parameter:
        grid : instance variable [] -> of either grid
        Prints the grid to terminal
        """
        print("       1    2    3    4    5    6    7    8    9    10")
        incrementor = 1
        while incrementor < len(grid):
            for row in grid:
                print(f"   {incrementor}: {row}")
                incrementor += 1

    def display_target_grid(self):
        print("                      TARGET GRID")
        self.grid_printer(self.target_grid)

    def display_ocean_grid(self):
        print("\n                     OCEAN GRID")
        self.grid_printer(self.ocean_grid)


    def select_coordinates(self, player):
        """
        Parameters:
        player : object -> The opposite player of the performing the method
        Returns:
        check_for_ships() : bool -> True if the enemy player has ships

        """
        try:
            print("\n CHOOSE WHERE TO STRIKE!")
            chosen_row = int(input("Select row(y): ")) - 1
            chosen_column = int(input("Select column(x): ")) - 1
            self.target_grid[chosen_row].pop(chosen_column) #your grid
            if player.ocean_grid[chosen_row][chosen_column] != "W" and player.ocean_grid[chosen_row][chosen_column] != "X": #enemy
                self.target_grid[chosen_row].insert(chosen_column, "X") #your grid
                print("\n HIT")

                player.ocean_grid[chosen_row].pop(chosen_column)
                player.ocean_grid[chosen_row].insert(chosen_column, "X") #enemy grid
            
            else:
                self.target_grid[chosen_row].insert(chosen_column, "O")
                print("\n MISS")
        except:
            print("Invalid input, please try again")
            self.select_coordinates(player)

        return self.check_for_ships(player)

    def check_for_ships(self, player):
        """
        Parameters:
        player : object -> The opposite player of the performing the method
        Returns:
        bool -> True if the enemy player has ships, False if all ships have been sunk
        """
        for ship in player.fleet:
            ship_id = ship.symbol 
            ship_track = 0

            for row in player.ocean_grid:
                ship_track += row.count(ship_id)

            if ship_track == 0:
                player.fleet.remove(ship) #enemy ship removed when destroyed, it wont check for it in further instances
                print("\n" + f"You sunk my {ship.name}!")
            
            if len(player.fleet) == 0:
                return False
            else:
                return True


    def place_ships(self, ship):
        """
        Parameters: 
        ship : object in self.fleet -> iterates via set_board(), each ship in a players fleet
        
        """
        try:
            self.display_ocean_grid()
            print(f"Place your {ship.name} ({ship.length} spaces)")
            chosen_row = int(input("Select row(y): ")) - 1
            chosen_column = int(input("Select column(x): ")) - 1

            choice = int(input("1:UP    2:Down       3:Right     4:Left"))

            if choice == 1 and (chosen_row - ship.length) >= -1: #UP
                for distance in range(chosen_column , (chosen_column - ship.length), -1):
                    if self.ocean_grid[chosen_row][chosen_column] == "W":
                        self.ocean_grid[chosen_row][chosen_column] = ship.symbol
                        chosen_row -= 1 # chosen_row = chosen_row + variable_for_direction???

                    #change below is working but needs more work/testing

                    else: 
                        chosen_row += ship.length
                        for distance in range(chosen_column , (chosen_column - ship.length), -1):
                            if self.ocean_grid[chosen_row][chosen_column] == ship.symbol or self.ocean_grid[chosen_row][chosen_column] == "W":
                                self.ocean_grid[chosen_row][chosen_column] = "W"
                                chosen_row -= 1
                 
                        raise Exception("Already a ship here")
            
            elif choice == 2 and (chosen_row + ship.length) <= 10: #DOWN
                for distance in range(chosen_column, (chosen_column + ship.length)):
                    if self.ocean_grid[chosen_row][chosen_column] == "W":
                        self.ocean_grid[chosen_row][chosen_column] = ship.symbol
                        chosen_row += 1

                    else:
                        print("\n There is a ship here already")
                        self.place_ships(ship)
            
            elif choice == 3 and (chosen_column + ship.length) <= 10: #RIGHT
                for distance in range(chosen_row, (chosen_row + ship.length)):
                    if self.ocean_grid[chosen_row][chosen_column] == "W":
                        self.ocean_grid[chosen_row][chosen_column] = ship.symbol
                        chosen_column += 1

                    
                    else:
                        print("\n There is a ship here already")
                        self.place_ships(ship)

            elif choice == 4 and (chosen_column - ship.length) >= -1: #LEFT
                for distance in range(chosen_row, (chosen_row - ship.length), -1):
                    if self.ocean_grid[chosen_row][chosen_column] == "W":
                        self.ocean_grid[chosen_row][chosen_column] = ship.symbol
                        chosen_column -= 1

                    
                    else:
                        print("\n There is a ship here already")
                        self.place_ships(ship)

            else:
                print("\n Critical Error: Restarting ship placement")
                self.place_ships(ship)

        except:
            print("\n Critical Error: Restarting ship placement")
            self.place_ships(ship)
        

    def set_board(self):
        for ship in self.fleet:
            self.place_ships(ship)




    #refactor for grids, to automate and allow selection of size
    # def board_size(self):
    #     size = input("Choose the size of the board x^2: ")
    #     grid = []
    #     i = 0
    #     while i < size:
    #         grid.append("W")


#Replace the ocean grid above with this test version, without using set_grid for faster testing!
# self.ocean_grid = [
#     ["D", "D", "W", "W", "W", "W", "W", "W", "W", "W"],
#     ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
#     ["S", "S", "S", "W", "W", "W", "W", "W", "W", "W"],
#     ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
#     ["B", "B", "B", "B", "W", "W", "W", "W", "W", "W"],
#     ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
#     ["A", "A", "A", "A", "A", "W", "W", "W", "W", "W"],
#     ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
#     ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
#     ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]
#     ] 


# def undo_placement(self):
#     for distance in range(chosen_column , (chosen_column - ship.length), -1):
#         if self.ocean_grid[chosen_row][chosen_column] == ship.symbol:
#             self.ocean_grid[chosen_row][chosen_column] = "W"
#             chosen_row -= 1
#         print("\n There is a ship here already")
#         return self.place_ships(ship)