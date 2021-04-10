from Natural import LCM_NN_N
from Integer import MUL_ZZ_Z
from Integer import SUB_ZZ_Z
from Integer import DIV_ZZ_Z
from RED_Q_Q import RED_Q_Q


def SUB_QQ_Q(arr1, arr2):
    nok = LCM_NN_N(arr1[1], arr2[1])
    nok1 = DIV_ZZ_Z([0, nok[0], list(nok[1])], [0, arr1[1][0], list(arr1[1][1])])
    nok2 = DIV_ZZ_Z([0, nok[0], list(nok[1])], [0, arr2[1][0], list(arr2[1][1])])
    ar1_ch = MUL_ZZ_Z(arr1[0], nok1)
    ar2_ch = MUL_ZZ_Z(arr2[0], nok2)
    res = SUB_ZZ_Z(ar1_ch, ar2_ch)
    res = [[res[0], res[1], list(res[2])], [nok[0], list(nok[1])]]

    return RED_Q_Q(res)
#Ельцов В.