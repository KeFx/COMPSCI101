def get_letter_frequency(text):
    text += 'abcdefghijklmnopqrstuvwxyz'
    text_as_list = list(text.lower())
    text_as_list.sort()

    letter_frequence_tuples = []

    previous = "0"
    count = -1
    for char in text_as_list:
        if char == previous:
            count += 1
        else:
            if previous.isalpha():
                letter_frequence_tuples.append((previous, count))
            count = 0
            previous = char

    if previous.isalpha():
                letter_frequence_tuples.append((previous, count))
                
    return letter_frequence_tuples
    
text = "A journey of a 1000 miles begins with a single step."
letter_freq_list = get_letter_frequency(text)
print(f"Letter Frequencies: {letter_freq_list}")
