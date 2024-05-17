def get_freq_of_e_ending_words(filename):
    f = open(filename, 'r')
    file_words_list = f.read().split()
    f.close()
    freq_of_words_ending_in_e = 0
    for word in file_words_list:
        if word[-1] == 'e':
            freq_of_words_ending_in_e += 1
    return freq_of_words_ending_in_e

print(get_freq_of_e_ending_words('13_6_file.txt'))