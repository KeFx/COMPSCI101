def get_encrypted(word, key):
    encrypted_word = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in word:
        encrypted_word += key[alphabet.index(char)]
    return encrypted_word