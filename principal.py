from fonctions_velomag import *	
from fonctions_parking import * 



parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_ARCE']#on chosit les parkings que l'on veut et on les met dans le tableau
les_id=['001','002','005','007','009','016','023','021',] # on choisit les parkings que l'on veut et on met leurs id dans le tableau
nbTours=12
vide=False
#if vide==False:
    #for t in range(len(parkings)):
       # f2=open(parkings[t]+".txt","w")
        #f2.write("")
        #vide=True
    #for s in range(len(les_id)):
        #f3=open(les_id[s]+".txt","w")
        #f3.write("")
        #f3.close()
        #vide=True
arret=0

for j in range(0,nbTours):
    for i in range(len(parkings)):  
       
        grat=getpourcentagePlacelibre(parkings[i],parkings)
        
        #print(grat)
    for l in range(len(les_id)):
        
        s1=getRequest("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_information.json","ficjson")
# ~ print(ss)
        s2=getRequest("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json","ficjson2")
        pl=getpourcentageVelo(les_id[l],s2,s1)

    #dernier=s1['last_updated']
    #dernier2=getDateVelo(dernier)
    #print(dernier2)
    #print(dernier)
    print("------------------------")   
    print(pl)
    arret+=1
    if arret < nbTours:
        time.sleep(3600)
    else:
        print('fin')