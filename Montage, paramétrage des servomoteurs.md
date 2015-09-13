[ :arrow_left: Vérification du kit] (https://github.com/cjlux/Poppy-ENSAM-Talence/blob/French/V%C3%A9rification%20du%20kit.md)
[ :house: Sommaire] (https://github.com/cjlux/Poppy-ENSAM-Talence/wiki/Version-Fran%C3%A7aise)
[ :arrow_right: Montage, assemblage global ] (https://github.com/cjlux/Poppy-ENSAM-Talence/blob/French/Montage%20et%20assemblage%20global.md)

# Montage et paramétrage des servomoteurs Dynamixel
---

## Montage des servomoteurs

Les servomoteurs Dynamixel MX-28T et MX-64 sont vendus partiellement montés :
[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/boite_1_contenu_face_ld.jpg" align="bottom" width="595" height="355">]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/boite_1_contenu_face_ld.jpg)  

Le montage consiste à fixer le palonnier à l'arbre moteur.

### Matériel nécessaire :
  - clef allen de 2 mm.

**Attention** Il faut aligner l'encoche sur le palonnier avec le poinçonnage sur l'arbre du servomoteur :  
[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/palonnier_ld.jpg" align="bottom" width="290" height="251" >]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/palonnier_ld.jpg)
[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/repere_et_poinconnage_ld.jpg" width="214" height="244" >]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/repere_et_poinconnage_ld.jpg)

La rondelle doit être intercalée entre le palonnier et le servomoteur :  
[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/rondelles_3.jpg" name="Image5" align="bottom" width="245" height="141" border="0" >]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/rondelles_3.jpg)

La vidéo montrant le montage est ici : 
[<img src="http://147.210.74.152/Poppy/Videos/assemblage_dynamixel_french_avec_music.png" align="center" width="180">.mp4]
(http://147.210.74.152/Poppy/Videos/assemblage_dynamixel_french_avec_music.mp4)
&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/Videos/assemblage_dynamixel_french_avec_music.png" align="center" width="180">.ogv]
(http://147.210.74.152/Poppy/Videos/assemblage_dynamixel_french_avec_music.ogv)


## Paramétrage

Le but du paramétrage est de fixer le numéro **id** de chacun des servomoteurs, ainsi qu'un certain nombre d'autres paramètres dont la valeur usine ne convient pas au focntionnement sur le robot Poppy.

### Matériel nécessaire :
  - électronique
    - une alimentation 12 V : par exemple l'alimentation SMPS 12V 5A PS-10  
    - une carte SMPS2Dynamixel comportant une entrée pour alimentation 12 V et 2 connecteurs 3 points pour le branchement d'un sermoteur Dynamixel
    - une carte USB2AX convertisseur USB <-> 3 points pour le pilotage d'un servomoteur Dynamixel
  - câblage
    - un câble USB mâle–femelle 
    - deux câbles avec connecteurs 3 points (Câble-3P, longueur indifférente)
  - servomoteur
    - un servomoteur MX-28T, MX-64 ou AX-12A.

[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/_1020822_ld.jpg" align="bottom" width="643" height="243" >]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/_1020822_ld.jpg)

### Logiciel nécessaire :
#### _Linux/Mac_
##### **PyPot**  
La paquet Python *Pypot* fournit entre autre le programme *herborist* qui permet de configurer les servomoteurs via un port USB. La commande  d'installation de *pypot* est : `sudo pip install pypot`.  
*pip* télécharge et installe le paquet *pypot* depuis le site https://pypi.python.org/pypi.   

Pour tester l'installation vous pouvez taper : `python -c "import pypot"` qui ne devrait pas retourner d'erreur !  
L'utilisation d'*Herborist* nécessite des *accès en écriture* sur les ports USB (on parle aussi de *port série*) : pour avoir ces accès, l'utilisateur doit faire partie du groupe *dialout*.  
Pour vérifier si vous faites partie du groupe *dialout*, tapez la commande `id` : 
[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/id_dialout.png" align="bottom" >]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/id_dialout.png)
  - si *dialout* est dans la liste, vous faites partie de ce groupe et vous bénéficiez automatiquement des accès en lecture/écriture au port série.
  - Sinon, il faut ajouter votre login au groupe *dialout* en tapant la commande `sudo adduser yourlogin dialout`. Sur la plupart des systèmes GNU/Linux, les attributs de session (liste des groupes par exemple...) sont fixés à l'ouverture de la session : pour activer le changement de groupe, fermez puis ouvrez à nouveau votre session utilisateur. Tapez à nouveau`id` : cette fois le groupe *dialout* doit apparaître.


#### _Windows_  
  - Il faut télécharger le driver [USB2AX.inf] (http://www.xevelabs.com/doku.php?id=product:usb2ax:quickstart) et l'installer sur votre PC pour pouvoir utiliser la carte USB2AX.
    - insérer la carte USB2AX dans un port USB du PC : la LED rouge s'allume ! annuler la recherche automatique de driver éventuellement lancée par Windows.
    - Ouvrir le _Gestionnaire de périphérique_ (_menu Démarrer_>_Panneau de Configration_>_Système et sécurité_>_Gestionnaire de périphériques_)
    - Dans la section des ports série, vous devriez voir un périphérique USB2X en erreur, signalé par un point d'excamation : avec un clic-droit sur USB2AX, lancer le menu _Mettre à jour le pilote_ en _recherchant le pilote sur mon ordinateur_
    - naviguer jusqu'au fichier _ USB2AX.inf_ que vous avez téléchargé

Une fois le pilote installé, la LED rouge de l'USB2AX doit s'éteindre, et sa LED verte doit s'allumer !

  - Paramètrage avec le logiciel **DynamixelWizard**, inclus dans la suite logicielle [RobotPlus] (http://support.robotis.com/en/software/roboplus_main.htm).

Vidéo du paramétrage :  
[<img src="http://147.210.74.152/Poppy/Videos/servomoteurs_parametrages_win.png" align="center" width="180">.mp4]
(http://147.210.74.152/Poppy/Videos/servomoteurs_parametrages_win.mp4)
&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/Videos/servomoteurs_parametrages_win.png" align="center" width="180">.ogv]
(http://147.210.74.152/Poppy/Videos/servomoteurs_parametrages_win.ogv)


[ :arrow_left: Vérification du kit] (https://github.com/cjlux/Poppy-ENSAM-Talence/blob/French/V%C3%A9rification%20du%20kit.md)
[ :house: Sommaire] (https://github.com/cjlux/Poppy-ENSAM-Talence/wiki/Version-Fran%C3%A7aise)
[ :arrow_right: Montage, assemblage global ] (https://github.com/cjlux/Poppy-ENSAM-Talence/blob/French/Montage%20et%20assemblage%20global.md)

