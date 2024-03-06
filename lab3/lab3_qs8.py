import operator

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

operators = {
    "equal to" : operator.eq,
    "greater than" : operator.gt,
    "less than" : operator.lt,
    "not equal to" : operator.ne,
    "greater than or equal to" : operator.ge,
    "less than or equal to" : operator.le
}

for current_operator in operators : 
    print(f"{first_number} {current_operator} {second_number}: {operators[current_operator](first_number, second_number)}")