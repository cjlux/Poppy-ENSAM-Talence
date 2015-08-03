# -*- coding: utf-8 -*-
# -*- Simulation Experience Tirage de type Bernoulli

from numpy.random import uniform
from numpy.random import randint

def TirageBernoulli(p):
    if uniform() <= p :
        return 1
    else :
        return 0
    
# -*- Simulation Experience Tirage de type géométrique
def TirageLoiGeometrique1(p):
    n=1
    while TirageBernoulli(p)==0:
        n+=1
    return n

# somme
def Sum(L):
    s=0
    for i in range(len(L)):
        s+=L[i]
    return s

# moyenne d'une liste
def Moy(L):
    return Sum(L)/len(L)

# Simulation loi discrete

def SimulationLoiDiscrete(L):
    r=uniform()
    i=0
    s=L[0][1]
    while r>s :
        i+=1
        s+=L[i][1]
    return L[i][0]

# Factorielle

def Factorielle(n):
    if n>1:
        return n*Factorielle(n-1)
    else:
        return 1

# Permutation aleatoire de n elements ou créé une liste aléatoire
# de nombres de 0 à n-1.
# NB : Bijection de [[0,n!-1]] dans les permutations de n éléments
# num dans [[0,n!-1]] et détermine entièrement la permutation de sortie
def PermutationIndices(num,n,L=None):
    if L==None:
        L=range(n)
    f=Factorielle(n-1)
    if n==1:
        return L
    else:
        l=[]
        l+=L[1:]
        q=num//f
        if 1 <= q:
            l[q-1]=L[0]
        return [L[q]]+PermutationIndices(num%f,n-1,l)

# génération d'une table aléatoire proba discrette de n cas possibles
def TableDiscret(n,l=None):
    l=PermutationIndices(randint(Factorielle(n)),n,l)
    L=[]
    p=1
    for i in l[:-1]:
        r=uniform(0,p)
        L.append([i,r])
        p-=r
    L.append([l[-1],p])
    return L


# Loi discrète
def LoiDiscrete(L):
    r=uniform()
    i=0
    s=L[0][1]
    while r>s and i<= len(L):
        i+=1
        s+=L[i][1]
    return L[i][0]

# Main
#L=TableDiscret(10)
#for i in L:
#    print i
#print LoiDiscrete(L)
#Ech=[]
#for i in range(50):
#    Ech.append(LoiDiscrete(L))
#print Ech
#l=[]
#for i in range(len(L)):
#    l.append(L[i][1])
#print 'somme probas = ',Sum(l)

n=4
print PermutationIndices(randint(Factorielle(n)),n)

