from fonctions_calculs import *
from fonctions_velomag import *
import matplotlib.pyplot as plt

parkings=['FR_MTP_CORU','FR_MTP_FOCH']
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
	#print(tab)
	tab2.clear() # tableau dans lequel on stock les données de parkings de chaque heure temporairement
	tab2.append(tab)
	#print("tableau:")
	#print(tab2)
	mot=moyenne(tab2[0])
	moyennita=format(mot,'.2f')
	#print(moyennita)
	tab3.append(float(moyennita)) 
print(tab3) # contient les moyenne de chaque parking 
moyenneTout=moyenne(tab3) # moyenne de toutes les moyennes de chaque heure
print(format(moyenneTout,'.2f'))

ecart=ecarttype(tab3,moyenneTout) #ecart type de toutes les moyennes par rapport a la moyenne de base 
print(ecart)

#-----------------------------------------------------------------------------------------------------------------------------------------------
tab4=[]
tab5=[]
for i in range(len(parkings)):
	f2=open(parkings[i]+"_VELO.txt","r",encoding='utf-8')

	lignes=f2.readlines()
	tab7=[]
	for ligne in lignes:
		ligne=ligne.replace('\n','')
		donnees2=ligne.split(',')
		tab7.append(float(donnees2[1]))
	print("------------------------")
	print(tab7)
	tab4.clear() # tableau dans lequel on stock les données de parkings de chaque heure temporairement
	tab4.append(tab7)
	print("-----------------------------------------------------")
	#print(tab4)
	moy2=moyenne(tab4[0])
	moyennitas=format(moy2,'.2f')
	#print(moyennita)
	tab5.append(float(moyennitas)) 
print('----------')
print(tab5) #contient les moyenne de chaque parking  
moyenneTout1=moyenne(tab5) #moyenne generale 
print(format(moyenneTout1,'.2f'))

ecart2=ecarttype(tab5,moyenneTout1) #ecart type de toutes les moyennes par rapport a la moyenne de base 
print("l ecart de velo est de ")
print(format(ecart2),'.2f')



#-------------------------------------------------------------------------------------------------------------------------

covarianca=covariance(tab3,tab5,moyenneTout,moyenneTout1)
print('-----------let sog')
print(format(covarianca),'.2f')
correlatione=correlation(tab3,tab5,moyenneTout,moyenneTout1)
print(correlatione)


dates=getDateVelo(19819815)
print(dates)

