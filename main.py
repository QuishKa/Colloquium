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

@eel.expose
def I_1(I1, I2):
    return Integer.ADD_ZZ_Z(I1, I2)

@eel.expose
def I_2(I1, I2):
    return Integer.SUB_ZZ_Z(I1, I2)

@eel.expose
def I_3(I1, I2):
    return Integer.MUL_ZZ_Z(I1, I2)

@eel.expose
def I_4(I1, I2):
    return Integer.DIV_ZZ_Z(I1, I2)

@eel.expose
def I_5(I1, I2):
    return Integer.MOD_ZZ_Z(I1, I2)

@eel.expose
def Q_1(Q1):
    return Rational.RED_Q_Q(Q1)

@eel.expose
def Q_2(Q1, Q2):
    return Rational.ADD_QQ_Q(Q1, Q2)

@eel.expose
def Q_3(Q1, Q2):
    return Rational.SUB_QQ_Q(Q1, Q2)

@eel.expose
def Q_4(Q1, Q2):
    return Rational.MUL_QQ_Q(Q1, Q2)

@eel.expose
def Q_5(Q1, Q2):
    return Rational.DIV_QQ_Q(Q1, Q2)

@eel.expose
def P_1(P1, P2):
    return Polynomial.ADD_PP_P(P1, P2)

@eel.expose
def P_2(P1, P2):
    return Polynomial.SUB_PP_P(P1, P2)

@eel.expose
def P_3(P1, P2):
    return Polynomial.MUL_PP_P(P1, P2)

@eel.expose
def P_4(P1, P2):
    return Polynomial.DIV_PP_P(P1, P2)

@eel.expose
def P_5(P1, P2):
    return Polynomial.MOD_PP_P(P1, P2)

@eel.expose
def P_6(P1, P2):
    return Polynomial.GCF_PP_P(P1, P2)

@eel.expose
def P_7(P1):
    return Polynomial.DER_P_P(P1)

@eel.expose
def P_8(P1):
    return Polynomial.NMR_P_P(P1)







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



# print(Natural.DIV_NN_N(Integer.get_int(-1, 1, 20), Integer.get_int(-1, 1, 20)))
# print(Natural.DIV_NN_Dk(Integer.get_int(5555), Integer.get_int()))
# print(Integer.DIV_ZZ_Z(Integer.get_int(), Integer.get_int()))
# print(Integer.MOD_ZZ_Z(Integer.get_int(), Integer.get_int()))

# num1 = Integer.get_int(0, 125)
# num2 = Integer.get_int(0, -25)
# num1 = Natural.get_int(88)
# num2 = Natural.get_int(88)
# start = time.time()
# print(Integer.DIV_ZZ_Z(num1, num2))
# end1 = time.time()
# print(end1 - start)

# print('Polynom = ', Polynomial.MUL_PP_P([0, [[[0, 1, [0]], [1, [1]]]]], [2, [[[1, 2, [1, 9]], [1, [7]]], [[0, 4, [5, 8, 9, 1]], [3, [2, 2, 9]]], [[1, 5, [9, 8, 7, 6, 2]], [4, [1, 9, 2, 4]]]]]))
# print('Polynom = ', Polynomial.MUL_PP_P([2, [[[0, 3, [1, 2, 3]], [4, [5, 6, 8, 9]]], [[1, 4, [3, 5, 7, 9]], [3, [9, 7, 1]]], [[1, 1, [9]], [2, [1, 9]]]]],  [2, [[[1, 2, [1, 2]], [1, [6]]], [[1, 4, [5, 0, 0, 0]], [3, [2, 0, 0]]], [[1, 5, [9, 8, 7, 6, 2]], [4, [1, 9, 2, 4]]]]]))

z1 = [1, 3, [1, 6, 4]]
n1 = [4, [1, 0, 0, 8]]
# print(Rational.RED_Q_Q([z1, n1]))


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
print('Time: ', time.time() - k)

# (X) - (X)
p1 = [1, [[[0, 1, [0]], [1, [1]]], [[0, 1, [1]], [1, [1]]]]]
p2 = [1, [[[0, 1, [0]], [1, [1]]], [[0, 1, [1]], [1, [1]]]]]
# print(Polynomial.SUB_PP_P(p1, p2))

print('Fac 1 = ', Polynomial.FAC_P_Q(
    [2, [[[0, 3, [1, 2, 3]], [4, [5, 6, 8, 9]]], [[1, 4, [3, 5, 7, 9]], [3, [9, 7, 1]]], [[1, 1, [9]], [2, [1, 9]]]]]))
print('Fac 2 = ', Polynomial.FAC_P_Q(
    [2, [[[0, 3, [2, 4, 6]], [4, [2, 2, 2, 2]]], [[1, 4, [4, 2, 8, 4]], [3, [2, 6, 4]]], [[1, 1, [8]], [2, [6, 2]]]]]))

k = time.time()
print('NOD: ', Polynomial.GCF_PP_P(
    [4, [[[0, 1, [0]], [1, [1]]], [[1, 1, [1]], [1, [1]]], [[0, 1, [4]], [1, [1]]], [[1, 1, [5]], [1, [1]]],
         [[0, 1, [6]], [1, [1]]]]],
    [2, [[[0, 1, [1]], [1, [1]]], [[1, 1, [1]], [1, [1]]], [[0, 1, [2]], [1, [1]]]]]))
print('NOD: ', Polynomial.GCF_PP_P([4, [[[1, 1, [6]], [1, [1]]], [[0, 1, [2]], [1, [1]]], [[1, 1, [1]], [1, [1]]],
                                        [[1, 1, [4]], [1, [1]]], [[0, 1, [3]], [1, [1]]]]], [3,
                                                                                             [[[1, 1, [0]], [1, [1]]],
                                                                                              [[1, 1, [1]], [1, [1]]],
                                                                                              [[1, 1, [8]], [1, [1]]],
                                                                                              [[1, 1, [4]], [1, [1]]]]]))
print('Time: ', time.time() - k)
k = time.time()
#print('NMR: ', Polynomial.NMR_P_P([4, [[[1, 1, [6]], [1, [1]]], [[0, 1, [2]], [1, [1]]], [[1, 1, [1]], [1, [1]]], [[1, 1, [4]], [1, [1]]], [[0, 1, [3]], [1, [1]]]]]))
#print('NMR: ', Polynomial.NMR_P_P([2, [[[1, 1, [4]], [1, [1]]], [[1, 1, [0]], [1, [1]]], [[0, 2, [1, 6]], [1, [1]]]]]))
print('NMR: ', Polynomial.NMR_P_P([4, [[[0, 1, [1]], [1, [1]]], [[1, 1, [0]], [1, [1]]], [[0, 1, [2]], [1, [1]]], [[1, 1, [0]], [1, [1]]], [[0, 1, [1]], [1, [1]]]]]))
print('Time: ', time.time() - k)
