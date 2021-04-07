# Author: Radabolsky V.S. 0308
# dividend - делимое
# divisor - делитель
# quotient - частное
# Функция возвращает остаток от деления dividend на divisor

from DIV_NN_N import DIV_NN_N
from COM_NN_D import COM_NN_D
from SUB_NN_N import SUB_NN_N
from MUL_NN_N import MUL_NN_N


def MOD_NN_N(ax, bx):
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
    x = DIV_NN_N(a, b)
    a = SUB_NN_N(a, MUL_NN_N(b, x))
    return a
