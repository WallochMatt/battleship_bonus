from players import Player

#x = Player()


# x.display_target_grid()
# x.display_ocean_grid()
# x.select_coordinates()

test = [[1, 2, 3, 4], 
[1, 2 ,3 ,4], 
[4, 6, 7, 8], 
[0, 9, 9, 9], 
[1, 0, 0, ]]

ship_id = 5
ship_track = 0
for row in test: #enemny ocean grid
    ship_track += row.count(ship_id)
if ship_track == 0:
    print("ship destroyed")