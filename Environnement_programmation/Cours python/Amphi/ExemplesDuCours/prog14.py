# -*- coding: utf-8 -*-
# 1/ Appel des bibliothèques et des modules
from prog13plus import Polynome
from cmath import sqrt
# 2/ Définition des classes et des fonctions
class Trinome(Polynome):
    def __init__(self,a,b,c):
        Polynome.__init__(self, [c,b,a]) # Appel du constructeur de la classe de base
        return
    def racines(self):
        cba = self.coefficients()
        delta = cba[1]**2-4.0*cba[2]*cba[0]
        r1 = (-cba[1]-sqrt(delta))/(2*cba[2])
        r2 = (-cba[1]+sqrt(delta))/(2*cba[2])
        return r1,r2
# 3/ Main
if __name__ == "__main__" :
    P = Polynome([2.0,-3.0,1.0])
    P.prt()
    print "P :", P
    T = Trinome(1.0,-3.0,2.0)
    T.prt()
    print "T :", T
    print T.racines()
    S = Trinome(1.0,1.0,2.0)
    print S.racines()
