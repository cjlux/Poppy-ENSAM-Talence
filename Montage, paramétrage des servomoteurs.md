[ :arrow_left: Vérification du kit] (https://github.com/cjlux/Poppy-ENSAM-Talence/blob/French/V%C3%A9rification%20du%20kit.md)
[ :house: Sommaire] (https://github.com/cjlux/Poppy-ENSAM-Talence/wiki/Version-Fran%C3%A7aise)
[ :arrow_right: Montage, assemblage global ] (https://github.com/cjlux/Poppy-ENSAM-Talence/blob/French/Montage%20et%20assemblage%20global.md)

# Montage et paramétrage des servomoteurs Dynamixel
---

## A - Montage des servomoteurs

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


## B - Paramétrage des servomoteurs

Le but du paramétrage est de fixer le numéro **id** de chacun des servomoteurs, ainsi qu'un certain nombre d'autres paramètres dont la valeur usine ne convient pas au focntionnement du robot Poppy.

### Matériel nécessaire :
  - électronique
    - une alimentation 12 V : par exemple l'alimentation SMPS 12V 5A PS-10  
    - une carte SMPS2Dynamixel comportant une entrée pour alimentation 12 V et 2 connecteurs 3 points pour le branchement d'un sermoteur Dynamixel
    - une carte USB2AX convertisseur USB <-> TTL 3 points pour le pilotage des servomoteurs Dynamixel
  - câblage
    - un câble USB mâle–femelle 
    - deux câbles avec connecteurs 3 points (Câble-3P, longueur indifférente)
  - servomoteur
    - un servomoteur MX-28T, MX-64 ou AX-12A.

[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/_1020822_ld.jpg" align="bottom" width="643" height="243" >]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/_1020822_ld.jpg)

### Logiciel nécessaire :
On peut utiliser au choix :
- le logiciel _herborist_ : programme Python utilisable sous GNU/Linux, Mac OS X et Windows, permettant de configurer les servomoteurs via une carte USB2AX. Il est fourni par le module _Pypot_.
- le logiciel _DynamixelWizard_, propriétaire Robotis, disponible pour Windows.

#### GNU/Linux
##### Programme Python _herborist_ 
L'installation du module _pypot_ se fait en tapant tant un terminal :
`sudo pip install pypot` (si vous utilisez Python3, la commande `pip` peut s'appeler `pip3`). _pip_ télécharge et installe le paquet _pypot_ depuis le site https://pypi.python.org/pypi. 

Pour tester l'installation vous pouvez taper dans un terminal `python -c "import pypot"` (si vous utilisez Python3, il faudra peut-être remplacer `python` par `python3`) : aucun message d'erreur ne doit apparaître à l'écran.

L'utilisation d'_herborist_ sous GNU/Linux nécessite que vous ayez des _accès en écriture_ sur les ports USB 
(on parle aussi de _port série_) : pour avoir ces accès, votre login doit faire partie du groupe `dialout`.  
Pour vérifier si vous faites partie du groupe `dialout`, tapez la commande `id` dans un terminal : 
[<img src="http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/id_dialout.png" align="bottom" >]
(http://147.210.74.152/Poppy/2_Montage_Parametrage_des_servomoteurs/id_dialout.png)
  - si `dialout` est dans la liste, vous bénéficiez des accès en lecture/écriture au port série.
  - sinon, il faut ajouter votre login au groupe `dialout` en tapant dans un terminal `sudo adduser yourlogin dialout` (remplacer `yourlogin` par votre nom d'utilisateur). 

**ATTENTION** : sur la plupart des systèmes GNU/Linux, les attributs de session (liste des groupes...) sont fixés à l'**ouverture de la session** => pour activer le changement de groupe, fermez puis ouvrez de nouveau votre session utilisateur. Tapez maintenant `id` dans un terminal : cette fois le groupe `dialout` doit apparaître.

Une fois l'installation faite, vous pouvez lancer *herborist* en tapant dans un terminal la commande `herborist` : l'interface graphique se lance, avec laquelle vous pouvez scanner et configurer un à un les servomoteurs nécessaires à Poppy.

#### Mac OS X
##### Programme Python _herborist_ 
L'installation du module _pypot_ se fait comme pour GNU/Linux, en tapant tant un terminal :
`sudo pip install pypot`. _pip_ télécharge et installe le paquet _pypot_ depuis le site https://pypi.python.org/pypi. 
Pour tester l'installation vous pouvez taper dans un terminal `python -c "import pypot"` : aucun message d'erreur ne doit apparaître à l'écran.

Une fois l'installation faite, vous pouvez lancer *herborist* en tapant dans un terminal la commande `herborist` : l'interface graphique se lance, avec laquelle vous pouvez configurer un à un les servomoteurs nécessaires à Poppy.

#### Windows
##### Pilote de la carte USB2AX
Il faut télécharger le pilote [USB2AX.inf] (http://www.xevelabs.com/doku.php?id=product:usb2ax:quickstart) et l'installer sur votre PC pour pouvoir utiliser la carte USB2AX :
  - insérer la carte USB2AX dans un port USB du PC : la LED <span style="color: #fb4141">rouge</span> s'allume ! annuler la recherche automatique de driver éventuellement lancée par Windows.
  - ouvrir le _Gestionnaire de périphérique_ (_menu Démarrer_ > _Panneau de Configration_ > _Système et sécurité_ > _Gestionnaire de périphériques_)
  - dans la section des ports série (COM et LP), vous devriez voir un périphérique USB2X en erreur, signalé par un point d'excamation : avec un clic-droit sur USB2AX, lancez le menu _Mettre à jour le pilote_ en _recherchant le pilote sur mon ordinateur_
  - naviguer jusqu'au fichier _USB2AX.inf_ que vous avez téléchargé : une fois le pilote installé, la LED rouge de l'USB2AX doit s'éteindre, et sa LED verte doit s'allumer !

##### Paramétrage avec le programme Python _herborist_
Sous Windows, vous devez également taper la commande `pip install pypot` dans la fenêtre de commande,  ou mieux, dans la fenetre *Anaconda command prompt*, si vous avez intallé Python sur votre PC avec Anaconda. 
_pip_ télécharge et installe le paquet _pypot_ depuis le site https://pypi.python.org/pypi. Pour tester l'installation vous pouvez taper la commande : `python -c "import pypot"` qui ne devrait pas retourner d'erreur !   
L'utilisation de _herborist_ est la même que pour GNU/Linux ou Mac OS X.

##### Paramètrage avec le logiciel **DynamixelWizard**, inclus dans la suite logicielle [RobotPlus] (http://support.robotis.com/en/software/roboplus_main.htm).
Vidéo du paramétrage avec le logiciel _DynamixelWizard_ :  
[<img src="http://147.210.74.152/Poppy/Videos/servomoteurs_parametrages_win.png" align="center" width="180">.mp4]
(http://147.210.74.152/Poppy/Videos/servomoteurs_parametrages_win.mp4)
&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/Videos/servomoteurs_parametrages_win.png" align="center" width="180">.ogv]
(http://147.210.74.152/Poppy/Videos/servomoteurs_parametrages_win.ogv)


[ :arrow_left: Vérification du kit] (https://github.com/cjlux/Poppy-ENSAM-Talence/blob/French/V%C3%A9rification%20du%20kit.md)
[ :house: Sommaire] (https://github.com/cjlux/Poppy-ENSAM-Talence/wiki/Version-Fran%C3%A7aise)
[ :arrow_right: Montage, assemblage global ] (https://github.com/cjlux/Poppy-ENSAM-Talence/blob/French/Montage%20et%20assemblage%20global.md)
