lists = [[1, ['a', 3, 5], ['cat'], 2], [3, 'dog'], 4, 5]

rev_list = []


def revAList(lisst):
    for x, y in enumerate(lisst):
        if type(lisst[x]) == list:
            revAList(lisst[x])
        else:
            if (x == len(lisst)-1):
                lisst.reverse()

    return lisst


print(revAList(lists))
