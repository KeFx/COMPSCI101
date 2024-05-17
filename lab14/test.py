

l = [[None,None],[None,None]]

idx = 1
for row_idx, row in enumerate(l):

    if row_idx + 1 <= 1:
        l[row_idx][idx] = '*'

print(l)
