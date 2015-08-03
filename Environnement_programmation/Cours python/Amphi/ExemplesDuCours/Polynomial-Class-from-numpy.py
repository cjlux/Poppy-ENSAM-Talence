# -*- coding: utf-8 -*-
from numpy.polynomial import Polynomial
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.polynomial.polynomial.Polynomial.html

p = Polynomial([ 2.5, -2.5, 1.0, -2.0, 1.0 ])
print u"\tPolynôme p :", p
def prt(z,ndec=3) :
    myfrmt = "\t\t\t({0.real:."+str(ndec)+"f} + {0.imag:."+str(ndec)+"f}*i)"
    print myfrmt.format(z)
    return
print u"\t\tde racines :"
map(prt, p.roots())
q = Polynomial([ 0.5*n for n in range(6) ])
print u"\tPolynôme q :", q
print u"\t\tde racines :"
map(lambda z : prt(z,4), q.roots())
print u"\tPolynôme dérivé q' :", q.deriv()
