def check_win(grid_as_string, player):
    grid = turn_to_gird(grid_as_string)
    return win_with_rows(grid, player) \
            or win_with_columns(grid, player) \
            or win_with_diagonals(grid, player)

def win_with_rows(grid, player):
    for row in grid:
        if (row[0] == row[1] == row[2] == player):
            return True
    return False

def win_with_columns(grid, player):
    for column in range(3):
        if (grid[0][column] == grid[1][column] == grid[2][column] == player):
            return True
    return False

def win_with_diagonals(grid, player):
    return win_with_decreasing_diagonal(grid, player) or win_with_increasing_diagonal(grid, player)

def win_with_increasing_diagonal(grid, player):
    for i in range(len(grid)):
        if grid[i][i] != player:
            return False
    return True

def win_with_decreasing_diagonal(grid, player):
    for slot_index, row in zip(range(len(grid[0]) - 1, -1, -1), grid):
        if row[slot_index] != player:
            return False
    return True

def turn_to_gird(grid):
    parsed_grid = []
    for first_slot_in_row in range(0, len(grid), 3):
        parsed_grid.append(grid[first_slot_in_row:first_slot_in_row + 3])
    return parsed_grid

grid = "XOXOXOOOX"
player1 = "X"
player2 = "O"
print(f"Player {player1} has won: {check_win(grid, player1)}")
print(f"Player {player2} has won: {check_win(grid, player2)}")