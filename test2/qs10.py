security_string = "$S***R**S*$*S**RR**S**RRR"
safe = True

def is_str_secure(start, stop, step, s_str):
    for j in s_str[start:stop:step]:
            if j == 'S':
                return True
            elif j == 'R':
                return False
    return True

for idx, i in enumerate(security_string):
    if i == '$':

        if not is_str_secure(idx,None,-1,security_string):
            safe = False
            break

        if not is_str_secure(idx,None,None,security_string):
            safe = False
            break
        
if not safe:
    print("A robbery has been detected!")
elif safe:
    print("The money is safe.")