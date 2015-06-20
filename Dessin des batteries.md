## DESSIN DES BATTERIES

**Consommation d’énergie:**
* plage de tension: 10 ~14.8V (tension recommandée 12V)
* courant consommé: 
  * minimum : moteurs en mode ‘compliant’ -> 1.53 A 
  * maximum : enregistré au cours d'une séquence qui met en mouvement la partie haute de Poppy (bras, torse...) -> 2 A

**Limites de couple (couple de décrochage):**
*  MX-64 : 5.5 Nm (at 11.1V, 3.9A), 6.0N.m (at 12V, 4.1A)
*  MX-28 : 2.3N.m (at 11.1V, 1.3A), 2.5N.m (at 12V, 1.4A)

**Temps d’autonomie:**
- théoriquement on a environ une heure de fonctionnement avec les batteries 2000mAh

**Types d'accumulateurs disponibles:**
- Alkaline: pas considéré pour ce projet (constamment besoin d'acheter des remplacements)

- Nickel: <BR>
  1.  NiCd: Ces batteries sont en train de disparaître à cause de leur effet mémoire.
  2.  NiMh: ils sont rechargeables (il n'y a presque pas d'effet mémoire), offrent un bon compromis (prix/capacité/poids), mais un long temps de charge est nécessaire.
  Exemple : 12V pour poids de 540g à partir de 40 $.
- Lead acid: ces batteries ont le défaut d'être très volumineuses et lourdes, elles doivent toujours être maintenues, elles n’ont pas la vitesse de décharge élevée que les batteries plus modernes.
- Lithium: batteries légères, temps de décharge élevé avec une relativement bonne capacité. La tension finale obtenue par combinaison de plusieurs éléments sera un multiple 3.7 V. Les solutions possibles sont les suivantes: 
  1. trois batteries de 3.7V, poids: 45g chacune; prix de chaque batterie: environn 20€ 
  2. une batterie de 11.1V, poids: 150g, prix: 50 €

**Emplacement:** 
Dans le cas d'une batterie unique, la seule solution est de la fixer moteur 'abs_x' (id = 32). Le problème de cette solution est que la partie supérieure du robot est déjà assez lourde, ce qui va pénaliser la dynamique du robot. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f8.png" width="350" height="160" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f8.png)

La solution avec trois batteries permet de localiser une batterie dans chaque jambe (entre la hanche et le genou) et de fixer la troisième batterie aux moteurs 'r_hip_x' (id = 11) et 'l_hip_x' (id = 21). La seule limitation de cette solution pourrait être le couple maximal des moteurs 'r_hip_y' (id = 23) et 'l_hip_y' (id = 13) (dabs sa version initiale, la dynamique de la jambe de Poppy sollicite environ 21% du couple maximal des moteurs 13 et 23). 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f9.png" width="350" height="160" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f9.png)

Par conséquent, une augmentation approximative de 100g pour chaque jambe ne va pas être un problème.

**Consommation d’énergie par Odroid U3:**

&nbsp;&nbsp;&nbsp;- puissance: 5V / 2A

Il faut utiliser un transformateur de tension 5V-12V comme celui de l’image suivant.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f9.tiff" width="350" height="140" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f9.tiff)

Par conséquent, une augmentation approximative de 100g pour chaque jambe ne va pas être un problème.

**Consommation d’énergie par Odroid U3:**<BR>

&nbsp;&nbsp;&nbsp; - puissance: 5V / 2A 

Il faut utiliser un transformateur de tension 5V-12V comme celui de l’image suivant.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f10.tiff" width="190" height="80" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f10.tiff)

**Solution mise en œuvre:**

&nbsp;&nbsp;&nbsp; - 3 Accumulateurs LG Lithium-Ion  en série avec les caractéristiques suivantes:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/tab_bat.tiff" width="400" height="80" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/tab_bat.tiff)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f11.tiff" width="350" height="160" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f11.tiff)

Les images suivants montrent le câblage pour les batteries

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img src="http://147.210.74.152/Poppy/8_dessin_des_batteries/f12.tiff" width="700" height="160" >]
(http://147.210.74.152/Poppy/8_dessin_des_batteries/f12.tiff)
