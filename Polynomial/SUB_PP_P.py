from Rational import SUB_QQ_Q


def SUB_PP_P(arr1, arr2):
    arr1 = copy_polynom(arr1)
    arr2 = copy_polynom(arr2)
    if arr1[0] > arr2[0]:
        for i in range(arr2[0] + 1):
            arr1[1][i] = SUB_QQ_Q(arr1[1][i], arr2[1][i])
        i = arr2[0]
        while arr1[1][i][0][2] == [0] and i > 0:
            arr1[1].pop()
            arr1[0] = arr1[0] - 1
            i = i - 1
        return arr1
    else:
        for i in range(arr1[0]+1):
            arr2[1][i] = SUB_QQ_Q(arr1[1][i], arr2[1][i])
        i = arr1[0]
        while arr2[1][i][0][2] == [0] and i > 0:
            arr2[1].pop()
            arr2[0] = arr2[0] - 1
            i = i - 1
        return arr2


def copy_polynom(p):
    new_p = [p[0], []]
    for i in range(p[0]+1):
        q = p[1][i]
        new_q = [[0,0,[]], [0,[]]]
        new_q[0][0] = q[0][0]
        new_q[0][1] = q[0][1]
        new_q[0][2] = q[0][2][:]
        new_q[1][0] = q[1][0]
        new_q[1][1] = q[1][1][:]
        new_p[1].append(new_q)
    return new_p
#Ельцов В.