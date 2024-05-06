def main():
    word = get_starting_word()
    hidden_word = get_hidden_word(word)
    request = "Enter your guess: "
    user_guess = get_user_guess(request, hidden_word)
    number_incorrect = get_number_incorrect(word, hidden_word, user_guess)
    print_feedback(word, user_guess, number_incorrect)