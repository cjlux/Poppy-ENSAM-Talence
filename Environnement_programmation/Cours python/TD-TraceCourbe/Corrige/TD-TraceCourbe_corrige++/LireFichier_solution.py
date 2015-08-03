# -*- coding: utf-8 -*-

# importation du module pyplot sous le nom "plt"
import matplotlib.pyplot as plt

#######################################
# Lecture du fichier ligne par ligne  #
# et importation des données          #
#######################################
dataFile="data001.txt"
time, stress, strain = [], [], []
f = open(dataFile, 'r')
for line in f:
    if line[0].isdigit():
        t, c, d = map(float, line.split())
        time.append(t)
        stress.append(c*1.e-6) # conversion en MPa
        strain.append(d)
f.close()


###########################
# Création des graphiques #
###########################
# Graphe stress, strain versus time
plt.figure()
plt.subplot(211)    # 2 lignes, une colonne, graphique no.1
plt.subplots_adjust(hspace=0.5)
plt.title("Stress, strain versus time")
plt.grid(True)
plt.xlabel('time [s]')
plt.xlim(0.,2.3)
plt.ylabel('Stress [MPa]',color='b')
plt.ylim(0.,50)
plt.plot(time,stress,'x-b')

plt.twinx()
plt.xlim(0.,2.3)
plt.ylim(0.,10.e-3)
plt.ylabel('strain',color='r')
plt.plot(time,strain,'o-r')

# Graphe stress versus strain
plt.subplot(212)    # 2 lignes, une colonne, graphique no.2
plt.title("Stress vs. Strain", color='g')
plt.grid(True)
plt.xlabel('Strain')
plt.xlim(0.,6.e-3)
plt.ylabel('Stress [MPa]')
plt.ylim(0.,40)
plt.plot(strain,stress,'x-g')

# tracé des courbes dans un fichier image :
imageFile = dataFile.replace(".txt", ".png")
plt.savefig(imageFile)

# Affichage des courbes dans une fenêtre écran.
# A faire imperativement en dernier, sinon
# on enregistre une image vide :
plt.show()
