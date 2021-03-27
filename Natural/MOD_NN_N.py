# Author: Radabolsky V.S. 0308
# dividend - делимое
# divisor - делитель
# quotient - частное
# Функция возвращает остаток от деления dividend на divisor


import SUB_NN_N
import DIV_NN_N


def MOD_NN_N(dividend, divisor):
    quotient = DIV_NN_N.DIV_NN_N(dividend, divisor)
    return SUB_NN_N.SUB_NN_N(dividend, quotient)
