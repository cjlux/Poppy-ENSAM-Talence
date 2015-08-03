# -*- coding: utf-8 -*-
#Q1
x=1.4e-3
i=154
s='jeudi'
print 'x = ',x,'; i = ',i,'; s = ',s

#Q2
L1=range(11)
print L1,len(L1)
print L1[0],L1[len(L1)-1]
print L1[2:len(L1)-1]

#Q3
import math as m
print m.pi," -> ",m.cos(m.pi)
print m.sqrt(3.)

#Q4
help(m.radians)
print m.sin(m.radians(30))
print m.cos(m.radians(45))==0.05*m.sqrt(2)
print m.cos(m.pi/4)**2+m.sin(m.pi/4)**2

#Q5
S1="My tailor is rich"
print S1
S2=S1.upper()
print S2
S3=S1+S2
print S3
print S1.split()

#Q6
for i in S1:
    print i
s=0
for i in L1:
    s+=i**2
print s

#Q7
def scale(a,b):
    return a*b
print scale(10,2)
def scale(a,b=1):
    return a*b
print scale(10)==10

#Q8
y=0
y=input("Entrer un nombre ")
print type(y)
y=float(y)
print type(y),"; y = ",y
n = input(u"Entrer un nombre dont le carré vaut 25 ")
while n!=5:
    n = input(u"Entrer un nombre dont le carré vaut n ")
print "nombre correct"


