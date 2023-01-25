from fonctions_velomag import *	
from fonctions_parking import * 



parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRCE','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_POLY']#on chosit les parkings que l'on veut et on les met dans le tableau
les_id=['001','002','004','007','012','023'] # on choisit les parkings que l'on veut et on met leurs id dans le tableau
nbTours=2
vide=False
if vide==False:
    for t in range(len(parkings)):
        f2=open(parkings[t]+".txt","w")
        f2.write("")
        vide=True
    for s in range(len(les_id)):
        f3=open(les_id[s]+".txt","w")
        f3.write("")
        f3.close()
        vide=True
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
        time.sleep(60)
    else:
        print('fin')
