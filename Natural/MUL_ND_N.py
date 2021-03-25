# Первый параметр - массив
# Второй параметр - цифра, на которую умножаем

# Функция возвращает новый массив

def MUL_ND_N(arr, digit):
    div = 0
    size = arr[0]
    for i in range((size - 1), -1, -1):
        mod = (arr[1][i] * digit + div) % 10
        div = (arr[1][i] * digit + div) // 10
        arr[1][i] = mod

    if div != 0:
        arr[1].insert(0, div)
        arr[0] = arr[0] + 1

    return arr
