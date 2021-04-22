# Main code and connection with JS GUI goes here
# Example of using functions: Natural.DIV_NN_Dk()
import Natural
import Integer
import Rational
import Polynomial
import time
import eel

@eel.expose
def N_1(N1, N2):
    return Natural.ADD_NN_N(N1, N2)

@eel.expose
def N_2(N1, N2):
    return Natural.SUB_NN_N(N1, N2)

@eel.expose
def N_3(N1, N2):
    return Natural.MUL_NN_N(N1, N2)

@eel.expose
def N_4(N1, N2):
    return Natural.DIV_NN_N(N1, N2)

@eel.expose
def N_5(N1, N2):
    return Natural.MOD_NN_N(N1, N2)

@eel.expose
def N_6(N1, N2):
    return Natural.GCF_NN_N(N1, N2)

@eel.expose
def N_7(N1, N2):
    return Natural.LCM_NN_N(N1, N2)






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

print('Polynom = ', Polynomial.MUL_PP_P([0, [[[0, 1, [0]], [1, [1]]]]], [2, [[[1, 2, [1, 9]], [1, [7]]], [[0, 4, [5, 8, 9, 1]], [3, [2, 2, 9]]], [[1, 5, [9, 8, 7, 6, 2]], [4, [1, 9, 2, 4]]]]]))
print('Polynom = ', Polynomial.MUL_PP_P([2, [[[0, 3, [1, 2, 3]], [4, [5, 6, 8, 9]]], [[1, 4, [3, 5, 7, 9]], [3, [9, 7, 1]]], [[1, 1, [9]], [2, [1, 9]]]]],  [2, [[[1, 2, [1, 2]], [1, [6]]], [[1, 4, [5, 0, 0, 0]], [3, [2, 0, 0]]], [[1, 5, [9, 8, 7, 6, 2]], [4, [1, 9, 2, 4]]]]]))


# web-connection
eel.init("web")

eel.start("main.html", size=(1920, 1080))



