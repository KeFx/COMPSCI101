def get_duplicates_count(numbers_list):
    numbers_list.sort()
    number_count_list = []
    
    for i in numbers_list:
        count = 0
        for j in numbers_list:
            if i == j:
                count += 1
            else
                

        number_count_tuple = (i, count)
        
        if (count != 1) and (number_count_tuple not in number_count_list):
            
            number_count_list.append(number_count_tuple)

    return number_count_list
            
numbers = [9, 5, 1, 4, 5, 1, 7, 7, 3, 2, 8, 1, 9, 4, 1, 2, 3, 9, 7, 6]
print(get_duplicates_count(numbers))
