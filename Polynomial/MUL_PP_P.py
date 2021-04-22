# 0308 Панько Иван


from MUL_PQ_P import MUL_PQ_P
from MUL_Pxk_P import MUL_Pxk_P
from ADD_PP_P import ADD_PP_P
import copy


def MUL_PP_P(p1, p2):
    if p1[0] > p2[0]:
        bigger = copy.deepcopy(p1)
        smaller = copy.deepcopy(p2)
    else:
        smaller = copy.deepcopy(p1)
        bigger = copy.deepcopy(p2)

    z = [0, 1, [0]]
    n = [1, [1]]
    q = [z, n]
    res = [0, [q]]

    for i in range(smaller[0] + 1):
        on_q = MUL_PQ_P(bigger, smaller[1][i])
        on_xk = MUL_Pxk_P(on_q, i)
        res = ADD_PP_P(res, on_xk)

    z = [0, 1, [0]]
    z1 = [1, 1, [0]]
    n = [1, [1]]
    q = [z, n]
    q1 = [z1, n]
    if res[1][res[0]] == q or res[1][res[0]] == q1:
        res = [0, [q]]

    return res
