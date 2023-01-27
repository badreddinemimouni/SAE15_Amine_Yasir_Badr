from fonctions_calculs import *
from fonctions_velomag import *
import matplotlib.pyplot as plt

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE']#on chosit les parkings que l'on veut et on les met dans le tableau
les_id=['001','002','005','007','009','016','023','021',] # on choisit les parkings que l'on veut et on met leurs id dans le tableau
tab2=[]
tab3=[]
for i in range(len(parkings)):
	f2=open(parkings[i]+".txt","r",encoding='utf-8')

	lignes=f2.readlines()
	tab=[]
	for ligne in lignes:
		ligne=ligne.replace('\n','')
		donnees=ligne.split(',')
		tab.append(float(donnees[0]))
	print(tab)
	tab2.clear() # tableau dans lequel on stock les données de parkings de chaque heure temporairement
	tab2.append(tab)
	#print("tableau:")
	#print(tab2)
	mot=moyenne(tab2[0])
	moyennita=format(mot,'.2f')
	#print(moyennita)
	tab3.append(float(moyennita)) 
#print(tab3) # contient les moyenne de chaque parking 
moyenneTout=moyenne(tab3) # moyenne de toutes les moyennes de chaque heure
#print(format(moyenneTout,'.2f'))

ecart=ecarttype(tab3,moyenneTout) #ecart type de toutes les moyennes par rapport a la moyenne de base 
#print(ecart)
print('---------------------------------------------------------------------------------')
#-----------------------------------------------------------------------------------------------------------------------------------------------
tab4=[]
tab5=[]
for i in range(len(les_id)):
	f2=open(les_id[i]+".txt","r",encoding='utf-8')

	lignes2=f2.readlines()
	tab7=[]
	for ligne1 in lignes2:
		ligne1=ligne1.replace('\n','')
		donnees2=ligne1.split(',')
		tab7.append(float(donnees2[1]))
	print(tab7)
	print('--------------------------------')
	
	#tab4.clear() # tableau dans lequel on stock les données de parkings de chaque heure temporairement
	for j in range(0,9):

		valeur=tab7[j]
		tab4.clear()
		tab4.append(valeur)
		
		f5=open(str(j)+'heure.txt','a')
		for x in range(0,len(tab4)):
			f5.write(str(tab4[x])+',')
#--------------------------------------------------------------------------------------------------- cette partie au dessus je creer des fichiers et chaque fichier correspond a une heure et il stocke dedeans les donnees de tout les parkings a cette heure ci
		# tab4 contient la moyenne de tout les parkings par heure par ex la moyenne de tout les parkings a 10h
		#print(tab4)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	moy2=moyenne(tab4[0])
	moyennitas=format(moy2,'.2f')
	print(moyennitas)
	tab5.append(float(moyennitas)) 
#print('----------')
#print(tab5) #contient les moyenne de chaque parking  
#moyenneTout1=moyenne(tab5) #moyenne generale 
#print(format(moyenneTout1,'.2f'))

ecart2=ecarttype(tab5,moyenneTout1) #ecart type de toutes les moyennes par rapport a la moyenne de base 
print("l ecart de velo est de ")
#print(format(ecart2),'.2f')



#-------------------------------------------------------------------------------------------------------------------------

covarianca=covariance(tab3,tab5,moyenneTout,moyenneTout1)
print('-----------let sog')
#print(format(covarianca),'.2f')
correlatione=correlation(tab3,tab5,moyenneTout,moyenneTout1)
#print(correlatione)


#dates=getDateVelo(19819815)
#print(dates)

