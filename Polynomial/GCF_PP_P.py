# Author: Doronin V.V. 0308
from MOD_PP_P import MOD_PP_P
from DEG_P_N import DEG_P_N
from DIV_PP_P import copy_polynom


def GCF_PP_P(pol1, pol2):
    pol1 = copy_polynom(pol1)
    pol2 = copy_polynom(pol2)
    if DEG_P_N(pol1) < DEG_P_N(pol2):
        tmp = pol1
        pol1 = pol2
        pol2 = tmp
    res = MOD_PP_P(pol1, pol2)
    while res[0] != 0:
        pol1 = pol2
        pol2 = res
        res = MOD_PP_P(pol1, pol2)
    if res[1][0][0][2][0] == 0:
        return pol2
    else:
        return [0, [[[1, 1, [1]], [1, [1]]]]]