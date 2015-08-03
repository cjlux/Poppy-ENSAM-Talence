# -*- coding: utf-8 -*-
# bibliothèque PySide
from PySide.QtGui import QFrame
from PySide.QtGui import QPushButton
from PySide.QtGui import QFileDialog
from PySide.QtGui import QImage
from PySide.QtGui import QPixmap
from PySide.QtGui import QLabel
from PySide.QtGui import QFont

from PySide.QtCore import SIGNAL

######################
#  CLASSE ZoneImage  #
######################

class ZoneImage(QFrame):
    u"Fenêtre d'interface avec l'utilisateur"
    def __init__(self, parent, posx = 0, posy = 0, image = None):
    # constructeur
        QFrame.__init__(self, parent)
        self.move(posx, posy)
        self.setFrameShape(QFrame.Box)
        self.__zonImag = QLabel(self)
        self.__comment = QLabel(self)
        self.__image = image
        self.__btnSauve = QPushButton(u"Sauver",self)
        self.__btnSauve.resize(58,18)
        self.__btnSauve.setToolTip(u"Sauver l'image affichée dans un fichier")
        self.__btnSauve.setFont(QFont(u"Times New Roman", 10, QFont.Normal, True))
        self.connect(self.__btnSauve, SIGNAL(u'clicked()'), self.SauverImage)

        if image != None:   # il y a une image à afficher
            AfficherImage(image)
        else :              # il n'y a pas d'image
            larg = 100
            haut = 36
            self.__btnSauve.move(150, 0) # on le planque...
            self.__comment.move(10, 10)
            self.__comment.resize(90, 20)
            self.__comment.setText(u"(pas d'image)")
            self.resize(larg, haut)


    def ImageQ(self):
        return self.__image != None

    def GetImage(self):
        return self.__image

    def AfficherImage(self, image):
        self.__image = image
        larg = self.__image.width() + 20
        if larg < 250: larg = 250
        haut = self.__image.height() + 90
        # Affichage de l'image dans un "label"
        self.__zonImag.setPixmap(QPixmap.fromImage(self.__image))
        self.__zonImag.resize(self.__image.width(),self.__image.height())
        self.__zonImag.move(10,10)
        # Placement du bouton "Save"
        self.__btnSauve.move(larg-60, haut-20)
        # Commentaire sur le format de l'image
        self.__comment.move(20,15 + self.__image.height())
        formats = [ 'Invalid', 'Mono', 'MonoLSB', 'Indexed8', 'RGB32', \
                    'ARGB32', 'ARGB32_Premultiplied', 'RGB16', 'ARGB8565_Premultiplied', \
                    'RGB666', 'ARGB6666_Premultiplied', 'RGB555', 'ARGB8555_Premultiplied', \
                    'RGB888', 'RGB444', 'ARGB4444_Premultiplied' ]
        flux = "Commentaire : \n     largeur = " + str(self.__image.width()) +\
                   " , \n     hauteur = " + str(self.__image.height())+\
                   " , \n     QImage::Format_" + formats[self.__image.format()]
        self.__comment.setText(flux)
        self.__comment.resize(larg-30,60)
        self.resize(larg, haut)

    def EffacerImage(self):
        self.__image = None
        self.__zonImag.clear()
        larg = 100
        haut = 40
        self.__btnSauve.move(150, 0) # on le planque...
        self.__comment.clear()
        self.__comment.move(10, 10)
        self.__comment.resize(90, 20)
        self.__comment.setText("(pas d'image)")
        self.resize(larg, haut) 

    def SauverImage(self):
        if self.__image != None: # il y a une image à sauver
        # choix du nom du fichier de sauvegarde, choisi par l'utilisateur
            fichier = QFileDialog.getSaveFileName(self,\
                      u'Sauvegarder une image pixellisée (*.png *.bmp *.jpg *.jpeg)',\
                      u"Images/untitled.png", 'Images (*.png *.bmp *.jpg *.jpeg)')
        # Exportation de l'objet QImage correspondant
            self.__image.save(fichier)           
