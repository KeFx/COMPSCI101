def get_pell_number(n):
    if n > 1:
        return 2 * get_pell_number(n-1) + get_pell_number(n-2)
    return n