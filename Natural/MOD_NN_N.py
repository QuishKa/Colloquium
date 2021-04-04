# Author: Radabolsky V.S. 0308
# dividend - делимое
# divisor - делитель
# quotient - частное
# Функция возвращает остаток от деления dividend на divisor


from DIV_NN_N import DIV_NN_N
from SUB_NN_N import SUB_NN_N
from COM_NN_D import COM_NN_D


def MOD_NN_N(dividend, divisor):
    quotient = DIV_NN_N(dividend, divisor)
    result = dividend
    while COM_NN_D(result, quotient) != 1:
        result = SUB_NN_N(result, quotient)
    return result
