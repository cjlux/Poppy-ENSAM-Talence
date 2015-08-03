# -*- coding: utf-8 -*-
# 1/ Appel des bibliothèques
from numpy import arange
from matplotlib.pyplot import figure, plot, show, grid
# 2/ Définition des fonctions
# Algorithme de Horner 
def Polynome(a):
    def P(t):
        val = a[-1]
        for c in a[-2::-1]:
            val = c + t*val # 1 add., 1 mult.
        return val
    return P
# 3/ Main
Q = Polynome([1.7,-2.3,0.6,-1.2])
print Q
LX = arange(-1.0,3.1,0.1)
LY = map(Q,LX)
figure()
plot(LX,LY,"or-")
LY = map(Polynome([3,-6,3]), LX )
plot(LX,LY,"sb-")
grid()
show()
