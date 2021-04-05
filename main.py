# Main code and connection with JS GUI goes here
# Example of using functions: Natural.DIV_NN_Dk()
import Natural
import Integer
import Rational
import Polynomial
import time


# Main code and all the tests go here
##print(Natural.DIV_NN_N(Integer.get_int(-1, 1, 20), Integer.get_int(-1, 1, 20)))
#print(Natural.DIV_NN_Dk(Integer.get_int(5555), Integer.get_int()))
#print(Integer.DIV_ZZ_Z(Integer.get_int(), Integer.get_int()))
#print(Integer.MOD_ZZ_Z(Integer.get_int(), Integer.get_int()))
num1 = Natural.get_int(10007)
num2 = Natural.get_int(-1, 1, 3)
start = time.time()
print(Natural.DIV_NN_N(num1, num2))
end1 = time.time()
print(end1 - start)
print(Natural.MOD_NN_N(num1, num2))
end2 = time.time()
print(end2 - end1)
