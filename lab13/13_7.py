def process_barchart(filename):
    f = open(filename, 'r')
    file_lines_list = f.read().split('\n')
    f.close()
    letter_freq_list = []
    for line in file_lines_list:
        letter_freq_list.append((line[0], len(line[2:])))
    return tuple(letter_freq_list)

print(process_barchart('13_7_file.txt'))