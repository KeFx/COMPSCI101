def get_string_length_tuples(words_list):
    word_length_tuples_list = []
    for word in words_list:
        word_length_tuple = word, len(word)
        word_length_tuples_list.append(word_length_tuple)
    return word_length_tuples_list