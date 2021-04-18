from COM_NN_D import COM_NN_D


def ADD_NN_N(arr1, arr2):
    big_num = COM_NN_D(arr1, arr2)
    arr1[1].reverse()
    arr2[1].reverse()
    shift = 0
    s = 0
    if big_num == 2:
        tmp = arr1[:]
        arr1 = arr2[:]
        arr2 = tmp[:]
    for i in range(arr1[0]):
        sum = arr1[1][i] + arr2[1][i] + shift
        arr2[1][i] = sum % 10
        shift = sum // 10
        s += 1
    if shift != 0:
        if arr1[0] == arr2[0]:
            arr2[1].insert(arr1[0], shift)
            arr2[0] += 1
        else:
            k = 0
            while arr2[1][arr1[0]+k] == 9:
                arr2[1][arr1[0]+k] = 0
                if (k + s + 1) >= arr2[0]:
                    arr2[1].insert(arr1[0]+1+k, 0)
                    arr2[0] += 1
                k += 1
            arr2[1][arr1[0]+k] += 1
    arr1[1].reverse()
    arr2[1].reverse()
    return arr2
#Ельцов В.