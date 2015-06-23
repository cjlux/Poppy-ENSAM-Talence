[ :arrow_left: Montage, assemblage global] (https://github.com/cjlux/Poppy-ENSAM-Talence/blob/French/Montage%20et%20assemblage%20global.md)
[ :house: Sommaire] (https://github.com/cjlux/Poppy-ENSAM-Talence/wiki/Version-Fran%C3%A7aise)
[ :arrow_right: Premier démarrage] (https://github.com/cjlux/Poppy-ENSAM-Talence/blob/French/Premier%20d%C3%A9marrage.md)

# Câblage des servomoteurs
---

On peut diviser le robot en deux parties pour le câblage : le haut (en rouge) et le bas (en vert). 
[<img src="http://147.210.74.152/Poppy/5_Cablage/CablageMoteurs.png" align="bottom" width="680" height="680">]
(http://147.210.74.152/Poppy/5_Cablage/CablageMoteur.png)<BR>
Chaque partie utilise :
- un convertisseur *USB2AX Dynamixel*, qui convertit le bus USB en bus TTL 3 points (3P), permettant de dialoguer avec les servomoteurs Dynamixel de la série AX et MX <BR>
[<img src="http://147.210.74.152/Poppy/5_Cablage/USB2AX_2.png"  width="120" height="80"  align="center">] (http://147.210.74.152/Poppy/5_Cablage/USB2AX_2.png) 
- une platine *Bioloid 3P Extension Board*, qui permet le raccordement 3P de 6 servomoteurs sur la platine 
[<img src="http://147.210.74.152/Poppy/5_Cablage/Bioloid3P.png" align="center">] (http://147.210.74.152/Poppy/5_Cablage/Bioloid3P.png)   
- un circuit *SMPS2 Dynamixel*, pour l'alimentation 12 V pour des servomoteurs grâce à 4 connecteurs :
  - 2 connecteurs 3P, pour le branchement de servomoteurs Dynamixel série AX,
  - 2 connecteurs 4P, pour le branchement de servomoteurs Dynamixel série DX ou RX.[<img src="http://147.210.74.152/Poppy/5_cablage/SMP2P_Dynamixel.png"  align="center">]
(http://147.210.74.152/Poppy/5_Cablage/SMP2P_Dynamixel.png) 

Les servomoteurs dynamixel sont *chaînés* les uns autres par un bus numérique qui les relie entre eux. Dans une chaîne ainsi formée, un seul des servomteurs est relié à un *Bioloid 3P Extension Board* ou à un *SMPS2 Dynamixel*.

## HAUT DU CORPS
Le *Bioloid 3P* du haut du corps est connecté au *SMPS2 Dynamixel* et aux 5 servomoteurs :
- `head_y (id=37)`
- `head_z (id=36)` 
- `r_shoulder_y (id=51)` 
- `l_shoulder_y (id=41)` 
- `bust_x (id=35)`.

Le servomoteur `head_y (id=37)` est également connecté au *USB2AX* qui permet la liason avec le *HUB USB 4 PORTS* situé dans la tête.

## BAS DU CORPS
Les servomoteurs des 2 jambes sont chaînés depuis la cheville jusqu'aux servomoteurs de la hanche, `r_hip_x (id=11)` et `l_hip_x (id=21)`.

Le *Bioloid 3P* du bas du corps est connecté au *SMPS2 Dynamixel* et aux 2 servomoteurs :
- `r_hip_x (id=11)`
- `l_hip_x (id=21)`. 

Le *SMPS2 Dynamixel* du bas du corsp est connecté au *USB2AX* relié au *USB HUB 4 PORTS* de la tête. Il faut réaliser un câble 3P d'environ 60cm (souder bout à bout plusieurs câbles 3P pour obtenir la longueur voulue).

Pour connecter les moteurs `r_hip_y (id=23)` et `r_knee_y (id=24)` (ainsi que `l_hip_y (id=13)` et `l_knee_y (id=14)`) au  *Bioloid 3P*, on a besoin d’un câble 3P d'environ 20cm de long (souder bout à bout plusieurs câbles 3P pour obtenir la longueur voulue).

[<img src="http://147.210.74.152/Poppy/5_Cablage/1.png" align="bottom" width="214" height="244" >]
(http://147.210.74.152/Poppy/5_Cablages/1.png)
&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/5_Cablage/3.jpg" width="240" height="244" >]
(http://147.210.74.152/Poppy/5_Cablage/3.jpg)
&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/5_Cablage/4.jpg" width="240" height="244" >]
(http://147.210.74.152/Poppy/5_Cablages/4.jpg)

[ :arrow_left: Montage, assemblage global] (https://github.com/cjlux/Poppy-ENSAM-Talence/blob/French/Montage%20et%20assemblage%20global.md)
[ :house: Sommaire] (https://github.com/cjlux/Poppy-ENSAM-Talence/wiki/Version-Fran%C3%A7aise)
[ :arrow_right: Premier démarrage] (https://github.com/cjlux/Poppy-ENSAM-Talence/blob/French/Premier%20d%C3%A9marrage.md)

