# Панько Иван

# Функция находит большее число и вычитает из него меньшее
# Если они равны, сразу возвращает [1, [0]]
# Если неравны, то функция возвращает результат вычитания из большего числа меньшего


from COM_NN_D import COM_NN_D


def SUB_NN_N(arr1, arr2):

    res = COM_NN_D(arr1, arr2)

    if res == 0:
        return [1, [0]]
    elif res == 2:
        bigger = [arr1[0], arr1[1].copy()]
        smaller = [arr2[0], arr2[1].copy()]
    else:
        smaller = [arr1[0], arr1[1].copy()]
        bigger = [arr2[0], arr2[1].copy()]

    diff = bigger[0] - smaller[0]

    for i in range((smaller[0] - 1), -1, -1):
        if bigger[1][i + diff] >= smaller[1][i]:
            bigger[1][i + diff] = bigger[1][i + diff] - smaller[1][i]
        else:
            bigger[1][i + diff] = bigger[1][i + diff] - smaller[1][i] + 10

            j = i - 1
            while bigger[1][j + diff] == 0:
                bigger[1][j + diff] = 9
                j = j - 1

            bigger[1][j + diff] = bigger[1][j + diff] - 1

    i = 0
    while bigger[1][i] == 0:
        i = i + 1

    bigger[1][:] = bigger[1][i:]
    bigger[0] = bigger[0] - i

    return bigger
