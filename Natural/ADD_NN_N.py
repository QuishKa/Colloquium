import COM_NN_D


def ADD_NN_N(arr1, arr2):
    big_num = COM_NN_D.COM_NN_D(arr1, arr2)
    arr1[1].reverse()
    arr2[1].reverse()
    shift = 0
    if big_num == 1:
        for i in range(arr1[0]):
            sum = arr1[1][i] + arr2[1][i] + shift
            arr2[1][i] = sum % 10
            shift = sum // 10
        if shift != 0:
            if arr1[0] == arr2[0]:
                arr2[1].insert(arr1[0], shift)
            else:
                arr2[1][arr1[0]] += shift
                if arr2[1][arr1[0]] == 10:
                    arr2[1][arr1[0]] = 0
                    arr2[1].insert(arr1[0]+1, shift)
        arr1[1].reverse()
        arr2[1].reverse()
        return arr2
    else:
        for i in range(arr2[0]):
            sum = arr1[1][i] + arr2[1][i] + shift
            arr1[1][i] = sum % 10
            shift = sum // 10
        if shift != 0:
            if arr1[0] == arr2[0]:
                arr1[1].insert(arr2[0], shift)
            else:
                arr1[1][arr2[0]] += shift
                if arr1[1][arr2[0]] == 10:
                    arr1[1][arr2[0]] = 0
                    arr1[1].insert(arr2[0]+1, shift)
        arr1[1].reverse()
        arr2[1].reverse()
        return arr1

#Ельцов В.