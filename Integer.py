# To add your file use import, for example: from ADD_1N_N import ADD_1N_N
# It will add all the functions from that file and they can be used both here and in main
import sys

sys.path.append('Integer\\')
import random


def get_int(exactnum=-1, maxlen=-1, minlen=1):
    if exactnum == -1:
        if random.randint(0, 100) < 20:
            num = str(random.randint(0, 2))
        else:
            if maxlen == -1:
                maxlen = random.randint(1, 10000)
            num = str(random.randint(10 ** (minlen - 1), 10 ** (maxlen - 1) * 9))
    else:
        num = str(exactnum)
    count = 0
    length = 1
    int_array = [length, []]
    for i in range(len(num)):
        if num[i] == '-':
            int_array[0] *= -1
        else:
            int_array[1].append(int(num[i]))
            count += 1
    int_array[0] *= count
    print(int_array[0])
    print(*int_array[1])
    return int_array
