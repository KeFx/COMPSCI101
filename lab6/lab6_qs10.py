expression = list(input("Enter an expression: "))
pairs_counter = 0
invalid_closing_bracket = False
num_of_open_brackets = 0

for char in expression :
    if char == "(":
        num_of_open_brackets += 1
    elif char == ')' and num_of_open_brackets:
        pairs_counter += 1
        num_of_open_brackets -= 1
    elif char == ')':
        invalid_closing_bracket = True

if invalid_closing_bracket or num_of_open_brackets:   
    print("Incorrect.") 
else :
    print("Correct.")
    print(f"There are {pairs_counter} pairs of parentheses.")