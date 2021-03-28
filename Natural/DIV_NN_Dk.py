# Author: Doronin V.V. 0308
from COM_NN_D import COM_NN_D
from MUL_ND_N import MUL_ND_N


def DIV_NN_Dk(ax, bx):
    a = [ax[0], list(ax[1])]
    b = [bx[0], list(bx[1])]
    if COM_NN_D(a, [1, [0]]) == 0:
        return [0, 0]
    if COM_NN_D(b, [1, [0]]) == 0:
        return [0, 0]
    com = COM_NN_D(a, b)
    if com == 0:
        return [1, 0]
    elif com == 1:
        tmp = a
        a = b
        b = tmp
    subnum = [b[0], a[1][:b[0]]]
    if COM_NN_D(b, subnum) == 2:
        subnum = [b[0] + 1, a[1][:b[0] + 1]]
    x = 1
    y = 9
    while x < y:
        mul = MUL_ND_N(b, (x + y) // 2)
        com = COM_NN_D(mul, subnum)
        if com == 2:
            y = (x + y) // 2 - 1
        elif com == 1 or com == 0:
            x = (x + y) // 2 + 1
    else:
        mul = MUL_ND_N(b, y)
        com = COM_NN_D(mul, subnum)
        if com == 2:
            y -= 1
    return [y, a[0] - subnum[0]]
