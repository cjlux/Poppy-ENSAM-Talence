# DESIGN DES BATTERIES

###Consommation d’énergie des servomoteurs
* plage de tension : 10 à ~14.8V (tension recommandée 12V)
* courant consommé : 
  * minimum : moteurs en mode *compliant* -> 1.53 A 
  * maximum : mesuré lors d'une séquence qui met en mouvement la partie haute de Poppy (bras, torse...) -> 2.5 A

###Limites de couple (couple de décrochage)
*  MX-64 : 5.5 Nm (at 11.1V, 3.9A), 6.0N.m (at 12V, 4.1A)
*  MX-28 : 2.3N.m (at 11.1V, 1.3A), 2.5N.m (at 12V, 1.4A)

##Temps d’autonomie
Théoriquement, avec des batteries permettant d'obtenir une capacité de 2600 mAh sous 12 volts, on peut espérer une autonomie de fonctionnement de Poppy proche d'une heure. Tout dépend bien sûr de la façon dont on sollicite les servomoteurs.

##Types de batteries utilisables
- **Alkaline** : piles non rechargeables, pas envissgeable pour l'utilisation avec Poppy.
- **Nickel** :
  * **NiCd** : (nickel-cadmium) technologie en voie de dsiparition à cause de l'*effet mémoire* lié.
  * **NiMh** : (nickel-métal hydrure) *effet mémoire* très faible, technologie offrant un bon compromis (prix/capacité/poids), mais nécessite un temps de charge assez long.
- **Plomb-acide** : ces batteries ont le défaut d'être volumineuses et lourdes, elles doivent toujours régulièrement chargées et ne permettent pas une vitesse de décharge aussi élevée que les autres technologies.
- **Lithium-ion** : batteries légères, pas d'*effet mémoire*, temps de décharge élevé avec une relativement bonne capacité. La tension d'un élément est voisinne de 3.7 V. Les solutions possibles pour atteindres les 12 V nécessaire pour Poppy sont :
 
  - trois batteries séparées de 3.7 V, banchées en série, poids: ~60g chacune; prix par batterie: ~ 20€. Permet de disposer les batteries séparémment dans la structure de Poppy <BR>
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/Batterie-lithium-ion_LG_RS.png" width="100" height="60" >] (http://147.210.74.152/Poppy/8_dessin_des_batteries/Batterie-lithium-ion_LG_RS.png)
  - un *pack batterie de 11.1 V, poids: 150g, prix: environ 50 € <BR>
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/Pack-lithium-ion_LG_RS1.png" width="180" height="100" >] (http://147.210.74.152/Poppy/8_dessin_des_batteries/Pack-lithium-ion_LG_RS1.png)

##Emplacement:
###Cas d'une batterie unique lithium-ion de 11.1 V
une solution possible est de fixer la betterie sur le robot au niveau du moteur `abs_x` (id = 32). Le problème de cette solution est que la partie supérieure de Poppy est déjà relativement lourde, ce qui peut pénaliser la dynamique du robot. 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f8.png" width="350" height="160" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f8.png)

#La solution avec trois batteries
permet de localiser une batterie dans chaque jambe (entre la hanche et le genou) et de fixer la troisième batterie aux moteurs 'r_hip_x' (id = 11) et 'l_hip_x' (id = 21). La seule limitation de cette solution pourrait être le couple maximal des moteurs 'r_hip_y' (id = 23) et 'l_hip_y' (id = 13) (dabs sa version initiale, la dynamique de la jambe de Poppy sollicite environ 21% du couple maximal des moteurs 13 et 23). 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f9.png" width="350" height="160" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f9.png)

Par conséquent, une augmentation approximative de 100g pour chaque jambe ne va pas être un problème.

##Consommation d’énergie par la carte Odroid U3

- consommation sous 5V : 2A. On peut utiliser un convertisseur de ension 12 V->5 V pour alimenter la acrte Odroid avec la tension de 12 V disponible dans Poppy.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f9.png" width="350" height="140" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f9.png)

**Consommation d’énergie par Odroid U3:**<BR>

&nbsp;&nbsp;&nbsp; - puissance: 5V / 2A 

Il faut utiliser un transformateur de tension 5V-12V comme celui de l’image suivant.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f10.png" width="190" height="80" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f10.png)

#Solution mise en œuvre

- 3 Accumulateurs LG Lithium-Ion  en série avec les caractéristiques suivantes:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/tab_bat.png" width="400" height="80" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/tab_bat.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f11.png" width="350" height="160" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f11.png)

Les images suivants montrent le câblage pour les batteries

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f12.png" width="700" height="160" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f12.png)
