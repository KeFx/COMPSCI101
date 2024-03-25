sentence = input("Please enter the sentence: ")
start_rm = sentence.find("(")
end_rm = sentence.rfind(")")

if start_rm == -1 or end_rm == -1 :
    print("No text to remove.")
else : 
    print(f"New sentence after removal: {sentence[:start_rm-1] + sentence[end_rm+1:]}")