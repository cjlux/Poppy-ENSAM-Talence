# -*- coding: utf-8 -*-
import time as t
from numpy import mean
import matplotlib.pyplot as plt
from math import factorial

# fonction n! (ne pas dépasser n=950 pb limite de récursivité)
def Factorielle(n):
    s=1
    for i in range(1,n):
        s*=i
    return s

# Permutation aleatoire de n elements ou bien crée une liste aléatoire
# de nombres de 0 à n-1.
# NB : Bijection de [[0,n!-1]] dans les permutations de n éléments
# num dans [[0,n!-1]] et détermine entièrement la permutation de sortie
# (ne pas dépasser n=950 pb limite de récursivité)
# Comportement optimal pour n <= 320 environ
def PermutationIndices(num,n,L=None,f=None):
    if L==None:
        L=range(n)
    if f==None:
        f=Factorielle(n-1)
    if n==1:
        return L
    else:
        l=[]
        l+=L[1:]
        q=num//f
        if 1 <= q:
            l[q-1]=L[0]
        return [L[q]]+PermutationIndices(num%f,n-1,l,f/(n-1))
        
# Main
if __name__=='__main__':
    nbEchantillons=300
    m=300
    ln=[]
    lt=[]
    lt2=[]
    for n in range(10,m+1,1):
        ln.append(n)
        l=[]
        for j in range(nbEchantillons):
            d=t.time()
            Factorielle(n)
            l.append(t.time()-d)
        lt.append(mean(l))
        l=[]
        for j in range(nbEchantillons):
            d=t.time()
            factorial(n)
            l.append(t.time()-d)
        lt2.append(mean(l))
    
    plt.figure()
    
    plt.subplots_adjust(hspace=0.5)
    plt.title("Execution time of PermutationIdices(n) versus 'n'")
    plt.grid(True)
    plt.xlabel('Time [s]')
    plt.ylabel('n', color ='b')
    plt.xlim(0.,m)
    plt.ylim(0.,5e-4)
    plt.plot(ln,lt,'o-b')
    
    plt.twinx()
    plt.ylim(0.,5.e-4)
    plt.xlim(0.,m)
    plt.ylabel('Math module n!',color='r')
    plt.plot(ln,lt2,'x-r')
    
    plt.show()
    