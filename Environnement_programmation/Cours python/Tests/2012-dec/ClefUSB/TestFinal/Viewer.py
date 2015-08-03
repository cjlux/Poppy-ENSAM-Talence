# -*- coding: utf-8 -*-

from PyQt4.QtGui  import QFrame, QLabel, QPushButton, QFileDialog
from PyQt4.QtGui  import QImage, QPixmap, QFont
from PyQt4.QtCore import SIGNAL

from SteganoGraphic import SteganoGraphicProcess

class Viewer(QFrame):
    u"Base class for the steganographic encoder/decoder viewers"

    def __init__(self, parent, posx, posy):
        QFrame.__init__(self, parent)
        
        self._steganoGP  = SteganoGraphicProcess()
        self._border     = 15
        self._imageWidth = 200
        self._imageHeight= 280
        self._btnHeight  = 30
        self._btnWidth   = 80
        self._textHeight = 90
        self._textWidth  = 2*self._imageWidth+self._btnWidth+2*self._border

        self._iniImageDisplay  = QLabel(self)
        self._initialImage     = None
        self._btnQuit          = QPushButton("Quit",self)
        self._btnLoad          = QPushButton("Load Image",self)
       
        B  = self._border
        Wi, Wb, Wt = self._imageWidth , self._btnWidth , self._textWidth
        Hi, Hb, Ht = self._imageHeight, self._btnHeight, self._textHeight
        self._width      = B + Wi + B   + Wb + B + Wi + B
        self._height     = B + Hb + B/2 + Hi + B + Ht + 2*B

        self._ConfigureWidgets()        
        self.resize(self._width, self._height)
        self.move(posx, posy)

    def _ConfigureWidgets(self):
        B  = self._border
        Wi, Wb = self._imageWidth , self._btnWidth 
        Hi, Hb = self._imageHeight, self._btnHeight

        self._btnLoad.resize(2*Wb, Hb)
        self._btnLoad.move(B, B)

        self._btnQuit.resize(Wb, Hb)
        self._btnQuit.move(B+Wi+B, B+Hb+B+Hb+B)
        self.connect(self._btnQuit, SIGNAL('clicked()'), self.parentWidget().close)

        self._iniImageDisplay.move(B,B+Hb+B/2)
        self._iniImageDisplay.resize(self._imageWidth, self._imageHeight)
        self._iniImageDisplay.setFrameShape(QFrame.Box)

    def GetWidth(self) : return self._width
    
    def GetHeight(self): return self._height
    
    def _LoadImage(self):
        f = QFileDialog.getOpenFileName(self,\
            u'Opens a bitmap image file (*.png *.bmp *.jpg *.jpeg *.tif)',\
            ".", 'Images (*.png *.bmp *.jpg *.jpeg *.tif)')
        self._initialImage = QImage(f)
        pixmap = QPixmap.fromImage(self._initialImage)
        pixmap = pixmap.scaledToWidth(self._imageWidth)
        self._iniImageDisplay.setPixmap(pixmap)
        self._iniImageDisplay.resize(pixmap.width(), pixmap.height())
 
