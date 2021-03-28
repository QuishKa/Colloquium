# Author: Doronin V.V. 0308
from DIV_NN_Dk import DIV_NN_Dk
from SUB_NDN_N import SUB_NDN_N
from COM_NN_D import COM_NN_D
from MUL_Nk_N import MUL_Nk_N


def DIV_NN_N(ax, bx):
    a = [ax[0], list(ax[1])]
    b = [bx[0], list(bx[1])]
    com = COM_NN_D(a, b)
    if com == 1:
        tmp = a
        a = b
        b = tmp
    if com == 0:
        return [1, [1]]
    com = 2
    last = 0
    res = [0, []]
    while com == 2 or com == 0:
        x = DIV_NN_Dk(a, b)
        while last - 1 > x[1]:
            res[0] += 1
            res[1].append(0)
            last -= 1
        res[0] += 1
        res[1].append(x[0])
        last = x[1]
        a = SUB_NDN_N(a, x[0], MUL_Nk_N(b, x[1]))
        com = COM_NN_D(a, b)
    while last - 1 >= 0:
        res[0] += 1
        res[1].append(0)
        last -= 1
    return res
