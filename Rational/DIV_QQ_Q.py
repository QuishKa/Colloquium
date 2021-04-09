#Author: Radabolsky Vladislav 0308

from MUL_QQ_Q import MUL_QQ_Q
from RED_Q_Q import RED_Q_Q

def DIV_QQ_Q(dividend, divisor):
    factor = list([[divisor[0][0], divisor[1][0], divisor[1][1]], [divisor[0][1], divisor[0][2]]])
    return RED_Q_Q(MUL_QQ_Q(dividend, factor))
