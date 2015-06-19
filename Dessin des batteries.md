## DESSIN DES BATTERIES

**Consommation d’énergie:** <BR>

&nbsp;&nbsp;&nbsp;- plage de tension: 10 ~14.8V (tension recommandé12V) <BR>
&nbsp;&nbsp;&nbsp;- courant électrique: minimum (les moteurs sont dans le mode ‘compliant’) 1.53A et le courant maximum <BR> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; enregistrée au cours de la présentation est 2A <BR>

**Limites de couple (couple de décrochage):** <BR>

&nbsp;&nbsp;&nbsp; -  MX-64 : 5.5 Nm (at 11.1V, 3.9A), 6.0N.m (at 12V, 4.1A) <BR>
&nbsp;&nbsp;&nbsp; -  MX-28 : 2.3N.m (at 11.1V, 1.3A), 2.5N.m (at 12V, 1.4A) <BR>

**Temps d’autonomie:** <BR>

&nbsp;&nbsp;&nbsp; - théoriquement on a une heure de vie de la batterie avec 2000mAh <BR>

**Chimie disponibles:** <BR>

&nbsp;&nbsp;&nbsp; - Alkaline: pas considéré pour ce projet (constamment besoin d'acheter des remplacements) <BR>

&nbsp;&nbsp;&nbsp; - Nickel: <BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.  NiCd: Ces batteries sont en train de disparaître à cause de leur  <BR>	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mémoire effet <BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.  NiMh: ils sont rechargeables (il n'y a presque pas d'effet 	 <BR>	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mémoire) et une bonne <BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valeur (prix / capacité / poids). Long temps de charge. <BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Principale solution: 12V pour 540g de poids. <BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Prix: à partir de 40 $ <BR>

&nbsp;&nbsp;&nbsp; - Lead acid: ces batteries ont le problème d'être très volumineux et lourds, elles doivent toujours être <BR> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maintenue, elles n’ont pas la vitesse de décharge  <BR>		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;élevée que les batteries plus modernes.	 <BR>

&nbsp;&nbsp;&nbsp; - Lithium: elles sont légers, le temps de décharge est élevé et elles ont relativement bonne capacité. La <BR> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tension augmente dans les étapes de 3.7V. Par <BR> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;conséquent, les solutions possibles sont les suivants: <BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. trois batteries de 3.7V, poids: 45g chacune, 			 <BR>	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prix chaque batterie: 20€ <BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. une batterie de 11.1V, poids: 150g, prix: 50 € <BR>

**Emplacement:** dans le cas de seulement une batterie, la seule solution est de la fixer au abs_x moteur (id = 32). Le problème de cette solution est que la partie supérieure du robot est déjà assez lourd et il va faire la dynamique du robot plus difficile. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f8.tiff" width="350" height="160" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f8.tiff)

Le deuxième cas est quand nous avons trois batteries. Dans cette solution, nous pouvons localiser une batterie de l'alimentation dans chaque jambe (entre la hanche et le genou) et l’autre batterie attaché aux moteurs r_hip_x (id = 11) et l_hip_x (id = 21). La seule limitation de cette solution pourrait être le couple maximal du moteur r_hip_y (id = 23) et l_hip_y (id = 13). Sans la batterie de la dynamique de la jambe de Poppy est faite dans le 21% du couple maximal du moteur 13 et 23. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f9.tiff" width="350" height="160" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f9.tiff)

Par conséquent, une augmentation approximative de 100g pour chaque jambe ne va pas être un problème.

**Consommation d’énergie par Odroid U3:**

&nbsp;&nbsp;&nbsp;- puissance: 5V / 2A

Il faut utiliser un transformateur de tension 5V-12V comme celui de l’image suivant.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f9.tiff" width="350" height="140" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f9.tiff)

Par conséquent, une augmentation approximative de 100g pour chaque jambe ne va pas être un problème.

**Consommation d’énergie par Odroid U3:**<BR>

&nbsp;&nbsp;&nbsp; - puissance: 5V / 2A 

Il faut utiliser un transformateur de tension 5V-12V comme celui de l’image suivant.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f10.tiff" width="190" height="80" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f10.tiff)

**Solution mise en œuvre:**

&nbsp;&nbsp;&nbsp; - 3 Accumulateurs LG Lithium-Ion  en série avec les caractéristiques suivantes:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/tab_bat.tiff" width="400" height="80" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/tab_bat.tiff)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f11.tiff" width="350" height="160" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f11.tiff)

Les images suivants montrent le câblage pour les batteries

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f12.tiff" width="700" height="160" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f12.tiff)
