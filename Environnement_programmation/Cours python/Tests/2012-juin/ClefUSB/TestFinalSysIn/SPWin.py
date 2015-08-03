# -*- coding: utf-8 -*-

from PyQt4.QtGui  import QApplication, QDesktopWidget, QToolTip, QFont
from PyQt4.QtGui  import QMainWindow, QPushButton, QImage, QLabel, QLineEdit
from PyQt4.QtGui  import QFileDialog, QAction, QCheckBox, QSlider, QSpinBox
from PyQt4.QtGui  import QDoubleSpinBox, QPalette, QColor, QFrame
from PyQt4 import QtCore

from os import remove
from os.path import dirname, basename, exists

import locale
import sys
from  copy import copy

from DigitalSignal import DigitalSignal
from SampledSignal import SampledSignal

from FrameImage import FrameImage

import matplotlib.pyplot as plt

class SPWin(QMainWindow):
    """
    Signal Processing Window : this is the main window that implements the graphical user interface
    to design and process analogue or digital signals
    """
    # class attributes
    fg = "QLabel {color:gray}"
    bg = "QLabel {background-color:gray}"
    xPosRef, yPosRef = 20, 100
    labelW,  labelH  = 130,25
    editW,   editH   = 70, labelH
    btnW,    btnH    = 55, labelH
    hSpace,  vSpace  = 6, labelH+2
    frameW, frameH   = 500, 300
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Signal Processing Window")
        self.statusBar().showMessage('Ready')
 
        self.__signal0    = None  # original digital or sampled signal (blue)
        self.__oldSignal0 = None  # copy of the original signal
        self.__signal1    = None  # processed original signal (magenta)
        
        self.__filePath  = None  # full path of the signal file
        self.__fileDir   = None  # name of the directory
        self.__fileName  = None  # name of the digital signal file
        
        self.__widgetDict  = {}  # dictionnary of all GUI widgets
        self.__cadre1    = None  # frame for time plotting
        self.__cadre2    = None  # frame for frequency plotting
       
        # now create all graphical decoration...
        self.__createMenus()
        self.__createFields()        
        self.__createFrames()
        self.__createButtons()
        self.__createZPaddGUI()
        self.__createDelayGUI()
        self.__createSamplingTGUI()
        self.__clear()
        self.__center()

    def __center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def __clear(self):
        self.__clearAllPlots()
        self.__clearAllGUI()
        self.__signal0 = None
        self.__oldSignal0 = None
        self.__signal1 = None
        self.__resetZPadGUI()
        self.__resetDelayGUI()
        self.__resetSamplingTGUI()
        
    def __reset(self):
        self.__clearAllPlots()
        self.__clearAllGUI()
        self.__regenerateSignal()
        self.__resetZPadGUI()
        self.__resetDelayGUI()
        self.__resetSamplingTGUI()
        
    def __clearAllPlots(self):
        # clear all frames
        self.__clearTimePlot()
        self.__clearFrequencyPlot()
        
    def __clearTimePlot(self):
        self.__cadre1.ClearImage()
        self.__cadre1.DisplayComment("")

    def __clearFrequencyPlot(self):
        self.__cadre2.ClearImage()
        self.__cadre2.DisplayComment("")
        
    def __clearAllGUI(self):
        # set all GUI decorations invisible
        self.__digitalSignalGUI(False)
        self.__sampledSignalGUI(False)

    def __createFrames(self):
        # Two frames are created : one for the time domain plot, 
        # the other for the frequency domain plots.
        frame1W, frame1H = SPWin.frameW, SPWin.frameH
        frame2W, frame2H = SPWin.frameW, SPWin.frameH
        spaceHL, spaceHR, spaceV = 300,20,40
        mainWitdh  = int(frame1W+spaceHL+spaceHR)
        mainHeight = int(frame1H+frame2H+2*spaceV)
        self.resize(mainWitdh,mainHeight)
        self.__cadre1 = FrameImage(self,spaceHL,spaceV,            frame1W,frame1H,True)
        self.__cadre2 = FrameImage(self,spaceHL,frame1H+1.5*spaceV,frame2W,frame2H,True)

    def __openReadFile(self,message,extension):
        self.__filePath = QFileDialog.getOpenFileName(self,message,'',extension)            
        path = str(self.__filePath)
        if path == "" : return        
        self.__fileDir  = dirname(path)
        self.__fileName = basename(path)

        lu = []
        f = open(self.__filePath,'r')
        for line in f:
            if line[0] == "#" : continue
            lu.append(line)
        f.close
        return lu
 
    def __openDiscreteSignalFile(self):
        "To open, read digital signal file, and create a DigitalSignal object"
        lu = self.__openReadFile('opens a digital signal file', 'Digital Signal File (*.dsf)')           
        if lu != None and len(lu) >= 4:
            n     = int(lu[0].split()[0])
            dt    = float(lu[1].split()[0])
            to    = float(lu[2].split()[0])
            s     = map(float,lu[3].split()[:n])
            self.__createDigitalSignal(dt,to,s)
        else:
            print "Read error in file <%s>" % self.__fileName

    def __openSampledSignalFile(self):
        lu = self.__openReadFile('opens a sampled signal file', 'Sampled Signal File (*.ssf)')            
        if lu != None and len(lu) >= 4:
            n     = int(lu[0].split()[0])
            Ts    = float(lu[1].split()[0])
            to    = float(lu[2].split()[0])
            expr  = lu[3].split()[0]
            self.__createSampledSignal(expr,n,Ts,to)
        else:
            print "Read error in file <%s>" % self.__fileName

    def __regenerateSignal(self):
        if self.__oldSignal0 != None:
            sig = self.__oldSignal0
            if isinstance(sig, SampledSignal):
                expr,n,dt,to = sig.parameters()
                self.__createSampledSignal(expr,n,dt,to)
            elif isinstance(sig, DigitalSignal):
                (dt,to),s  = sig.parameters(), sig.sigValues()
                self.__createDigitalSignal(dt,to,s)

    def __createDigitalSignal(self, dt, to, s):
        self.__clear()
        self.__digitalSignalGUI(True)
        self.__signal0 = DigitalSignal(dt, to, s)
        self.__oldSignal0 = copy(self.__signal0)
        Fs = self.__signal0.samplingFreq()
        df = self.__signal0.deltaF()
        self.__initSignalFields(dt,to,len(s),Fs,df)
        self.__plot(clearAll=True)

    def __initSignalFields(self,Ts=1.0,to=0.0,N=10,Fs=1.0,df=0.1,expr="sin(4*pi*t)"):
        self.__widgetDict["Edt_Ts"].setText("%6.2e"%Ts)
        self.__widgetDict["Edt_to"].setText("%6.2e"%to)
        self.__widgetDict["Edt_N"].setText(str(N))
        self.__widgetDict["Edt_Fs"].setText("%6.2e"%Fs)
        self.__widgetDict["Edt_df"].setText("%6.2e"%df)
        self.__widgetDict["Edt_mTs"].setText("")
        self.__widgetDict["Edt_mto"].setText("")
        self.__widgetDict["Edt_mN"].setText("")
        self.__widgetDict["Edt_mFs"].setText("")
        self.__widgetDict["Edt_mdf"].setText("")
        self.__widgetDict["Edt_Expr"].setText(expr)

    def __updateSignalFields(self):
        if self.__signal0 == None: return
        Ts = self.__signal0.step()
        to = self.__signal0.start()
        N  = self.__signal0.nbVal()
        Fs = self.__signal0.samplingFreq()
        df = self.__signal0.deltaF()
        self.__widgetDict["Edt_Ts"].setText("%6.2e"%Ts)
        self.__widgetDict["Edt_to"].setText("%6.2e"%to)
        self.__widgetDict["Edt_N"].setText(str(N))
        self.__widgetDict["Edt_Fs"].setText("%6.2e"%Fs)
        self.__widgetDict["Edt_df"].setText("%6.2e"%df)

    def __updateModifiedSignalFields(self):
        if self.__signal1 == None: return
        Ts = self.__signal1.step()
        to = self.__signal1.start()
        N  = self.__signal1.nbVal()
        Fs = self.__signal1.samplingFreq()
        df = self.__signal1.deltaF()
        self.__widgetDict["Edt_mTs"].setText("%6.2e"%Ts)
        self.__widgetDict["Edt_mto"].setText("%6.2e"%to)
        self.__widgetDict["Edt_mN"].setText(str(N))
        self.__widgetDict["Edt_mFs"].setText("%6.2e"%Fs)
        self.__widgetDict["Edt_mdf"].setText("%6.2e"%df)

    def __createSampledSignal(self,expr,n,Ts,to):
        self.__clear()
        self.__sampledSignalGUI(True)
        self.__signal0 = SampledSignal(expr, n, Ts, to)
        self.__oldSignal0 = copy(self.__signal0)        
        Fs = self.__signal0.samplingFreq()
        df = self.__signal0.deltaF()
        n  = self.__signal0.nbVal()
        expr = self.__signal0.expression()
        self.__initSignalFields(Ts,to,n,Fs,df,expr)
        self.__plot(clearAll=True)
                                         
    def __createMenus(self):
        # to create menu bar
        MOpenDS = QAction('Open &Digital Signal', self)
        MOpenDS.setShortcut('Ctrl+D')
        MOpenDS.setStatusTip('Opens an ASCII file containing a digital signal data')

        MCreaSS = QAction('Open &Sampled Signal', self)
        MCreaSS.setShortcut('Ctrl+C')
        MCreaSS.setStatusTip('Opens an ASCII file containing a sampled signal')

        MQuit = QAction('&Quit', self)
        MQuit .setShortcut('Ctrl+Q')
        MQuit.setStatusTip('Quits the application')

        self.connect(MQuit,   QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))  
        self.connect(MOpenDS, QtCore.SIGNAL('triggered()'), self.__openDiscreteSignalFile)
        self.connect(MCreaSS, QtCore.SIGNAL('triggered()'), self.__openSampledSignalFile)        

        menubar = self.menuBar()  
        menuF = menubar.addMenu('File')  
        menuF.addAction(MOpenDS)    
        menuF.addAction(MCreaSS)    
        menuF.addAction(MQuit)    
                    
    def __createFields(self):
        "To create the graphical widgets holding signal object attributes"

        palette = QPalette()
        # edit widget with read-only label
        infos  = [["to","Start Time (s)"],
                  ["Ts","Sampling Period (s)"],
                  ["N", "Number of Samples"],
                  ["Fs","Sampling Freq.  (Hz)"],
                  ["df","Frequency Step (Hz)"],
                  ["Expr","Analog Signal"],]
        
        xPosRef = SPWin.xPosRef
        ypos    = SPWin.yPosRef
        xpos    = xPosRef+SPWin.labelW
        xposm   = xpos + SPWin.hSpace + SPWin.editW
        for i in range(len(infos)-1):
            # setGeometry(x_pos, y_pos, width, height):

            # label:
            label = QLabel(infos[i][1],self)
            label.setGeometry(xPosRef, ypos, SPWin.labelW, SPWin.labelH)
            self.__widgetDict["Lab_"+infos[i][0]] =label

            # line edit for signal:
            edit = QLineEdit(self)
            edit.setReadOnly(True)
            edit.setDisabled(True)
            palette.setColor(edit.foregroundRole(), QColor('blue'))
            edit.setPalette(palette)
            edit.setGeometry(xpos, ypos, SPWin.editW, SPWin.editH)
            self.__widgetDict["Edt_"+infos[i][0]]=edit

            # line edit for modified signal
            edit = QLineEdit(self)
            edit.setReadOnly(True)
            edit.setDisabled(True)
            palette.setColor(edit.foregroundRole(), QColor('magenta'))
            edit.setPalette(palette)
            edit.setGeometry(xposm, ypos, SPWin.editW, SPWin.editH)
            self.__widgetDict["Edt_m"+infos[i][0]]=edit

            ypos += SPWin.vSpace

        # expr field is larger
        label = QLabel(infos[-1][1],self)
        label.setGeometry(xPosRef, ypos, SPWin.labelW, SPWin.labelH)
        self.__widgetDict["Lab_"+infos[-1][0]] =label
        edit = QLineEdit(self)
        edit.setReadOnly(True)
        edit.setDisabled(True)
        palette.setColor(edit.foregroundRole(), QColor('blue'))
        edit.setPalette(palette)
        edit.setGeometry(xPosRef+SPWin.labelW, ypos, 2.09*SPWin.editW, SPWin.editH)
        self.__widgetDict["Edt_"+infos[-1][0]]=edit

    def __createZPaddGUI(self):
        xPosRef = SPWin.xPosRef
        ypos    = SPWin.yPosRef+265
        xpad, ypad = 4, 4

        frame = QFrame(self)
        frame.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        frame.move(xPosRef-xpad,ypos-ypad)
        frameW = SPWin.labelW + SPWin.editW + SPWin.btnW + 3*SPWin.hSpace
        frameH = 2*SPWin.labelH + SPWin.vSpace
        frame.resize(frameW, frameH)
        self.__widgetDict["Fra_ZPad"]=frame

        label = QLabel("<B>Zero Padding</B>",self)
        label.setGeometry(xPosRef-1, ypos-7, SPWin.labelW, SPWin.labelH)

        ypos += SPWin.vSpace/2
        label = QLabel("Number of zeros ",self)
        label.setGeometry(xPosRef, ypos, SPWin.labelW, SPWin.labelH)
        
        spinB = QSpinBox(self)
        spinB.setGeometry(xPosRef+SPWin.labelW, ypos, SPWin.editW, SPWin.editH)
        spinB.setRange(0,1000)
        spinB.setValue(0)
        self.__widgetDict["Lab_ZPad"], self.__widgetDict["Spi_ZPad"] = label, spinB

        slide = QSlider(QtCore.Qt.Horizontal, self)
        slide.setGeometry(xPosRef, ypos+SPWin.vSpace, SPWin.labelW + SPWin.editW, SPWin.editH)
        slide.valueChanged.connect(spinB.setValue)
        spinB.valueChanged.connect(slide.setValue)
        self.__widgetDict["Sli_ZPad"] = slide

        x = xPosRef + SPWin.labelW + SPWin.hSpace + SPWin.editW 
        btn = QPushButton('Apply',self)
        btn.setGeometry(x, ypos, SPWin.btnW, SPWin.btnH)
        btn.setToolTip('Applies zero padding to the signal')
        self.connect(btn, QtCore.SIGNAL('clicked()'), self.__applyZPadGUI)
        
    def __resetZPadGUI(self):
        self.__widgetDict["Spi_ZPad"].setValue(0)
        self.__widgetDict["Sli_ZPad"].setValue(0)

    def __applyZPadGUI(self):
        if self.__signal0 == None:
            return
        # retrieve number of zero padding and update signal 
        nbZeros = int(self.__widgetDict["Sli_ZPad"].value())
        if self.__signal1 != None:
            source = self.__signal1
        else:
            source = self.__signal0
        self.__signal1 = source.zeroPadding(nbZeros)
        self.__updateModifiedSignalFields()            
        self.__plot()

    def __createDelayGUI(self):
        x1, y1, x2, y2 = self.__widgetDict["Fra_ZPad"].geometry().getCoords()
        
        xPosRef = SPWin.xPosRef
        ypos    = y2 + SPWin.vSpace
        xpad, ypad = 4, 4

        frame = QFrame(self)
        frame.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        frame.move(xPosRef-xpad,ypos-ypad)
        frameW = SPWin.labelW + SPWin.editW + SPWin.btnW + 3*SPWin.hSpace
        frameH = SPWin.labelH + SPWin.vSpace
        frame.resize(frameW, frameH)
        self.__widgetDict["Fra_Delay"]=frame

        label = QLabel("<B><font color='blue'>Set Delay</font></B>",self)
        label.setGeometry(xPosRef-1, ypos-7, SPWin.labelW, SPWin.labelH)

        xpos = xPosRef
        ypos += SPWin.vSpace/2
        label = QLabel("<font color='blue'>Delay (sec)</font>",self)
        label.setGeometry(xPosRef, ypos, SPWin.labelW, SPWin.labelH)

        xpos += SPWin.labelW
        edit = QLineEdit(self)
        edit.setGeometry(xpos, ypos, SPWin.editW, SPWin.editH)
        edit.setText(str(0.0))
        self.__widgetDict["Edt_Delay"] = edit

        xpos += SPWin.hSpace + SPWin.editW 
        btn = QPushButton('Apply',self)
        btn.setGeometry(xpos, ypos, SPWin.btnW, SPWin.btnH)
        btn.setToolTip('Applies the delay to the signal')
        self.connect(btn, QtCore.SIGNAL('clicked()'), self.__applyDelayGUI)
        
    def __resetDelayGUI(self):
        self.__widgetDict["Edt_Delay"].setText(str("0.0"))

    def __applyDelayGUI(self):
        if self.__signal0 == None:
            return
        # retrieve number of zero padding and update signal 
        delay = float(self.__widgetDict["Edt_Delay"].text())
        self.__signal0.delay(delay)
        if self.__signal1 != None:
            self.__signal1 = None
        self.__updateSignalFields()            
        self.__plot()

    def __createSamplingTGUI(self):
        x1, y1, x2, y2 = self.__widgetDict["Fra_Delay"].geometry().getCoords()
        
        xPosRef = SPWin.xPosRef
        ypos    = y2 + SPWin.vSpace
        xpad, ypad = 4, 4

        frame = QFrame(self)
        frame.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        frame.move(xPosRef-xpad,ypos-ypad)
        frameW = SPWin.labelW + SPWin.editW + SPWin.btnW + 3*SPWin.hSpace
        frameH = SPWin.labelH + SPWin.vSpace
        frame.resize(frameW, frameH)
        self.__widgetDict["Fra_SamplingT"]=frame

        label = QLabel("<font color='blue'><B>Set Sampling Period</B></font>",self)
        label.setGeometry(xPosRef-1, ypos-7, SPWin.labelW, SPWin.labelH)

        xpos = xPosRef
        ypos += SPWin.vSpace/2
        label = QLabel("<font color='blue'>Sampling period (sec)</font>",self)
        label.setGeometry(xPosRef, ypos, SPWin.labelW, SPWin.labelH)

        xpos += SPWin.labelW
        edit = QLineEdit(self)
        edit.setGeometry(xpos, ypos, SPWin.editW, SPWin.editH)
        edit.setText(str(1.0))
        self.__widgetDict["Edt_SamplingT"] = edit

        xpos += SPWin.hSpace + SPWin.editW 
        btn = QPushButton('Apply',self)
        btn.setGeometry(xpos, ypos, SPWin.btnW, SPWin.btnH)
        btn.setToolTip('Apply the new sampling period to the signal')
        self.connect(btn, QtCore.SIGNAL('clicked()'), self.__applySamplingTGUI)
        
    def __resetSamplingTGUI(self):
        self.__widgetDict["Edt_SamplingT"].setText(str("1.0"))

    def __applySamplingTGUI(self):
        if self.__signal0 == None:
            return
        # retrieve number of zero padding and update signal 
        newTs = float(self.__widgetDict["Edt_SamplingT"].text())
        self.__signal0.setPeriod(newTs)
        if self.__signal1 != None:
            self.__signal1 = None
        self.__updateSignalFields()            
        self.__plot()

    def __createButtons(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        xPosRef, yPosRef = SPWin.xPosRef, SPWin.yPosRef-50
        x = xPosRef
        self.__btnQuit = QPushButton('Quit',self)
        self.__btnQuit.setGeometry(x, yPosRef, SPWin.btnW, SPWin.btnH)
        self.__btnQuit.setToolTip('Quits the application')
        self.connect(self.__btnQuit, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'))
        
        x += SPWin.btnW + SPWin.hSpace
        self.__btnReset = QPushButton('Reset',self)
        self.__btnReset.setGeometry(x, yPosRef, SPWin.btnW, SPWin.btnH)
        self.connect(self.__btnReset, QtCore.SIGNAL('clicked()'), self.__reset)        
    
    def __plot(self, clearAll=False):
        if clearAll: self.__clearAllPlots()
        self.__signalPlot()
        self.__spectrumPlot()

    def __signalPlot(self):
        # plots all what is needed...
        if self.__signal0 != None:
            file="DSplotTime.png"  
            fig = self.__signal0.signalPlot(show=False, screen=False, figSize=(7, 4))
            if self.__signal1 != None :
                self.__signal1.signalPlot(show=False, screen=False, figSize=(7, 4),
                                         color='magenta', size=4, resetXlim=False, resetYlim=False)
            fig.savefig(file, format='png', transparent=True, dpi=80, bbox_inches='tight')
            image = QImage(file)                
            self.__cadre1.DisplayImage(image)
            remove(file)
            fig.clear()

    def __spectrumPlot(self):
        # plots all what is needed...
         if self.__signal0 != None:
            file="DSplotFreq.png"
            plt.clf()
            fig = self.__signal0.spectrumPlot(show=False, screen=False, figSize=(7, 4))
            if self.__signal1 != None :
                self.__signal1.spectrumPlot(show=False, screen=False, figSize=(7, 4),
                                           color='magenta', size=3)
            fig.savefig(file, format='png', transparent=True, dpi=80, bbox_inches='tight')
            image = QImage(file)                
            self.__cadre2.DisplayImage(image)
            remove(file)
            fig.clear()

    def __sampledSignalGUI(self,vis):
        self.__digitalSignalGUI(vis)
        self.__widgetDict["Lab_Expr"].setVisible(vis)
        self.__widgetDict["Edt_Expr"].setVisible(vis)
        
    def __digitalSignalGUI(self,vis):
        self.__widgetDict["Lab_to"].setVisible(vis)
        self.__widgetDict["Lab_Ts"].setVisible(vis)
        self.__widgetDict["Lab_N"].setVisible(vis)
        self.__widgetDict["Lab_Fs"].setVisible(vis)
        self.__widgetDict["Lab_df"].setVisible(vis)
        self.__widgetDict["Edt_to"].setVisible(vis)
        self.__widgetDict["Edt_Ts"].setVisible(vis)
        self.__widgetDict["Edt_N"].setVisible(vis)
        self.__widgetDict["Edt_Fs"].setVisible(vis)
        self.__widgetDict["Edt_df"].setVisible(vis)
        self.__widgetDict["Edt_mto"].setVisible(vis)
        self.__widgetDict["Edt_mTs"].setVisible(vis)
        self.__widgetDict["Edt_mN"].setVisible(vis)
        self.__widgetDict["Edt_mFs"].setVisible(vis)
        self.__widgetDict["Edt_mdf"].setVisible(vis)
                
if __name__=="__main__":

    def main(args):
        app=QApplication(args)
        win=SPWin()
        win.show()
        # main loop waiting mouse events :
        r=app.exec_()
        return r

    main(sys.argv)

