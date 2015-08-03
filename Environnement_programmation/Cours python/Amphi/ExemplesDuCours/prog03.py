def P(t):
    r = 2.3*t**4-3.4*t**3-2.1*t**2+1.2*t+2
    return r
def PrintP(d):
    print "P(", d, ") = ", P(d)
    return
lx = [-1.2,3.2,1.0]
ly = [ P(x) for x in lx ] # 'Comprehension list'
print lx, "->", ly
map(PrintP,lx) # comme avec Mathematica
    
