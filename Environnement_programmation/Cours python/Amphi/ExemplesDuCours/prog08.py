# -*- coding: utf-8 -*-
# Algorithme de Horner 
def P(a,t):
    val = a[-1]
    for c in a[-2::-1]:
        val = c + t*val # 1 add., 1 mult.
    return val
c = [1.7,-2.3,0.6,-1.2,2.3,-1.3]
x = 1.0
print u"Le polynôme de coefficients", c, u"vaut", P(c,x), u"en", x
