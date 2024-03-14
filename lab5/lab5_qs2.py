import operator

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

input_operator = input("Enter the operator: ")
operators_table = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv
}
if input_operator in operators_table :
    answer = operators_table[input_operator](number1, number2)
    answer_rounded = round(answer, 1)

    print(f"{number1} {input_operator} {number2} = {answer_rounded}")

else :
    print(f"Operator not supported.")

