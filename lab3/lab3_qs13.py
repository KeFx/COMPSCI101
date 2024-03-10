import operator

# def delta_find(a, b, c) :
#     return b**2 - 4*a*c

def quadratic_find(a, b, c) :
    delta = b**2 - 4*a*c
    if (delta > 0):
        return ()
    else 
    return 1;
return None
    return sign(-b, delta**(1/2))/(2*a)

print("A quadratic equation has the form: ax^2 + bx + c")

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

delta = delta_find(a, b, c)

if delta > 0:
    print(f"There are two roots: {round(quadratic_find(a, b, delta, operator.sub), 2)} and {round(quadratic_find(a, b, delta, operator.add), 2)}")
elif delta == 0:
    print(f"There is a single root: {round(quadratic_find(a, b, delta, operator.add), 2)}")
else:
    print("There is no root in the space of real numbers.")



#############################
def get_input(prompt):
    return [1, 2, 3]


    [a, b,c ] = get_input("Enter a, b ,c please");

    roots = get_roots(a, b, c);

    if (roots == [] && length == 2) {

    } else if (roots istype of number) {

    } else if {roots == None} {

    } else {
        throw Error
    }
        
# paramater a , bc, 
        # return array[] consists of roots
        # if delta < 0, the array will be empty
def get_roots(a, b, c)