def MUL_Nk_N(num, k):
    '''
    Multiplies the given number num by 10^k.

    If the number equals to zero, returns the number without changing it.
    Parameters
    ----------
    num - number to multiply.

    k - the power of 10 to multiply on.
    '''
    new_num = [num[0], num[1][:]]
    if new_num[0] > 1 or (new_num[0] == 1 and new_num[1][0] > 0):
        new_num[0] += k
        for i in range(k):
            new_num[1].append(0)
    return new_num
