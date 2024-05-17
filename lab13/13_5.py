def read_length_per_line(filename):
    f  = open(filename, 'r')
    file_lines_list = f.readlines()
    f.close()
    file_line_lengths_list = []
    for line in file_lines_list:
        file_line_lengths_list.append(len(line.strip()))
    return file_line_lengths_list

print(read_length_per_line('13_5_sentences_example.txt'))