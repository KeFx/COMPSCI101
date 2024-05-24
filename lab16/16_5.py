def print_students_with_target_grade(grade_dict, target_grade):
    any_student_met_target = False
    first_student_to_meet_target = True

    for student, grade in sorted(grade_dict.items()):
        
        if grade == target_grade:
            if first_student_to_meet_target:
                any_student_met_target = True

                print(f"The following students have the "
                      f"target grade {target_grade}:", end = "")
                first_student_to_meet_target = False

            print(f" {student}", end = '')

    if not any_student_met_target:
        print(f"No students have the target grade {target_grade}")
    else:
        print()
    
    

grade_dict = {"Peter":"B", "Jane":"A", "Kathy":"A", "Mark":"A", "Tom":"C"}
target_grade = "D"
print_students_with_target_grade(grade_dict, target_grade)
target_grade = "D"
print_students_with_target_grade(grade_dict, target_grade)