sequence = input("Enter a sequence of words: ")

words = sequence.split(" ")
counter = 0
    
for i in words:
    if i != "" and i[0].isupper() :
        counter += 1
    
print(f"{counter} word(s) start with an uppercase letter.")
