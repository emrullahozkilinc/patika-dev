lists = [[1, ['a', [3, 5]], ['cat'], 2], [[[3]], 'dog'], 4, 5]

flist = []


def birlestir(gelen_liste):
    for r, z in enumerate(gelen_liste):
        if type(z) == list:
            birlestir(gelen_liste[r])
        else:
            flist.append(z)
    return flist


print(birlestir(lists))
