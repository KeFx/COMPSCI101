txt = input("Enter your text: ")

for char in txt:
    if not char.isalpha() and not char.isnumeric() and char != ' ': 
        print(char, end='')