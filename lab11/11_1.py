def move_largest_to_end(number_list):
    number_list.reverse()
    index_max = number_list.index(max(number_list))
    swap_positions(number_list, 0, index_max)
    number_list.reverse()

def swap_positions(list_, pos1, pos2):
    list_[pos1], list_[pos2] = list_[pos2], list_[pos1]