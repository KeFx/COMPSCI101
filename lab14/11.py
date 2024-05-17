def create_frequency_chart_file(letter_frequencies):
    frequency_chart_list = []

    max_length = 0
    for letter in letter_frequencies:
        
        if letter[1] + 1 > max_length:
            max_length = letter[1] + 1

        frequency_chart_list.append(letter[0] + '#' * letter[1])
        
    frequency_chart_list.reverse()

    text = ''
    for row_number in range(max_length):
        for column in frequency_chart_list:
            if len(column) == 1:
                pass
            elif len(column) - 1 >= row_number:
                text += column[row_number]
            else:
                text += ' '
        if row_number != max_length-1:
            text += '\n'

    f = open('khu772.txt', 'w')
    f.write(text[::-1])
    f.close()

def print_contents(filename):
    input_file = open(filename, 'r')
    content = input_file.read()
    input_file.close()
    print(content)

letter_frequencies = [('a', 16), ('b', 1), ('c', 6), ('d', 10), ('e', 18),
                     ('f', 3), ('g', 8), ('h', 14), ('i', 13), ('j', 0),
                     ('k', 1), ('l', 4), ('m', 4), ('n', 15), ('o', 12),
                     ('p', 6), ('q', 0), ('r', 10), ('s', 10), ('t', 8),
                     ('u', 2), ('v', 2), ('w', 6), ('x', 0), ('y', 5), ('z', 0)]

# lf = [('a', 5), ('b', 2), ('c', 1), ('d', 2), ('e', 10),
#                      ('f', 5), ('g', 5), ('h', 7), ('i', 5), ('j', 0),
#                      ('k', 0), ('l', 3), ('m', 5), ('n', 5), ('o', 5),
#                      ('p', 0), ('q', 0), ('r', 10), ('s', 3), ('t', 11),
#                      ('u', 3), ('v', 0), ('w', 1), ('x', 0), ('y', 6), ('z', 0)]

lf = [('a', 5), ('b', 2), ('c', 1)]
create_frequency_chart_file(lf)
print_contents('khu772.txt')