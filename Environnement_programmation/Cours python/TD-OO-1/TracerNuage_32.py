# -*- coding: utf-8 -*-

# Chargement de fonctions
from matplotlib.pyplot import figure, plot, show, axis

# Chargement de la classe PtGeom
from PtGraph import PtGraph

# Chargement d'un utilitaire 'maison'
from Utils import setAutoRange

cpt = PtGraph("M",[1.6,0],"*")
cpt.setColors('brown','yellow')

figure()
for k in range(61):
    cpt.setTheta(12.0*k)
    cpt.setRho(1.02*cpt.getRho())
    cpt.setSize(0.2*k+7)
    cpt.plot()

for k in range(5):
    cpt.setY(cpt.getY()+1.0)
    cpt.plot()

for k in range(11):
    cpt.setX(cpt.getX()-1.0)
    cpt.plot()

setAutoRange()
show()

# Remarque : pour les types de marqueurs, voir
# http://matplotlib.org/api/markers_api.html#module-matplotlib.markers
