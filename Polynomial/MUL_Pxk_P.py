# 0308 Панько Иван


import copy


def MUL_Pxk_P(p, k):
    newp = copy.deepcopy(p)
    for i in range(k):
        z = [0, 1, [0]]
        n = [1, [1]]
        q = [z, n]
        newp[1].insert(0, q)

    newp[0] = newp[0] + k

    return newp
