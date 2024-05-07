def get_palindromes(words_list):
    palindromes = []
    not_palindromes = []

    for word in words_list:
        if is_palindrome(word):
            palindromes.append(word)
        else:
            not_palindromes.append(word)

    return (palindromes, not_palindromes)

def is_palindrome(word):
    return word == word[::-1]

word_list = ['cat', 'the', 'bag', 'wow', 'out', 'can']
result = get_palindromes(word_list)
print(result)
