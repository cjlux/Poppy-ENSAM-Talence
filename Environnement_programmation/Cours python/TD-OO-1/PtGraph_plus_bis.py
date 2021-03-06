# -*- coding: utf-8 -*-

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#  Chargement des modules nécessaires (bibliothèques)         #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
from math import atan2, sin, cos, degrees, radians, sqrt
from matplotlib.pyplot import figure, plot, text, show

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#  Chargement de la définition de la classe  de base PtGeom   #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
from PtGeom import PtGeom
 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#    Définition de la classe 'PtGraph' qui dérive de 'PtGeom' #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
class PtGraph(PtGeom) :
    u'Classe de points avec directives graphiques'
    
    __lptg = []
    
    def __init__(self, label, xy=[0,0], marker='o'):
    
        PtGeom.__init__(self, xy)            # Construction de la classe de base !
        self.__label = label                        # att. privé label (fourni en argument) 
        self.__mrk = marker                        # att. privé mrk : type de point, fourni en argument
        self.__size = 7.0                        # att. privé size: taille du point, 7.0 par défaut
        self.__color = 'black'
        self.__fillColor = 'grey'
        
        PtGraph.__lptg.append(self)
    
    @staticmethod
    def nb():
        return len(PtGraph.__lptg)
    @staticmethod
    def plotAll(showLabel=False):
        for pt in PtGraph.__lptg:
            pt.plot(showLabel)
        show()
    @staticmethod
    def select(labels):
        pts=[]
        if isinstance(labels,list):
            for label in labels:
                for pt in PtGraph.__lptg:
                    if pt.getLabel()==label:
                        pts.append(pt)
        else:
            for pt in PtGraph.__lptg:
                    if pt.getLabel()==labels:
                        pts.append(pt)
                        
        print u"nombre d'éléments trouvés : ",len(pts)
        return pts
            
    
# Remarque : pour les types de points, voir
# http://matplotlib.org/api/markers_api.html#module-matplotlib.markers
            
    # accès en lecture
    def getColor(self): return self.__color
    def getFillColor(self): return self.__fillColor
    def getColors(self): return self.__color, self.__fillColor
    def getSize(self): return self.__size
    def getLabel(self): return self.__label
    def getMarker(self): return self.__mrk
    
    # accès en écriture
    def setColor(self,clr): self.__color = clr
    def setFillColor(self,fclr): self.__fillColor = fclr
    def setSize(self,sz): self.__size = sz
    def setMarker(self,mk): self.__mrk = mk
    def setColors(self, clr, fclr = None):
        if fclr == None : 
            self.setColor(clr)
            self.setFillColor(clr)
        else: 
            self.setColor(clr)
            self.setFillColor(fclr)
               
    # Trace du point
    def plot(self, showLabel=False, noFig=1):
        figure(noFig)
        plot(self.getX(),self.getY(),
             marker = self.__mrk,
             markeredgecolor = self.__color,
             markerfacecolor = self.__fillColor,
             markersize = self.__size,
             markeredgewidth = 1.2)
        if showLabel :
            text(self.getX(),self.getY(),'  '+self.getLabel(),\
                 color = self.getColor())
            
##################### TEST DE LA CLASSE #########################
if __name__ == "__main__":
    pt1 = PtGraph('A')             # constructeur appelé avec un seul argument
    print u"Coordonnées :", pt1.getXY(), u", label :", pt1.getLabel(),\
          u", marque :", pt1.getMarker(), u", couleurs :", pt1.getColors()
    
    pt2 = PtGraph('B' ,[1.,-2.5])  # constructeur appelé avec deux arguments
    print u"Coordonnées :", pt2.getXY(), u", label :", pt2.getLabel(),\
          u", marque :", pt2.getMarker(), u", couleurs :", pt2.getColors()
    
    pt3 = PtGraph('C', [-1,1], '*')# constructeur appelé avec trois arguments
    print u"Coordonnées :", pt3.getXY(), u", label :", pt3.getLabel(),\
          u", marque :", pt3.getMarker(), u", couleurs :", pt3.getColors()
    
    print PtGraph.select('A')
    print PtGraph.select(['A','B'])
    
    pt4 = PtGraph(pt3)
    print u"Coordonnées :", pt4.getXY(), u", label :", pt4.getLabel(),\
          u", marque :", pt4.getMarker(), u", couleurs :", pt4.getColors()
          