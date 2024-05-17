def write_words_start_vowel(filename, names):
    f = open(filename, 'w')
    
    vowels = 'aeiouAEIOU'
    for name in names:
        if name[0] in vowels:
            f.write(name + '\n')
    f.close()

def print_contents(filename):
    input_file = open(filename, 'r')
    content = input_file.read()
    input_file.close()
    print(content)

write_words_start_vowel('khu772.txt', ['life', 'is', 'a', 'long', 'journey', 'with', 'problems', 'to', 'solve'])
print_contents('khu772.txt')
