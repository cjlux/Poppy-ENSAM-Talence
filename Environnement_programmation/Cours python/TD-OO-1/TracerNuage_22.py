# -*- coding: utf-8 -*-

# Chargement des modules et fonctions utiles
from matplotlib.pyplot import figure, plot, show, axis

# Chargement de la classe PtGeom
from PtGeom import PtGeom

cpt = PtGeom([1.6,0])

figure()
for k in range(61):
    cpt.setTheta(12.0*k)
    cpt.setRho(1.02*cpt.getRho())
    plot([cpt.getX()],[cpt.getY()], marker='*', markersize=0.2*k+7)

for k in range(5):
    cpt.setY(cpt.getY()+1.0)
    plot([cpt.getX()],[cpt.getY()], marker='*', markersize=19.0)

for k in range(11):
    cpt.setX(cpt.getX()-1.0)
    plot([cpt.getX()],[cpt.getY()], marker='*', markersize=19.0)

axis('equal')
show()

# Remarque : pour les types de marqueurs, voir
# http://matplotlib.org/api/markers_api.html#module-matplotlib.markers
