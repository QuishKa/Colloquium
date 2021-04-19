# Main code and connection with JS GUI goes here
# Example of using functions: Natural.DIV_NN_Dk()
import Natural
import Integer
import Rational
import Polynomial
import time


# Main code and all the tests go here
#print(Natural.DIV_NN_N(Integer.get_int(-1, 1, 20), Integer.get_int(-1, 1, 20)))
#print(Natural.DIV_NN_Dk(Integer.get_int(5555), Integer.get_int()))
#print(Integer.DIV_ZZ_Z(Integer.get_int(), Integer.get_int()))
#print(Integer.MOD_ZZ_Z(Integer.get_int(), Integer.get_int()))

#num1 = Integer.get_int(0, 125)
#num2 = Integer.get_int(0, -25)
#num1 = Natural.get_int(88)
#num2 = Natural.get_int(88)
#start = time.time()
#print(Integer.DIV_ZZ_Z(num1, num2))
#end1 = time.time()
#print(end1 - start)

#print('Polynom = ', Polynomial.MUL_PP_P([0, [[[0, 1, [0]], [1, [1]]]]], [2, [[[1, 2, [1, 9]], [1, [7]]], [[0, 4, [5, 8, 9, 1]], [3, [2, 2, 9]]], [[1, 5, [9, 8, 7, 6, 2]], [4, [1, 9, 2, 4]]]]]))
#print('Polynom = ', Polynomial.MUL_PP_P([2, [[[0, 3, [1, 2, 3]], [4, [5, 6, 8, 9]]], [[1, 4, [3, 5, 7, 9]], [3, [9, 7, 1]]], [[1, 1, [9]], [2, [1, 9]]]]],  [2, [[[1, 2, [1, 2]], [1, [6]]], [[1, 4, [5, 0, 0, 0]], [3, [2, 0, 0]]], [[1, 5, [9, 8, 7, 6, 2]], [4, [1, 9, 2, 4]]]]]))

z1 = [1, 3, [1,6,4]]
n1 = [4, [1,0,0,8]]
#print(Rational.RED_Q_Q([z1, n1]))


'''q1_3 = [[0, 2, [1, 3]], [1, [1]]]
q1_2 = [[0, 1, [7]], [1, [1]]]
q1_1 = [[1, 3, [1, 6, 0]], [1, [1]]]
q1_0 = [[0, 2, [4, 3]], [1, [1]]]

q2_1 = [[1, 2, [4, 9]], [1, [1]]]
q2_0 = [[1, 1, [2]], [1, [1]]]
p1 = [3, [q1_0, q1_1, q1_2, q1_3]]
p2 = [1, [q2_0, q2_1]]'''
q1 = [[0, 1, [1]], [1, [1]]]
q0 = [[0, 1, [1]], [1, [1]]]
q3 = [[1, 1, [1]], [1, [1]]]
p1 = [1, [q0, q1]]
p2 = [2, [q0, q3, q1]]
print('-----------------------------------')
k = time.time()
print(Polynomial.DIV_PP_P(p1, p2))
print(Polynomial.MOD_PP_P(p1, p2))
print('Time: ', time.time()-k)

# (X) - (X)
p1 = [1, [[[0, 1, [0]], [1, [1]]], [[0, 1, [1]], [1, [1]]]]]
p2 = [1, [[[0, 1, [0]], [1, [1]]], [[0, 1, [1]], [1, [1]]]]]
#print(Polynomial.SUB_PP_P(p1, p2))