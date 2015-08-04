# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:42:24 2015

@author: Xavier MARIOT
@contact: xavier.mariot@gadz.org
"""

import numpy as np
from scipy.stats import threshold


"""     --- Description jacobian ---

jacobian calcul la jacobienn de la fonction vectorielle f au point q.
nb_q est le nombre de paramètres que prend f c.à.d. la longueur de la liste q
On peut régler le pas utilisé pour calculer la dérivée grâce au paramètre h.
La dérivée est calculée par la méthode des acroissements finis.
jacobian retourne une matrice de type numpy.matrix
        --- Fin description ---
"""
def jacobian(f,nb_q,q,h=0.01):
    """     === Description des arguments ===
    f       --->    Fonction de cinématique directe qui retourne un numpy.array
    nb_q    --->    'int' qui indique le nombre de paramétres de f contenu dans q
    q       --->    valeurs numériques du point auquel est calculé la jacobienne de f, q est au format numpy.array
    h       --->    Valeur du pas de calcul de la dérivée avec la formule des acroissements finis
    
            === Fin description ===
    """
    # On vérifie que q est bien un numpy.array sous forme de liste et non de tableau
    if len(q) != nb_q:
        return False
    
    # On définit le vecteur infinitésimal dh qui vont servir au calcul de J
    dh = np.array([])
    for i in range(nb_q) :
        dh = np.append(dh,0)
    
    # On calcule la jacobienne colonne par colonne c.à.d. chaque vecteur df/dqi en q
    # NB : pour des raisons pratiques on enregistre ces vecteurs en ligne, on transpose ensuite pour obtenir j
    j = []
    for i in range(nb_q):
        dh[i] = h  # On donne la valeur dh à la ième composante du vecteur dh
        j.append(1/h*(f(q+dh)-f(q))) # On calcule df/dqi par la formule des accroissements finis
        dh[i] = 0 # On remet la ième composante de dh à zéro pour la suite
    
    j = np.matrix(j) # On transforme j en matrice, pour l'instant on a en fait la transposée de la jacobienne de f en q
    j = threshold(j.T,1e-13) # On obtient la jacobienne en tronquant les zéros numériques
    
    return np.matrix(j)

"""     --- Description ik_num ---

ik_num pour 'inverse kinematic numeric' est la fonction de cinématique inverse numérique qui
retourne la liste de valeurs des nb_q paramètres d'entére de f qui permettent
d'obtenir la position xfinal en sortie.

        --- Fin de la description ---
"""
def ik_num(f, nb_q, map_qinit, xfinal, it=1, imax=10):
    """     === Descriptions des arguments ===
    
    f           --->    'arg: nd.array 1D; return: nd.array 1D' fonction vectorielle représentative du modèle de cinématique direct
    nb_q        --->    'int' qui représente le nombre de paramètres d'entrée que prend la fonction f, 
                    c.à.d. la taille de la liste q.
    map_qinit   --->    'numpy.array 2D' mapping de l'ensemble des positions initiales utilisées pour démmarrer l'algorithme
    xfinal      --->    'numpy.array 1D' résultat final visé pour le modèle de cinématiue directe
    it          -->     'float' tolérence admise entre le résultat retourné et la position finale souhaitée (norme de la différence)
    imax        --->    'int' nombre maximal d'itérations à partir duquel l'algorithme s'arrête.
    
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
    delta_x = xfinal-xinit # calcul du vecteur déplacement total.
    nb_div = np.floor(np.linalg.norm(delta_x)/(5*it)) + 1 # l'unité de découpage est arbitrairement 5*it
    if nb_div > 1:
        dx = (1/float(nb_div))*delta_x
    
    xf=[] # xf sera la liste des points intermédiaires à atteindre.
    for i in range(nb_div + 1): # on crée la liste des points intermédiaires
        xf.append(xinit + i*dx)
    
    xf[-1] = xfinal # On s'assure que la dernière valeur ne sera pas altérée par des erreurs de calcul
    
    """ Application de la méthode de jacobi pour chaque trajet intermédiaire """
    for xi in xf:
        for i in range(imax):
            # calcul de dx à l'itération considérée
            dx = xi-xinit
            dx = np.matrix(dx)
            dx = dx.T # dx est maintenant un vecteur colonne qui va pouvoir être mutiplié par une matrice
            
            # Calcul numérique de la jacobienne j au point considéré
            j = jacobian(f,nb_q,qinit,it/10000.)
            
            
            # incrémentation de qinit au point considéré
            # NB : j.I retourne la pseudo inverse de j
            qinit = qinit + (j.I*dx).T.getA()[0]
            
            # mise à jour de xinit
            xinit = f(qinit)
            
            # vérification de la condition d'arrêt
            if np.linalg.norm(xi-xinit) <= it :
                break
            # si la condition d'arrêt n'est pas vérifiée, on itère le calcul jusqu'à imax fois 
    
    # A la sortie de la méthode de jacobi, qinit vérifie ||xfinal - f(qinit)|| <= it
    return qinit

"""     --- Définition de dk_l_hand    ---

dk_l_hand pour 'direct kinematic left hand' représente la fonction de cinématique directe
qui retourne sous la forme d'un 'numpy.array 1D' la position x,y,z de la main gauche de poppy
avec pour origine (0,0,0) le centre du servomoteur de l'épaule (l_shoulder_y) cf. schema de la doc
elle prend comme argument un 'numpy.array 1D' noté q qui contient les angles des 4 servomoteurs
du bras gauche dans l'ordre suivant : q=[l_shoulder_y, l_shoulder_x, l_arm_z, l_elbow_y].
Les zéros de chaque angles et les sens positifs sont définis à partir de la config par défaut de poppy
voir shéma cinématique du bras gauche dans la doc pour leur représentation.

"""
def dk_l_hand(q=np.array([0,0,0,0])):
    

if __name__=='__main':
    
