# Панько Иван

# Функция принимает два натуральных числа и перемножает их
# Возвращает результат умножения, исходные числа не меняются


from COM_NN_D import COM_NN_D
from new_MUL_ND_N import new_MUL_ND_N
from MUL_Nk_N import MUL_Nk_N
from new_ADD_NN_N import new_ADD_NN_N


def new_MUL_NN_N(arr1, arr2):

    com = COM_NN_D(arr1, arr2)

    if com == 2:
        bigger = [arr1[0], arr1[1].copy()]
        smaller = [arr2[0], arr2[1].copy()]
    else:
        smaller = [arr1[0], arr1[1].copy()]
        bigger = [arr2[0], arr2[1].copy()]

    res = [1, [0]]

    for i in range((smaller[0] - 1), -1, -1):
        on_digit = new_MUL_ND_N(bigger, smaller[1][i])
        on10k = MUL_Nk_N(on_digit, (smaller[0] - 1 - i))
        res = new_ADD_NN_N(res, on10k)

    for i in range(res[0] - 1, 0, -1):
        if res[1][i] > 9:
            res[1][i - 1] += res[1][i] // 10
            res[1][i] %= 10
    else:
        if res[1][0] > 9:
            res[1].insert(0, res[1][0] // 10)
            res[1][1] %= 10
            res[0] += 1

    if res[1][0] == 0:
        return [1, [0]]

    return res
