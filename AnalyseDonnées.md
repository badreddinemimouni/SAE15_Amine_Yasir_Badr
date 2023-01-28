### SAE 15 - MINIPROJET - Akhrouf, El Haouat, Mimouni
# Analyse des données 


## Description du miniprojet  :
<br>

Durant ce mini projet nous avons écrit plusieurs programmes python, afin de recueillir les données du site open data de Montpellier, dans le but de les analyser.

<br>

![Open data](Images/opendata.jpg)

<br>

Cette technique, nommée *Web Scrapping* permet de récupérer des informations d’un site, grâce à un programme et de les réutiliser ensuite. En automatisant ce process, on évite ainsi de devoir récolter les données manuellement, et on gagne du temps.

<br>

## Notre démarche :
<br>

Premièrement avant de commencer le miniprojet, nous nous sommes posé des questions sur le projet avant de commencer quoi que ce soit. 
- Que demande le cahier des charges ?
- Quels sont les livrables attendus par le client ?
- Comment procéder ?


Nous nous sommes vite reparti les tâches de ce miniprojet après avoir répondu à nos questions.
Vu qu'il fallait utiliser plusieures librairies, nous avons fait une librairie chacun, nous avons 3 librairies. Une pour le recueil des données des parkings voiture, une pour pour le recueil des données des stands vélos, et une autre pour les calculs qu'on devra utiliser lors du traitement de données.

La librairie fonctions_calculs a été fait par Yasir Akhrouf, la librairie fonctions_velomag par Badr Mimouni, et la librairie fonctions_parking par Mohamed-Amine El Haouat.

Puis finalement chacun de nous avons contribué à l'écriture du programme principal.


<br><br>

## Analyses des données :
<br>
Pour l'analyse nous nous sommes consacrés sur  parkings voitures avec leur stand vélo. Nous avons choisis les parkings.


Nous avons calculé la moyenne des pourcentages de remplissage des parkings à chaque heure avec le fichier python nommé TraitementDonnées. 
Ce fichier nous retourne la moyenne des parkings à chaque heure, l'écart type, la covariance et la corrélaton.
<br><br>

Voici la représentation du taux de place libre des parkings, avec le taux de vélos libres :

<br> 

![Moyenne](Images/placesLibre_compare.png)

<br>
Sur ce graphe, nous pouvons constater que les vélos ne sont pas vraiment utilisés dans la ville de Montpellier et que les parkings ont un taux d'occupation élevé.

Mais le fait que les vélos ne soient pas utilisés est normal puisque les gens aujourd'hui préfèrent se déplacer en trotinette électrique ou bien en tram.

<br><br>

![Alt text](image.png)

<br>

Ici nous avons les valeurs de l'écart type por les parkings de voiture et des vélos. Pour le parking voiture l'écart type est de 2,47. Une valeur pas trop grande puisque les gens laissent leur voiture dans les parkings pour aller travailler le jour ou bien la nuit lorsqu'ils ne trouvent pas de places dans les rues la nuit. Ce qui fait que les parkings de voitures sont presque jamais vides.

Ensuite nous avons aussi l'écart type des vélos qui est de 4,03. Les vélos ne sont pas trop utilisés, ce qu'il fait que lorsque une ou deux  personnes vont emprunter un vélo, et bien l'écart type va augmenter.

L’écart-type est sensible aux valeurs aberrantes. Une seule valeur très aberrante peut accroître l’écart-type et, par le fait même, déformer le portrait de la dispersion.


<br>
Au vu des données traitées ci-dessus des parkings voitures de la ville de Montpellier et des parking vélo, nous ne pouvons pas établir une corrélation puisque il n'y a aucun lien qui prouve que le parking vélo a un taux d’occupation qui est en relation avec l’usage de la voiture. 

On peut constater que nous avons commencé à récupérer les données le 26 janvier à 10h et que jusqu'à 19h, le nombre de places occupés de  chaque parking choisi varie légèrement. 
