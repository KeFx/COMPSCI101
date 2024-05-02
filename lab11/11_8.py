def print_grid(grid):
    rows = []
    for first_slot_in_row in range(0, len(grid), 3):
        rows.append('|'.join(grid[first_slot_in_row:first_slot_in_row+3]))
    print('\n-----\n'.join(rows))    
