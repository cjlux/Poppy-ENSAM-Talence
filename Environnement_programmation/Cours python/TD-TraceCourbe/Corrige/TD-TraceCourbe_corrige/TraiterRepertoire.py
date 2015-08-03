# -*- coding: utf-8 -*-

#########################################
# Traitement TCD d'un répertoire entier #
#########################################
def TraiterRepertoire(repName, ecran=False):
    u""" Traitement de tous les fichiers de données se trouvant dans le
         sous-répertoire "Essais" du répertoire donné par 'repName'."""
    import os
    from TraiterTCD import LireFichierTCD, TracerTCD

    # Si le répertoire 'Essais' existe, lister ses fichiers *.txt :
    Ldir = os.listdir(repName)
    if 'Essais' in Ldir :
        dirEssais = os.listdir(repName+'/Essais')
        Ld = []
        for f in dirEssais :
            if f[-4:] == ".txt" :
                Ld.append(f)
    nbf = len(Ld)

    # Si on a trouvé des fichiers *.txt dans Essais,
    # créer le répertoire 'Courbes' s'il n'existe pas:
    if nbf > 0 :
        if 'Courbes' not in Ldir :
            print u"Création du répertoire 'Courbes'"
            os.mkdir(repName+'/Courbes')

    # Boucle sur tous les essais
    for f in Ld :
        print "Traitement du fichier ", f
        LT, LC, LD = LireFichierTCD(repName+'/Essais/'+f)
        if ecran == False :
            TracerTCD(LT, LC, LD, repName+'/Courbes/'+f[:-4]+'.png')
        else :            
            TracerTCD(LT, LC, LD)

if __name__=='__main__' :

    # test de la fonction TraiterRepertoire :
    TraiterRepertoire('ResultatsTraction')
