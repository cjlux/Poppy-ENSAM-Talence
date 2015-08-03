# -*- coding: utf-8 -*-

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#    Définition de la classe 'PtGeom'           #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#

# imporation bibliothèques
import math as m

class PtGeom :
    u'Classe de points géometriques (sans propriété graphique)'

    # Le Constructeur :
    def __init__(self, xy = [0,0]):
        if isinstance(xy,list):
            self.__x = float(xy[0])
            self.__y = float(xy[1])
        else:
            self.__x = xy.getX()
            self.__y = xy.getY()
        self.__r = float(m.sqrt(self.__x**2 + self.__y**2))
        self.__a = float(m.atan2(self.__y,self.__x))

    # Méthodes d'accès en lecture :
    def getX(self): return self.__x
    def getY(self): return self.__y
    def getXY(self): return [self.getX(),self.getY()]
    def getRho(self): return self.__r
    def getTheta(self): return m.degrees(self.__a)
    def getRhoTheta(self): return [self.getRho(),self.getTheta()]
    
    # Méthodes d'écriture
    def setTheta(self,angle): 
        self.__a = m.radians(float(angle))
        self.__updateXY()
    def setRho(self,rho):
        self.__r = rho
        self.__updateXY()
    def setX(self,x):
        self.__x = x
        self.__updateRhoTheta()
    def setY(self,y):
        self.__y = y
        self.__updateRhoTheta()
    def __updateXY(self):
        self.__x = self.__r*m.cos(self.__a)
        self.__y = self.__r*m.sin(self.__a)
    def __updateRhoTheta(self):
        self.__r = float(m.sqrt(self.__x**2 + self.__y**2))
        self.__a = float(m.atan2(self.__y,self.__x))
    def move(self,dx=0,dy=0):
        self.__x += float(dx)
        self.__y += float(dy)
        self.__updateRhoTheta()
    
    
if __name__ == "__main__":

    # Partie du code Python qui n'est exécuté que si ce fichier
    # est interprété directement (sans passer par un 'import PtGeom.py')
    # Ceci est très utile pour écrire des lignes de test de la classe...
    
    # Test de toutes les façons d'appeler le constructeur :
    pt1 = PtGeom([10,10])           # constructeur appelé sans argument    
    pt2 = PtGeom([1.,-2.5])  # constructeur appelé avec une liste de deux float
    pt3 = PtGeom(['-1','1']) # constructeur appelé avec une liste de deux str

    # Test des méthodes d'accès :
    print u"Point créé par : PtGeom(); ", pt1
    print u"  abscisse : ", PtGeom.getX(pt1), u", ordonnée : ", PtGeom.getY(pt1)
    print u"  abscisse : ", pt1.getX(),       u", ordonnée : ", pt1.getY()
    print u"  r : ", pt1.getRho(),       u", theta : ", pt1.getTheta()

    print u"Point créé par PtGeom([1.,-2.5]); ", pt2
    print u"  abscisse : ", pt2.getX(), u", ordonnée :", pt2.getY()

    print u"Point créé par PtGeom(['-1','1']); ", pt3
    print u"  abscisse : ", pt3.getX(), u", ordonnée :", pt3.getY()
    print "[x,y] = ", pt3.getXY()
    
    pt2.setTheta(90)
    print u"  abscisse : ", pt1.getX(),       u", ordonnée : ", pt1.getY()
    print u"  r : ", pt1.getRho(),       u", theta : ", pt1.getTheta()
    
    pt4 = PtGeom(pt2)
    print u"pt4 :",pt4.getXY()
    
    pt4.move(1.,2.)
    print u"New pt4 :",pt4.getXY()
    
