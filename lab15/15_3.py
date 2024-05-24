def word_length_analysis(text):
    words = text.split()

    word_length_dict = {}
    for word in words:
        if len(word) not in word_length_dict:
            word_length_dict[len(word)] = 1
        else:
            word_length_dict[len(word)] += 1

    return word_length_dict