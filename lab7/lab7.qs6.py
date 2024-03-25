registered_upis = ["cron777", "emac263", "gclo450", 
                "jcoc100", "jduj117", "lmes754", "mjac999"]

registered_passwords = ["SuiiiAlNassr23", "PcqcNP2022", "WhatElse06", 
                "HatOn4414", "BlanQueTTe2006", "GoatWC2022", "thriLLer82"]

print("Current list of UPIs:", registered_upis)
print("Current list of passwords:", registered_passwords)

u_action = input("Enter A to add a UPI/password pair or D to delete a pair: ")

if u_action == "A" :
    while True :
        new_UPI = input("Enter a new UPI: ")
        if new_UPI not in registered_upis :
            registered_upis.append(new_UPI)
            new_pass = input("Enter a new password: ")
            registered_passwords.append(new_pass)
            break
        else :
            print(f"{new_UPI} is already used!")
            
elif u_action == "D" :
    while True :
        delete_UPI = input("Enter the UPI to be deleted: ")
        if delete_UPI in registered_upis :
            while True :
                delete_password = input("Enter the current password: ")
                if delete_password == registered_passwords[registered_upis.index(delete_UPI)]:
                    registered_upis.remove(delete_UPI)
                    registered_passwords.remove(delete_password)
                    break
                else :
                    print("The password does not match!")
            break
        else :
            print(f"{delete_UPI} does not exist!")
            
print(f"Updated list of UPIs: {registered_upis}")
print(f"Updated list of passwords: {registered_passwords}")
