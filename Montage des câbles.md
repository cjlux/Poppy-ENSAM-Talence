# Montage des câbles
---

On peut diviser le robot en deux parties pour la description du montage des câbles: le haut (en rouge) et le bas (en vert). Chaque partie a un Bioloid 3P Extension Board et un SMPS2 Dynamixel.

## HAUT DU CORPS

Le Bioloid 3P Extension Board du haut du corps est connecté au SMPS2 Dynamixel et aux moteurs “head_y (id=37)”, “head_z (id=36)”, “r_shoulder_y (id=51)”, “l_shoulder_y (id=41)” et “bust_x (id=35)”. Enfin, la partie supérieure du robot est attachée à l’USB HUB 4 PORTS par le moteur “head_y (id=37)”.

## BAS DU CORPS

Le Bioloid 3P Extension Board du bas du corps est connecté au SMPS2 Dynamixel et aux moteurs “r_hip_x (id=11)” et “l_hip_x (id=21)”. La partie inférieure du robot est attachée à l’USB HUB 4 PORTS par le SMPS2 Dynamixel.
Pour connecter les moteurs “r_hip_y (id=23)” - “r_knee_y (id=24)” et “l_hip_y (id=13)” - “l_knee_y (id=14)” on a besoin d’un câble d'au moins 20cm de long (Voir figure 3a) et pour la connexion USB HUB 4 PORTS - SMPS2 Dynamixel d’un câble de 60cm.

## PREMIER DÉMARRAGE DU ROBOT

Après avoir branché l’alimentation, on peut vérifier que chaque moteur est détecté avec le code suivant:

`cd Bureau/poppy/my_code`
`python check_ports.py`

“check_ports.py”

*import pypot.dynamixel
ports = pypot.dynamixel.get_available_ports()
if not ports:
      raise IOError('no port found')
print ports[0]
dxl_io1 = pypot.dynamixel.DxlIO(ports[0],baudrate=1000000,use_sync_read=False)#upper body
print dxl_io1.scan(range(60))
print ports[1]
dxl_io2 = pypot.dynamixel.DxlIO(ports[1],baudrate=1000000,use_sync_read=False)#lower body
print dxl_io2.scan(range(60))*

le résultat devrait être:

*/dev/ttyACM1
[11, 12, 13, 14, 15, 21, 22, 23, 24, 25]
/dev/ttyACM0
[31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 51, 52, 53, 54]*

IL veut dire que tous les moteurs sont détectés.
Ensuite, on doit créer le fichier de configuration de Poppy avec:

`cd path/to/poppy-software`
`cd poppytools/configuration`
`python poppy_config_generation.py`


où il faut définir les ports “/dev/ttyACM1” et “/dev/ttyACM0”:

“poppy_config_generation.py”


*poppy_config={}
poppy_config['controllers'] = {}
poppy_config['controllers']['lower_body_controller'] = {
    "port": “/dev/ttyACM1", #to change
    "sync_read": True,
    "attached_motors": ["legs"],
}
poppy_config['controllers']['upper_body_controller'] = {
    "port": “/dev/ttyACM0", #to change
    "sync_read": True,
    "attached_motors": ["torso", "head", “arms"],
...
    import json
    poppy_config['controllers']['lower_body_controller']['port'] = “/dev/ttyACM1" #to change
    poppy_config['controllers']['upper_body_controller']['port'] = “/dev/ttyACM0" #to change
...*


Il va créer un fichier de .json avec la configuration du robot. Maintenant, on peut créer poppy robot comme ça:
`cd Bureau/poppy/my_code`
`python create_poppy.py`

“create_poppy.py”

*import time
import pypot.robot
from poppytools.configuration.config import poppy_config
poppy = pypot.robot.from_config(poppy_config)
poppy.start_sync()*

“poppy_config.json” décrit pour chaque moteur l’offset, le type, l’id et l’angle_limit. Il faut que nous vérifions qu'on utilise la même configuration des moteurs quand on travail avec différents programmes et codes. (Voir figure 4)

La première chose à faire est de vérifier que le configuration du robot avec les moteurs en position 0° est come l’image suivant:

On peut le faire avec le code starting_position.py:

`cd Bureau/poppy/my_code`
`python starting_position.py`

“starting_position.py”

*import time
import pypot.robot
from poppytools.configuration.config import poppy_config
poppy = pypot.robot.from_config(poppy_config)
poppy.start_sync()

**main program**
for m in poppy.motors:
        m.compliant = False
        m.torque_limit = 65 # Reduce max torque to keep motor temperature low
        m.moving_speed = 65
for m in poppy.motors:
        print m,"\n"
        m.goto_position(0, 3)
time.sleep(12)
print 'final position'
for m in poppy.motors:
print m,"\n"*

Si il n’est pas comme cela, il faut changer la configuration des moteurs mécaniquement ou avec l’offset. Le programme Herborist peut aider dans cette tâche et pour tester les moteurs, mais il a une configuration de l’offset différente de celle précédemment établie.

**N.B.** Il faut toujours définir la vitesse de déplacement, parce que la fonction m.goto_position établit une vitesse de la trajectoire qui peut être égal à 0. Dans ce cas, cette vitesse reste stocké dans la configuration du moteur et il ne bouge pas jusqu'à ce qu’on posera m.moving_speed différent de 0.


