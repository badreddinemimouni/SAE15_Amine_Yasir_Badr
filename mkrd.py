import matplotlib.pyplot as plt
parkings=['FR_MTP_CORU','FR_MTP_FOCH']
#for i in range(len(parkings)):
f2=open("FR_MTP_CORU.txt","r",encoding='utf-8')

lignes=f2.readlines()
tab=[]
tab2=[]
for ligne in lignes:
	ligne=ligne.replace('\n','')
	donnees=ligne.split(',')
	tab.append(float(donnees[0]))
for ligne2 in lignes:
    ligne2=ligne2.replace('\n','')
    donnees2=ligne2.split(',')
    tab2.append(donnees2[1])

#print(tab2)
plt.plot(tab)
plt.plot_date(tab2,tab)
plt.ylabel('pourcentage')
plt.xlabel('heures')
plt.show()
