from Rational import SUB_QQ_Q
from Rational import RED_Q_Q


def SUB_PP_P(arr1, arr2):
    if arr1[0] > arr2[0]:
        r = arr2[0]
        for i in range(arr2[0] + 1):
            arr1[1][i] = SUB_QQ_Q(arr1[1][i], arr2[1][i])
        i = 0
        while i != r + 1:
            if arr1[1][i][0][2] == [0]:
                arr1[1].remove(arr1[1][i])
                arr1[0] -= arr1[0]
                r = r - 1
                i -= 1
            i += 1
            return arr1
    else:
        r = arr1[0]
        for i in range(arr1[0]+1):
            arr2[1][i] = SUB_QQ_Q(arr1[1][i], arr2[1][i])
        i = 0
        while i != r + 1:
            if arr2[1][i][0][2] == [0]:
                arr2[1].remove(arr2[1][i])
                arr2[0] -= arr2[0]
                r = r - 1
                i -= 1
            i += 1
        return arr2
#Ельцов В.