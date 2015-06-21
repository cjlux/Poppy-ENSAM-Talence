# Premier démarrage de Poppy
(pilotage avec un portable Linux)

Après avoir branché l’alimentation, on peut vérifier que chaque moteur est détecté en tapant dans le shell Linux les commandes :

    cd path_to_check_ports.py    # se positionner dans le répertoire qui contient check_ports.py
    python check_ports.py        # exécuter check_ports.py avec python.

Le contenu du programme Python *check_ports.py* est :

    import pypot.dynamixel
    ports = pypot.dynamixel.get_available_ports()
    if not ports:
      raise IOError('no port found')
    print ports[0]
    dxl_io1 = pypot.dynamixel.DxlIO(ports[0],baudrate=1000000,use_sync_read=False) #upper body
    print dxl_io1.scan(range(60))
    print ports[1]
    dxl_io2 = pypot.dynamixel.DxlIO(ports[1],baudrate=1000000,use_sync_read=False) #lower body
    print dxl_io2.scan(range(60))

le résultat devrait ressembler à :

    /dev/ttyACM1
    [11, 12, 13, 14, 15, 21, 22, 23, 24, 25]
    /dev/ttyACM0
    [31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 51, 52, 53, 54]

L'affichage montre que tous les moteurs sont détectés sur les 2 ports USB. 

Ensuite, on doit créer le fichier de configuration de Poppy avec :

    cd path/to/poppy-software           # se positionner dans le répertoire 'poppy-software'
    cd poppytools/configuration         # aller dans le sous-répertoire 'poppytools/configuration'
    python poppy_config_generation.py   # exécuter 'poppy_config_generation.py' avec Python

où il faut définir les ports */dev/ttyACM1* et */dev/ttyACM0* (ou ceux de votre ordinateur) dans le fichier *poppy_config_generation.py* :

    poppy_config={}
    poppy_config['controllers'] = {}
    poppy_config['controllers']['lower_body_controller'] = {
    "port": “/dev/ttyACM1",  # value to change 
    "sync_read": True,
    "attached_motors": ["legs"],
    }
    poppy_config['controllers']['upper_body_controller'] = {
    "port": “/dev/ttyACM0", # value to change 
    "sync_read": True,
    "attached_motors": ["torso", "head", “arms"], 
    ...
    import json
    poppy_config['controllers']['lower_body_controller']['port'] = “/dev/ttyACM1" # value to change
    poppy_config['controllers']['upper_body_controller']['port'] = “/dev/ttyACM0" # value to change 
    ...

Pour créer la configuration du robot (création d'un fichier .json avec la configuration du robot) :

    cd path_to_create_poppy.py
    python create_poppy.py

Programme *create_poppy.py*

    import time
    import pypot.robot
    from poppytools.configuration.config import poppy_config
    poppy = pypot.robot.from_config(poppy_config)
    poppy.start_sync()

Le fichier **poppy_config.json** décrit pour chaque servomoteur : l’offset, le type, l’id et l’angle_limit. <BR>
Il faut vérifier qu'on utilise la bonne configuration des moteurs quand on travail avec différents programmes  (la figure de droite montre la configuration ENSAM) :

[<img src="http://147.210.74.152/Poppy/6_premier_demarrage/MoteursPoppy.png" align="bottom" width="400" height="550" >]
(http://147.210.74.152/Poppy/6_Montage_des_cacbles/MoteursPoppy.png)
[<img src="http://147.210.74.152/Poppy/6_premier_demarrage/2.png" width="350" height="550" >]
(http://147.210.74.152/Poppy/6_Montage_des_cables/2.png)

La première chose à faire est de vérifier que le configuration du robot avec les moteurs en position 0° donne un positionnement de Poppy comme montré sur cette photo :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/6_premier_demarrage/PoppyRepos.png" align="bottom" width="250" height="450">]
(http://147.210.74.152/Poppy/6_premier_demarrage/PoppyRepos.png)  

On peut le faire avec le programme *starting_position.py* :

    cd path_to_starting_position.py
    python starting_position.py

Contenu du fichier *starting_position.py* :

    import time
    import pypot.robot 
    from poppytools.configuration.config import poppy_config
    poppy = pypot.robot.from_config(poppy_config)
    poppy.start_sync()
    # main program
    for m in poppy.motors
        m.compliant = False
        m.torque_limit = 65 # Reduce max torque to keep motor temperature low
        m.moving_speed = 65
    for m in poppy.motors:
        print m,"\n"
        m.goto_position(0, 3)
    time.sleep(12)
    print 'final position'
    for m in poppy.motors:
    print m,"\n"

Si le robbot ne se présente pas comme sur l'image, il faut changer la configuration des moteurs mécaniquement ou avec l’offset. Le programme **Herborist** peut aider dans cette tâche et pour tester les moteurs, mais il a une configuration de l’offset différente de celle précédemment établie.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/6_premier_demarrage/8.png" align="bottom" width="595" height="355">]
(http://147.210.74.152/Poppy/6_premier_demarrage/8.png)  

**N.B.** Il faut toujours définir la vitesse de déplacement, parce que la fonction **m.goto_position** établit une vitesse de la trajectoire qui peut être égal à 0. Dans ce cas, cette vitesse reste stocké dans la configuration du moteur et il ne bouge pas jusqu'à ce qu’on posera m.moving_speed différent de 0.

## Programme simple de présentation du robot

Le programme suivant est utilisé pour une présentation simple du robot. Il employe les codes primitives dans poppy-software qui ont été mis au point par l’equipe Flower de l’Inria. Les primitives sont :
- **MoveRecorder** qui permet d'enregistrer un mouvement du robot décidé par l’utilisateur,
- **ArmsCopyMotion** qui permet de bouger les bras du robot en mode miroir.

    `cd path_to_presentation.py`<BR>
    `python presentation.py`

Contenu du programme *presentation.py* :

    # main program
    # starting presentation
    StartingPos()
    SittingPos()
    print 'sit down the robot and hold it from the handle pls'
    raw_input("press Enter if you are ready to continue..") 
    print 'The presentation is starting..'
    ShakingLegs()
    time.sleep(0.5)
    Hands2tab()
    time.sleep(1)
    PlayHello()
    # ask different options
    AskWhat2Do1()
    while True:
        AskKeyPress() 
        if char == 'r':
            Recording() 
            AskWhat2Do2() 
            char = None 
        elif char == 'c':
            CopyArm()
            AskWhat2Do1()
            char = None
        elif char == 'p':
            Presentation()
            AskWhat2Do1()
            char = None
        elif char == 'm':
            PlayRecord()
            AskWhat2Do2()
           nbsp;char = None
    else: break
    # final position
    time.sleep(1)
    FinalPos()
    print 'going to finish...'
    raw_input("press Enter if you want to make the motors compliant..")
    MotorsCompl()

Les images suivantes montrent les trois modes possibles :

[<img src="http://147.210.74.152/Poppy/6_premier_demarrage/f7.png" align="bottom" width="800" height="290">]
(http://147.210.74.152/Poppy/6_premier_demarrage/f7.png) 

[<img src="http://147.210.74.152/Poppy/6_premier_demarrage/f7text.png" align="bottom" width="790" height="200">]
(http://147.210.74.152/Poppy/6_premier_demarrage/f7text.png)

vidéo:

[<img src="http://147.210.74.152/Poppy/6_premier_demarrage/pres.png" align="center" width="180">.mp4]
(http://147.210.74.152/Poppy/6_premier_demarrage/Presentation.mp4)
[<img src="http://147.210.74.152/Poppy/6_premier_demarrage/pres.png" align="center" width="180">.ogv]
(http://147.210.74.152/Poppy/6_premier_demarrage/Presentation.ogv)

[ :arrow_left: Montage, Câblage des servomoteurs] (https://github.com/cjlux/Poppy-ENSAM-Talence/blob/French/Cablage%20des%20servomoteurs.md)
[ :house: Sommaire] (https://github.com/cjlux/Poppy-ENSAM-Talence/wiki/Version-Fran%C3%A7aise)
