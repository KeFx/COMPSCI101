lowered_input_sequence = input("Please enter a sequence of words: ").lower()

list = lowered_input_sequence.split(" ")
list.sort()

index = 0
for item in list :
        if item != '' :
            print(f"{index}. {item.capitalize()}")
            index += 1

