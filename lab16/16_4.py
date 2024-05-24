def count_word_occurrences(sentence):
    sentence = sentence.split()

    word_counts_dict = {}
    for word in sentence:
        if word not in word_counts_dict:
            word_counts_dict[word] = 1
        else:
            word_counts_dict[word] += 1
    
    return word_counts_dict

sentence = 'ann met an ant'
word_counts_dict = count_word_occurrences(sentence)
for key in sorted(word_counts_dict):
    print(key, word_counts_dict[key])