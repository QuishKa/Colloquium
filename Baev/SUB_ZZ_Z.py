def SUB_ZZ_Z(num1z, num2z):
    # a - b = a + -b
    if num2z[0] == 2:
        num2z[0] = 1
    elif num2z[0] == 1:
        num2z[0] = 2
    return ADD_ZZ_Z(num1z, num2z)
