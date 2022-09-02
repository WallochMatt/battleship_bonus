battle_board = [
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
]#copy() may come in handy


def print_board():
    print("       1    2    3    4    5    6    7    8    9    10")
    incrementor = 1
    while incrementor < len(battle_board):
        for row in battle_board:
            print(f"  {incrementor}: {row}")
            incrementor += 1

def select_coordinates():
    chosen_row = int(input("Select row(y): ")) #turn to a player attack method?
    chosen_column = int(input("Select column(x): "))
    battle_board[chosen_row-1].pop(chosen_column-1)
    battle_board[chosen_row-1].insert(chosen_column-1, "X") #if opp_board (coordinates) == "S" then it hits


print_board()
select_coordinates()
print_board()