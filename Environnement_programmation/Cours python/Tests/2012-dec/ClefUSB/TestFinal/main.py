# -*- coding: utf-8 -*-
import sys

# bibliothèque PyQt4
from PyQt4.QtGui  import QApplication, QMainWindow, QTabWidget
from PyQt4.QtCore import QTextCodec

from EncodeView import EncodeView
from DecodeView import DecodeView

class MainWindow(QMainWindow):
    u"Steganographic application user's interface"
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Steganographic application')
        self.__left   = 50
        self.__top    = 50
        self.__tab1   = EncodeView(self, 10, 10)
        self.__tab2   = DecodeView(self, 10, 10)
        self.__width  = self.__tab1.GetWidth() + 10
        self.__height = self.__tab1.GetHeight()+ 10
        self.__stack    = QTabWidget(self)
        
        self.__stack.addTab(self.__tab1, 'Encode')
        self.__stack.addTab(self.__tab2, 'Decode')
        
        self.setCentralWidget(self.__stack)
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)

if __name__ == '__main__' :
    # Qt context initialisation
    print 'Encoding system: ', sys.stdin.encoding
    app = QApplication(sys.argv)
    QTextCodec.setCodecForTr(QTextCodec.codecForName('UTF-8'));
    # Displays the main window
    win = MainWindow()
    win.show();
    # main loop : waiting for mouse graphical events
    app.exec_()
    # destroy all windows
    win.destroy()
