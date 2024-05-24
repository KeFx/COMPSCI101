def translate_english_maori(maori_dictionary, word):
    if word in maori_dictionary:
        print(f"'{word}' is translated into '{maori_dictionary[word]}'.")
    else:
        print("Sorry that word doesn't exist in Maori!")