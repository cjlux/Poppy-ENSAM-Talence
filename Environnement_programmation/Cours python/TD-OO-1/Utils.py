# -*- coding: utf-8 -*-

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#  Chargement des modules nécessaires (bibliothèques)         #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
from matplotlib.pyplot import figure, plot, subplot, axis, show

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Utilitaire de réglage automatique de la plage d'affichage (methode générale)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def setAutoRange( nofig=1, margin=10.0, aspectRatio = 0.77 ) :
    u"Réglage automatique de la plage d'affichage"
    
    print u"Ajustement de la plage d'affichage de la figure %d :" % nofig
    coefZoom = 1.0 + 0.02*margin
    figure(nofig)    
    xmin, xmax = subplot(111).get_xlim()
    ymin, ymax = subplot(111).get_ylim()
    print u'\tPlage automatique :[[%.2f,%.2f],[%.2f,%.2f]]' % (xmin,xmax,ymin,ymax)
    ratio = aspectRatio*(xmax-xmin)/(ymax-ymin)
    if ratio < 1 :
        cy = coefZoom
        cx = coefZoom/ratio
    else :
        cx = coefZoom
        cy = coefZoom*ratio
    ax = 0.5*(1.0+cx)
    bx = 1.0 - ax
    ay = 0.5*(1.0+cy)
    by = 1.0 - ay
    axis([ax*xmin+bx*xmax, bx*xmin+ax*xmax, ay*ymin+by*ymax, by*ymin+ay*ymax])    
    xmin, xmax = subplot(111).get_xlim()
    ymin, ymax = subplot(111).get_ylim()
    print u'\tPlage ajustée     :[[%.2f,%.2f],[%.2f,%.2f]]' % (xmin,xmax,ymin,ymax)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Utilitaire de contrôle (méthode générale)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def ref(obj) :
    return u"Instanciation de la classe '%s' à l'adresse <%s>'" %\
                   (obj.__class__.__name__,hex(id(obj)))
