from Natural import ADD_NN_N
from Natural import SUB_NN_N
from Natural import COM_NN_D
from POZ_Z_D import POZ_Z_D
from ABS_Z_N import ABS_Z_N

def ADD_ZZ_Z(num1z, num2z):
    num1n = ABS_Z_N(num1z)
    num2n = ABS_Z_N(num2z)
    resn = [1, [0]]
    resz = [0, 1, [0]]
    # a = 0, b = 0 => a + b = 0
    if POZ_Z_D(num1z) == 0 and POZ_Z_D(num2z) == 0:
        return [0, 1, [0]]
    # a = 0, b != 0 => a + b = b
    if POZ_Z_D(num1z) == 0 and POZ_Z_D(num2z) != 0:
        return num2z
    # a != 0, b = 0 => a + b = a
    if POZ_Z_D(num1z) != 0 and POZ_Z_D(num2z) == 0:
        return num1z

    # a > 0, b > 0 => a + b = |a| + |b|
    if POZ_Z_D(num1z) == 2 and POZ_Z_D(num2z) == 2:
        resn = ADD_NN_N(num1n, num2n)
        return [0, resn[0], resn[1]]

    # a > 0, b < 0, |a| > |b| => a + b = |a| - |b|
    if POZ_Z_D(num1z) == 2 and POZ_Z_D(num2z) == 1 and COM_NN_D(num1n, num2n) == 2:
        resn = SUB_NN_N(num1n, num2n)
        return [0, resn[0], resn[1]]
    # a > 0, b < 0, |a| < |b| => a + b = -1 * (|b| - |a|)
    if POZ_Z_D(num1z) == 2 and POZ_Z_D(num2z) == 1 and COM_NN_D(num1n, num2n) == 1:
        resn = SUB_NN_N(num2n, num1n)
        return [1, resn[0], resn[1]]
    # a > 0, b < 0, |a| = |b| => a + b = 0
    if POZ_Z_D(num1z) == 2 and POZ_Z_D(num2z) == 1 and COM_NN_D(num1n, num2n) == 0:
        return [0, 1, [0]]

    # a < 0, b > 0, |a| > |b| => a + b = -1 * (|a| - |b|)
    if POZ_Z_D(num1z) == 1 and POZ_Z_D(num2z) == 2 and COM_NN_D(num1n, num2n) == 2:
        resn = SUB_NN_N(num1n, num2n)
        return [1, resn[0], resn[1]]
    # a < 0, b > 0, |a| < |b| => a + b = |b| - |a|
    if POZ_Z_D(num1z) == 1 and POZ_Z_D(num2z) == 2 and COM_NN_D(num1n, num2n) == 1:
        resn = SUB_NN_N(num2n, num1n)
        return [0, resn[0], resn[1]]
    # a < 0, b > 0, |a| = |b| => a + b = 0
    if POZ_Z_D(num1z) == 1 and POZ_Z_D(num2z) == 2 and COM_NN_D(num1n, num2n) == 0:
        return [0, 1, [0]]

    # a < 0, b < 0 => a + b = -1 * (|a| + |b|)
    if POZ_Z_D(num1z) == 1 and POZ_Z_D(num2z) == 1:
        resn = ADD_NN_N(num1n, num2n)
        return [1, resn[0], resn[1]]
