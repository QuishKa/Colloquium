from DIV_NN_Dk import DIV_NN_Dk
from COM_NN_D import COM_NN_D
from SUB_NDN_N import SUB_NDN_N
from MUL_Nk_N import MUL_Nk_N


def MOD_NN_N_2(ax, bx):
    a = [ax[0], ax[1].copy()]
    b = [bx[0], bx[1].copy()]
    if COM_NN_D(a, [1, [0]]) == 0:
        return [1, [0]]
    if COM_NN_D(b, [1, [0]]) == 0:
        return [1, [0]]
    com = COM_NN_D(a, b)
    if com == 1:
        tmp = a
        a = b
        b = tmp
    if com == 0:
        return [1, [1]]
    com = 2
    while com == 2 or com == 0:
        x = DIV_NN_Dk(a, b)
        a = SUB_NDN_N(a, x[0], MUL_Nk_N(b, x[1]))
        com = COM_NN_D(a, b)
    return a
