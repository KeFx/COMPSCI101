def draw_letter_frequency_chart(letter_freq_tuples):
    for freq_tuple in letter_freq_tuples:
        letter = freq_tuple[0]
        freq = freq_tuple[1]
        print(f"{letter}|{'#'*freq}{freq}")

def get_letter_frequency(text):
    text_as_list = list(text.lower())
    text_as_list.sort()

    letter_freq_tuples = []

    previous = "0"
    count = 0
    for char in text_as_list:
        if char == previous:
            count += 1
        else:
            if previous.isalpha():
                letter_freq_tuples.append((previous, count))
            count = 1
            previous = char

    if previous.isalpha():
                letter_freq_tuples.append((previous, count))
                
    return letter_freq_tuples

text = "A journey of a 1000 miles begins with a single step."
letter_freq_list = get_letter_frequency(text)
print("Letter Frequencies:")
draw_letter_frequency_chart(letter_freq_list)
