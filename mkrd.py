import matplotlib.pyplot as plt
parkings=['FR_MTP_CORU','FR_MTP_FOCH']
#for i in range(len(parkings)):
f2=open("FR_MTP_CORU.txt","r",encoding='utf-8')

lignes=f2.readlines()
tab=[]
for ligne in lignes:
	ligne=ligne.replace('\n','')
	donnees=ligne.split(',')
	tab.append(float(donnees[0]))
for i in range(len(tab)):
    plt.plot(tab[i])
    plt.ylabel('Label 1')
    plt.show()
