from GCF_NN_N import GCF_NN_N, copy_num
from MUL_NN_N import MUL_NN_N
from DIV_NN_N import DIV_NN_N

def LCM_NN_N(a, b):
    a_c = copy_num(a)
    b_c = copy_num(b)

    mul = MUL_NN_N(a_c, b_c)
    gcf = GCF_NN_N(a_c, b_c)
    return DIV_NN_N(mul, gcf)
