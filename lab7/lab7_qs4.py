password = input("Please enter your password: ").strip()

def atleast_5_alpha(psswrd):
    count = 0
    for char in psswrd :
        if char.isalpha() :
            count += 1
        if count == 5 :
            return True

def atleast_4_num(psswrd):
    count = 0
    for char in psswrd :
        if char.isnumeric() :
            count += 1
        if count == 5 :
            return True

def is_password_valid(psswrd) :
    return (len(psswrd) >= 10) and ("123" not in psswrd) and ("abc" not in psswrd) and atleast_5_alpha(psswrd) and atleast_4_num(psswrd)

if is_password_valid(password):
    print("Your password is valid!")
else :
    print("Your password is invalid!")