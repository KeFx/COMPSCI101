vowels = "aeiouAEIOU"
word = input("Enter a word: ")

consonant_counter = 0

for letter in word: 
    if letter not in vowels:
        consonant_counter += 1

print(f"{consonant_counter} consonants.")