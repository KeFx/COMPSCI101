def move_largest_to_end(number_list):
    number_list.reverse()
    index_max_number = number_list.index(max(number_list))
    number_list[0], number_list[index_max_number] = number_list[index_max_number], number_list[0]
    number_list.reverse()