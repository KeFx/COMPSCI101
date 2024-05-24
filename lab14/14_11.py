# letter_frequencies = [('a', 1)]

letter_frequencies = [('a', 16), ('b', 1), ('c', 6), ('d', 10), ('e', 18),
                     ('f', 3), ('g', 8), ('h', 14), ('i', 13), ('j', 0),
                     ('k', 1), ('l', 4), ('m', 4), ('n', 15), ('o', 12),
                     ('p', 6), ('q', 0), ('r', 10), ('s', 10), ('t', 8),
                     ('u', 2), ('v', 2), ('w', 6), ('x', 0), ('y', 5), ('z', 0)]
chart_list = []

max_frequency = 0
for (letter, frequency) in letter_frequencies:
    if frequency > 0:
        chart_list.append(letter + '#' * frequency)

        if frequency > max_frequency:
            max_frequency = frequency

chart_list.reverse()

text = ''
for i in range(max_frequency):
    for row in chart_list:
        if len(row) > i:
            text += row[i]
        else:
            text += ' '
    text += '\n'

text = text[::-1]

print(text)