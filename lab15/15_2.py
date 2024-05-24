def word_analysis(text):
    text = text.lower()

    word_analysis_dict = {}

    words_in_text = text.split()
    for word in words_in_text:
        if word[0] not in word_analysis_dict:
            word_analysis_dict[word[0]] = 1
        else:
            word_analysis_dict[word[0]] += 1

    return word_analysis_dict

text = "The quick brown fox jumps over the lazy dog"
print(word_analysis(text))