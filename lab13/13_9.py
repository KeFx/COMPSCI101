def get_target_numbers(filename):
    f = open(filename, 'r')
    max_amount = int(f.readline().strip())
    range_min = int(f.readline().strip())
    range_max = int(f.readline().strip())

    numbers = list(map(int, f.read().split()))
    f.close()
    numbers.sort()

    target_numbers = []
    for number in numbers:
        if len(target_numbers) == max_amount:
            return target_numbers
        elif range_min <= number <= range_max:
            target_numbers.append(number)

    return target_numbers

print(get_target_numbers('13_9_number.txt'))
    
