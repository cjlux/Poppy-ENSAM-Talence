## Premier démarrage du robot  
(pilotage avec un portable Linux)

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

L'affichage montre que tous les moteurs sont détectés.
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


Il va créer un fichier de .json avec la configuration du robot. Maintenant, on peut créer la configuration du robot comme suit :
`cd Bureau/poppy/my_code` <BR>
`python create_poppy.py` <BR>

“create_poppy.py”

*import time <BR>
import pypot.robot <BR>
from poppytools.configuration.config import poppy_config <BR>
poppy = pypot.robot.from_config(poppy_config) <BR>
poppy.start_sync()* <BR>

“poppy_config.json” décrit pour chaque moteur l’offset, le type, l’id et l’angle_limit. Il faut vérifier qu'on utilise la bonne configuration des moteurs quand on travail avec différents programmes. (Voir la figure suivant)

&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/6_Montage_des_cables/7.png" align="bottom" width="500" height="450" >]
(http://147.210.74.152/Poppy/6_Montage_des_cacbles/7.png)
[<img src="http://147.210.74.152/Poppy/6_Montage_des_cables/2.png" width="200" height="450" >]
(http://147.210.74.152/Poppy/6_Montage_des_cables/2.png)

La première chose à faire est de vérifier que le configuration du robot avec les moteurs en position 0° est come l’image suivant:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/6_Montage_des_cables/5.jpg" align="bottom" width="250" height="450">]
(http://147.210.74.152/Poppy/6_Montage_des_cables/5.jpg)  

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

Si le robbot ne se présente pas comme sur l'image, il faut changer la configuration des moteurs mécaniquement ou avec l’offset. Le programme Herborist peut aider dans cette tâche et pour tester les moteurs, mais il a une configuration de l’offset différente de celle précédemment établie.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/6_Montage_des_cables/8.png" align="bottom" width="595" height="355">]
(http://147.210.74.152/Poppy/6_Montage_des_cables/8.png)  

**N.B.** Il faut toujours définir la vitesse de déplacement, parce que la fonction m.goto_position établit une vitesse de la trajectoire qui peut être égal à 0. Dans ce cas, cette vitesse reste stocké dans la configuration du moteur et il ne bouge pas jusqu'à ce qu’on posera m.moving_speed différent de 0.

## Code de présentation du robot

Le code suivant est utilisé pour une petit presentation du robot. Il employe les codes primitives dans poppy-software qui ont été mis au point par l’equipe Flower de l’Inria. Les primitives sont MoveRecorder qui permet d'enregistrer un mouvement du robot décidé par l’utilisateur et ArmsCopyMotion qui permet de bouger les bras du robot en mode miroir.


`cd Bureau/poppy/my_code` <BR>
`python presentation.py`<BR>

“presentation.py”

**main program** <BR>
**starting presentation** <BR>
StartingPos() <BR>
SittingPos() <BR>
print 'sit down the robot and hold it from the handle pls' <BR>
raw_input("press Enter if you are ready to continue..") <BR>
print 'The presentation is starting..' <BR>
ShakingLegs() <BR>
time.sleep(0.5) <BR>
Hands2tab() <BR>
time.sleep(1) <BR>
PlayHello() <BR>
**ask different options** <BR>
AskWhat2Do1() <BR>
while True: <BR>
    AskKeyPress() <BR>
    if char == 'r': <BR>
        Recording() <BR>
        AskWhat2Do2() <BR>
        char = None <BR>
    elif char == 'c': <BR>
        CopyArm() <BR>
        AskWhat2Do1() <BR>
        char = None <BR>
    elif char == 'p': <BR>
        Presentation() <BR>
        AskWhat2Do1() <BR>
        char = None <BR>
    elif char == 'm': <BR>
        PlayRecord() <BR>
        AskWhat2Do2() <BR>
        char = None <BR>
else: break <BR>
**final position** <BR>
time.sleep(1) <BR>
FinalPos() <BR>
print 'going to finish...' <BR>
raw_input("press Enter if you want to make the motors compliant..") <BR>
MotorsCompl() <BR>

Les images suivantes montrent les trois modes possibles:

[<img src="http://147.210.74.152/Poppy/7_demerrage_du_robot/f7.tiff" align="bottom" width="800" height="300">]
(http://147.210.74.152/Poppy/7_demerrage_du_robot/f7.tiff) 

[<img src="http://147.210.74.152/Poppy/7_demerrage_du_robot/f7text.tiff" align="bottom" width="800" height="300">]
(http://147.210.74.152/Poppy/7_demerrage_du_robot/f7text.tiff)
