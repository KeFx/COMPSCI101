word1 = input("Please enter the first 6 letter word: ")
word2 = input("Please enter the second 6 letter word: ")
pokemon_name = word1[0:4] + word2[-3:]
print(f"New Pokemon name: {pokemon_name}")