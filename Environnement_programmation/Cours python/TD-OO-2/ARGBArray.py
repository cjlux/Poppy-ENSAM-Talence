# -*- coding: utf-8 -*-
# bibliothèque PySide
from PySide.QtGui import QImage

# conversions des codes couleur
from PySide.QtGui import qRed
from PySide.QtGui import qGreen
from PySide.QtGui import qBlue
from PySide.QtGui import qAlpha
from PySide.QtGui import qRgba

# pour travailler sur les tableaux
from numpy import ndarray    

######################
#  CLASSE ARGBArray  #
######################
class ARGBArray:
    u"Tableaux de niveaux de couleurs, entre 0 et 1"
    # constructeur
    def __init__(self, *args):
        # on fait des tests sur le nombre d'arguments (pas de surcharge en Python...)
        if len(args)==1 and type(args[0])==QImage:
            # construction à partir d'un objet QImage :
            self.__initImage(args[0])     
        elif len(args)>=2 and type(args[0])==int and type(args[1])==int :
            # construction d'une image unie
            self.__InitImageUnie(self,args)
        else:
            # objet vide
            self.__nbL = 1
            self.__nbC = 1
            self.__initNdarrays()

    def __initImage(self, image):
        imageloc = image.convertToFormat(QImage.Format_ARGB32)
        self.__nbL = imageloc.height()
        self.__nbC = imageloc.width()
        self.__initNdarrays()
        coef = 1./255.
        for l in range(self.__nbL):
            for c in range(self.__nbC):
                pixel = imageloc.pixel(c,l)
                self.__rouges[l, c]   = coef*qRed(pixel)
                self.__verts[l, c]    = coef*qGreen(pixel)
                self.__bleus[l, c]    = coef*qBlue(pixel)
                self.__opacites[l, c] = coef*qAlpha(pixel)

    def __initImageUnie(self,args):   
        print u"construction d'un objet ARGBArray en image unie"
        self.__nbC = args[0]
        self.__nbL = args[1]
        r = g = b = 0;
        o = 255                     # opaque
        if len(args)>=3:            # niveau de rouge 0-255
            r = args[2]
            if len(args)>=4:        # niveau de vert 0-255
                g = args[3]
                if len(args)>=5:    # niveau de bleu 0-255
                    b = args[4]
                    if len(args)>=6:
                        o = args[6] # opacité 0-255 
        self.__initNdarrays()
        coef = 1./255.
        fr, fg, fb, fo  = coef*r,coef*g,coef*b,coef*o
        self.__rouges.fill(fr)
        self.__verts.fill(fg)
        self.__bleus.fill(fb)
        self.__opacites.fill(fo)

    def __initNdarrays(self):
        self.__rouges   = ndarray(shape=(self.__nbL,self.__nbC), dtype=float)
        self.__verts    = ndarray(shape=(self.__nbL,self.__nbC), dtype=float)
        self.__bleus    = ndarray(shape=(self.__nbL,self.__nbC), dtype=float)
        self.__opacites = ndarray(shape=(self.__nbL,self.__nbC), dtype=float)
        
    def ConvertToQImage(self):
        imageloc = QImage(self.__nbC, self.__nbL, QImage.Format_ARGB32)
        for l in range(self.__nbL):
            for c in range(self.__nbC):
                imageloc.setPixel(c, l, qRgba( \
                    int( 255.0*self.__rouges[l,c] + 0.5 ), \
                    int( 255.0*self.__verts[l,c] + 0.5 ), \
                    int( 255.0*self.__bleus[l,c] + 0.5 ), \
                    int( 255.0*self.__opacites[l,c] + 0.5 ) \
                    ))
        return imageloc    

################################################################################
#  TRAVAIL A FAIRE :
################################################################################

####################  TRAITEMENTS ########################            

    def HReverse(self):
        u'renversement gauche/droite'
        print u"Méthode ARGBArray.HReverse() à compléter"

    def VReverse(self):
        u'renversement haut/bas'
        print u"Méthode ARGBArray.VReverse() à compléter"    

    def Transpose(self):
        u'permutation des axes x et y'
        print u"Méthode ARGBArray.Transpose() à compléter"
        
    def TournerD(self):
        u'rotation de 90° dans le sens horaire'
        print u"Méthode ARGBArray.TournerD() à compléter"

    def TournerG(self):
        u'rotation de 90° dans le sens trigonométrique'
        print u"Méthode ARGBArray.TournerG() à compléter"

    def AjouterCadre(self, argb = [1, 1, 1, 1], nbx = 3, nby = None):
        u'ajoute un cadre de couleur'
        print u"Méthode ARGBArray.AjouterCadre() à compléter"
            

    def Negatif(self):
        def neg(tab,nbl,nbc):
            for ilig in range(nbl):
                for icol in range(nbc):
                    tab[ilig, icol] = 1. - tab[ilig, icol]
                    # remarque : map difficile à utiliser avec un tableau ndarray
        neg(self.__rouges, self.__nbL, self.__nbC)
        neg(self.__verts, self.__nbL, self.__nbC)
        neg(self.__bleus, self.__nbL, self.__nbC)        

    def VoirOpacite(self):  
        self.__rouges = self.__opacites
        self.__verts = self.__opacites
        self.__bleus = self.__opacites         

    def ChangerBalance(self, CoefRGB = [1.,1.,1.]):
        cR = CoefRGB[0]
        cG = CoefRGB[1]
        cB = CoefRGB[2]
        for nolig in range(self.__nbL):
            for nocol in range(self.__nbC):
                niveau = cR*self.__rouges[nolig, nocol]
                if niveau < 0.: niveau = 0.
                if niveau > 1.: niveau = 1.
                self.__rouges[nolig, nocol] = niveau
                niveau = cG*self.__verts[nolig, nocol]
                if niveau < 0.: niveau = 0.
                if niveau > 1.: niveau = 1.
                self.__verts[nolig, nocol] = niveau
                niveau = cB*self.__bleus[nolig, nocol]
                if niveau < 0.: niveau = 0.
                if niveau > 1.: niveau = 1.
                self.__bleus[nolig, nocol] = niveau                

    def NoirEtBlanc(self, pdsR = 0.3, pdsG = 0.4, pdsB = None):
        if pdsB == None: pdsB = 1. - (pdsR+pdsG)
        for nolig in range(self.__nbL):
            for nocol in range(self.__nbC):
                niveau = pdsR*self.__rouges[nolig, nocol]\
                         +pdsG*self.__verts[nolig, nocol]\
                         +pdsB*self.__bleus[nolig, nocol]
                if niveau < 0.: niveau = 0.
                if niveau > 1.: niveau = 1.
                self.__rouges[nolig, nocol] = niveau
                self.__verts[nolig, nocol] = niveau
                self.__bleus[nolig, nocol] = niveau

    def Transparent(self, seuil): # le blanc devient transparent...
        for nolig in range(self.__nbL):
            for nocol in range(self.__nbC):
                if self.__bleus[nolig, nocol] > seuil and \
                   self.__verts[nolig, nocol] > seuil and \
                   self.__rouges[nolig, nocol] > seuil :
                    self.__opacites[nolig, nocol] = 0.    
