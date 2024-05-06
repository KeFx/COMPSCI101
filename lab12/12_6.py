def get_min_median_max(numbers):
    min_ = min(numbers)
    max_ = max(numbers)
    median = get_median(numbers)

    return min_, median, max_

def get_median(numbers):
    numbers.sort()
    middle_index = (len(numbers) - 1) / 2
    if middle_index.is_integer():
        return numbers[int(middle_index)]
    else:
        return (numbers[int(middle_index-0.5)] + numbers[int(middle_index+0.5)]) / 2

print(get_min_median_max([2, 42, 12]))

