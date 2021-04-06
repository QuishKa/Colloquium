# Первый параметр - массив
# Второй параметр - цифра, на которую умножаем

# Функция возвращает новый массив

def new_MUL_ND_N(arr, digit):
    tmp = [arr[0], arr[1].copy()]
    size = tmp[0]
    for i in range(size):
        tmp[1][i] *= digit

    return tmp
