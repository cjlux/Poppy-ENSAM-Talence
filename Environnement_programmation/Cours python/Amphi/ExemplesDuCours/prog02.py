def P(t):
    r = 2.3*t**4-3.4*t**3-2.1*t**2+1.2*t+2
    return r
def PrintP(d):
    print "P(", d, ") = ", P(d)
    return
for x in [-1.2,3.2,1.0]: # x parcourt la liste [-1.2,3.2,1.0]
    PrintP(x)
