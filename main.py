# Main code and connection with JS GUI goes here
# Example of using functions: Integer.Test.ssum(a, b)
import Natural
import Integer
import Rational
import Polynomial

# Main code and all the tests go here
num = input()
count = 0
int_array = []
dec_array = []
while num != 'exit':
    int_array.append(1)
    pos = len(num)
    for i in range(len(num)):
        if num[i] == '.':
            pos = i
            break
        if num[i] == '-':
            int_array[0] *= -1
        else:
            int_array.append(num[i])
            count += 1
    int_array[0] *= count
    count = 0
    dec_array.append(0)
    for i in range(pos + 1, len(num)):
        dec_array.append(num[i])
        count += 1
    dec_array[0] = count
    print(*int_array)
    print(*dec_array)
    num = input()
    int_array.clear()
    dec_array.clear()
    count = 0

