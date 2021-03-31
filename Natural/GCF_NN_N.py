from MOD_NN_N import MOD_NN_N
from DIV_NN_N import DIV_NN_N
from COM_NN_D import COM_NN_D
from NZER_N_B import NZER_N_B

def copy_num(x):
    return [x[0], x[1][:]]

def GCF_NN_N(a, b):
    '''
    Returns the greatest common factor of a and b.
    '''
    a_c = copy_num(a)
    b_c = copy_num(b)
    while not (NZER_N_B(a_c) or NZER_N_B(b_c)):
        if(COM_NN_D(a_c, b_c)==2):
            a_c = MOD_NN_N(a_c, b_c)
        else:
            b_c = MOD_NN_N(b_c, a_c)
    if(NZER_N_B(a_c)):
        return b_c
    else:
        return a_c
