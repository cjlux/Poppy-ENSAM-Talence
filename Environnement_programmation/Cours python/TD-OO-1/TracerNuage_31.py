# -*- coding: utf-8 -*-

# Chargement de la classe PtGraph
from PtGraph import PtGraph

# Chargement des modules et fonctions utiles
from matplotlib.pyplot import figure, show, axis
from Utils import setAutoRange

# Six instanciations de la classe 'PtGraph'

pt1 = PtGraph("A",[1.,-2.5],"o")
pt1.setColors('blue','cyan')
pt1.plot(True)

pt2 = PtGraph("B",[-0.3,-1.25],"+")
pt2.setColors('green')
pt2.plot(True)

pt3 = PtGraph("C",[-1.6,1.32],"x")
pt3.setColors('magenta')
pt3.plot(True)

pt4 = PtGraph("D",[1.6,1.1],"*")
pt4.setColors('maroon')
pt4.plot(True)

pt5 = PtGraph("a",marker="s")
pt5.setColors('blue')
pt5.plot(True)

pt6 = PtGraph("b",(1.2,-1.0))
pt6.setColors('red')
pt6.plot(True)

setAutoRange()
show()

# Remarque : pour les types de marqueurs, voir
# http://matplotlib.org/api/markers_api.html#module-matplotlib.markers
