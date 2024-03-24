word = input("Enter a word: ")
if len(word) != 1 :
    converted_word = word[0].upper() + word[1:-1].lower() + word[-1].upper()
else :
    converted_word = word.upper()
print(f"The converted word is: {converted_word}.")