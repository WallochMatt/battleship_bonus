
class Ship():
    def __init__(self, name, length, symbol): 
        self.name = name
        self.length = length #use length to determine how many spaces a ship takes when placed
        self.symbol = symbol

class  Destroyer(Ship):
    def __init__(self):
        super().__init__("Destroyer", 2, "D")

class Submarine(Ship):
    def __init__(self):
        super().__init__("Submarine", 3, "S")

class Battleship(Ship):
    def __init__(self):
        super().__init__("Battleship", 4, "B")

class AircraftCarrier(Ship):
    def __init__(self):
        super().__init__("Aircraft Carrier", 5, "A")
