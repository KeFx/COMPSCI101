def get_list_of_four_letter_words(words_list):
    list_of_four_letter_words = []
    for i in words_list:
        if len(i) == 4:
            list_of_four_letter_words.append(i.lower())
    return list_of_four_letter_words