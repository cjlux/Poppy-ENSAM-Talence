# -*- coding: utf-8 -*-

# Chargement de la classe PtGraph
from PtGraph_plus import PtGraph

# Six instanciations de la classe 'PtGraph'

pt1 = PtGraph("A",[1.,-2.5],"o")
pt1.setColors('blue','cyan')

pt2 = PtGraph("B",[-0.3,-1.25],"+")
pt2.setColors('green')

pt3 = PtGraph("C",[-1.6,1.32],"x")
pt3.setColors('magenta')

pt4 = PtGraph("D",[1.6,1.1],"*")
pt4.setColors('maroon')

pt5 = PtGraph("a",marker="s")
pt5.setColors('blue')

pt6 = PtGraph("b",[1.2,-1.0])
pt6.setColors('red')

print u"nombre de points graphiques créés :", PtGraph.nb()

PtGraph.plotAll(True)

# Remarque : pour les types de marqueurs, voir
# http://matplotlib.org/api/markers_api.html#module-matplotlib.markers
