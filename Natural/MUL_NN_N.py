# Панько Иван

# Функция принимает два натуральных числа и перемножает их
# Возвращает результат умножения, исходные числа не меняются


from COM_NN_D import COM_NN_D
from MUL_ND_N import MUL_ND_N
from MUL_Nk_N import MUL_Nk_N
from ADD_NN_N import ADD_NN_N


def MUL_NN_N(arr1, arr2):

    com = COM_NN_D(arr1, arr2)

    if com == 2:
        bigger = [arr1[0], list(arr1[1])]
        smaller = [arr2[0], list(arr2[1])]
    else:
        smaller = [arr1[0], list(arr1[1])]
        bigger = [arr2[0], list(arr2[1])]

    res = [1, [0]]

    for i in range((smaller[0] - 1), -1, -1):
        on_digit = MUL_ND_N(bigger, smaller[1][i])
        on10k = MUL_Nk_N(on_digit, (smaller[0] - 1 - i))
        res = ADD_NN_N(res, on10k)

    if res[1][0] == 0:
        return [1, [0]]

    return res
