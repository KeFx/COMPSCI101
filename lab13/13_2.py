def read_lines(filename):
    f = open(filename, 'r')
    l = f.read().split('\n')
    f.close()
    return l