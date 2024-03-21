expression = list(input("Enter an expression: "))
pairs_counter = 0
invalid_closing_bracket = False
pending_opens = []

for char in expression :
    if char == "(":
        pending_opens.append(char)
    elif char == ')' and (len(pending_opens) != 0):
        pairs_counter += 1
        pending_opens.pop()
    elif char == ')':
        invalid_closing_bracket = True
        break

if invalid_closing_bracket or len(pending_opens) != 0:   
    print("Incorrect.") 
else :
    print("Correct.")
    print(f"There are {pairs_counter} pairs of parentheses.")