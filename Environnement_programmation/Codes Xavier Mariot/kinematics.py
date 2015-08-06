# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:42:24 2015

@author: Xavier MARIOT
@contact: xavier.mariot@gadz.org
"""

import numpy as np
import math


"""     --- Description jacobian ---

jacobian calcul la jacobienne de la fonction vectorielle f au point q.
nb_q est le nombre de paramètres que prend f c.à.d. la longueur de la liste q
On peut régler le pas utilisé pour calculer la dérivée grâce au paramètre h.
La dérivée est calculée par la méthode des acroissements finis.
jacobian retourne une matrice de type numpy.matrix
        --- Fin description ---
"""
def jacobian(f,nb_q,q,h=0.001):
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
    
    j = np.matrix(j) # On transforme j en matrice, pour l'instant on a en stocké la transposée de la jacobienne de f en q
    
    return j.T


"""     === Description ik_num_base ===

Cette fonction est l'algorithme de cinématique inverse pour des petits déplacements
autour d'une position initiale. La position initiale est donnée par le paramètre qi.
Le petit déplacement par rapport à la position xi=f(qi) est noté dxf.
La position finale visée vaut xf = xi + dxf


"""    
def ik_num_base(f, nb_q, qi, dxf, it=1, imax=10):
    """     === Descriptions des arguments ===
    
    f           --->    'arg: nd.array 1D; return: nd.array 1D' fonction vectorielle représentative du modèle de cinématique directe
    nb_q        --->    'int' qui représente le nombre de paramètres d'entrée que prend la fonction f, 
                    c.à.d. la taille de la liste q.
    qi          --->    'numpy.array 1D' position initiale du système
    dxf         --->    'numpy.array 1D' déplacement infinitésimal du système par rapport à sa position initale
    it          -->     'float' tolérence admise entre le résultat retourné et la position finale souhaitée (norme de la différence)
    imax        --->    'int' nombre maximal d'itérations à partir duquel l'algorithme de Jacobi s'arrête.
    
            === Fin de la description ===
    """    
    
    """     --- Initialisation ---      """
    q = qi # on initialise la valeur des paramètres q
    x = f(q) # on enregistre la position initiale du système
    
    xf = x + dxf # on calcule la position finale à atteindre
    dx = dxf # on initialise la variation à effectuer pour se rapprocher de la position finale
    
    
    """     --- Recurrence ---      """
    for i in range(imax):
        # Calcul du nouveau dx au format 'numpy.array 1D'
        dx = xf-x
        
        # vérification de la condition d'arrêt
        if np.linalg.norm(dx) <= it :
           break
        else:
            # mise en forme de dx à l'itération considérée
            dx = np.matrix(dx)
            dx = dx.T # dx est maintenant un vecteur colonne qui va pouvoir être mutiplié par une matrice
            
            # Calcul numérique de la jacobienne j au point considéré
            j = jacobian(f,nb_q,q,1e-6)
            
            
            # incrémentation de q au point considéré en gardant le type 'numpy.array 1D'
            # NB : j.I retourne la pseudo inverse de j
            q = q + (j.I*dx).T.getA()[0]
            
            
            # mise à jour de x
            x = f(q)
        
        # si la condition d'arrêt n'est pas vérifiée, on itère le calcul jusqu'à imax fois
    
    # A la sortie de la méthode de jacobi, q vérifie ||xfinal - f(q)|| <= it
    return q


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
    q = map_qinit[imin]
    x = map_xinit[imin]
    
    
    """ Décoposition du trajet entre xinit et xfinal en plusieurs petits déplacements """
    
    delta_x = xfinal-x # calcul du vecteur déplacement total.
    
    # l'unité de découpage est arbitrairement 5*it
    nb_div = int(np.floor(np.linalg.norm(delta_x)/(10*it)) + 1)
    
    
    if nb_div > 1:
        dx = (1/float(nb_div))*delta_x
    
    xf=[] # xf sera la liste des points intermédiaires à atteindre.
    for i in range(nb_div + 1): # on crée la liste des points intermédiaires
        xf.append(x + i*dx)
    
    xf[-1] = xfinal # On s'assure que la dernière valeur ne sera pas altérée par des erreurs de calcul
    xf.pop(0) # On retire la position intiale
    
    
    """ Application de la méthode de jacobi pour chaque trajet intermédiaire avec ik_num_base """
    
    for xi in xf:
        # le petit déplacement vaut la différence entre la position finale intermédiare visée et la position théorique actuelle
        dx = xi-f(q)
        
        # Calcul de la nouvelle valeur de q par la méthode de Jacobi pour les petits déplacements
        q = ik_num_base(f, nb_q, q, dx, it, imax)
    
    # A la sortie de la méthode de jacobi, qi vérifie ||xfinal - f(q)|| <= it
    return q


"""     --- Définition de dk_l_hand    ---

dk_l_hand pour 'direct kinematic left hand' représente la fonction de cinématique directe
qui retourne sous la forme d'un 'numpy.array 1D' la position x,y,z de la main gauche de poppy
avec pour origine (0,0,0) le centre du servomoteur de l'épaule (l_shoulder_y) cf. schema de la doc
elle prend comme argument un 'numpy.array 1D' noté q qui contient les angles des 4 servomoteurs
du bras gauche dans l'ordre suivant : q=[l_shoulder_y, l_shoulder_x, l_arm_z, l_elbow_y].
Les zéros de chaque angles et les sens positifs sont définis à partir de la config par défaut de poppy
voir shéma cinématique du bras gauche dans la doc pour leur représentation.
voir 'cinematique directe.nb' pour le calcul de la formule de x, y et z

"""
def dk_l_hand(q=np.array([0,0,0,0])):
    ab = 30
    bc = 30
    cd = 70
    de = 90
    
    x = -bc*np.cos(q[1])*np.sin(q[0]) - cd*np.cos(q[1])*np.sin(q[0]) - de*(np.cos(q[1])*np.cos(q[3])*np.sin(q[0]) + (np.cos(q[0])*np.cos(q[2]) + np.sin(q[0])*np.sin(q[1])*np.sin(q[2]))*np.sin(q[3]))
    y = ab + bc*np.sin(q[1]) + cd*np.sin(q[1]) - de*(-np.cos(q[3])*np.sin(q[1]) + np.cos(q[1])*np.sin(q[2])*np.sin(q[3]))
    z = -bc*np.cos(q[0])*np.cos(q[1]) - cd*np.cos(q[0])*np.cos(q[1]) - de*(np.cos(q[0])*np.cos(q[1])*np.cos(q[3]) + (-np.cos(q[2])*np.sin(q[0]) + np.cos(q[0])*np.sin(q[1])*np.sin(q[2]))*np.sin(q[3]))
    
    return np.array([x,y,z])

mapping_dk_l_hand = np.array()

if __name__=='__main__':
    
    
    qinit = np.array(map(math.radians,[1,45,1,-85]))
    print "mapping = ", qinit
    
    dx = np.array([10,20,10])
    xi = dk_l_hand(qinit)
    xfinal = xi + dx
    
    print "xinit th = ",xi
    print "xfinal th = ",xfinal
    
    print "\n\n"
    
    qf = ik_num(dk_l_hand,4,np.array([qinit,[0,0,0,0]]),xfinal)
    
    print "xfinal calc = ",dk_l_hand(qf)
    print "\n\n"
    
    qf = map(math.degrees,qf)
    
    print "qf en degree = ",qf
     
    