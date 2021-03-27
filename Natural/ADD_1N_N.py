def ADD_1N_N(int_arr):
    k = 1
    while int_arr[1][int_arr[0] - k] == 9:
        int_arr[1][int_arr[0] - k] = 0
        k += 1
    if k == int_arr[0] + 1:
        int_arr[1].insert(0, 0)
        int_arr[0] += 1
    int_arr[1][int_arr[0] - k] += 1

    return int_arr

#Ельцов В.