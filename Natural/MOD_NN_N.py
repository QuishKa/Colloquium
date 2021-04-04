# Author: Radabolsky V.S. 0308
# dividend - делимое
# divisor - делитель
# quotient - частное
# Функция возвращает остаток от деления dividend на divisor

from SUB_NN_N import SUB_NN_N
from COM_NN_D import COM_NN_D



def MOD_NN_N(dividend, divisor):
    result = dividend
    while COM_NN_D(result, divisor) != 1:
        print(result)
        result = SUB_NN_N(result, divisor)
    return result