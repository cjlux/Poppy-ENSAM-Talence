# -*- coding: utf-8 -*-
# 1/ Appel des bibliothèques
from numpy import arange
from matplotlib.pyplot import figure, plot, show, grid
# 2/ Définition des fonctions
# Algorithme de Horner 
def P(a,t):
    val = a[-1]
    for c in a[-2::-1]:
        val = c + t*val # 1 add., 1 mult.
    return val
# 3/ Main
c = [1.7,-2.3,0.6,-1.2]
LX = arange(-1.0,3.1,0.1)
LY = [ P(c,v) for v in LX ]
figure()
plot(LX,LY,"or-")
LY = [ P([1,-2,1],v) for v in LX ]
plot(LX,LY,"sb-")
grid()
show()
