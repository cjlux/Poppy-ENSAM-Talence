# -*- coding: utf-8 -*-
from numpy.fft import fft,ifft
from math import pi
from cmath import exp as cexp
from copy import copy

from DiscreteTime import DiscreteTime
from DSPlotUtils import DSsignalPlot, DSspectrumPlot

class DigitalSignal(DiscreteTime):
    "To implement the digital Signal concept"
    def __init__(self, deltaT=1.0, startT=0.0, values = [0.0]):
        DiscreteTime.__init__(self, len(values), deltaT, startT)
        self.__vX = values      # digital signal values (time domain)
        self.__vZ = None        # Fourier Transform  values
        self.__updateFT()       # computes the Fourier Transform (FT)

    # access methods to read attributes (getters):
    def sigValues(self):  return copy(self.__vX)    # returns a copy of vX
    def FTValues(self):   return copy(self.__vZ)    # returns a copy of vZ
    def parameters(self): return self.step(), self.start()

    # computed values:
    def samplingFreq(self): return 1./self.step()
    def deltaF(self): return 1./(self.step()*self.nbVal())
    def frequencies(self):
        liste = []
        for i in range(len(self.__vZ)): liste.append(i*self.deltaF())
        return liste    
    
    # delay() and setPeriod() are re-defined in the derived class DigitalSignal.
    # To call the methods of the base class DiscreteTime, one must use a syntaxe
    # like : DiscreteTime.delay(self,...) or DiscreteTime.setPeriod(self,...)

    # access methods to write attributes (setters)
    def setPeriod(self, newP):
        "To set a new time step value"
        DiscreteTime.setPeriod(self, newP)
        self.__updateFT()

    # useful methods:   
    def delay(self, d):
        "To delay the digital signal by the given value (d)"
        DiscreteTime.delay(self, d)     # executes delay() in the base class !
########### PARTIE A COMPLETER ###########
        # c = 
        # FTval =
        # for
        
        # self.__vZ =
##########################################

    def zeroPadding(self, nbZeros = 0):
        "To compute and return a new digital signal, using the zero-padding transform"
        if nbZeros==0: return copy(self)
########### PARTIE A COMPLETER ###########
        # N =
        # to =
        # Te =
        # Fe =
        # vY =
        # m =
        # c =










        
##########################################
        cvalues = list(ifft(vY))
        # elimination of the complex numerical residues
        values = []
        for z in cvalues:
            if abs(z.imag) > 1e-12 :
                print "Problem in 'ZeroPadding':",
                print "non-real value of the rebuilt signal:", z
            values.append(z.real)
        # a new digital signal is returned
        return DigitalSignal(Te, to, values)
            
    def __updateFT(self):
        "To compute FT of the signal"
        m = self.nbVal()/2 + 1
        LZ = list(fft(self.sigValues()))[0:m]
        T  = self.step()
        df = self.deltaF()
        to = self.start()
        c  = -2*(1j)*pi*df*to
        for k in range(m):
            LZ[k] *= T*cexp(c*k)
        self.__vZ = LZ
        
    def signalPlot(self, show = True, noFig=1,
                   size=5, color='b', marker='o', 
                   resetXlim = True, resetYlim = True, screen=True, figSize=None):
        return DSsignalPlot(self, show, noFig, size, color, marker, resetXlim, resetYlim, screen, figSize)

    def spectrumPlot(self, show = True, noFig=2,
                     size=5, color='b', marker='o',
                     resetYlim = True, screen=True,  figSize=None):
        return DSspectrumPlot(self, show, noFig, size, color, marker, resetYlim, screen, figSize)

if __name__=="__main__":
    "to test the 'DigitalSignal' class"
