# -*- coding: utf-8 -*-

#########################################
# Traitement TCD d'un répertoire entier #
#########################################
def TraiterRepertoire(repName, memoriserEnPNG=True):
    u""" Traitement de tous les fichiers de données se trouvant dans le
         sous-répertoire "Essais" du répertoire donné par 'repName'."""
    import os
    from TraiterTCD import LireFichierTCD, TracerTCD, CalculerW, EcrireFichierTCDW
    from TraiterTCD import Maintenant

    print u"Début de l'exécution de la fonction 'TraiterRepertoire' pour le répertoire :",repName
    print Maintenant()

    try : Ldir = os.listdir(repName)
    except : 
        print u'Erreur : Le répertoire '+repName+" n'existe pas"
        print u"Fin de l'exécution du programme 'TraiterRepertoire'"
        print Maintenant()
        return
    
    if 'Essais' not in Ldir :
        print u'Erreur : Le répertoire '+repName+' ne contient pas de répertoire "Essais"'
        print u"Fin de l'execution du programme 'TraiterRepertoire'"
        print Maintenant()
        return

    # Fichiers d'essais :
    lfn = os.listdir(repName+'/Essais')
    fileNames = []
    for fn in lfn :
        if fn[-4:] == ".txt" :
            fileNames.append(fn)
    nbf = len(fileNames)
    
    if nbf > 0 :
        print u"Fichiers trouvés : ",fileNames
    else :
        print u"Erreur : aucun fichier de données présent dans "+repName+'/Essais'
        print u"Fin de l'exécution du programme 'TraiterRepertoire'"
        print Maintenant()
        return
    
    # Répertoires de sortie :
    if 'Courbes' not in Ldir :
        print u"Création du répertoire 'Courbes'"
        os.mkdir(repName+'/Courbes')

    if 'DataW' not in Ldir :
        print "Création du repertoire 'DataW'"
        os.mkdir(repName+'/DataW')

    # Barre d'avancement :
    if nbf > 2 :
        print '|',
        for i in range(nbf-2) : print '-',
        print '|' 

    # Boucle sur tous les essais :
    for fn in fileNames :
        LT, LC, LD = LireFichierTCD(repName+'/Essais/'+fn)
        if memoriserEnPNG :
            TracerTCD(LT, LC, LD, repName+'/Courbes/'+fn[:-4]+'.png')
        else :            
            TracerTCD(LT, LC, LD)
        LW = CalculerW(LC, LD)
        EcrireFichierTCDW(LT, LC, LD, LW, repName+'/DataW/'+fn[:-4]+'-W.txt')
        print ">" ,

    print "\nFin de l'execution du programme 'TraiterRepertoire'"
    print Maintenant()

####################################
# Tests incorporés dans le fichier #
####################################
if __name__=='__main__' :  
    TraiterRepertoire('ResultatsTraction')
