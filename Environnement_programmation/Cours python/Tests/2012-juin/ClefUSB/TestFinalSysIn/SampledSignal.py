# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from math import *                          # import all from math module

from DigitalSignal import DigitalSignal

class SampledSignal(DigitalSignal):
    "To model a sampled signal resulting from an analog signal sampling"
    def __init__(self, expression, n, Ts=1.0, start=0.0):
        self.__s = expression   # string denoting the analog expression with
        # respect to t. Examples : 'cos(3*pi*t)', 'exp(-10*t)'
        values = self.__sampleSignal(n, Ts, start)  # to do the sampling !
        DigitalSignal.__init__(self, Ts, start, values)

    # access methods to read attributes (getters):
    def analogSignal(self): return "Sampled Signal: t |-> "+self.__s
    def expression(self): return self.__s
    def parameters(self): return self.expression(), self.nbVal(), self.step(), self.start()
    
    # delay() and setPeriod() are re-defined in the derived class SampledSignal.
    # To call the methods of the base class DigitalSignal, one must use a syntaxe
    # like : DigitalSignal.delay(self,...) or DigitalSignal.setPeriod(self,...)

    def delay(self, delayVal):
        to = self.start() + delayVal
        values = self.__sampleSignal(start=to)
        DigitalSignal.__init__(self, self.step(), to, values)
        
    def setPeriod(self, newTs):
        values = self.__sampleSignal(Ts=newTs)
        DigitalSignal.__init__(self, newTs, self.start(), values)

    def __sampleSignal(self, n=None, Ts=None, start=None):
        'private method to do the sampling of the analog expression'
        if start == None : start = self.start()
        if    Ts == None :    Ts = self.step()
        if    n  == None :     n = self.nbVal()
        values = []
        t = start
        for no in range(n):
            exec 'values.append('+self.expression()+')'
            t += Ts
        return values

    # useful methods
    def signalPlot(self, show=True, noFig=1,
                   size=5, color='b', marker='o', linecolor = 'g', linewidth = 1.0,
                   resetXlim = True, resetYlim = True, screen=True, figSize=None):
        'To plot the analog signal and the sampling result'
        exec 'def s(t): return ' + self.expression()
        tmin = self.start()-self.step()
        tmax = self.last()+1.2*self.step()
        deltaT = 0.005 * (tmax-tmin)
        t = tmin
        x, y = [], []
        while t<tmax :
            x.append(t)
            exec 'y.append(' + self.__s + ')'
            t += deltaT
            
        if figSize != None:
            fig = plt.figure(noFig, figsize=figSize)
        else:
            fig = plt.figure(noFig)
        # anlog signal plot:
        plt.plot(x,y,'-',color = linecolor, linewidth = linewidth)
        # sampled (digital) signal plot:
        ymin, ymax = min(y),max(y)
        plt.ylim(1.05*ymin-0.05*ymax,1.05*ymax-0.05*ymin)
        DigitalSignal.signalPlot(self, show, noFig, size, color, marker,
                                 resetXlim, resetYlim, screen, figSize )
        if show: plt.show()
        return fig
        
if __name__=="__main__":
    "to test the 'SampledSignal' class"
