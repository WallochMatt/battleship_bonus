
class Ship():
    def __init__(self): 
        self.name = ""
        self.length = "" #use length to determine how many spaces a ship takes when placed
        self.symbol = ""

class  Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.name = "Destroyer"
        self.length = 2 
        self.symbol = "D"

class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.name = "Submarine"
        self.length = 3 
        self.symbol = "S"

class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self.name = "Battleship"
        self.length = 4 
        self.symbol = "B"

class AircraftCarrier(Ship):
    def __init__(self):
        super().__init__()
        self.name = "Aircraft Carrier"
        self.length = 5 
        self.symbol = "A"