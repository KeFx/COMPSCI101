def get_duplicates_count(numbers_list):
    numbers_list.sort()
    print(numbers_list)
    number_count = {}

    previous = 'x'
    count  = 0
    
    for index, i in enumerate(numbers_list):
        if i == previous:
            count += 1
        else:
            if (count > 1) :
                number_count[previous] = count
            previous = i
            count = 1

    if (count > 1) :
        number_count[previous] = count

    print(number_count)
            
# numbers = [1]
numbers = [9, 5, 1, 4, 5, 1, 7, 7, 3, 2, 8, 1, 9, 4, 1, 2, 3, 9, 7, 6]
print(get_duplicates_count(numbers))
