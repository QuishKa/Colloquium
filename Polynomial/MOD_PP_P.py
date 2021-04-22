from MUL_PP_P import MUL_PP_P
from DIV_PP_P import *
from SUB_PP_P import SUB_PP_P

def MOD_PP_P(numerator, denumerator):
    num, dnum = copy_polynom(numerator), copy_polynom(denumerator)
    div = DIV_PP_P(num, dnum)
    mul = MUL_PP_P(div, denumerator)
    return SUB_PP_P(num, mul)
    