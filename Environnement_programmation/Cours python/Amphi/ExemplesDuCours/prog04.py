def P(t):
    r = 2.3*t**4-3.4*t**3-2.1*t**2+1.2*t+2
    return r
def PrintP(d):
    print "P(", d, ") = ", P(d)
    return
while True :
    s = raw_input("Entrer la valeur de x ('q' pour quitter): ")
    if s == 'q' :
        break
    else :
        try :
            x = float(s)
            PrintP(x)
        except :
            print "Valeur '",s,"'incorrecte. Recommencer."
            continue
