exp_a = "not(a or ((not b) or (not c)))"
exp_b = "(not a) and b and c"
inputs = [0, 1]


def check_expressions_equivalence(exp_1, exp_2):
    for a in inputs :
        for b in inputs:
            for c in inputs:
                if eval(exp_1) != eval(exp_2) :
                    print("no")
                    return
                
check_expressions_equivalence(exp_a, exp_b)