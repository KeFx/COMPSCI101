def read_numbers(filename):
    f = open(filename, 'r')
    file_string = f.read()
    f.close()
    file_elements = file_string.split()
    numbers = []
    for element in file_elements:
        numbers.append(int(element.strip()))
    
    total = sum(numbers)
    average = round(sum(numbers)/len(numbers), 1)
    
    return (total, average)