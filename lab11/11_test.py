def turn_grid_string_to_grid_array(grid_as_string):
    arrayified_grid = []
    for first_slot_in_row in range(0, len(grid_as_string), 3):
        row = grid_as_string[first_slot_in_row:first_slot_in_row + 3]
        arrayified_grid.append(row)
    return arrayified_grid