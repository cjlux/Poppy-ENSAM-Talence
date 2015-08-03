import matplotlib.pyplot as plt

def setPlotLimits(array, setGetLimFunction, resetLim, setMinNull=False):
    "To update plot axes limits, taking into account any already existing plot"
    aMin, aMax =  min(array), max(array)
    if setMinNull: aMin=0.
    offset = (aMax-aMin)*0.1
    limMin, limMax = aMin-offset, aMax+offset            
    if resetLim is False:
        pltMin, pltMax = setGetLimFunction()
        limMin = min(pltMin, limMin)
        limMax = max(pltMax, limMax)
    setGetLimFunction(limMin, limMax)
        
def DSsignalPlot(signal, show = True, noFig=1,
               size=5, color='b', marker='o', 
               resetXlim = True, resetYlim = True, screen=True, figSize=None):
    "To plot a digital signal values versus time"
    time   = signal.timeValues()
    signal = signal.sigValues()
    if figSize != None:
        fig = plt.figure(noFig, figsize=figSize)
    else:
        fig = plt.figure(noFig)
    if screen == True: plt.title("Time Domain")
    setPlotLimits(time  , plt.xlim, resetXlim)
    setPlotLimits(signal, plt.ylim, resetYlim)
    plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%+2.1f'))
    plt.plot(time, signal,
             linewidth=0.0, # do not draw the line
             marker=marker, markersize = size,
             markeredgecolor=color, markerfacecolor=color)
    plt.vlines(time,[0],signal,colors=color)
    plt.ylabel("Signal Values")
    plt.xlabel("Time (s)")
    plt.grid(True,linewidth=1.1)
    if show: plt.show()
    return fig

def DSspectrumPlot(signal, show = True, noFig=2,
                 size=5, color='b', marker='o',
                 resetYlim = True, screen=True,  figSize=None):
    "To plot the module of the Fourier transform of the signal"
    freq = signal.frequencies()
    def ds(v): return 2*abs(v)
    vds = map(ds, signal.FTValues())
    yMin, yMax = 0, max(vds)
    yOffset = (yMax-yMin)*0.1        
    if figSize != None:
        fig = plt.figure(noFig, figsize=figSize)
    else:
        fig = plt.figure(noFig)            
    if screen == True: plt.title("Frequency Domain")
    plt.xlim(-0.8*signal.deltaF(), 0.5*signal.samplingFreq() + 0.8*signal.deltaF())
    setPlotLimits(vds, plt.ylim, resetYlim, setMinNull=True)
    plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%+3.2f'))
    plt.plot(freq,vds,
             linewidth=0.0, # do not draw the line
             marker=marker, markersize = size,
             markeredgecolor=color, markerfacecolor=color)
    plt.vlines(freq,[0],vds,colors=color)
    plt.ylabel("Spectral Density")
    plt.xlabel("Frequency (Hz)")
    plt.grid(True,linewidth=1.1)
    if show: plt.show()
    return fig
