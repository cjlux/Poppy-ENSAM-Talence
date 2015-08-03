# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:42:24 2015

@author: poppy
"""

import numpy as np


"""     --- Description jacobienne ---

jacobienne calcul la jacobienn de la fonction vectorielle f au point q.
nb_q est le nombre de paramètres que prend f c.à.d. la longueur de la liste q
On peut régler le pas utilisé pour calculer la dérivée grâce au paramètre h.
La dérivée est calculée par la méthode des acroissements finis.
jacobienne retourne une matrice.
        --- Fin description ---
"""
def jacobienne(f,nb_q,q,h=0.01):
    
    
    return j

"""     --- Description ik_num ---

ik_num est la fonction de cinématique inverse entièrement numérique
elle retourne la liste de valeurs des nb_q paramètres d'entére de f qui permettent
d'obtenir la position xfinal en sortie.

        --- Fin de la description ---
"""
def ik_num(f, nb_q, map_qinit,  xfinal, it=1, imax=10):
    """     === Descriptions des arguments ===
    
    -> f est la fonction vectorielle représentative du modèle de cinématique direct
    -> nb_q est le nombre de paramètres d'entrée que prend la fonction f, 
        c.à.d. la taille de la liste q.
    -> map_qinit est le mapping de l'ensemble des positions initiales utilisées pour démmarrer l'algorithme
    -> xfinal est le résultat final visé pour le modèle de cinématiue directe
    -> it est la tolérence admise entre le résultat retourné et la position finale souhaitée
    -> imax est le nombre maximal d'itérations à partir duquel l'algorithme s'arrête.
    
            === Fin de la description ===
    """
    
    
    
    """ détermination du mapping xinit """
    map_xinit = map(f,map_qinit)
    
    """ détermination du point de départ de l'algorithme """
    imin = 0 # index de la position x qui engendre une distance minimale ||x-xfinal||
    dxmin = np.linalg.norm(xfinal-map_xinit[0]) 
    for i in range(len(map_xinit)): # On parcourt l'ensemble des position du mapping
        dx = np.linalg.norm(xfinal-map_xinit[i])
        
        # On enregistre l'index minimal et la distance minimale si on trouve une distance inférieure 
        # à celles enregistrées précédemment.
        if dx < dxmin : 
            dxmin = dx
            imin = i
    
    # On fixe la position initiale à partir de la plus petite distance trouvée.
    qinit = map_qinit[imin]
    xinit = map_xinit[imin]
    
    """ Décoposition du trajet entre xinit et xfinal en plusieurs petits déplacements """
    delta_x = xfinal-xinit
    nb_div = np.floor(np.linalg.norm(delta_x)/(5*it)) + 1 # l'unité de découpage est arbitrairement 5*it
    if nb_div > 1:
        dx = delta_x / nb_div
    
    xf=[] # xf sera la liste des points intermédiaires à atteindre.
    for i in range(nb_div + 1): # on crée la liste des points intermédiaires
        xf.append(xinit + i*dx)
    
    xf[-1] = xfinal # On s'assure que la dernière valeur ne sera pas altérée par des erreurs de calcul
    
    """ Application de la méthode de jacobi pour chaque trajet intermédiaire """
    for xi in xf:
        for i in range(imax):
            # calcul de dx à l'itération considérée
            dx = xi-xinit
            
            # Calcul numérique de la jacobienne j au point considéré
            j = jacobienne(f,nb_q,qinit)
            
            # calcul de la pseudo inverse de j, notée j_plus, au point considéré
            j_plus = np.linalg.pinv(j)
            
            # incrémentation de qinit au point considéré
            qinit = qinit + j_plus*dx
            
            # mise à jour de xinit
            xinit = f(qinit)
            
            # vérification de la condition d'arrêt
            if np.linalg.norm(xi-xinit) <= it :
                break
            # si la condition d'arrêt n'est pas vérifiée, on itère le calcul jusqu'à imax fois 
    # A la sortie de la méthode de jacobi, qinit vérifie ||xfinal - f(qinit)|| <= it
    
    return qinit



if __name__=='__main':
    
