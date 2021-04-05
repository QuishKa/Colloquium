from Natural import NZER_N_B
from ABS_Z_N import ABS_Z_N
def POZ_Z_D(num):
    if NZER_N_B(ABS_Z_N(num)) == 1:
        return 0
    elif num[0] == 0:
        return 2
    else:
        return 1
