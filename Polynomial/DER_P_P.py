from Rational import MUL_QQ_Q



def DER_P_P(polynom):
    p = polynom.copy()
    for i in range(p[0] - 1):
        zi = list(map(int, str(i)))
        zi = [[0, len(zi), zi], [1, [1]]]
        p[1][i] = MUL_QQ_Q(p[1][i + 1], zi)
    p[1].pop()
    return p

