# Author: Doronin V.V. 0308
from GCF_PP_P import GCF_PP_P
from DER_P_P import DER_P_P
from DIV_PP_P import DIV_PP_P
from DIV_PP_P import copy_polynom


def NMR_P_P(pol):
    a = copy_polynom(pol)
    b = DER_P_P(a)
    c = GCF_PP_P(a, b)
    res = DIV_PP_P(a, c)
    return res
