from MUL_NN_N import MUL_NN_N


def MUL_ZZ_Z(arr1, arr2):

    ar1 = [arr1[1], list(arr1[2])]
    ar2 = [arr2[1], list(arr2[2])]

    res = MUL_NN_N(ar1, ar2)

    if res[1] == [0]:
        return [0, 1, [0]]
    elif (arr1[0] == 1 or arr2[0] == 1) and (arr1[0] != 1 or arr2[0] != 1):
        return [1, res[0], list(res[1])]
    else:
        return [0, res[0], list(res[1])]
#Ельцов В.