def get_acceptable_input(acceptable_words):
    prompt = "Enter a word: "
    while True:
        word = input(prompt)
        if word in acceptable_words:
            return word

chosen = get_acceptable_input(["WORDS", "TEST", "EXAM", "QUESTION"])
print(chosen)
