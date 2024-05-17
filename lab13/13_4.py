def get_list_of_words_start_with(filename, target_letter):
    f = open(filename, 'r')
    words_list = f.read().lower().split()
    target_words_list = []
    f.close()
    for word in words_list:
        if (word[0] == target_letter) and (word not in target_words_list):
            target_words_list.append(word)
    return target_words_list

words_list = get_list_of_words_start_with('13_4_file.txt', 's')
print(words_list)