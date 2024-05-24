def write_high_score(filename, scores_list):
    scores_list.sort(reverse = True)

    txt = 'High Scores\n===========\n'
    for score, player in scores_list:
        txt +=  '\n' + player + '\t' + str(score)

    f = open(filename, 'w')
    f.write(txt)
    f.close()

write_high_score('khu772.txt', [(1500, "Ken"), (2700, "Ryu"), (1200, "Blanka"), (1100, "Zangief")])
