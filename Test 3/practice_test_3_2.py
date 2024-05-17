def add_full_stop(word_list):
    for index, word in enumerate(word_list):
        word_list[index] = word + '.'

data = ["hello", "world"]
add_full_stop(data)
print(data)
