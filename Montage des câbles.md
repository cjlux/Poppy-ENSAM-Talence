# Montage des câbles
---

On peut diviser le robot en deux parties pour la description du montage des câbles: le haut (en rouge) et le bas (en vert). Chaque partie a un Bioloid 3P Extension Board et un SMPS2 Dynamixel.

[<img src="http://147.210.74.152/Poppy/6_Montage_des_câbles/6.png" align="bottom" width="595" height="355">]
(http://147.210.74.152/Poppy/6_Montage_des_câbles/6.png)  

## HAUT DU CORPS

Le Bioloid 3P Extension Board du haut du corps est connecté au SMPS2 Dynamixel et aux moteurs “head_y (id=37)”, “head_z (id=36)”, “r_shoulder_y (id=51)”, “l_shoulder_y (id=41)” et “bust_x (id=35)”. Enfin, la partie supérieure du robot est attachée à l’USB HUB 4 PORTS par le moteur “head_y (id=37)”.

## BAS DU CORPS

Le Bioloid 3P Extension Board du bas du corps est connecté au SMPS2 Dynamixel et aux moteurs “r_hip_x (id=11)” et “l_hip_x (id=21)”. La partie inférieure du robot est attachée à l’USB HUB 4 PORTS par le SMPS2 Dynamixel.
Pour connecter les moteurs “r_hip_y (id=23)” - “r_knee_y (id=24)” et “l_hip_y (id=13)” - “l_knee_y (id=14)” on a besoin d’un câble d'au moins 20cm de long (Voir figure 3a) et pour la connexion USB HUB 4 PORTS - SMPS2 Dynamixel d’un câble de 60cm.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/6_Montage_des_câbles/1.tiff" align="bottom" width="214" height="244" >]
(http://147.210.74.152/Poppy/6_Montage_des_câbles/1.tiff)
&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/6_Montage_des_câbles/3.jpg" width="240" height="244" >]
(http://147.210.74.152/Poppy/6_Montage_des_câbles/3.jpg)
&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/6_Montage_des_câbles/4.jpg" width="240" height="244" >]
(http://147.210.74.152/Poppy/6_Montage_des_câbles/4.jpg)

## PREMIER DÉMARRAGE DU ROBOT

Après avoir branché l’alimentation, on peut vérifier que chaque moteur est détecté avec le code suivant:

`cd Bureau/poppy/my_code` <BR>
`python check_ports.py`<BR>

“check_ports.py”

*import pypot.dynamixel <BR>
ports = pypot.dynamixel.get_available_ports() <BR>
if not ports: <BR>
      raise IOError('no port found') <BR>
print ports[0] <BR>
dxl_io1 = pypot.dynamixel.DxlIO(ports[0],baudrate=1000000,use_sync_read=False)#upper body <BR>
print dxl_io1.scan(range(60)) <BR>
print ports[1] <BR>
dxl_io2 = pypot.dynamixel.DxlIO(ports[1],baudrate=1000000,use_sync_read=False)#lower body <BR>
print dxl_io2.scan(range(60))* <BR>

le résultat devrait être:

*/dev/ttyACM1 <BR>
[11, 12, 13, 14, 15, 21, 22, 23, 24, 25] <BR>
/dev/ttyACM0 <BR>
[31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 51, 52, 53, 54]* <BR>

IL veut dire que tous les moteurs sont détectés.
Ensuite, on doit créer le fichier de configuration de Poppy avec:

`cd path/to/poppy-software`<BR>
`cd poppytools/configuration` <BR>
`python poppy_config_generation.py` <BR>


où il faut définir les ports “/dev/ttyACM1” et “/dev/ttyACM0”:

“poppy_config_generation.py”


*poppy_config={} <BR>
poppy_config['controllers'] = {} <BR>
poppy_config['controllers']['lower_body_controller'] = { <BR>
    "port": “/dev/ttyACM1", #to change <BR>
    "sync_read": True, <BR>
    "attached_motors": ["legs"], <BR>
} <BR>
poppy_config['controllers']['upper_body_controller'] = { <BR>
    "port": “/dev/ttyACM0", #to change <BR>
    "sync_read": True, <BR>
    "attached_motors": ["torso", "head", “arms"], <BR>
... <BR>
    import json <BR>
    poppy_config['controllers']['lower_body_controller']['port'] = “/dev/ttyACM1" #to change <BR>
    poppy_config['controllers']['upper_body_controller']['port'] = “/dev/ttyACM0" #to change <BR>
...* <BR>


Il va créer un fichier de .json avec la configuration du robot. Maintenant, on peut créer poppy robot comme ça:
`cd Bureau/poppy/my_code` <BR>
`python create_poppy.py` <BR>

“create_poppy.py”

*import time <BR>
import pypot.robot <BR>
from poppytools.configuration.config import poppy_config <BR>
poppy = pypot.robot.from_config(poppy_config) <BR>
poppy.start_sync()* <BR>

“poppy_config.json” décrit pour chaque moteur l’offset, le type, l’id et l’angle_limit. Il faut que nous vérifions qu'on utilise la même configuration des moteurs quand on travail avec différents programmes et codes. (Voir figure 4)

[<img src="http://147.210.74.152/Poppy/6_Montage_des_câbles/2.tiff" align="bottom" width="200" height="400">]
(http://147.210.74.152/Poppy/6_Montage_des_câbles/2.tiff)  
[<img src="http://147.210.74.152/Poppy/6_Montage_des_câbles/7.png" width="500" height="400">]
(http://147.210.74.152/Poppy/6_Montage_des_câbles/7.png)  
[<img src="http://147.210.74.152/Poppy/6_Montage_des_câbles/2.tiff" align="bottom" width="200" height="400" >]
(http://147.210.74.152/Poppy/6_Montage_des_câbles/2.tiff)
&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/6_Montage_des_câbles/7.png" width="240" height="400" >]
(http://147.210.74.152/Poppy/6_Montage_des_câbles/7.png)

La première chose à faire est de vérifier que le configuration du robot avec les moteurs en position 0° est come l’image suivant:

On peut le faire avec le code starting_position.py:

`cd Bureau/poppy/my_code` <BR>
`python starting_position.py` <BR>

“starting_position.py”

*import time <BR>
import pypot.robot <BR>
from poppytools.configuration.config import poppy_config <BR>
poppy = pypot.robot.from_config(poppy_config) <BR>
poppy.start_sync() <BR>*
**main program** <BR>
*for m in poppy.motors: <BR>
        m.compliant = False <BR>
        m.torque_limit = 65 # Reduce max torque to keep motor temperature low <BR>
        m.moving_speed = 65 <BR>
for m in poppy.motors: <BR>
        print m,"\n" <BR>
        m.goto_position(0, 3) <BR>
time.sleep(12) <BR>
print 'final position' <BR>
for m in poppy.motors: <BR>
print m,"\n"* <BR>

Si il n’est pas comme cela, il faut changer la configuration des moteurs mécaniquement ou avec l’offset. Le programme Herborist peut aider dans cette tâche et pour tester les moteurs, mais il a une configuration de l’offset différente de celle précédemment établie.

**N.B.** Il faut toujours définir la vitesse de déplacement, parce que la fonction m.goto_position établit une vitesse de la trajectoire qui peut être égal à 0. Dans ce cas, cette vitesse reste stocké dans la configuration du moteur et il ne bouge pas jusqu'à ce qu’on posera m.moving_speed différent de 0.


