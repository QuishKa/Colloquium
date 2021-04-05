# Author: Radabolsky V.S. 0308
# dividend - делимое
# divisor - делитель
# quotient - частное
# Функция возвращает остаток от деления dividend на divisor

from SUB_NN_N import SUB_NN_N
from COM_NN_D import COM_NN_D
from DIV_NN_N import DIV_NN_N
from MUL_NN_N import MUL_NN_N


def MOD_NN_N(dividend, divisor):
    com = COM_NN_D(dividend, divisor)
    if com == 0:
        return 0
    elif com == 1:
        tmp = dividend
        dividend = divisor
        divisor = tmp
    divres = DIV_NN_N(dividend, divisor)
    res = SUB_NN_N(dividend, MUL_NN_N(divisor, divres))
    return res
