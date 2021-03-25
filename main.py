# Main code and connection with JS GUI goes here
# Example of using functions: Integer.Test.ssum(a, b)
import Natural
import Integer
import Rational
import Polynomial
import random


# Main code and all the tests go here
def get_int_num():
    num = str(random.randint(10 ** 49, 99 ** 50))
    count = 0
    length = 1
    int_array = [length, []]
    for i in range(len(num)):
        if num[i] == '-':
            int_array[0] *= -1
        else:
            int_array[1].append(num[i])
            count += 1
    int_array[0] *= count
    print(int_array[0])
    print(*int_array[1])
    return int_array


for i in range(100):
    get_int_num()
