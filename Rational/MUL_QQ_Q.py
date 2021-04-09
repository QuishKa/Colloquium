#Author: Radabolsky Vladislav 0308

import sys
sys.path.append(r'E:\ETU\Дискретка\Коллоквиум\Colloquium')
sys.path.append(r'E:\ETU\Дискретка\Коллоквиум\Colloquium\Integer')
sys.path.append(r'E:\ETU\Дискретка\Коллоквиум\Colloquium\Natural')

from Natural import new_MUL_NN_N


def MUL_ZZ_Z(arr1, arr2):

    ar1 = [arr1[1], list(arr1[2])]
    ar2 = [arr2[1], list(arr2[2])]

    res = new_MUL_NN_N(ar1, ar2)

    if res[1] == [0]:
        return [0, 1, [0]]
    elif (arr1[0] == 1 or arr2[0] == 1) and (arr1[0] != 1 or arr2[0] != 1):
        return [1, res[0], list(res[1])]
    else:
        return [0, res[0], list(res[1])]



def MUL_QQ_Q(first, second):
    result = list([MUL_ZZ_Z(first[0], second[0]), new_MUL_NN_N(first[1], second[1])])
    return result





