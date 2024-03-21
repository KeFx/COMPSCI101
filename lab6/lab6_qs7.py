running = True
grades = []

while running :
    grade_input = (input("Enter a grade (blank to exit): "))
    if grade_input != "" :
        grades.append(int(grade_input))
    elif grade_input == "" :
        running = False

print(f"Grades: {grades}.")
if len(grades) != 0 :

    minimum = min(grades)
    maximum = max(grades)
    average = round(sum(grades)/len(grades), 1)

    print(f"The minimum grade is {minimum}.")
    print(f"The maximum grade is {maximum}.")
    print(f"The average grade is {average}.")