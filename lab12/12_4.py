def word_analysis(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    word_score = 0

    for char in word:
        word_score += letters.index(char)

    return word, len(word), word_score