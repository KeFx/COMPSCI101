inputs = [0, 1]

expression_1_format = input("Enter expression 1")
expression_2_format = input("Enter expression 2")

def evaluate_expression(expression) :
    return eval(expression)

def expression_are_equivalent(exp1, exp2):
    for a in inputs :
        for b in inputs :
            for c in inputs :
                if exp1(a, b, c) != exp2(a, b, c):
                    return False
    return True

if expression_are_equivalent(evaluate_expression(expression_1_format), evaluate_expression(expression_2_format)) :
    print("equivalent.")
else : 
    print("not equivalent.")
