def get_sum_evens_odds(numbers_list):
    even_sum = 0
    odd_sum = 0

    for number in numbers_list:
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number
    
    return even_sum, odd_sum