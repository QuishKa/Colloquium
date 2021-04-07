#Author: Doronin V.V. 0308
#result rounded to floor
from ABS_Z_N import ABS_Z_N
from POZ_Z_D import POZ_Z_D
from DIV_NN_N import DIV_NN_N
from MOD_NN_N import MOD_NN_N
from ADD_1N_N import ADD_1N_N
from TRANS_N_Z import TRANS_N_Z


def DIV_ZZ_Z(int1, int2):
    a = POZ_Z_D(int1)
    b = POZ_Z_D(int2)
    int1 = ABS_Z_N(int1)
    int2 = ABS_Z_N(int2)
    res = DIV_NN_N(int1, int2)
    if a == b:
        return TRANS_N_Z(res)
    elif MOD_NN_N(int1, int2)[1] != [0]:
        res = TRANS_N_Z(ADD_1N_N(res))
        res[0] += 1
        return res
    else:
        res = TRANS_N_Z(res)
        res[0] += 1
        return res
