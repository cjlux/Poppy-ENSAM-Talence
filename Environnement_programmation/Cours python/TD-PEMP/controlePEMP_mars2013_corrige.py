# -*- coding: utf-8 -*-

#################################################################
###             Centre ENSAM de Bordeaux, mars 2013           ###
###             Prise en main Python : Contrôle machine       ###
#################################################################
###
### Modalités :
### - contrôle individuel sur session Python, dans l'environnement IDLE
### - seul document autorisé : document PDF de la séance "prise en main Python" (sur la clef USB)
### - 8 thèmes de questions, 20 minutes.
###
### 1) sauvegarder ce fichier sur la clef USB (menu "File>Save As"),
###    sous le nom : "votre_nom-votre_prenom.py" (pas d'accent, pas d'espace).
### 2) Répondre aux questions dans le document.
### 3) Utiliser F5 pour exécuter ce programme et vérifier vos réponses
###    avec le shell Python.
### 4) à la fin de l'épreuve, sortir la clef USB et la remettre à l'enseignant.
###

# Q.1 - Définir la variable x égale à 0.0014, en utilisant la notation scientifique.
#     - Définir la variable entière i égale à 154.
#     - Définir la variable s chaîne de caractère égale à 'jeudi'.
#     - Faire afficher la valeur de x, i et s.      
print u"*** Réponses à la Question 1 ***"
x = 1.4e-3
i = 154
s = 'jeudi'
print "x :", x, "; i :", i, "; s :", s

# Q.2 - À l'aide de la fonction range() définir une variable L1 comme une liste 
#       contituée des nombres entiers de 0 à 10 inclus.
#     - Faire afficher L1 et la taille de L1.
#     - Faire afficher les premier et dernier éléments de L1.
#     - Faire afficher la sous-liste allant du deuxième à l'avant dernier élément de L1.
print u"*** Réponses à la Question 2 ****"
L1 = range(11)
print "L1 :", L1, "de taille", len(L1)
print L1[0], L1[-1]
print L1[1:-1]

# Q.3 - Importer le module math, avec m comme alias.
#     - Faire afficher la valeur de pi et du cosinus de pi.
#     - Faire afficher la valeur de la racine carrée de trois.
print u"*** Réponses à la Question 3 ****"
import math as m
print "pi :", m.pi
print "cos(pi) :", m.cos(m.pi)
print "sqrt(3) :",m.sqrt(3)

# Q.4 - Faire afficher l'aide sur la fonction radians du module math.
#     - Faire afficher la valeur du sinus de 30 degrés.
#     - Faire afficher le résultat du test :
#         cosinus de 45 degrés == 0.5*(racine carrée de 2).
#     - Faire afficher la valeur de :
#         (cosinus de pi/4) élévé au carré + (sinus de Pi/4) élevé au carré.
print u"*** Réponses à la Question 4 ****"
help(m.radians)
print u"sin(30°) :", m.sin(m.radians(30))
print u"cos(45°)==sqrt(2)/2 :", m.cos(m.radians(45)) == 0.5*m.sqrt(2)
print m.cos(m.pi/4)**2 + m.sin(m.pi/4)**2

# Q.5 - Définir puis afficher la variable S1, chaîne de caractère contenant "My tailor is rich".
#     - Définir puis afficher la variable S2 égale à S1 convertie en majuscules.
#     - Définir puis afficher S3 comme étant la concaténation de S1 et S2.
#     - Faire afficher la liste des mots de S1
print u"*** Réponses à la Question 5 ****"
S1 = "My tailor is rich"
print S1
S2 = S1.upper()
print S2
S3 = S1 + S2
print S3
print S1.split()

# Q.6 - Ecrire une boucle qui balaye S1 et affiche ses caractères.
#     - Ecrire une boucle qui balaye L1 et fait la somme des carrés de ses éléments.
#     - Faire afficher la valeur de la somme des carrés.
print u"*** Réponses à la Question 6 ****"
for c in S1:
    print c
som = 0
for i in L1:
    som += i*i
print som

# Q.7 - Définir la fonction scale qui retourne le produit de ses 2 arguments.
#     - Faire afficher la valeur de scale(10,2).
#     - Re-définir la fonction scale en rendant deuxième argument optionnel,
#       avec 1. comme valeur par défaut.
#     - Vérifier que scale(10) == 10 est vrai.
print u"*** Réponses à la Question 7 ****"
def scale(a, b):
    return a*b
print scale(10,2)
def scale(a, b = 1.):
    return a*b
print scale(10) == 10

# Q.8 - Faire une saisie clavier affichant le message "Entrer un nombre ",
#       et affecter la saisie à la variable y.
#     - Faire afficher le type de y.
#     - Convertir y en float, faire afficher son type et sa valeur.
#     - Faire une deuxième saisie clavier affichant le message
#       "Entrer un nombre dont le carré vaut 25 ", et affecter la saisie à la variable n.
#     - utiliser un "tant que" pour faire en sorte que l'utilisateur saisisse un nombre correct.

print u"*** Réponses à la Question 8 ****"
y = raw_input("Entrer un nombre ")
print "Type de y :", type(y)
y = float(y)
print "Type de y :", type(y), "; valeur de y :", y
n = int(raw_input(u"Entrer un nombre dont le carré vaut 25 "))
while n*n != 25:    
    print u"Carré", n*n, u"différent de 25."
    n = int(raw_input(u"Recommencer SVP "))
print u"Le carré de", n, u"est bien 25."

##############
print u"*** c'est fini ***"


     


