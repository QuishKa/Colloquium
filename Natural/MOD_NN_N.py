# Author: Radabolsky V.S. 0308
# dividend - делимое
# divisor - делитель
# quotient - частное
# Функция возвращает остаток от деления dividend на divisor


from DIV_NN_N import DIV_NN_N
from SUB_NDN_N import SUB_NDN_N


def MOD_NN_N(dividend, divisor):
    quotient = DIV_NN_N(dividend, divisor)
    print(quotient[1][0])
    return SUB_NDN_N(dividend, quotient[1][0], divisor)