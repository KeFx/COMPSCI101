expression = list(input("Enter an expression: "))
pairs_counter = 0

def tell_if_character_is_in_list_and_remove_first_one_seen(char, list_) :
    for character in list_ :
        if character == char :
            expression[list_.index(character)] = " "
            return True
    return False

index = 0
while index < len(expression) :
    if expression[index] == "(" :
        if tell_if_character_is_in_list_and_remove_first_one_seen(")", expression) :
            expression[index] = " "
            pairs_counter += 1
    elif expression[index] == ")":
        expression[index] = "invalid"
    index += 1

if ("invalid" in expression) or ("(" in expression) :
    print("Incorrect.")
else :
    print("Correct.")
    print(f"There are {pairs_counter} pairs of parentheses.")
        
