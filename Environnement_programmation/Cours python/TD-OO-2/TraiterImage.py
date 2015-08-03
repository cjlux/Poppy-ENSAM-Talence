# -*- coding: utf-8 -*-
import sys

# bibliothèque PySide
from PySide.QtGui import QApplication

# import de la classe "FenetrePrincipale"
from FenetrePrincipale import FenetrePrincipale

##########
#  MAIN   #
##########

# On crée d'abord un objet "application" pour l'environnement graphique global
#app = QApplication(sys.argv)

## Fenêtre principale : création
fenetre = FenetrePrincipale(560, 200, u"Application Python de traitement d'image")
#
# Fenêtre principale : affichage
fenetre.show();
#
## Boucle principale : système en attente d'évènement 
app.exec_()
#
## destruction des fenêtres
fenetre.destroy()
#
print u"C'est fini !"
