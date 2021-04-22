from Integer import POZ_Z_D
from Integer import ABS_Z_N
from Natural import GCF_NN_N
from Natural import LCM_NN_N
from Integer import TRANS_N_Z

def FAC_P_Q(pol1):
    # pol1[1] - массив дробей
    # pol1[1][i] - дробь
    # pol1[1][i][0] - числитель дроби, целое
    # ABS_Z_N(pol1[1][i][0]) - числитель дроби, натуральное
    # pol1[1][i][1] - знаменатель дроби, натуральное
    m = pol1[0]
    NOD = [1, [1]]
    NOK = [1, [1]]
    i = 0
    while i <= m and POZ_Z_D(pol1[1][i][0]) == 0:
        i += 1
    if i <= m:
        NOD = ABS_Z_N(pol1[1][i][0])
        NOK = pol1[1][i][1]
        i += 1
    while i <= m:
        if POZ_Z_D(pol1[1][i][0]) != 0:
            if NOD != [1, [1]]:
                NOD = GCF_NN_N(NOD, ABS_Z_N(pol1[1][i][0]))
            NOK = LCM_NN_N(NOK, pol1[1][i][1])
        i = i + 1
    return [TRANS_N_Z(NOD), NOK]