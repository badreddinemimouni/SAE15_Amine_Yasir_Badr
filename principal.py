from fonctions_velomag import *	
from fonctions_parking import * 

s1=getRequest("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_information.json","ficjson")
# ~ print(ss)
s2=getRequest("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json","ficjson2")


parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRCE','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']

nbTours=8
vide=False
if vide==False:
    for t in range(len(parkings)):
        f2=open(parkings[t]+".txt","w")
        f2.write("")
        vide=True
    for s in range(1,9):
        f3=open('00'+str(s)+".txt","w")
        f3.write("")
        f3.close()
        vide=True

for j in range(0,nbTours):
    pl=getpourcentageVelo(s2,s1)
    for i in range(len(parkings)):  
       
        grat=getpourcentagePlacelibre(parkings[i],parkings)
        
        print(grat)
    print("------------------------")
    time.sleep(3600)


