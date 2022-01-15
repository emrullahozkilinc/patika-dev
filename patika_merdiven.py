from itertools import permutations as per
from itertools import combinations as com
import numpy as np

pers = per([1, 2], 4)


def is_true(tup):
    st = False
    newl = tup.copy()
    for x in newl:
        for y in x:
            if y > 2:
                tup.remove(x)
                break
    return tup


def new_fun(n):
    l1 = []
    one_two = []
    for a in range(n):
        one_two.append(1)
        one_two.append(2)

    for x in range(2, n):
        perm = com(one_two, x)
        print(len(list(perm)))
        for y in perm:
            if (np.sum(y) == n) & (y not in l1):
                l1.append(y)
    return l1


def combinationss(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


print(combinationss(list(range(5)), 3))

