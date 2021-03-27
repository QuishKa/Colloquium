# Author: Radabolsky V.S. 0308
# decreasing - уменьшаемое
# digit - цифра на которую умножается второе число
# subtraction - второе число
# Функция возвращает результат вычитания из первого введенного числа
# второго, умноженного на цифру. В случае, когда вычитаемое оказывается
# больше уменьшаемого, возвращается None

import SUB_NN_N
import MUL_ND_N
import COM_NN_D


def SUB_NDN_N(decreasing, digit, subtraction):
    sub = MUL_ND_N.MUL_ND_N(subtraction, digit)
    condition = COM_NN_D.COM_NN_D(decreasing, sub)
    if condition == 2:
        return SUB_NN_N.SUB_NN_N(decreasing, sub)
    elif condition == 0:
        return [1, [0]]
    else:
        return None


