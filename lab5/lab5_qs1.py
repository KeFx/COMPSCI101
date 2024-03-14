side_1 = int(input("Enter the length of the first side: "))
side_2 = int(input("Enter the length of the second side: "))
side_3 = int(input("Enter the length of the third side: "))

if side_1 >= (side_2 + side_3) or side_2 >= (side_1 + side_3) or side_3 >= (side_2 + side_1) :
    print("The triangle does not exist.")
elif side_1 == side_2 == side_3 :
    print("The triangle is equilateral.")
elif side_1 == side_2 or side_3 == side_2 or side_1 == side_3 :
    print("The triangle is isosceles.")
else :
    print("The triangle is obtuse.")
    
