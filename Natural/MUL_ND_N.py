# Первый параметр - массив
# Второй параметр - цифра, на которую умножаем

# Функция возвращает новый массив

def MUL_ND_N(arr, digit):
    div = 0
    tmp = [arr[0], arr[1].copy()]
    size = tmp[0]
    for i in range((size - 1), -1, -1):
        mod = (tmp[1][i] * digit + div) % 10
        div = (tmp[1][i] * digit + div) // 10
        tmp[1][i] = mod
    if div != 0:
        tmp[1].insert(0, div)
        tmp[0] = tmp[0] + 1

    return tmp
