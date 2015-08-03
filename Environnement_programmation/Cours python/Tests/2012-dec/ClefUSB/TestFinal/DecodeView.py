# -*- coding: utf-8 -*-

from PyQt4.QtGui  import QFrame, QLabel, QPushButton
from PyQt4.QtCore import SIGNAL

from Viewer import Viewer

class DecodeView(Viewer):
    'To view the loaded image and the hidden text (if any)'

    def __init__(self, parent, posx, posy):
        Viewer.__init__(self, parent, posx, posy)
        self.__hiddenText = QLabel(self)        
        self.__btnDecode  = QPushButton("Decode",self)
        self.__ConfigureWidgets()        

    def __ConfigureWidgets(self):
        # configures widgets in base class:
        Viewer._ConfigureWidgets(self)
        self.connect(self._btnLoad, SIGNAL('clicked()'), self.LoadImage)
      
        B  = self._border
        Wi, Wb, Wt = self._imageWidth , self._btnWidth , self._textWidth
        Hi, Hb, Ht = self._imageHeight, self._btnHeight, self._textHeight

        # resizes, moves and connects the button "Decode":
        self.__btnDecode.resize(Wb, Hb)
        self.__btnDecode.move(B+Wi+B, B+Hb+B)
        self.connect(self.__btnDecode, SIGNAL('clicked()'), self.Decode)

        # resizes, moves and configures the text area:                
        self.__hiddenText.move(B, B+Hb+B/2+Hi+B)
        self.__hiddenText.resize(Wt, Ht)
        self.__hiddenText.setText("")
        self.__hiddenText.setWordWrap(True)
        self.__hiddenText.setFrameShape(QFrame.Box)

    def LoadImage(self):
        # call LoadImage in base class:
        Viewer._LoadImage(self)
        
        self.__hiddenText.setText("")
        
    def Decode(self):
        'To retrieve the hidden texte inside the image'
        if self._initialImage != None:
            # calls method FindTextInImage() on the object steganoGP in base class:
            hiddenText = self._steganoGP.FindTextInImage(self._initialImage)
            # unicode(text,'utf-8') returns the text encoded with the UTF-8 standard.
            texte = unicode(hiddenText,'utf-8')
            # Displays the text in the appropriate widget:
            self.__hiddenText.setText(texte)
