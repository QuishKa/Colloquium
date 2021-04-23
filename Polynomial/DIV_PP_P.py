from DIV_QQ_Q import DIV_QQ_Q
from DEG_P_N import DEG_P_N
from MUL_Pxk_P import MUL_Pxk_P
from SUB_PP_P import SUB_PP_P
from ADD_PP_P import ADD_PP_P
from time import time



from MUL_PQ_P import MUL_PQ_P


#structure: [m, [q0, q1, ..., qn]]

def copy_polynom(p):
    new_p = [p[0], []]
    for i in range(p[0]+1):
        q = p[1][i]
        new_q = [[0,0,[]], [0,[]]]
        new_q[0][0] = q[0][0]
        new_q[0][1] = q[0][1]
        new_q[0][2] = q[0][2][:]
        new_q[1][0] = q[1][0]
        new_q[1][1] = q[1][1][:]
        new_p[1].append(new_q)
    return new_p

def DIV_PP_P(num, denum):
    nnum, ndenum = copy_polynom(num), copy_polynom(denum)
    res = [-1, []]
    last = 0
    if(DEG_P_N(nnum)<DEG_P_N(ndenum)):
        res = [0, [[[0, 1, [0]], [1, [1]]]]]
    while(DEG_P_N(nnum)>=DEG_P_N(ndenum)):
        n = DEG_P_N(nnum)
        while last - 1 > n:
            res[1].insert(0, [[0, 1, [0]], [1, [1]]])
            res[0] += 1
            last -= 1
        s = DEG_P_N(ndenum)
        an = nnum[1][n]
        bs = ndenum[1][s]

        coefficient = DIV_QQ_Q(an, bs)
        sub = MUL_Pxk_P(ndenum, n-s)
        sub = MUL_PQ_P(sub, coefficient)
        res[1].insert(0,coefficient)
        res[0]+=1
        nnum = SUB_PP_P(nnum, sub)
        last = n
    return res