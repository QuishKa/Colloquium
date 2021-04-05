def ADD_ZZ_Z(num1z, num2z):
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
        return [0, ADD_NN_N(num1z, num2z)[0], ADD_NN_N(num1z, num2z)[1]]

    # a > 0, b < 0, |a| > |b| => a + b = |a| - |b|
    if POZ_Z_D(num1z) == 2 and POZ_Z_D(num2z) == 1 and COM_NN_D(ABS_Z_N(num1z), ABS_Z_N(num2z)) == 2:
        return [0, SUB_NN_N(ABS_Z_N(num1z), ABS_Z_N(num2z))[0], SUB_NN_N(ABS_Z_N(num1z), ABS_Z_N(num2z))[1]]
    # a > 0, b < 0, |a| < |b| => a + b = -1 * (|b| - |a|)
    if POZ_Z_D(num1z) == 2 and POZ_Z_D(num2z) == 1 and COM_NN_D(ABS_Z_N(num1z), ABS_Z_N(num2z)) == 1:
        return [1, SUB_NN_N(ABS_Z_N(num2z), ABS_Z_N(num1z))[0], SUB_NN_N(ABS_Z_N(num2z), ABS_Z_N(num1z))[1]]
    # a > 0, b < 0, |a| = |b| => a + b = 0
    if POZ_Z_D(num1z) == 2 and POZ_Z_D(num2z) == 1 and COM_NN_D(ABS_Z_N(num1z), ABS_Z_N(num2z)) == 0:
        return [0, 1, [0]]

    # a < 0, b > 0, |a| > |b| => a + b = -1 * (|a| - |b|)
    if POZ_Z_D(num1z) == 1 and POZ_Z_D(num2z) == 2 and COM_NN_D(ABS_Z_N(num1z), ABS_Z_N(num2z)) == 2:
        return [1, SUB_NN_N(ABS_Z_N(num1z), ABS_Z_N(num2z))[0], SUB_NN_N(ABS_Z_N(num1z), ABS_Z_N(num2z))[1]]
    # a < 0, b > 0, |a| < |b| => a + b = |b| - |a|
    if POZ_Z_D(num1z) == 1 and POZ_Z_D(num2z) == 2 and COM_NN_D(ABS_Z_N(num1z), ABS_Z_N(num2z)) == 1:
        return [0, SUB_NN_N(ABS_Z_N(num2z), ABS_Z_N(num1z))[0], SUB_NN_N(ABS_Z_N(num2z), ABS_Z_N(num1z))[1]]
    # a < 0, b > 0, |a| = |b| => a + b = 0
    if POZ_Z_D(num1z) == 1 and POZ_Z_D(num2z) == 2 and COM_NN_D(ABS_Z_N(num1z), ABS_Z_N(num2z)) == 0:
        return [0, 1, [0]]

    # a < 0, b < 0 => a + b = -1 * (|a| + |b|)
    if POZ_Z_D(num1z) == 1 and POZ_Z_D(num2z) == 1:
        return [1, ADD_NN_N(num1z, num2z)[0], ADD_NN_N(num1z, num2z)[1]]
