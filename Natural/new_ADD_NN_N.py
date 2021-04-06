def new_ADD_NN_N(num1, num2):
    num1 = [num1[0], num1[1].copy()]
    num2 = [num2[0], num2[1].copy()]
    if num1[0] < num2[0]:
        tmp = num1
        num1 = num2
        num2 = tmp
    j = num1[0] - 1
    for i in range(num2[0] - 1, -1, -1):
        num1[1][j] += num2[1][i]
        j -= 1
    return num1
