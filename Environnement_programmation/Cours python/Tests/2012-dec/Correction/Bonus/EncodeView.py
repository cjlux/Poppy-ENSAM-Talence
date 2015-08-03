# -*- coding: utf-8 -*-

from PyQt4.QtGui  import QFrame, QLabel, QPushButton, QFileDialog
from PyQt4.QtGui  import QPixmap, QPlainTextEdit
from PyQt4.QtCore import SIGNAL

from Viewer import Viewer

class EncodeView(Viewer):
    'To view the original image and the steganographic encoded image'

    def __init__(self, parent, posx, posy):
        Viewer.__init__(self, parent, posx, posy)
        
        self.__encImageDisplay  = QLabel(self)
        self.__textToHide       = QPlainTextEdit(self)
        self.__encodedImage     = None
        self.__btnEncode        = QPushButton('Encode',self)
        self.__btnSave          = QPushButton('Save modified Image'  ,self)

        self.__ConfigureWidgets()   
       
    def __ConfigureWidgets(self):
        # configures widgets in base class:
        Viewer._ConfigureWidgets(self)
        self.connect(self._btnLoad, SIGNAL('clicked()'), self.LoadImage)
       
        B  = self._border
        Wi, Wb, Wt = self._imageWidth , self._btnWidth , self._textWidth
        Hi, Hb, Ht = self._imageHeight, self._btnHeight, self._textHeight

        # resizes, moves and connects the button "Save":
        self.__btnSave.resize(2*Wb, Hb)
        self.__btnSave.move(B+Wi+B+Wb+B+Wi-2*Wb, B)
        self.connect(self.__btnSave, SIGNAL('clicked()'), self.SaveEncodedImage)

        # resizes, moves and connects the button "Encode":
        self.__btnEncode.resize(Wb, Hb)
        self.__btnEncode.move(B+Wi+B, B+Hb+B)
        self.connect(self.__btnEncode, SIGNAL('clicked()'), self.Encode)
        
        # resizes, moves and configures the modified image area:
        self.__encImageDisplay.move(B+Wi+B+Wb+B,B+Hb+B/2)
        self.__encImageDisplay.resize(self._imageWidth, self._imageHeight)
        self.__encImageDisplay.setFrameShape(QFrame.Box)
        
        # resizes, moves and configures text area:
        self.__textToHide.move(B, B+Hb+B/2+Hi+B)
        self.__textToHide.resize(Wt, Ht)
        self.__textToHide.setPlainText(u'Text to hide in the image')
        self.__textToHide.setFrameShape(QFrame.Box)

    def LoadImage(self):
        Viewer._LoadImage(self)
        self.__encImageDisplay.clear()
        
    def SaveEncodedImage(self):
        if self.__encodedImage != None: 
            f = QFileDialog.getSaveFileName(self,\
                u'To save a bitmap image (*.png *.bmp *.jpg *.jpeg *.gif *.tif)',\
                u'.', 'Images (*.png *.bmp *.jpg *.jpeg *.gif *.tif)')
            self.__encodedImage.save(f)           

    def Encode(self):
        'To encode the hidden texte inside the image'
        text = self.__textToHide.document().toPlainText().toUtf8()
        print "text to hide :",text
        # the work is done by the object steganoGP:
        self.__encodedImage = self._steganoGP.HideTextInImage(text, self._initialImage)
        pixmap = QPixmap.fromImage(self.__encodedImage)
        pixmap = pixmap.scaledToWidth(self._imageWidth)
        self.__encImageDisplay.setPixmap(pixmap)
        self.__encImageDisplay.resize(pixmap.width(), pixmap.height())

