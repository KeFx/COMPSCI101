def has_at_least_amount_alpha(amount, string):
    counter = 0
    for i in string:
        if i.isalpha():
            counter += 1
    return counter >= amount

def has_at_least_amount_num(amount, string):
    counter = 0
    for i in string:
        if i.isnumeric():
            counter += 1
    return counter >= amount

def is_valid_password(password):
    if (len(password) < 10) or ('123' in password) or ('abc' in password) or (not has_at_least_amount_alpha(5, password)) or (not has_at_least_amount_num(4, password)):
        return False
    return True