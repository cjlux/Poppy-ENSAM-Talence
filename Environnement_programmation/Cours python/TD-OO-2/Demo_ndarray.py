# -*- coding: utf-8 -*-
from numpy import ndarray
t1 = ndarray( (2, 3) , 'int')
print u"Tableau brut :\n", t1

t1.fill(0) # remplissage avec une valeur
print u"\nTableau initialisé :\n", t1

t1[0] = [1,2,3] # modification de la première ligne de t1
print u"\nTableau modifié :\n", t1

t2 = t1 # copie par référence
t2[:,-1] = [-4,-5] # modification de la dernière colonne de t2
t2[-1,0:2] = [3, 4] # deux premiers termes de la dernière ligne
print u"\nTableau t1 après modification de t2 :\n", t1

t3 = t1.copy() # copie par valeurs
t3.fill(-2)
print u"\nTableau t1 après modification de t3 :\n", t1
print u"... et tableau t3 :\n", t3

print u"\n---\nOpération de transposition..."
print u"Tableau t2 transposé :\n", t2.transpose()
print u"Tableau t2 :\n", t2 # t2 n'est pas modifié par t2.transpose()
t2 = t2.transpose() # ici, oui
print u"Tableau t1 :\n", t1
print u"Tableau t2 :\n", t2
print u"Tableau t3 :\n", t3
print u"\n########",
print u"On peut continuer à tester directement dans le shell",
print u"########"
