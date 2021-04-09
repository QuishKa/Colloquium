from Natural import GCF_NN_N
from Integer import ABS_Z_N
from Integer import DIV_ZZ_Z


def RED_Q_Q(fract):
    res = [fract[0][:], fract[1][:]]
    gcd = GCF_NN_N(ABS_Z_N(res[0]), res[1])
    gcd.insert(0, 0)
    res[1].insert(0,0)
    res[0] = DIV_ZZ_Z(res[0], gcd)
    res[1] = ABS_Z_N(DIV_ZZ_Z(res[1], gcd))
    return res