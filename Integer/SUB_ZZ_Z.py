from ADD_ZZ_Z import ADD_ZZ_Z
def SUB_ZZ_Z(num1z, num2z):
    # a - b = a + -b
    if num2z[0] == 0:
        num2z[0] = 1
    elif num2z[0] == 1:
        num2z[0] = 0
    return ADD_ZZ_Z(num1z, num2z)
