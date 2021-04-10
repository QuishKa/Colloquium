# 0308 Панько Иван


from Rational import MUL_QQ_Q
import copy


def MUL_PQ_P(p, q):
    pnew = copy.deepcopy(p)
    m = pnew[0] + 1
    for i in range(m):
        pnew[1][i] = MUL_QQ_Q(pnew[1][i], q)

    return pnew
