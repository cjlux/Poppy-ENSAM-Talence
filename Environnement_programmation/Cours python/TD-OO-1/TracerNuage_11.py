# -*- coding: utf-8 -*-

# Chargement des modules et fonctions utiles
from math import pi, cos
from cmath import exp
from random import uniform
import matplotlib.pyplot as plt

# Chargement de la classe PtGeom
from PtGeom import PtGeom

# Lpts : une liste d'instanciations de la classe 'PtGeom' avec des coordonnées
# judicieusement calculées :
r = exp( pi * 0.1j )
Lpts = []
for k in range(20) :
    z = ( 2.5 + cos( 0.5*pi*k ) ) * r**k
    x = z.real + uniform(-0.3,0.3)
    y = z.imag + uniform(-0.3,0.3)
    Lpts.append(PtGeom([x, y]))
print len(Lpts), u" objets, réalisations de la classe 'PtGeom', ont été mis dans la liste Lpts"

# liste (fermée) Lpts :
Lx = [ Lpts[-1].getX() ]
Ly = [ Lpts[-1].getY() ]
for pt in Lpts :
    Lx.append(pt.getX())
    Ly.append(pt.getY())
    
# Tracé reliant les points : 
plt.figure()      
plt.plot(Lx, Ly, color = "blue", linestyle = "solid",
         linewidth = 2.5,  marker = 'o',
         markerfacecolor = "pink",
         markeredgecolor = "magenta",
         markeredgewidth = 1.5,
         markersize = 5.5)
plt.axis('equal')   # normalisation des axes ('equal' ou 'scaled')
plt.show()          # affichage des figures

# Remarque : pour les types de marqueurs, voir
# http://matplotlib.org/api/markers_api.html#module-matplotlib.markers
