def main():
    grid = input("Please enter a string representing TicTacToe grid: ")
    player1 = "X"
    player2 = "O"

    print("TicTacToe Grid:")
    print()
    print_grid(grid)
    print()

    print(f"Player {player1} has won: {check_win(grid, player1)}")
    print(f"Player {player2} has won: {check_win(grid, player2)}")

def print_grid(grid):
    rows = []
    for first_slot_in_row in range(0, len(grid), 3):
        rows.append('|'.join(grid[first_slot_in_row:first_slot_in_row+3]))
    print('\n-----\n'.join(rows))    

def check_win(grid_as_string, player):
    grid = turn_grid_string_to_grid_array(grid_as_string)
    return win_with_rows(grid, player)\
        or win_with_columns(grid, player)\
        or win_with_diagonals(grid, player)

def win_with_rows(grid, player):
    for row in grid:
        if is_row_completed_with(player, row):
            return True
    return False

def win_with_columns(grid, player):
    for column_index in range(len(grid)):
        if is_column_completed_with(player, column_index, grid):
            return True
    return False

def win_with_diagonals(grid, player):
    return is_main_diagonal_completed_with(player, grid)\
        or is_secondary_diagonal_completed_with(player, grid)

def is_row_completed_with(player, row):
    for slot in row:
        if slot != player:
            return False
    return True

def is_column_completed_with(player, column_index, grid):
    for row in grid:
        if row[column_index] != player:
            return False
    return True

def is_main_diagonal_completed_with(player, grid):
    for index in range(len(grid)):
        if grid[index][index] != player:
            return False
    return True

def is_secondary_diagonal_completed_with(player, grid):
    for index in range(len(grid)):
        if grid[index][(len(grid) - 1) - index] != player:
            return False
    return True

def turn_grid_string_to_grid_array(grid_as_string):
    arrayed_grid = []
    for first_slot_in_row in range(0, len(grid_as_string), 3):
        row = grid_as_string[first_slot_in_row:first_slot_in_row + 3]
        arrayed_grid.append(row)
    return arrayed_grid