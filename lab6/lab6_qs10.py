expression = list("))((")
# expression = list("((1 + 2) * (2 - (2 + 4) / 4))")
# print(expression)
counter = 0

def tell_if_character_in_list_and_remove_first_seen(char, list_) :
    for character in list_ :
        if character == char:
            expression[expression.index(character)] = " "
            return True
    return False

for character in expression :
    # print("index", expression.index(character))
    # print("list:", expression)
    if character == "(":
        if tell_if_character_in_list_and_remove_first_seen(")", expression):
            # print(True)
            expression[expression.index(character)] = " "
            
            # print(expression)
            counter += 1
            # print(counter)

if ("(" in expression) or (")" in expression):
    print("Incorrect.")
else:
    print("Correct.")

print(f"There are {counter} pairs of parentheses.")
        
