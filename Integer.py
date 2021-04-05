# To add your file use import, for example: from ADD_1N_N import ADD_1N_N
# It will add all the functions from that file and they can be used both here and in main
import sys
import random
sys.path.append('Integer\\')
from ABS_Z_N import ABS_Z_N
from ADD_ZZ_Z import ADD_ZZ_Z
from COM_NN_D import COM_NN_D
from DIV_ZZ_Z import DIV_ZZ_Z
from MUL_ZM_Z import MUL_ZM_Z
from POZ_Z_D import POZ_Z_D
from SUB_ZZ_Z import SUB_ZZ_Z
from TRANS_N_Z import TRANS_N_Z
from TRANS_Z_N import TRANS_Z_N
from MOD_ZZ_Z import MOD_ZZ_Z


def get_int(minus=0, exactnum=-1, minlen=1, maxlen=10000):
    if exactnum == -1:
        if random.randint(0, 100) < 20:
            num = str(random.randint(0, 2))
        else:
            leng = random.randint(minlen, maxlen)
            num = str(random.randint(10 ** (minlen - 1), 10 ** (leng - 1) * 9))
    else:
        num = str(exactnum)
    count = 0
    int_array = [random.choice([0, minus]), 1, []]
    for i in range(len(num)):
        if num[i] == '-':
            int_array[0] = 1
        else:
            int_array[2].append(int(num[i]))
            count += 1
    int_array[1] *= count
    print(int_array[0], int_array[1])
    print(*int_array[2])
    return int_array
