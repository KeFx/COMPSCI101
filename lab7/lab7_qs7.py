sentence = input("Please enter a sentence: ")
newlist = (list(dict.fromkeys(sentence.split(" "))))
newlist.reverse()
print("Unique words: " + ", ".join(newlist))