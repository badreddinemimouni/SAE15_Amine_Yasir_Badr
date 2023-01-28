from fonctions_calculs import *
from fonctions_velomag import *
import matplotlib.pyplot as plt

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE']#on chosit les parkings que l'on veut et on les met dans le tableau
les_id=['001','002','005','007','009','016','023','021',] # on choisit les parkings que l'on veut et on met leurs id dans le tableau
tab2=[]
tab3=[]
tab1=[]
tab2=[]
tab3=[]
tab4=[]
tab5=[]
tab6=[]
tab7=[]
tab8=[]
tab9=[]

#-------

for i in range(len(parkings)):
	f2=open(parkings[i]+".txt","r",encoding='utf-8')

	lignes=f2.readlines()
	tab=[]
	for ligne in lignes:
		ligne=ligne.replace('\n','')
		donnees=ligne.split(',')
		tab.append(float(donnees[0]))
	

	moy_h=[]
	tab_h=[tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8]
	for j in range(len(tab_h)):
		
		valeur=tab[j]
		tab3.clear() # dans tab3 on stocke les donnees temporairement pour ensuite les faire passer dans le tableau correspondant a l'heure
		tab3.append(valeur)
		#print("tabel")
		#print(tab7)
		let=tab_h[j]
		for x in range(0,len(tab3)):
			let.append(tab3[x])
		moyennes1=moyenne(let)
		moy_h.append(float(format(moyennes1,'.2f'))) # contient les moyennes de chaque heure de tout les parkings 
#print(tab1)
	#print(moy_h)
	moyenneG=moyenne(moy_h)
print("La moyenne des pourcentages de parkings de la journée est de :"+format(moyenneG,'.2f'))	
	
ecarttype_voiture=ecarttype(moy_h,moyenneG)
print("l'ecart type des moyennes de pourcentage de places libres par heure(voitures) : "+format(ecarttype_voiture,'.2f'))


	
	

print('---------------------------------------------------------------------------------')
#-----------------------------------------------------------------------------------------------------------------------------------------------
tab4=[]
tab5=[]
tab10=[]
tab11=[]
tab12=[]
tab13=[]
tab14=[]
tab15=[]
tab16=[]
tab19=[]
tab22=[]
moy10=[]
moy11=[]
moy12=[]
moy13=[]
moy14=[]
moy15=[]
moy16=[]
moy19=[]
moy22=[]

for l in range(len(les_id)):
	f2=open(les_id[l]+".txt","r",encoding='utf-8')

	lignes2=f2.readlines()
	tab7=[]
	for ligne1 in lignes2:
		ligne1=ligne1.replace('\n','')
		donnees2=ligne1.split(',')
		tab7.append(float(donnees2[1]))
	#print(tab7)
	
	heure=0
	#tab4.clear() # tableau dans lequel on stock les données de parkings de chaque heure temporairement



	nom_tab=[tab10,tab11,tab12,tab13,tab14,tab15,tab16,tab19,tab22]
	tab_moy=[]
	for j in range(len(nom_tab)):
		
		valeur=tab7[j]
		tab4.clear()
		tab4.append(valeur)
		#print("tabel")
		#print(tab7)
		let=nom_tab[j]
		for x in range(0,len(tab4)):
			let.append(tab4[x])
		moyennes=moyenne(let)
		tab_moy.append(float(format(moyennes,'.2f'))) # contient les moyennes de chaque heure de tout les parkings 

#print(tab22)
#print(tab_moy)
moyenneG_velo=moyenne(tab_moy)
print("la moyenne des porucentage des places libres à ce jour (vélo) : " +format(moyenneG_velo,'.2f'))
ecarttype_velo=ecarttype(tab_moy,moyenneG_velo)
print("l'ecart type des moyennes de pourcentages de places libres par heure (vélo) : "+format(ecarttype_velo,'.2f'))
print('---------------')
covariances=covariance(moy_h,tab_moy,moyenneG,moyenneG_velo)
print("la covariance des deux types de véhicules est de:"+format(covariances,'.2f'))

