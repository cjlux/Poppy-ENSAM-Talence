# -*- coding: utf-8 -*-

from PyQt4.QtGui import QImage
from PyQt4.QtGui import qRed, qGreen, qBlue, qAlpha, qRgb

from numpy import ndarray    

class SteganoGraphicProcess:
    u"To hide a text in an image"

    def __init__(self):
        self.__nbR = 0    # number of raws
        self.__nbC = 0    # number of columns
        self.__R   = None # ndarray of red pixels
        self.__G   = None # ndarray of green pixels
        self.__B   = None # ndarray of blue pixels
        self.__Pix = None # working ndarray

    def __Clear(self):
        self.__Pix = self.__R = self.__G = self.__B = None
        self.__nbR = self.__nbC = 0 
         
    def LoadQImage(self, image):
        self.__Clear()
        imageloc = image.convertToFormat(QImage.Format_RGB32)
        self.__nbR, self.__nbC = imageloc.height(), imageloc.width()
        self.__R = ndarray((self.__nbR,self.__nbC), dtype=int)
        self.__G = ndarray((self.__nbR,self.__nbC), dtype=int)
        self.__B = ndarray((self.__nbR,self.__nbC), dtype=int)
        for r in range(self.__nbR):
            for c in range(self.__nbC):
                pixel = imageloc.pixel(c,r)
                self.__R[r, c] = qRed(pixel)
                self.__G[r, c] = qGreen(pixel)
                self.__B[r, c] = qBlue(pixel)
        # Pix is a one dimensionnal array build with all the elements of
        # self.__R (raw by raw), using the flatten() method of the class ndarray:
        self.__Pix = self.__R.flatten()

    def GetPix(self): return self.__Pix
    
    def __ConvertToQImage(self):
        # re-shape the array Pix:
        if self.__Pix != None:
            self.__Pix.shape = (self.__nbR, self.__nbC)
            self.__R = self.__Pix        
        # re-build the image from color arrays:        
        imageloc = QImage(self.__nbC, self.__nbR, QImage.Format_RGB32)
        for r in range(self.__nbR):
            for c in range(self.__nbC):
                imageloc.setPixel(c, r, qRgb(self.__R[r,c],
                                             self.__G[r,c],
                                             self.__B[r,c]))
        return imageloc
    
    def bin8bits(self, n):
        """Converts an integer into a tring of 8 binary digits"""
        q, res = -1, ''
        for i in range(8):
            q = n // 2     # integer division
            res = str(n % 2) + res
            n = q
        return res

################################################################################
#  TRAVAIL A FAIRE :
################################################################################
       
    def __FindByteIn8Pixels(self, pixels, atRank):
        print " >>> Method to be implemented"


    def __FindCharIn8Pixels(self, pixels, atRank):
        print " >>> Method to be implemented"


    def FindTextInImage(self, image):
        print " >>> Method to be implemented"


    def PreProcessImage(self):
        print " >>> Method to be implemented"


    def __HideByteIn8Pixels(self,byteToHide, pixels, atRank):
        print " >>> Method to be implemented"


    def __HideCharIn8Pixels(self, charToHide, pixels, atRank):
        print " >>> Method to be implemented"


    def HideTextInImage(self, textToHide, image):
        print " >>> Method to be implemented"


if __name__ == '__main__':
    from PyQt4.QtGui  import QImage

    stg = SteganoGraphicProcess()
    print u'La représentation sur 8 bits de 254 est :',stg.bin8bits(254)

    # tests avec une petite image 8x8 sans text caché:
    print u"\nChargement d'une image test 8x8 (64 entiers dans le tableau Pix)"
    image  = QImage('test1_8x8.png')
    stg.LoadQImage(image)
    print u'Tableau Pix avant PreProcessImage(): \n',stg.GetPix()
    stg.PreProcessImage()
    print u'Tableau Pix après PreProcessImage(): \n',stg.GetPix()

    # tests avec une petite image 8x8 AVEC text caché ("Yes"):
    print u"\nChargement d'une image test 8x8 avec texte dissimulé"
    image  = QImage('test2_8x8.png')
    stg.LoadQImage(image)
    print u'FindTextInImage('+u'test2_8x8.png'+u') a trouvé :'
    print stg.FindTextInImage(image)
