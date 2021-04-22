from Rational import MUL_QQ_Q
from DIV_PP_P import copy_polynom



def DER_P_P(polynom):
    p = copy_polynom(polynom)
    for i in range(p[0] - 1):
        zi = list(map(int, str(i)))
        zi = [[0, len(zi), zi], [1, [1]]]
        p[1][i] = MUL_QQ_Q(p[1][i + 1], zi)
    p[1].pop()
    p[0] -= 1
    return p

