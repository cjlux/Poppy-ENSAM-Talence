# -*- coding: utf-8 -*-
# bibliothèque PySide
from PySide.QtGui import QWidget
from PySide.QtGui import QDesktopWidget
from PySide.QtGui import QPushButton
from PySide.QtGui import QMenu
from PySide.QtGui import QFileDialog
from PySide.QtGui import QDialog
from PySide.QtGui import QInputDialog
from PySide.QtGui import QImage
from PySide.QtGui import QFont
from PySide.QtGui import QIcon
from PySide.QtGui import QStyleFactory
from PySide.QtGui import QLineEdit
from PySide.QtGui import QFormLayout
from PySide.QtGui import QVBoxLayout
from PySide.QtGui import QDoubleSpinBox
from PySide.QtGui import QGridLayout
from PySide.QtGui import QLabel

from PySide.QtCore import QSize
from PySide.QtCore import SIGNAL

from ZoneImage import ZoneImage

from ARGBArray import ARGBArray

###############################
#  CLASSE Fenêtre principale  #
###############################

class FenetrePrincipale(QWidget):
    u"Fenêtre d'interface avec l'utilisateur"
    def __init__(self, larg = 500, haut = 200, titre = u"Fenêtre principale"):
    # constructeur
        QWidget.__init__(self, None)
        self.setWindowTitle(titre)
        self.__screen = QDesktopWidget().screenGeometry()
        self.__top = 50
        self.__right = self.__screen.width()-50
        # création d'un objet ARGBArray vide 
        self.__argbTab = ARGBArray()
        # création du bouton 'Ouvrir image' 
        self.__btnOuvrir = self.__creerBoutonOuvrir()
        self.connect(self.__btnOuvrir, SIGNAL('clicked()'), self.OuvrirNouvelleImage)
        # création du bouton de lancement du menu 'Traiter'
        self.__btnTraiter = self.__creerBoutonTraiter()
        self.__menuTraiter = self.__creerMenuTraiter()
        self.__btnTraiter.setMenu(self.__menuTraiter)
        # création des 2 zones d'affichage des images
        self.__cadre1 = ZoneImage(self, 20,80,None)
        self.__cadre2 = ZoneImage(self,290,80,None)
        # redimensionnement de la fenetre principale
        self.__Redimensionner()

    def __creerBoutonOuvrir(self):
        # Bouton d'ouverture de fichier image
        b = QPushButton(u"Charger une image", self)   
        b.resize(220,40)
        b.move(20, 20)
        b.setToolTip(u"Ouvrir un sélecteur de fichier pour charger image")
        b.setFont(QFont("Times New Roman", 12, QFont.Bold, True))
        b.setIcon(QIcon("Images/Gadget_Main_Background_QuickLaunch.png"))
        b.setIconSize(QSize(50,35))
        return b

    def __creerBoutonTraiter(self):
        # Bouton d'ouverture de fichier image
        b = QPushButton(u"Traiter l'image", self)
        b.resize(220,40)
        b.move(290, 20)
        b.setToolTip(u"Ouvre le menu de traitement de l'image")
        b.setFont(QFont("Times New Roman", 12, QFont.Bold, True))
        b.setIcon(QIcon("Images/engrenage-3.png"))
        b.setIconSize(QSize(50,35))
        return b        

    def __creerMenuTraiter(self):
        # Menu 'traiter' avec ses item
        m = QMenu()    
        m.addAction('Reinit', self.__Reinit)
        m.addAction('HReverse', self.__HReverse)
        m.addAction('VReverse', self.__VReverse)
        m.addAction('Transpose', self.__Transpose)
        m.addAction('TournerD', self.__TournerD)
        m.addAction('TournerG', self.__TournerG)
        m.addAction('AjouterCadre', self.__AjouterCadre)
        m.addAction('Negatif', self.__Negatif)
        m.addAction('VoirOpacite', self.__VoirOpacite)
        m.addAction('ChangerBalance', self.__ChangerBalance)
        m.addAction('NoirEtBlanc', self.__NoirEtBlanc)
        m.addAction('Transparent', self.__Transparent)
        return m 

    def __Reinit(self):         self.__TraiterImage(self.__ReinitImage2)
    def __HReverse(self):       self.__TraiterImage(self.__argbTab.HReverse)
    def __VReverse(self):       self.__TraiterImage(self.__argbTab.VReverse)
    def __Transpose(self):      self.__TraiterImage(self.__argbTab.Transpose)
    def __TournerD(self):       self.__TraiterImage(self.__argbTab.TournerD)
    def __TournerG(self):       self.__TraiterImage(self.__argbTab.TournerG)
    def __AjouterCadre(self):      
        win = CadreForm(self)
        win.exec_()
        self.__TraiterImage(self.__argbTab.AjouterCadre, win.getARGB(), win.getNBX(), win.getNBY())
        
    def __Negatif(self):        self.__TraiterImage(self.__argbTab.Negatif)
    def __VoirOpacite(self):    self.__TraiterImage(self.__argbTab.VoirOpacite)
    def __ChangerBalance(self):
        win = ColorBalanceForm(self)
        win.exec_()
        self.__TraiterImage(self.__argbTab.ChangerBalance, win.getCoefRGB())
    def __NoirEtBlanc(self):    self.__TraiterImage(self.__argbTab.NoirEtBlanc)
    def __Transparent(self):
        seuil = 0.97
        text, ok = QInputDialog.getText(self, '?', 'Seuil [0..1] : ')
        if ok: seuil = float(text)
        self.__TraiterImage(self.__argbTab.Transparent, seuil)  

    def __Redimensionner(self):
        larg1 = self.__cadre1.width()
        haut1 = self.__cadre1.height()
        larg2 = self.__cadre2.width()
        haut2 = self.__cadre2.height()
        largeurtot = 560 
        if larg1 > 250:
            dlarg1 = larg1 - 250
            largeurtot += dlarg1
        else : larg1 = 250
        #self.sauver.move(40 + larg1, 20)
        self.__cadre2.move(40 + larg1, 80)
        if larg2 > 250:
            dlarg2 = larg2 - 250
            largeurtot += dlarg2
        hauteurtot = 200
        if haut1 > haut2:
            if haut1 > 100: hauteurtot += haut1-100
        elif haut2 > 100: hauteurtot += haut2-100
        self.setGeometry(self.__right - largeurtot, self.__top, largeurtot, hauteurtot) 

    def OuvrirNouvelleImage(self):
        # ouverture d'un fichier image choisi par l'utilisateur
        fichier = QFileDialog.getOpenFileName(self,\
                      u'Ouvrir une image pixellisée (*.png *.bmp *.jpg *.jpeg)',\
                      "Images", 'Images (*.png *.bmp *.jpg *.jpeg)')
        # Création de l'objet QImage correspondant
        self.__image = QImage(fichier)
        # Conversion et stockage de la copie de l'image en format ARGBArray
        self.__argbTab = ARGBArray(self.__image)
        # Affichage dans le cadre 1
        self.__cadre1.AfficherImage(self.__image)
        # Effacement du cadre 2
        self.__cadre2.EffacerImage()
        # Ajustement de la fenêtre
        self.__Redimensionner()

    def __ReinitImage2(self):
        # Effacement du cadre 2
        self.__cadre2.EffacerImage()
        # Conversion et stockage de la copie de l'image en format ARGBArray
        self.__argbTab = ARGBArray(self.__image)
        # Conversion et affichage
        newimage = self.__argbTab.ConvertToQImage()
        # Affichage dans le cadre 2
        self.__cadre2.AfficherImage(self.__image)
        # Ajustement de la fenêtre
        self.__Redimensionner()        

    def __TraiterImage(self,traitement,*args):
        u"lance le traitement de l'image et l'affiche dans cadre2"
        if self.__cadre1.ImageQ():
            # effectuer le traitement choisi
            traitement(*args)
            # Conversion, affichage et ajustement de la fenêtre
            newimage = self.__argbTab.ConvertToQImage()
            self.__cadre2.AfficherImage(newimage)
            self.__Redimensionner()

class CadreForm(QDialog):
    def __init__(self,parent):
        QDialog.__init__(self,parent)   
        self.__argb = [ 1., 1., 0.8, 1. ]
        self.__nbX = 5
        self.__nbY = 5
        self.a = QDoubleSpinBox()
        self.a.setSingleStep(0.1)
        self.a.setRange(0,1)
        self.a.setValue(self.__argb[0])
        self.alabel = QLabel("Alpha")
        self.r = QDoubleSpinBox()
        self.r.setSingleStep(0.1)
        self.r.setRange(0,1)
        self.r.setValue(self.__argb[1])
        self.rlabel = QLabel("Red")
        self.g = QDoubleSpinBox()
        self.g.setSingleStep(0.1)
        self.g.setRange(0,1)
        self.g.setValue(self.__argb[2])
        self.glabel = QLabel("Green")
        self.b = QDoubleSpinBox()
        self.b.setSingleStep(0.1)
        self.b.setRange(0,1)
        self.b.setValue(self.__argb[3])
        self.blabel = QLabel("Blue ")
        self.nbPixX = QDoubleSpinBox()
        self.nbPixXlabel = QLabel("Nb pixels en X")
        self.nbPixX.setValue(self.__nbX)
        self.nbPixY = QDoubleSpinBox()
        self.nbPixYlabel = QLabel("Nb pixels en Y")
        self.nbPixY.setValue(self.__nbY) 
        self.btnOK = QPushButton('OK',self) 

        # layout
        layout = QGridLayout()
        layout.addWidget(self.a, 0, 1)
        layout.addWidget(self.alabel, 0, 0)
        layout.addWidget(self.r, 1, 1)
        layout.addWidget(self.rlabel, 1, 0)
        layout.addWidget(self.g, 2, 1)
        layout.addWidget(self.glabel,2, 0)
        layout.addWidget(self.b, 3, 1)
        layout.addWidget(self.blabel,3, 0)
        layout.addWidget(self.nbPixX, 4, 1)
        layout.addWidget(self.nbPixXlabel,4, 0)
        layout.addWidget(self.nbPixY,5, 1)
        layout.addWidget(self.nbPixYlabel, 5, 0)
        layout.addWidget(self.btnOK,6,1)
        self.setLayout(layout)
        self.a.setFocus()
        self.setWindowTitle("Param. cadre") 

        # Connections

        self.connect(self.btnOK, SIGNAL('clicked()'), self.update)

    def getARGB(self) : return self.__argb
    def getNBX(self) : return self.__nbX
    def getNBY(self) : return self.__nbY

    def update(self):
        "update user interface"
        # get values   
        self.__argb = (self.a.value(),self.r.value(),self.g.value(),self.b.value())
        self.__nbX = int(self.nbPixX.value())
        self.__nbY = int(self.nbPixY.value())
        self.done(0)

class ColorBalanceForm(QDialog):
    def __init__(self,parent):
        QDialog.__init__(self,parent)
        self.__crgb = [ 1., 1., 1. ]
        self.r = QDoubleSpinBox()
        self.r.setSingleStep(0.1)
        self.r.setRange(0,10)
        self.r.setValue(self.__crgb[0])
        self.rlabel = QLabel("Red")
        self.g = QDoubleSpinBox()
        self.g.setSingleStep(0.1)
        self.g.setRange(0,10)
        self.g.setValue(self.__crgb[1])
        self.glabel = QLabel("Green")
        self.b = QDoubleSpinBox()
        self.b.setSingleStep(0.1)
        self.b.setRange(0,10)
        self.b.setValue(self.__crgb[2])
        self.blabel = QLabel("Blue ")
        self.btnOK = QPushButton('OK',self) 

        # layout
        layout = QGridLayout()
        layout.addWidget(self.r, 0, 1)
        layout.addWidget(self.rlabel, 0, 0)
        layout.addWidget(self.g, 1, 1)
        layout.addWidget(self.glabel, 1, 0)
        layout.addWidget(self.b, 2, 1)
        layout.addWidget(self.blabel, 2, 0)
        layout.addWidget(self.btnOK, 3, 1)
        self.setLayout(layout)
        self.r.setFocus()
        self.setWindowTitle("Correction des couleurs") 
        self.resize(250,150)

        # Connections

        self.connect(self.btnOK, SIGNAL('clicked()'), self.update)

    def getCoefRGB(self) : return self.__crgb

    def update(self):
        "update user interface"
        # get values   
        self.__crgb = (self.r.value(),self.g.value(),self.b.value())
        self.done(0)

        


