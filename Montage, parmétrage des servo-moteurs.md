# Montage des servomoteurs

Les servomoteurs Dynamixel MX-28T et MX-64 sont vendus partiellement montés :
[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/boite_1_contenu_face_ld.jpg" align="bottom" width="595" height="355">]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/boite_1_contenu_face_ld.jpg)  

Le montage consiste à fixer le palonnier à l'arbre moteur.
## Matériel nécessaire :
  - [ ] clef allen de 2 mm.
**Attention** Il faut aligner l'encoche sur le palonnier avec le poinçonnage sur l'arbre du servomoteur :  
[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/palonnier_ld.jpg" align="bottom" width="290" height="251" >]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/palonnier_ld.jpg)
[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/repere_et_poinconnage_ld.jpg" width="214" height="244" >]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/repere_et_poinconnage_ld.jpg)

La rondelle doit être intercalée entre le palonnier et le servomoteur :  
[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/rondelles_3.jpg" name="Image5" align="bottom" width="245" height="141" border="0" >]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/rondelles_3.jpg)

Procédure de montage : 
[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/assemblage_dynamixel_french_avec_music.png" align="center">]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/assemblage_dynamixel_french_avec_music.mp4)


# Paramétrage

## Matériel nécessaire :
  - électronique
    - alimentation 12 V : SMPS 12V 5A PS-10 x1
    - carte pour alimenter en 12 V les servos : SMPS2Dynamixel x1
    - convertisseur USB <-> 3 points : USB2AX x1
  - câblage
    - câble USB 30 cm  mâle–femalle x1
    - deux câbles avec connecteurs 3 points : Cable-3P x2 (longueur indifférente)
  - servomoteur
    - MX-28T ou MX-64 ou AX-12A x1

[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/_1020822_ld.jpg" align="bottom" width="643" height="243" >]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/_1020822_ld.jpg)

## Logiciel nécessaire:
### _Linux/Mac_
  - **PyPot**  
commande d'installation: `sudo pip install pypot`
    Tester l'installation : `python -c "import pypot"` ne doit pas retourner d'erreur !  
    _Pypot_ fournit le programme _herborist_ qui permlet de configurer les servomoteurs via un port USB.  
    L'utilisation d'**H****erborist** nécessite des _accès en écriture_ sur les ports USB : l'utilisateur doit faire partie du groupe dialout
    Pour vérifier si vous êtes dans le groupe dialout, taper la commande `id`.
    Si dialout est dans la liste, vous possédez la permission d'accès au port série.   
    Sinon, il taper la commande `sudo adduser yourlogin dialout` 
    
    tester le succès de la procédure:	id
    
    Si vous ne voyez toujours pas *dialout* dans la liste, c'est que les attibuts de votre session sont fixés au démarrage de la session : fermez puis ouvrez à nouveau votre session utilisateur. Taper à nouveau `id`pour vérifier.
    
    
    Nota
    
    L'installation de PyPot peut s'effectuer à
    l'échelle locale ou globale. La procédure qui vous est proposée
    est à l'échelle globale. L'installation est faite au niveau
    administrateur et impacte l'arborescence machine.
    
    L'installation locale pip
    install -user
    pypot
    installe des modules dans l'arborescence de l'utilisateur. J'ignore
    pour quel type d'installation PyPot et Herborist ont été conçus.
    Je conseille par défaut l'installation globale.
    
    
    Procédure :  vidéo en cours de création


_Windows_  
  - FTDI (VCP) Driver&nbsp_place_holder;: **USB2AX.inf** pour communiquer avec USB2Dynamixel
  - **DynamixelWizard** inclus dans la suite logicielle RobotPlus

Procédure : assemblage dynamixel french music et commentaires.mp4
