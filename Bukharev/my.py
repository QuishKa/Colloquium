
def MUL_Nk_N(num, k):
    if(num[0]>1):
        num[0]+=k
        for i in range(k):
            num[1].append(0)
    return num
pass