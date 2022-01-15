import numpy as np


def ret_cat(x, y):
    if (x <= 3) & (y <= 3):
        return 1
    elif ((x > 3) & (x <= 6)) & (y <= 3):
        return 2
    elif ((x > 6) & (x <= 9)) & (y <= 3):
        return 3
    elif (x <= 3) & ((y > 3) & (y <= 6)):
        return 4
    elif ((x > 3) & (x <= 6)) & ((y > 3) & (y <= 6)):
        return 5
    elif ((x > 6) & (x <= 9)) & ((y > 3) & (y <= 6)):
        return 6
    elif (x <= 3) & ((y > 6) & (y <= 9)):
        return 7
    elif ((x > 3) & (x <= 6)) & ((y > 6) & (y <= 9)):
        return 8
    elif ((x > 6) & (x <= 9)) & ((y > 6) & (y <= 9)):
        return 9


quads = []


def control_mat(mat, con):
    for i, x in enumerate(mat):
        for j, y in enumerate(x):
            if (y in sud[i][:j] + sud[i][j + 1:]) & (y != "x"):
                if (con == 1) & (ret_cat(j + 1, i + 1) not in quads):
                    quads.append(ret_cat(j + 1, i + 1))
                elif (con == 2) & (ret_cat(i + 1, j + 1) not in quads):
                    quads.append(ret_cat(i + 1, j + 1))
                elif (con == 3) & (i+1 not in quads):
                    quads.append(i+1)


inp = ["(1,2,3,4,5,6,7,8,1)",
       "(x,x,x,x,x,x,x,x,x)",
       "(x,x,x,x,x,x,x,x,x)",
       "(1,x,x,x,x,x,x,x,x)",
       "(x,x,x,x,x,x,x,x,x)",
       "(x,x,x,x,x,x,x,x,x)",
       "(x,x,x,x,5,x,x,x,x)",
       "(x,x,x,5,x,x,x,x,2)",
       "(x,x,x,x,x,x,x,2,x)"]

sud = [j.split(",") for j in inp]

for a, b in enumerate(sud):
    sud[a][0] = b[0][1]
    sud[a][8] = b[8][0]

control_mat(sud, 1)

t_sud = [list(l) for l in np.array(sud).T]
control_mat(t_sud, 2)


sub_quad = [[] for _ in range(9)]
for i, x in enumerate(sud):
    for j, y in enumerate(x):
        sub_quad[ret_cat(j+1, i+1)-1].append(y)

control_mat(sub_quad, 3)
print(quads)
