# To add your file use import, for example: from ADD_1N_N import ADD_1N_N
# It will add all the functions from that file and they can be used both here and in main
import sys
import random
sys.path.append('Natural\\')
from ADD_1N_N import ADD_1N_N
from ADD_NN_N import ADD_NN_N
from COM_NN_D import COM_NN_D
from MOD_NN_N import MOD_NN_N
from MUL_ND_N import MUL_ND_N
from MUL_Nk_N import MUL_Nk_N
from MUL_NN_N import MUL_NN_N
from NZER_N_B import NZER_N_B
from SUB_NDN_N import SUB_NDN_N
from SUB_NN_N import SUB_NN_N
from DIV_NN_Dk import DIV_NN_Dk
from DIV_NN_N import DIV_NN_N


def get_int(exactnum=-1, minlen=1, maxlen=10000):
    if exactnum == -1:
        if random.randint(0, 100) < 15:
            num = str(random.randint(0, 2))
        else:
            leng = random.randint(minlen, maxlen)
            num = str(random.randint(10 ** (minlen - 1), 10 ** (leng - 1) * 9))
    else:
        num = str(exactnum)
    count = 0
    int_array = [1, []]
    for i in range(len(num)):
        int_array[1].append(int(num[i]))
        count += 1
    int_array[0] *= count
    print(int_array[0])
    print(*int_array[1])
    return int_array