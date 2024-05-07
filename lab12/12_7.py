def get_duplicates_count(numbers_list):
    numbers_list.sort()
    number_count = []

    previous = 'x'
    count  = 0
    for i in numbers_list:
        
        if i == previous:
            count += 1
        else:
            if (count > 1) :
                number_count.append((previous, count))
            previous = i
            count = 1
            
    if (count > 1) :
        number_count.append((i, count))

    return number_count
            
# numbers = [1]
numbers = [9, 5, 1, 4, 5, 1, 7, 7, 3, 2, 8, 1, 9, 4, 1, 2, 3, 9, 7, 6]
print(get_duplicates_count(numbers))
