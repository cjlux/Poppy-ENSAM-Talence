# -*- coding: utf-8 -*-
# 1/ Appel des bibliothèques et des modules

# 2/ Définition des classes et des fonctions
# Algorithme de Horner 
class Polynome:
    def __init__(self, a): # Constructeur
        self.__c = a # attribut (accès privé)
        while self.__c[-1] == 0.0 and len(self.__c) > 1:
            del self.__c[-1]
        return
    def coefficients(self): # méthode d'accès en lecture
        return self.__c
    def valeur(self, t): # calcul par l'algo. de Horner
        val = self.__c[-1]
        for e in self.__c[-2::-1]:
            val = e + t*val 
        return val
    def __call__(self, t):
        return self.valeur(t)
    def degre(self):
        return len(self.__c)-1
    def prt(self,t=None):
        if t==None :
            print u"Polynôme de coefficients",self.coefficients(),\
                  u" de degré", self.degre()
        else :
            print u"Le polynôme de coefficients",self.coefficients(),\
                  u'vaut', self.valeur(t),u"en",t
        return
    def derive(self):
        if self.degre() == 0 :
            return Polynome([0])
        else :
            a = [ i*self.__c[i] for i in range(1,len(self.__c)) ]
            return Polynome(a)
    
# 3/ Main
if __name__ == "__main__" :
    Q = Polynome([1.7,-2.3,0.6,-1.2]) # Construction d'un objet
    Q.prt(1.0)
    print u"Q(1.0) :",Q(1.0)
    R = Q.derive()
    print R
    R.prt(-2.0)
