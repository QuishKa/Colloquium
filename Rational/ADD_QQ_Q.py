from Natural import LCM_NN_N
from Integer import MUL_ZZ_Z
from Integer import ADD_ZZ_Z
from Integer import DIV_ZZ_Z


def ADD_QQ_Q(arr1, arr2):
    nok = LCM_NN_N(arr1[1], arr2[1])
    nok1 = DIV_ZZ_Z([0, nok[0], list(nok[1])], [0, arr1[1][0], list(arr1[1][1])])
    nok2 = DIV_ZZ_Z([0, nok[0], list(nok[1])], [0, arr2[1][0], list(arr2[1][1])])
    ar1_ch = MUL_ZZ_Z(arr1[0], nok1)
    ar2_ch = MUL_ZZ_Z(arr2[0], nok2)
    res = ADD_ZZ_Z(ar1_ch, ar2_ch)

    return [[res[0], res[1], list(res[2])], [nok[0], list(nok[1])]]
#Ельцов В.