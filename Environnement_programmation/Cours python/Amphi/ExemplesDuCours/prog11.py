# -*- coding: utf-8 -*-
# 1/ Appel des bibliothèques

# 2/ Définition des fonctions
# Algorithme de Horner 
class Polynome:
    def __init__(self, a): # Constructeur
        self.__c = a # attribut (accès privé)
        return
    def coefficients(self): # méthode d'accès en lecture
        return self.__c
    def valeur(self, t):
        val = self.__c[-1]
        for e in self.__c[-2::-1]:
            val = e + t*val # 1 add., 1 mult.
        return val
    
# 3/ Main
Q = Polynome([1.7,-2.3,0.6,-1.2]) # Construction d'un objet
print Q.coefficients()
print Q.valeur(1.0)
