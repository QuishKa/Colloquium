#Author: Doronin V.V. 0308
#result rounded to floor
from ABS_Z_N import ABS_Z_N
from POZ_Z_D import POZ_Z_D
from Natural import MOD_NN_N
from Natural import ADD_1N_N
from TRANS_N_Z import TRANS_N_Z


def MOD_ZZ_Z(int1, int2):
    a = POZ_Z_D(int1)
    b = POZ_Z_D(int2)
    int1 = ABS_Z_N(int1)
    int2 = ABS_Z_N(int2)
    res = MOD_NN_N(int1, int2)
    if a == b:
        return TRANS_N_Z(res)
    elif res[1][0] != 0:
        res = TRANS_N_Z(ADD_1N_N(res))
        return res
    else:
        return res
