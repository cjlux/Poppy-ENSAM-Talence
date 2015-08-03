# -*- coding: utf-8 -*-
def P(a,t):
    val = a[0]
    n = len(a)-1
    for i in range(1,n+1):
        val += a[i]*t**i # 1 add., 1 mult., 1 puis.
    return val
c = [1.7,-2.3,0.6,-1.2,2.3,-1.3]
x = 1.0
print u"Le polynôme de coefficients", c, u"vaut", P(c,x), u"en", x
