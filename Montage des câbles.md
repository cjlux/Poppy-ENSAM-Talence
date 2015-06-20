# Câblage des servomoteurs
---

On peut diviser le robot en deux parties pour le câblage : le haut (en rouge) et le bas (en vert). 
[<img src="http://147.210.74.152/Poppy/6_Montage_des_cables/6.png" align="bottom" width="620" height="680">]
(http://147.210.74.152/Poppy/6_Montage_des_cables/6.png)<BR>
Chaque partie utilise :
- une platine *Bioloid 3P Extension Board* (multiprise pour les connecteurs 3 pins (3P)), qui permet le roccordement des servomoteurs sur la platine [<img src="http://147.210.74.152/Poppy/6_Montage_des_cables/Bioloid3P.png" align="center">] (http://147.210.74.152/Poppy/6_Montage_des_cables/Bioloid3P.png)   
- un circuit *SMPS2 Dynamixel*, pour l'alimentation 12 V pour des servomoteurs [<img src="http://147.210.74.152/Poppy/6_Montage_des_cables/SMP2P_Dynamixel.png"  align="center">]
(http://147.210.74.152/Poppy/6_Montage_des_cables/SMP2P_Dynamixel.png) 


## HAUT DU CORPS
Le *Bioloid 3P* du haut du corps est connecté au *SMPS2 Dynamixel* et aux moteurs :
- `head_y (id=37)`
- `head_z (id=36)` 
- `r_shoulder_y (id=51)` 
- `l_shoulder_y (id=41)` 
- `bust_x (id=35)`.
Enfin, la partie supérieure du robot est attachée à un bloc USB 4 PORTS par le moteur “head_y (id=37)”.

## BAS DU CORPS
Le *Bioloid 3P* du bas du corps est connecté au *SMPS2 Dynamixel* et aux moteurs :
- `r_hip_x (id=11)`
- `l_hip_x (id=21)`. 
La partie inférieure du robot est attachée à l'USB HUB 4 PORTS par le *SMPS2 Dynamixel*.

Pour connecter les moteurs `r_hip_y (id=23)`, `r_knee_y (id=24)`, `l_hip_y (id=13)` et `l_knee_y (id=14)`, on a besoin d’un câble 3P d'environ 20cm de long, et pour la connexion du *USB HUB 4 PORTS* au *SMPS2 Dynamixel* d’un câble 3P d'environ 60cm. Ces câbles sont obtenus en soudant ensemble plusieur câbles 3P pour obtenir les longueurs voulues.

[<img src="http://147.210.74.152/Poppy/6_Montage_des_cables/1.png" align="bottom" width="214" height="244" >]
(http://147.210.74.152/Poppy/6_Montage_des_cables/1.png)
&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/6_Montage_des_cables/3.jpg" width="240" height="244" >]
(http://147.210.74.152/Poppy/6_Montage_des_cables/3.jpg)
&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/6_Montage_des_cables/4.jpg" width="240" height="244" >]
(http://147.210.74.152/Poppy/6_Montage_des_cables/4.jpg)
