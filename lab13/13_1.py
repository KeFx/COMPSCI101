def get_total(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def create_tuples_list(n):
    tuples_list = []
    for i in range(1, n + 1):
        tuples_list.append((i, get_total(i)))
    return tuples_list