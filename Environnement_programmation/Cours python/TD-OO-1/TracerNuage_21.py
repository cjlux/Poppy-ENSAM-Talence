# -*- coding: utf-8 -*-

# Chargement des modules et fonctions utiles
from matplotlib.pyplot import figure, plot, show, axis

# Chargement de la classe PtGeom
from PtGeom import PtGeom

cpt = PtGeom([1.6,0])

figure()
for k in range(24):
    cpt.setTheta(15.0*k)
    plot([cpt.getX()],[cpt.getY()], marker='*', markersize=k+7)

axis('equal')
show()

# Remarque : pour les types de marqueurs, voir
# http://matplotlib.org/api/markers_api.html#module-matplotlib.markers
