import operator

def my_calculation(a, b, sign):
    return sign(a, b)

print(my_calculation(1, 2.2**(0.5), operator.add))