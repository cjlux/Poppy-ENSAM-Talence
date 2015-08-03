class DiscreteTime:
    """
    This class models the concept of 'discrete time',
    useful for digital signal design.
    """
    def __init__(self, n, step =1.0, start =0.0):
        self.__to = start         # time origin
        self.__dt = step          # time step
        self.__nb = n             # number of discrete values
        
    # access methods to read attributes (getters)
    def start(self): return self.__to
    def step(self):  return self.__dt
    def nbVal(self): return self.__nb    
    
    # access methods to write attributs (setters)
    def setPeriod(self, newStep): self.__dt = newStep

    # useful methods
    def timeValues(self):
        'returns the list of the discrete time values'
        liste = []
        to = self.__to
        for i in range(self.__nb):
            liste.append(to + i*self.__dt)
        return liste

    def t(self, i): return self.__to + (i%self.__nb)*self.__dt
    def last(self): return self.t(-1)
    def delay(self, delayVal):
        'applies a delay value to modify the start time'
        self.__to += delayVal
    
if __name__=="__main__":  
    "to test the 'DiscreteTime' class"
    t1 = DiscreteTime(5,0.1,1.0)
    print "nbValues:", t1.nbVal()
    print "start:", t1.start()
    print "step:", t1.step()
    print "values:", t1.timeValues()
    t1.delay(5.0)
    print "5s delay applied..."
    print "start:", t1.start()
    t1.setPeriod(1.0)
    print "period change applied..."
    print "values:", t1.timeValues()
    print "last:", t1.last()
    print "values (one by one):", 
    for no in range(t1.nbVal()):
        print no,"->",t1.t(no),"\n                    ",
    
    
