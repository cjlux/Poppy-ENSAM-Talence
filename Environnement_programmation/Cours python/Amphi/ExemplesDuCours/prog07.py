# -*- coding: utf-8 -*-
def P(a,t):
    val = 0.0
    tpi = 1.0
    for c in a: # on décrit la liste directement (sans numéro)
        val += c*tpi # 1 add., 1 mult.
        tpi *= t # 1 mult.
    return val
c = [1.7,-2.3,0.6,-1.2,2.3,-1.3]
x = 1.0
print u"Le polynôme de coefficients", c, u"vaut", P(c,x), u"en", x

