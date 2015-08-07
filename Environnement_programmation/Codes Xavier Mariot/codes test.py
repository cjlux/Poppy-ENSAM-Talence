# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ce script temporaire est sauvegardé ici :
/home/poppy/.spyder2/.temp.py
"""


# bibliothèques nécessaires au fonctionnement de Poppy humanoide
import pypot
from poppy.creatures import PoppyHumanoid
import kinematics as kin



# démmarrer la simulation poppy dans vrep. Il faut lancer V-rep avant d'executer le code.
poppy = PoppyHumanoid(simulator='vrep')


# Relancer la simulation
poppy.reset_simulation()


# Arrêter complètement la simulation poppy
poppy.stop_simulation()
pypot.vrep.close_all_connections()


# Affiche la liste des moteurs. Le schema de Poppy avec les moteurs est dans la doc.
print"Réponse:"
print "j'ai", len( poppy.motors ), "moteurs"
print "ils sont tous indexés dans une ", type( poppy.motors ), "qui s'appelle poppy.motors \n\n la voici: "
for m in poppy.motors:
    print "-------------"
    print "nom du moteur: ", m.name
    print "position actuelle du moteur: ", m.present_position, "degrès"
    
    
    
# Poppy dit oui
for i in range(2):
    poppy.head_y.goal_position = -20
    poppy.head_y.goal_position = +20
poppy.head_y.goal_position = 0

poppy.l_shoulder_y.goal_position = -45
poppy.l_shoulder_x.goal_position = 45
