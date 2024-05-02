def get_user_selection():
    user_selection = int(input("Enter your selection: "))
    while user_selection < 0 or user_selection > 7:
        print("Invalid selection!")
        user_selection = int(input("Enter your selection: "))
    return user_selection
