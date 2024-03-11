import math
pi_unicode = "\u03C0"

ordinal_words = ["First", "Second", "Third"]
questions = [f"Enter the value of sin({pi_unicode}/2): ", f"Enter the value of cos({pi_unicode}): ", f"Enter the value of sin({pi_unicode}/6): "]
answers = [math.sin(math.pi/2), math.cos(math.pi), math.sin(math.pi/6)]
user_answers = []

for question in questions :
    user_answers.append(float(input(question)))

for answer in answers :
    current_order = answers.index(answer)
    if math.isclose(answer, user_answers[current_order], abs_tol = 0.001) :
        print(f"{ordinal_words[current_order]} answer is correct.")
    else:
        print(f"{ordinal_words[current_order]} answer is incorrect.")